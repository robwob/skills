/*
 * measure.js  -  objective checks for ui-review
 *
 * Computes the numeric parts of the UI standards library against a rendered page:
 * text contrast (1.4.3), non-text contrast on control borders (1.4.11), target size (2.5.8),
 * body size, line height and line length.
 *
 * Run it against anything served: paste into the devtools console, or inject with the browser
 * tool's javascript_tool. It reads the page and returns a result object. It changes nothing.
 *
 *   const r = __uiMeasure();            // whole page
 *   const r = __uiMeasure('main');      // scoped to a selector
 *
 * Reported numbers are computed, not estimated. Anything this script cannot reach, a canvas,
 * an image background, text inside a cross-origin iframe, is listed under `unmeasured` and must be
 * reported as not assessed rather than assumed to pass.
 */

function __uiMeasure(rootSelector) {
  const root = rootSelector ? document.querySelector(rootSelector) : document.body;
  if (!root) return { error: 'root not found: ' + rootSelector };

  // ---- colour ----------------------------------------------------------------

  const parse = (str) => {
    if (!str) return null;
    const m = str.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[,\s/]+/).filter(Boolean).map(Number);
    if (p.length < 3 || p.some(Number.isNaN)) return null;
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };

  // src over dst, both non-premultiplied
  const over = (src, dst) => {
    if (src.a >= 1) return { ...src, a: 1 };
    const a = src.a + dst.a * (1 - src.a);
    if (a === 0) return { r: 0, g: 0, b: 0, a: 0 };
    const ch = (s, d) => (s * src.a + d * dst.a * (1 - src.a)) / a;
    return { r: ch(src.r, dst.r), g: ch(src.g, dst.g), b: ch(src.b, dst.b), a };
  };

  const luminance = ({ r, g, b }) => {
    const f = (v) => {
      const c = v / 255;
      return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
    };
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b);
  };

  const ratio = (a, b) => {
    const l1 = luminance(a), l2 = luminance(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  };

  const round = (n) => Math.round(n * 100) / 100;

  // Composite every ancestor background down to an opaque colour.
  // Returns null when something unreadable sits in the stack, an image or a gradient,
  // because a guessed background is worse than an admitted gap.
  const backgroundOf = (el) => {
    let acc = { r: 0, g: 0, b: 0, a: 0 };
    let node = el;
    while (node && node.nodeType === 1) {
      const cs = getComputedStyle(node);
      if (cs.backgroundImage && cs.backgroundImage !== 'none') return null;
      const bg = parse(cs.backgroundColor);
      if (bg && bg.a > 0) {
        acc = over(acc, bg);
        if (acc.a >= 1) return acc;
      }
      node = node.parentElement;
    }
    const page = parse(getComputedStyle(document.documentElement).backgroundColor);
    acc = over(acc, page && page.a > 0 ? page : { r: 255, g: 255, b: 255, a: 1 });
    return acc.a >= 1 ? acc : over(acc, { r: 255, g: 255, b: 255, a: 1 });
  };

  const visible = (el) => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || Number(cs.opacity) === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };

  const label = (el) => {
    const id = el.id ? '#' + el.id : '';
    const cls = typeof el.className === 'string' && el.className.trim()
      ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.')
      : '';
    return el.tagName.toLowerCase() + id + cls;
  };

  const snippet = (t) => {
    const s = t.replace(/\s+/g, ' ').trim();
    return s.length > 60 ? s.slice(0, 57) + '...' : s;
  };

  const results = {
    textContrast: [], nonTextContrast: [], targetSize: [],
    typography: [], unmeasured: [], summary: {}
  };

  // ---- text contrast, 1.4.3 --------------------------------------------------

  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, {
    acceptNode: (n) =>
      n.nodeValue.trim().length > 1 && n.parentElement && visible(n.parentElement)
        ? NodeFilter.FILTER_ACCEPT
        : NodeFilter.FILTER_REJECT
  });

  const seen = new Set();
  const typographyIndex = new Map();
  let node;
  while ((node = walker.nextNode())) {
    const el = node.parentElement;
    if (seen.has(el)) continue;
    seen.add(el);

    const cs = getComputedStyle(el);
    const size = parseFloat(cs.fontSize);
    const weight = Number(cs.fontWeight) || (cs.fontWeight === 'bold' ? 700 : 400);
    const bg = backgroundOf(el);

    if (!bg) {
      results.unmeasured.push({
        element: label(el), text: snippet(node.nodeValue),
        reason: 'sits on an image or gradient background, contrast not computable from CSS'
      });
      continue;
    }

    const fg = parse(cs.color);
    if (!fg) continue;
    const composited = fg.a < 1 ? over(fg, bg) : fg;

    const large = size >= 24 || (size >= 18.667 && weight >= 700);
    const required = large ? 3 : 4.5;
    const r = ratio(composited, bg);

    if (r < required) {
      results.textContrast.push({
        element: label(el), text: snippet(node.nodeValue),
        ratio: round(r), required, fontSize: round(size), fontWeight: weight,
        large, color: cs.color, background: `rgb(${Math.round(bg.r)}, ${Math.round(bg.g)}, ${Math.round(bg.b)})`,
        severity: 'Blocker', criterion: '1.4.3 Contrast (Minimum), AA'
      });
    }

    // typography, checked once per text-bearing element
    const lh = cs.lineHeight === 'normal' ? size * 1.2 : parseFloat(cs.lineHeight);
    const width = el.getBoundingClientRect().width;
    const chars = Math.round(width / (size * 0.5)); // ~0.5em average advance
    const issues = [];
    if (size < 16) issues.push(`font-size ${round(size)}px is below the 16px de facto floor [Convention]`);
    if (lh / size < 1.5 && node.nodeValue.trim().length > 120) {
      issues.push(`line-height ${round(lh / size)} is below 1.5 on a paragraph [1.4.8 AAA]`);
    }
    if (chars > 80 && node.nodeValue.trim().length > 120) {
      issues.push(`~${chars} characters per line exceeds 80 [1.4.8 AAA], 50-75 is the evidenced range`);
    }
    // Grouped by selector plus issue, not pushed per text node. One rule applied to forty elements
    // is one finding with a count, and a raw per-node list is unusable without post-processing.
    if (issues.length) {
      const key = label(el) + ' :: ' + issues.join(' :: ');
      const seenIssue = typographyIndex.get(key);
      if (seenIssue) seenIssue.occurrences++;
      else typographyIndex.set(key, {
        element: label(el), issues, occurrences: 1, example: snippet(node.nodeValue)
      });
    }
  }
  results.typography = [...typographyIndex.values()].sort((a, b) => b.occurrences - a.occurrences);

  // ---- interactive elements: target size 2.5.8, non-text contrast 1.4.11 ------

  const interactive = root.querySelectorAll(
    'a[href], button, input:not([type=hidden]), select, textarea, [role=button], [role=link], [role=checkbox], [role=tab], [tabindex]:not([tabindex="-1"])'
  );

  // Geometry for the 2.5.8 spacing exception, gathered before judging any single target.
  const targets = [...interactive].filter(visible).map((el) => {
    const r = el.getBoundingClientRect();
    return { el, rect: r, cx: r.left + r.width / 2, cy: r.top + r.height / 2,
             undersized: r.width < 24 || r.height < 24 };
  });

  // 2.5.8 Spacing exception: a 24px-diameter circle centred on an undersized target must not
  // intersect another target, nor the circle of another undersized target. Computing this is the
  // difference between reporting a real failure and reporting every small link on the page.
  const spacingExempt = (t) => {
    for (const o of targets) {
      if (o.el === t.el) continue;
      if (o.undersized) {
        if (Math.hypot(o.cx - t.cx, o.cy - t.cy) < 24) return false;
      } else {
        const dx = Math.max(o.rect.left - t.cx, 0, t.cx - o.rect.right);
        const dy = Math.max(o.rect.top - t.cy, 0, t.cy - o.rect.bottom);
        if (Math.hypot(dx, dy) < 12) return false;
      }
    }
    return true;
  };

  targets.forEach(({ el, rect, undersized }) => {
    const cs = getComputedStyle(el);
    const inline = el.tagName === 'A' && cs.display.includes('inline');

    if (!inline && undersized) {
      const exempt = spacingExempt({ el, rect, cx: rect.left + rect.width / 2, cy: rect.top + rect.height / 2 });
      const entry = {
        element: label(el), text: snippet(el.textContent || el.value || ''),
        width: round(rect.width), height: round(rect.height),
        criterion: '2.5.8 Target Size (Minimum), AA, 24x24 CSS px'
      };
      if (exempt) {
        entry.severity = 'Pass, spacing exception';
        entry.note = 'under 24px, but no other target comes within the 24px exclusion circle, so 2.5.8 is met. ' +
                     'Still under the 44 to 48px comfortable minimum Apple and Material recommend [Convention]';
      } else {
        entry.severity = 'Blocker';
        entry.note = 'under 24px and an adjacent target sits inside the exclusion circle, so the spacing exception does not apply';
      }
      results.targetSize.push(entry);
    }

    // A control's boundary can be drawn by any single edge, an underline is a boundary, so check
    // all four rather than assuming a box. It can also be drawn by a wrapper, a segmented control
    // being the usual case, which this pass cannot attribute and must not fail.
    const parentBg = el.parentElement ? backgroundOf(el.parentElement) : null;
    const ownBg = parse(cs.backgroundColor);

    const sides = ['Top', 'Right', 'Bottom', 'Left']
      .map((s) => ({
        side: s.toLowerCase(),
        width: parseFloat(cs['border' + s + 'Width']),
        colour: parse(cs['border' + s + 'Color'])
      }))
      .filter((b) => b.width > 0 && b.colour && b.colour.a > 0);

    if (parentBg && !el.disabled) {
      // 1.4.11 governs the visual information required to *identify* a control. Where a control
      // carries its own visible text label, W3C treats it as identified by that text, and the text
      // contrast requirement applies instead. So a labelled button with a weak boundary is an
      // advisory, not a failure, and saying otherwise overstates the finding.
      const textLabelled = (el.textContent || '').trim().length > 0 &&
        el.tagName !== 'INPUT' && el.tagName !== 'SELECT' && el.tagName !== 'TEXTAREA';
      const grade = (r) => ({
        severity: textLabelled ? 'Advisory' : 'Blocker',
        note: textLabelled
          ? 'the control carries its own visible text label, so 1.4.11 is arguably satisfied by the ' +
            'label rather than the boundary. Report as contested, not as a clear failure'
          : undefined,
        ratio: round(r), required: 3, criterion: '1.4.11 Non-text Contrast, AA'
      });

      if (sides.length) {
        // the strongest edge carries the boundary, so the control passes if any single one does
        const best = sides.reduce((acc, b) => {
          const r = ratio(b.colour.a < 1 ? over(b.colour, parentBg) : b.colour, parentBg);
          return r > acc.ratio ? { ratio: r, side: b.side } : acc;
        }, { ratio: 0, side: null });

        if (best.ratio < 3) {
          results.nonTextContrast.push({
            element: label(el),
            part: `border (${sides.map((s) => s.side).join(', ')}), strongest edge`,
            ...grade(best.ratio)
          });
        }
      } else if (ownBg && ownBg.a > 0) {
        const r = ratio(over(ownBg, parentBg), parentBg);
        if (r < 3) {
          results.nonTextContrast.push({
            element: label(el), part: 'fill, no border present', ...grade(r)
          });
        }
      } else if (el.tagName === 'INPUT' || el.tagName === 'SELECT' || el.tagName === 'TEXTAREA') {
        // no edge and no distinguishing fill of its own. A wrapper may still be drawing the
        // boundary, so this is reported as needing a look rather than as a failure.
        const wrapper = el.parentElement;
        const wrapperCs = wrapper ? getComputedStyle(wrapper) : null;
        const wrapperDraws = wrapperCs && (
          ['Top', 'Right', 'Bottom', 'Left'].some((s) => parseFloat(wrapperCs['border' + s + 'Width']) > 0)
        );
        results[wrapperDraws ? 'unmeasured' : 'nonTextContrast'].push(
          wrapperDraws
            ? {
                element: label(el),
                reason: `no border of its own, but ${label(wrapper)} draws one. Confirm by eye that the field boundary reads, 1.4.11`
              }
            : {
                element: label(el), part: 'no border, and no fill distinct from its surroundings',
                severity: 'Blocker', criterion: '1.4.11 Non-text Contrast, AA',
                note: 'field boundary is not identifiable against its surroundings'
              }
        );
      }
    }

    // focus styling has to be inspected in the focused state, which this pass cannot enter
    if (cs.outlineStyle === 'none' && !el.disabled) {
      results.unmeasured.push({
        element: label(el),
        reason: 'outline:none in the resting state, focus indicator must be confirmed by tabbing to it, 2.4.7'
      });
    }
  });

  // A page defining two palettes has two sets of numbers, and this pass only ever sees the one the
  // browser is currently in. Reporting a clean result without saying which palette it came from is
  // how a light-mode-only failure gets shipped.
  const scheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  const definesBothSchemes = [...document.styleSheets].some((sheet) => {
    try {
      return [...sheet.cssRules].some(
        (r) => r.type === CSSRule.MEDIA_RULE && /prefers-color-scheme/.test(r.conditionText || '')
      );
    } catch (e) {
      return false; // cross-origin sheet, cannot inspect
    }
  });

  results.summary = {
    schemeMeasured: scheme,
    definesBothSchemes,
    textContrastFailures: results.textContrast.length,
    nonTextContrastFailures: results.nonTextContrast.filter((f) => f.severity === 'Blocker').length,
    nonTextContrastAdvisories: results.nonTextContrast.filter((f) => f.severity === 'Advisory').length,
    targetSizeFailures: results.targetSize.filter((f) => f.severity === 'Blocker').length,
    targetSizeExempt: results.targetSize.filter((f) => f.severity !== 'Blocker').length,
    typographyFindings: results.typography.length,
    unmeasured: results.unmeasured.length,
    elementsChecked: seen.size + targets.length,
    viewport: `${window.innerWidth}x${window.innerHeight}`,
    note: 'Contrast and size are computed. Focus appearance, hover and active states are not, they need the element in that state.'
  };

  if (definesBothSchemes) {
    results.summary.warning =
      `This page defines a ${scheme === 'dark' ? 'light' : 'dark'} palette too, and it has NOT been measured. ` +
      'These numbers cover the ' + scheme + ' palette only. Measure the other one before reporting a clean result.';
  }

  return results;
}

if (typeof module !== 'undefined') module.exports = { __uiMeasure };
