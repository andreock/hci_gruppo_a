// Stampa relazione.html in relazione.pdf con Chromium headless (Playwright), PDF taggato con segnalibri.
// Uso: node genera_pdf.js [relazione.html] [relazione.pdf]
const path = require("path");
function playwright() {
  for (const c of [process.env.PLAYWRIGHT_DIR, "/tmp/a11y-dopo/assignment2/website/tools/node_modules/playwright",
    path.join(__dirname, "..", "..", "..", "assignment2", "website", "tools", "node_modules", "playwright"), "playwright"]) {
    if (!c) continue;
    try { return require(c); } catch (e) { /* prova il successivo */ }
  }
  console.error("Playwright non trovato: npm --prefix assignment2/website/tools ci"); process.exit(2);
}
(async () => {
  const dir = path.resolve(__dirname, "..");
  const html = path.resolve(process.argv[2] || path.join(dir, "relazione.html"));
  const pdf = path.resolve(process.argv[3] || path.join(dir, "relazione.pdf"));
  const { chromium } = playwright();
  let browser;
  try { browser = await chromium.launch(); } catch (e) { browser = await chromium.launch({ channel: "chrome" }); }
  const page = await browser.newPage();
  await page.goto("file://" + html, { waitUntil: "networkidle" });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: pdf, format: "A4", printBackground: true, preferCSSPageSize: true,
    displayHeaderFooter: false,
    tagged: true, outline: true,
  });
  await browser.close();
  console.log("PDF:", pdf);
})().catch((e) => { console.error(e); process.exit(1); });
