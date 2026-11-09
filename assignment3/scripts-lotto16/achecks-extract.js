() => { const out = [];
for (const pane of ['achecker-errors', 'achecker-warnings']) {
  const root = document.getElementById(pane); if (!root) continue;
  for (const card of root.querySelectorAll('.mdl-card')) {
    const a = card.querySelector('a[href*="suggestion.php?id="]');
    const id = a ? a.href.match(/id=(\d+)/)[1] : null;
    const msg = card.querySelector('.mdl-card__title-text').innerText.trim();
    const li = [...card.querySelectorAll('li')].find(l => /Line number/.test(l.innerText));
    const line = li ? parseInt(li.querySelector('.imdl-list__item-secondary-content').innerText) : null;
    const c = card.cloneNode(true); c.querySelector('.mdl-card__title')?.remove(); c.querySelector('ul')?.remove();
    const rest = c.textContent.replace(/\s+/g, ' ').trim();
    out.push({ id, pane, msg, line, rest });
  } }
return out; }
