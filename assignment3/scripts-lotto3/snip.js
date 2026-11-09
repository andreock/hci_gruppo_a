async (page) => {
  const fs = require('fs');
  const dir = '/Users/andreock/Desktop/hci_gruppo_a/assignment2/website/a11y/tmp-lotto3/';
  const all = JSON.parse(fs.readFileSync(dir + 'xp-all.json', 'utf8'));
  const base = 'https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/';
  const p2 = await page.context().newPage();
  const res = {};
  for (const [p, xs] of Object.entries(all)) {
    await p2.goto(base + p + '.html', { waitUntil: 'load' });
    res[p] = await p2.evaluate((xs) => {
      const out = {};
      for (const x of xs) {
        // MAUVE usa XPath senza namespace: per gli svg serve local-name()
        const q = x.replace(/\/(svg|path|circle|rect|g|use|line|polyline|polygon)(\[\d+\])?/g, (m, t, i) => `/*[local-name()='${t}']${i || ''}`);
        let el = null;
        try { el = document.evaluate(q, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; } catch (e) {}
        if (!el) { out[x] = null; continue; }
        const h = el.outerHTML;
        const open = h.slice(0, h.indexOf('>') + 1);
        out[x] = (el.children.length === 0 && h.length <= 200) ? h : open;
      }
      return out;
    }, xs);
  }
  await p2.close();
  fs.writeFileSync(dir + 'snip.json', JSON.stringify(res, null, 1));
  return Object.fromEntries(Object.entries(res).map(([p, o]) => [p, Object.values(o).filter(v => v === null).length + ' non risolti su ' + Object.keys(o).length]));
}
