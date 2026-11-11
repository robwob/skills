# Option explorer template

A prototype file for comparing structural options across several screens, plus a record of
every iteration. Plain HTML, no dependencies, no build step. Open the files directly in a
browser.

```
index.html               the prototype: screens, options, the latest version of each
explorations/
  index.html             the record viewer: every iteration, frozen, with its reasons
  records.js             the record entries (JSON after the "=")
  freeze.py              freezes the prototype into the record
  <screen>/NN-name.html  frozen copies (written by freeze.py, never edited)
  .autosave/             optional safety-net snapshots (keep out of git)
```

## The prototype

**Layout.** The left panel holds the controls; the screen sits in a phone or browser frame
on the right. Under 1000px the panel becomes a drawer and the frame becomes the whole
screen. Inside the frame is the design, greyscale. Outside it is the instrument, dark, and
colour is allowed there as a measuring tool only.

**The panel, top to bottom:**

1. A sticky top bar that stays put while the panel scrolls: **Mobile / Desktop** and
   **Annotations**, with a one-line hint that the notes are at the bottom.
2. The title and a line on what is being compared, with a link to every iteration.
3. **Screens**: one button per screen in the file.
4. **Options** for the chosen screen, each with a status tag: Exploring, Chosen, Not chosen.
5. Any project-specific controls (a state switch for one screen, for example).
6. **Readout**: measured values only.
7. **Questions**: open questions for the owner.
8. **Notes**: numbered to match the markers on the screen. Annotations hides both.

**Desktop.** A browser frame up to 1180px wide, above a 1000px viewport only. A mobile
screen is never stretched to fill it: an option with `renderDesktop()` fills the frame with
that layout, one without keeps its phone screen at phone width, centred.

**URL parameters** open a specific state, which is how frozen copies open where they were:
`?screen=home&option=B&device=desktop&annot=0`.

**To use.** Edit `PROJECT` and `SCREENS` at the bottom of `index.html` and delete the
placeholder screens:

```js
const SCREENS = {
  home: { name:'Home', options:{
    A: { name:'A. Option name', status:'exploring', claim:'What it claims, in a sentence.',
         render:() => '...mobile screen HTML...',
         renderDesktop:() => '...desktop layout HTML...',     // optional
         readout:[{l:'Taps to goal', v:'2', s:'How it was measured'}],  // optional
         notes:[['Title','Detail']],                          // optional, matches mk(1)...
         questions:['Open question'] },                       // optional
  }},
};
```

Put `mk(1)`, `mk(2)` inside any positioned element on the screen to place a numbered
marker. Options are never deleted: change `status` instead, so every direction explored
stays one click away.

## The record

Every iteration is frozen into `explorations/` with why it was made, what it aimed for, what
happened to it and the owner's own words. Open `explorations/index.html` to browse it; each
entry shows its frozen copy beside it.

```
python3 explorations/freeze.py --screen home --option B --title "B2: shorter list"
python3 explorations/freeze.py --check
```

`freeze.py` copies the prototype into `explorations/<screen>/`, adds an entry to
`records.js` and marks that option's previous entry as replaced. The why, aim and outcome
start as `TODO` and are filled in afterwards. `--check` says whether the prototype has
changed since the last freeze, which catches an iteration nobody recorded. Freeze after
every change, so the record is complete without anyone remembering to save.
