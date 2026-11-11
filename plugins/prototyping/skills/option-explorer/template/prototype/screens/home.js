/* option-explorer screen: home. One file per screen; edit only this file to
   change this screen. Shared styles go in prototype/design.css. */
defineScreen('home', {
  name: 'Home',
  // Optional: switches shown in the panel only for this screen. Their values
  // reach render(v) as v.<key>, and the screen can change them with OE.set().
  controls: [
    { key:'state', label:'State', options:[['default','Default'], ['empty','Empty']] }
  ],
  options: {
    A: {
      name: 'A. Option name', status: 'exploring',
      claim: 'What this option claims, in a sentence.',
      readout: [{l:'Taps to goal', v:'2', s:'Counted from the screen, not estimated'}],
      notes: [['Module one', 'Why it is first.'], ['Module two', 'What it replaces.']],
      questions: ['Something only the owner can decide.'],
      render: v => v.state === 'empty'
        ? ph('Nothing here yet', 'The empty state for this option', 1)
        : ph('Module one', 'Replace with the real screen', 1) + ph('Module two', 'Keep to what a screen would show', 2),
      renderDesktop: v => `<div class="dsk">${ph('Navigation', 'Side nav on desktop')}
        <div class="dsk-main">${ph('Module one', 'Spans the full width', 1, 'wide')}${ph('Module two', 'Side by side', 2)}${ph('Module three', 'on desktop')}</div></div>`
    },
    B: {
      name: 'B. Competing option', status: 'notchosen',
      claim: 'The competing claim.',
      notes: [['Module one', 'Same content, different structure.']],
      render: v => ph('Module one', 'Different structure, same content', 1)
    }
  }
});
