/* option-explorer screen: detail. One file per screen; edit only this file to
   change this screen. Shared styles go in prototype/design.css. */
defineScreen('detail', {
  name: 'Detail',
  options: {
    A: {
      name: 'A. Only option so far', status: 'chosen',
      claim: 'A screen with one option is fine.',
      render: v => ph('Detail', 'A second screen in the same prototype')
    }
  }
});
