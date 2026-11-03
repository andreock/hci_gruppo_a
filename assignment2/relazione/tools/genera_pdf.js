// Stampa relazione.html in PDF con Chromium headless (Playwright).
// Uso: node genera_pdf.js <file.html> <file.pdf>
// Playwright è quello già installato per le verifiche del sito (website/tools/node_modules).
const path = require("path");

function caricaPlaywright() {
  const candidati = [
    path.join(__dirname, "..", "..", "website", "tools", "node_modules", "playwright"),
    "playwright",
  ];
  for (const c of candidati) {
    try { return require(c); } catch (e) { /* prova il successivo */ }
  }
  console.error("Playwright non trovato: esegui `cd website/tools && npm install`.");
  process.exit(2);
}

(async () => {
  const [html, pdf] = process.argv.slice(2);
  const { chromium } = caricaPlaywright();
  let browser;
  try { browser = await chromium.launch(); }
  catch (e) { browser = await chromium.launch({ channel: "chrome" }); }
  const page = await browser.newPage();
  await page.goto("file://" + path.resolve(html), { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: pdf,
    format: "A4",
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: "<span></span>",
    footerTemplate:
      '<div style="width:100%;font:8pt Helvetica,Arial,sans-serif;color:#66544a;padding:0 19mm;display:flex;justify-content:space-between">' +
      '<span>Gruppo A · Uso dell\'IA in assignment 2</span>' +
      '<span>Pagina <span class="pageNumber"></span> di <span class="totalPages"></span></span></div>',
    tagged: true,
    outline: true,
  });
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
