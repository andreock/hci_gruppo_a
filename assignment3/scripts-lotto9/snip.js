() => { const xs = window.__xs; const out = {};
for (const x of xs) {
  const q = x.replace(/\/(svg|path|circle|rect|g|use|line|polyline|polygon)(\[\d+\])?/g, (m, t, i) => "/*[local-name()='" + t + "']" + (i || ''));
  let el = null;
  try { el = document.evaluate(q, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; } catch (e) {}
  if (!el) { out[x] = null; continue; }
  const h = el.outerHTML; const open = h.slice(0, h.indexOf('>') + 1);
  out[x] = (el.children.length === 0 && h.length <= 200) ? h : open;
}
return out; }
