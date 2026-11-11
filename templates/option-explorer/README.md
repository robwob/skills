# Option explorer template

A review shell for comparing structural options on one screen. One HTML file,
no dependencies, no build step.

**Layout.** The left rail explains what is being compared and holds the
controls: option switch, measured readouts, view toggles. The stage on the right
shows the option's name and claim, then the screen inside a phone frame. Under
1000px the rail becomes a drawer and the frame becomes the whole screen.

**Two systems, kept apart.** Inside `.device` is the design, greyscale. Outside
it is the instrument, dark, and colour is allowed there as a measuring tool only.

**Device switch.** Mobile and Desktop chips in the rail, and `?device=desktop`
links straight to it. Desktop is a browser frame up to 1180px wide, shown above
a 1000px viewport only. A mobile screen is never stretched to fill it:

- An option with a `renderDesktop()` fills the browser frame with that layout.
- An option without one keeps its mobile screen at phone width, centred in the
  frame, with a note under it saying there is no desktop layout yet.

Stretching a mobile layout is what puts sheets over maps and floating buttons
over content, so add `renderDesktop()` only when there is a desktop design.

**To use.** Copy `index.html` into your project. Edit the `OPTIONS` table and
the rail copy. Delete the placeholder `.ph` blocks. The file path is the
hand-back: open it directly in a browser.

```js
const OPTIONS = {
  A: { name:'Option A', claim:'What this option claims, in a sentence.',
       readout:[{l:'Taps to goal', v:'2', s:'Counted from the screen, not estimated'}],
       render:() => '...mobile screen HTML...',
       renderDesktop:() => '...desktop layout HTML...' },   // optional
};
```

**Worth adding when needed:** theme isolation chips, readouts measured from the
rendered screen, an edit-layout mode with per-option remembered order,
annotation tags, a bottom sheet, a script to inline CSS and JS into one file,
and a screenshot script.
