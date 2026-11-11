# Option explorer template

A prototype for comparing structural options across several screens, plus a record of every
iteration. Plain HTML and JavaScript, no dependencies, no build step. Open the files directly
in a browser.

```
index.html                   the prototype: PROJECT and SCREEN_FILES. Rename it per project.
prototype/
  screens/<name>.js          one file per screen: its options, how each renders, its notes
  design.css                 styles inside the frame, shared by the screens
  shell.js, shell.css        the panel and the frame. Not edited per project.
explorations/
  index.html                 the record viewer: every iteration, frozen, with its reasons
  records.js                 the record entries (JSON after the "=")
  freeze.py                  freezes the prototype into the record
  <screen>/NN-name.html      frozen copies (written by freeze.py, never edited)
  .autosave/                 optional safety-net snapshots (git-ignored)
```

**Why one file per screen.** A prototype grows with every screen and every direction. Kept
in one file it becomes slow and risky to change. Split by screen, a change to the Explore
screen means opening `prototype/screens/explore.js` and nothing else.

**Why the screens are `.js` files.** Opened straight from disk, a browser will load scripts
and stylesheets from beside the page but will not read other HTML files. So each screen is a
script that registers itself with `defineScreen()`, with its HTML written inside it.

## The prototype

**Layout.** The left panel holds the controls; the screen sits in a phone or browser frame
on the right. Under 1000px the panel becomes a drawer and the frame becomes the whole
screen. Inside the frame is the design, greyscale. Outside it is the instrument, dark, and
colour is allowed there as a measuring tool only.

**The panel, top to bottom:**

1. A sticky top bar that stays put while the panel scrolls: **Mobile / Desktop** and
   **Annotations**, with a one-line hint that the notes are at the bottom.
2. The title and a line on what is being compared, with a link to every iteration.
3. **Screens**: one button per screen file.
4. **Options** for the chosen screen, each with a status tag: Exploring, Chosen, Not chosen.
5. The screen's own controls, if it has any (a state switch, a sheet height).
6. **Readout**: measured values only.
7. **Questions**: open questions for the owner.
8. **Notes**: numbered to match the markers on the screen. Annotations hides both.

**A screen file:**

```js
/* option-explorer screen: explore */
defineScreen('explore', {
  name: 'Explore',
  controls: [{ key:'sheet', label:'Sheet height',                    // optional
               options:[['medium','Medium'], ['large','Large']] }],
  options: {
    A: { name:'A. Map first', status:'exploring', claim:'What it claims, in a sentence.',
         render: v => `...mobile screen HTML, v.sheet is the control value...`,
         renderDesktop: v => '...',          // optional, only with a desktop design
         after: (body, v) => {},             // optional, wire up taps; OE.set('sheet','large')
         readout: [{l:'Taps to goal', v:'2', s:'How it was measured'}],  // or (body, v) => rows
         notes: [['Title', 'Detail']],       // numbered to match mk(1), mk(2)...
         questions: ['Open question'] },
  }
});
```

The full contract is in the comment at the top of `prototype/shell.js`. `mk(n)` inside any
positioned element places marker n. Options are never deleted: change `status` instead, so
every direction explored stays one click away. Styles for one screen go in that screen's
section of `design.css`.

**Desktop.** A browser frame up to 1180px wide, above a 1000px viewport only. A mobile
screen is never stretched to fill it: an option with `renderDesktop()` fills the frame with
that layout, one without keeps its phone screen at phone width, centred.

**URL parameters** open a specific state, which is how frozen copies open where they were:
`?screen=home&option=B&device=desktop&annot=0`, plus any control key, e.g. `&sheet=large`.

## The record

Every iteration is frozen into `explorations/` with why it was made, what it aimed for, what
happened to it and the owner's own words. Open `explorations/index.html` to browse it; each
entry shows its frozen copy beside it.

```
python3 explorations/freeze.py --screen home --option B --title "B2: shorter list"
python3 explorations/freeze.py --check
```

`freeze.py` bundles the prototype and every file it loads into one self-contained HTML file
in `explorations/<screen>/`, so a frozen copy never changes when the screen files do. It adds
an entry to `records.js` and marks that option's previous entry as replaced. The why, aim
and outcome start as `TODO` and are filled in afterwards. `--check` says whether anything has
changed since the last freeze, which catches an iteration nobody recorded.
