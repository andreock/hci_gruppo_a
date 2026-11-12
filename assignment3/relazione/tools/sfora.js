// Controlla in modalità stampa (larghezza utile A4) che nessun elemento sfori a destra.
const { chromium } = (() => { for (const c of ["/tmp/a11y-dopo/assignment2/website/tools/node_modules/playwright", require("path").join(__dirname, "..", "..", "..", "assignment2", "website", "tools", "node_modules", "playwright")]) { try { return require(c); } catch (e) { /* prova il successivo */ } } throw new Error("Playwright non trovato"); })();
const path = require("path");
(async () => {
  const b = await chromium.launch({ channel: "chrome" }); const p = await b.newPage();
  await p.setViewportSize({ width: Math.round((210 - 36) / 25.4 * 96), height: 1000 });
  await p.emulateMedia({ media: "print" });
  await p.goto("file://" + path.resolve(__dirname, "..", "relazione.html"));
  const r = await p.evaluate(() => { const W = document.documentElement.clientWidth; const out = [];
    for (const el of document.querySelectorAll("main *")) { const x = el.getBoundingClientRect(); if (x.right > W + 1 && x.width) out.push([el.tagName, el.className, Math.round(x.right - W), (el.textContent || "").slice(0, 40)]); }
    return { W, sw: document.documentElement.scrollWidth, out: out.slice(0, 15) }; });
  console.log(JSON.stringify(r, null, 1)); await b.close();
})();
