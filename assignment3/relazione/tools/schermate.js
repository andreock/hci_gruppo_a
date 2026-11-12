// Schermate PRIMA/DOPO per la relazione. Serve i due worktree già compilati:
//   /tmp/a11y-prima (adc8f85) su :8801 e /tmp/a11y-dopo (HEAD) su :8802.
// Uso: node schermate.js   (Playwright da /tmp/a11y-dopo/assignment2/website/tools/node_modules)
const path = require("path"), fs = require("fs"), { spawn } = require("child_process");
const { chromium } = (() => { for (const c of ["/tmp/a11y-dopo/assignment2/website/tools/node_modules/playwright", require("path").join(__dirname, "..", "..", "..", "assignment2", "website", "tools", "node_modules", "playwright")]) { try { return require(c); } catch (e) { /* prova il successivo */ } } throw new Error("Playwright non trovato"); })();
const OUT = path.resolve(__dirname, "..", "img");
const VERS = { prima: ["/tmp/a11y-prima/assignment2", 8801], dopo: ["/tmp/a11y-dopo/assignment2", 8802] };
const albero = {};
(async () => {
  const server = Object.values(VERS).map(([dir, porta]) =>
    spawn("python3", ["-m", "http.server", String(porta), "--bind", "127.0.0.1", "--directory", dir], { stdio: "ignore" }));
  await new Promise((r) => setTimeout(r, 900));
  const browser = await chromium.launch({ channel: "chrome" });
  for (const [v, [, porta]] of Object.entries(VERS)) {
    const B = `http://127.0.0.1:${porta}/website/`;
    const ctx = await browser.newContext({ viewport: { width: 1100, height: 700 }, deviceScaleFactor: 2, reducedMotion: "reduce" });
    const page = await ctx.newPage();
    // 1. Albero di accessibilità del collegamento-logo
    await page.goto(B + "index.html");
    albero["logo_" + v] = await page.locator("a.brand").ariaSnapshot();
    albero["logo_nome_" + v] = await page.evaluate(() => {
      const a = document.querySelector("a.brand"); return { aria_label: a.getAttribute("aria-label"), testo: a.textContent.replace(/\s+/g, " ").trim() };
    });
    // 2. Focus del link «Salta al contenuto», tema chiaro
    await page.evaluate(() => { document.documentElement.setAttribute("data-theme", "light"); });
    await page.waitForTimeout(400);
    await page.keyboard.press("Tab");
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(OUT, `skip-${v}.png`), clip: { x: 0, y: 0, width: 330, height: 76 } });
    // 2b. tema scuro
    await page.goto(B + "index.html");
    await page.evaluate(() => { document.documentElement.setAttribute("data-theme", "dark"); });
    await page.waitForTimeout(400);
    await page.keyboard.press("Tab");
    await page.waitForTimeout(400);
    await page.screenshot({ path: path.join(OUT, `skip-scuro-${v}.png`), clip: { x: 0, y: 0, width: 330, height: 76 } });
    // 3. Bersagli della pagina «Proponi» a 375 px, con contorno dell'area cliccabile
    await page.setViewportSize({ width: 375, height: 800 });
    await page.goto(B + "proponi.html");
    await page.evaluate(() => document.documentElement.setAttribute("data-theme", "light"));
    await page.addStyleTag({ content: ".howto > li > p > a:only-child { outline: 1.5px dashed #a3271a; outline-offset: 0; }" });
    const link = page.locator(".howto > li > p > a:only-child").first();
    await link.scrollIntoViewIfNeeded();
    await page.waitForTimeout(200);
    const bb = await link.boundingBox();
    albero["bersaglio_" + v] = await page.$$eval(".howto > li > p > a:only-child", (as) => as.map((a) => { const r = a.getBoundingClientRect(); return [a.textContent.trim(), Math.round(r.width), Math.round(r.height)]; }));
    await page.screenshot({ path: path.join(OUT, `bersaglio-${v}.png`), clip: { x: 0, y: Math.max(0, bb.y - 40), width: 375, height: 80 } });
    // 4. Intestazione dei risultati di ricerca nell'albero di accessibilità
    await page.setViewportSize({ width: 1100, height: 700 });
    await page.goto(B + "cerca.html?q=api");
    await page.waitForTimeout(400);
    albero["cerca_" + v] = await page.locator("main").ariaSnapshot();
    albero["cerca_heading_" + v] = await page.evaluate(() => { const h = document.querySelector(".result-count"); return { role: h.getAttribute("role"), parentRole: h.parentElement.getAttribute("role"), testo: h.textContent.trim() }; });
    // 5. Marchio: header e footer (nessun cambiamento visivo atteso)
    await page.goto(B + "index.html");
    await page.evaluate(() => document.documentElement.setAttribute("data-theme", "light"));
    await page.waitForTimeout(300);
    const brand = await page.locator("a.brand").boundingBox();
    await page.screenshot({ path: path.join(OUT, `marchio-${v}.png`), clip: { x: brand.x - 6, y: brand.y - 6, width: brand.width + 12, height: brand.height + 12 } });
    await ctx.close();
  }
  await browser.close();
  server.forEach((s) => s.kill());
  fs.writeFileSync(path.join(OUT, "alberi.json"), JSON.stringify(albero, null, 1));
  console.log(JSON.stringify(albero, null, 1));
})().catch((e) => { console.error(e); process.exit(1); });
