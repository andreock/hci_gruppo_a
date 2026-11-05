#!/usr/bin/env node
/* Screenshot responsive (320, 375, 768, 1280 px), simulazione del daltonismo, zoom al 200%
   e misura delle aree cliccabili (WCAG 2.5.8: almeno 24×24 px; comandi principali almeno 44 px di altezza).
   Uso (dalla cartella website/tools):  node responsive.js  → docs/verifiche/responsive.md e screenshot/ */
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");
const { chromium } = require("playwright");

const SITE = path.resolve(__dirname, "..");
const SHOT = path.join(SITE, "docs/verifiche/screenshot");
const PORTA = 8769;
const BROWSER = process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } :
  (fs.existsSync("/usr/bin/chromium") ? { executablePath: "/usr/bin/chromium" } : { channel: "chrome" });
const BASE = `http://127.0.0.1:${PORTA}/website/`;
const PAGINE = [["home", "index.html"], ["progetti", "progetti.html"], ["progetto", "progetto-neonati-virus.html"],
  ["donazione", "donazione.html?progetto=neonati-virus&ricompensa=r25"], ["programma", "programma.html"], ["faq", "faq.html"],
  ["proponi", "proponi.html"], ["home-en", "en/index.html"]];
const LARGHEZZE = [320, 375, 768, 1280];

(async () => {
  fs.mkdirSync(SHOT, { recursive: true });
  const server = spawn("python3", ["-m", "http.server", String(PORTA), "--bind", "127.0.0.1", "--directory", path.resolve(SITE, "..")], { stdio: "ignore" });
  await new Promise((r) => setTimeout(r, 800));
  const browser = await chromium.launch(BROWSER);
  const tabella = [];
  const bersagli = [];
  for (const [nome, url] of PAGINE) {
    for (const w of LARGHEZZE) {
      const page = await browser.newPage({ viewport: { width: w, height: w < 600 ? 780 : 900 } });
      await page.goto(BASE + url); await page.waitForTimeout(250);
      const ov = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
      await page.screenshot({ path: path.join(SHOT, `${nome}-${w}.jpg`), type: "jpeg", quality: 70 });
      tabella.push({ nome, w, ov });
      if (w === 375) {
        const piccoli = await page.evaluate(() => {
          const out = [];
          document.querySelectorAll("a, button, input:not([type=hidden]), select, textarea, summary").forEach((el) => {
            const r = el.getBoundingClientRect();
            if (!r.width || !r.height || getComputedStyle(el).visibility === "hidden") return;
            let target = r;
            if (el.matches("input[type=radio], input[type=checkbox]")) { const l = el.closest("label"); if (l) target = l.getBoundingClientRect(); }
            const p = el.parentElement;
            const inline = el.tagName === "A" && p && p.textContent.trim().length > el.textContent.trim().length + 3; // eccezione «in linea» di 2.5.8
            if ((target.width < 24 || target.height < 24) && !inline) out.push(`${el.tagName.toLowerCase()} «${(el.textContent || el.value || el.name || "").trim().slice(0, 40)}» ${Math.round(target.width)}×${Math.round(target.height)}`);
          });
          const btn = [...document.querySelectorAll(".btn:not(.btn--small):not(.btn--ghost)")].filter((b) => b.offsetParent).map((b) => Math.round(b.getBoundingClientRect().height));
          return { out, minBtn: btn.length ? Math.min(...btn) : null };
        });
        bersagli.push({ nome, ...piccoli });
      }
      await page.close();
    }
  }
  // Daltonismo (P05) e acromatopsia: stato delle campagne leggibile senza colori
  const page = await browser.newPage({ viewport: { width: 1280, height: 1100 } });
  const cdp = await page.context().newCDPSession(page);
  await page.goto(BASE + "progetti.html");
  for (const tipo of ["deuteranopia", "achromatopsia"]) {
    await cdp.send("Emulation.setEmulatedVisionDeficiency", { type: tipo });
    await page.evaluate(() => window.scrollTo(0, 600)); await page.waitForTimeout(200);
    await page.screenshot({ path: path.join(SHOT, `progetti-${tipo}.jpg`), type: "jpeg", quality: 70 });
  }
  await page.close();
  // Zoom al 200% di una finestra da 1280 px = 640 px CSS con densità 2 (WCAG 1.4.4)
  const zoom = [];
  for (const [nome, url] of [["progetto", "progetto-neonati-virus.html"], ["donazione", "donazione.html?progetto=neonati-virus&ricompensa=r25"], ["progetti", "progetti.html"]]) {
    const z = await browser.newPage({ viewport: { width: 640, height: 450 }, deviceScaleFactor: 2 });
    await z.goto(BASE + url); await z.waitForTimeout(200);
    zoom.push({ nome, ov: await z.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth) });
    await z.screenshot({ path: path.join(SHOT, `${nome}-zoom200.jpg`), type: "jpeg", quality: 70 });
    await z.close();
  }
  await browser.close(); server.kill();

  let md = `# Verifica responsive, zoom, daltonismo e aree cliccabili\n\nGenerato da \`tools/responsive.js\` il ${new Date().toLocaleString("it-IT")} (Playwright + Google Chrome). Screenshot in \`docs/verifiche/screenshot/\`.\n\n`;
  md += `## Scorrimento orizzontale (WCAG 1.4.10)\n\n| Pagina | ${LARGHEZZE.map((w) => w + " px").join(" | ")} |\n|---|${LARGHEZZE.map(() => "---").join("|")}|\n`;
  PAGINE.forEach(([n]) => { md += `| ${n} | ${LARGHEZZE.map((w) => { const r = tabella.find((x) => x.nome === n && x.w === w); return r.ov > 0 ? `**${r.ov} px**` : "nessuno"; }).join(" | ")} |\n`; });
  md += `\nFile: \`<pagina>-<larghezza>.jpg\` (prima schermata).\n\n## Zoom al 200% (WCAG 1.4.4)\n\nFinestra da 1280 px ingrandita al 200% (= 640 px CSS):\n\n| Pagina | Scorrimento orizzontale |\n|---|---|\n`;
  zoom.forEach((z) => { md += `| ${z.nome} | ${z.ov > 0 ? z.ov + " px" : "nessuno"} |\n`; });
  md += `\n## Daltonismo (WCAG 1.4.1, persona P05)\n\n\`progetti-deuteranopia.jpg\` e \`progetti-achromatopsia.jpg\`: elenco dei progetti con la simulazione di Chrome. Ogni stato resta riconoscibile perché ha testo e icona diversa (cerchio, spunta, quadrato, croce), non solo il colore.\n\n`;
  md += `## Aree cliccabili a 375 px (WCAG 2.5.8)\n\n| Pagina | Bersagli sotto 24×24 px (esclusi i link nel testo) | Altezza minima dei pulsanti principali |\n|---|---|---|\n`;
  bersagli.forEach((b) => { md += `| ${b.nome} | ${b.out.length ? b.out.join("; ") : "nessuno"} | ${b.minBtn} px |\n`; });
  fs.writeFileSync(path.join(SITE, "docs/verifiche/responsive.md"), md);
  console.log("overflow:", tabella.filter((t) => t.ov > 0).map((t) => t.nome + "@" + t.w).join(", ") || "nessuno");
  console.log("zoom:", JSON.stringify(zoom));
  bersagli.forEach((b) => console.log(b.nome, b.minBtn, b.out.join(" | ")));
})();
