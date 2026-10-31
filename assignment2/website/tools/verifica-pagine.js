#!/usr/bin/env node
/* Verifica automatica di tutte le pagine di ideaBlume (italiano ed inglese).
   - errori JavaScript e messaggi di errore nella console
   - un solo h1, titolo della pagina univoco
   - nessuno scorrimento orizzontale a 320 px (WCAG 1.4.10)
   - axe-core con le regole WCAG 2.0/2.1/2.2 livello A e AA
   Uso (dalla cartella website/tools):  npm install  &&  node verifica-pagine.js
   Usa Google Chrome installato (channel "chrome") e un server statico locale (python3 -m http.server). Scrive docs/verifiche/axe.md e axe.json. */
const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { spawn } = require("child_process");
const PORTA = 8765;
// Server statico locale con il sito in una sottocartella (/website/), come su GitHub Pages.
// Da file:// axe-core non può rileggere i fogli di stile (CORS) e segnalerebbe errori estranei al sito.
const BASE = `http://127.0.0.1:${PORTA}/website/`;

const SITE = path.resolve(__dirname, "..");
const AXE = fs.readFileSync(require.resolve("axe-core/axe.min.js"), "utf8");
const pagine = []
  .concat(fs.readdirSync(SITE).filter((f) => f.endsWith(".html")).map((f) => f))
  .concat(fs.readdirSync(path.join(SITE, "en")).filter((f) => f.endsWith(".html")).map((f) => "en/" + f))
  .sort();

(async () => {
  const server = spawn("python3", ["-m", "http.server", String(PORTA), "--bind", "127.0.0.1", "--directory", path.resolve(SITE, "..")], { stdio: "ignore" });
  await new Promise((r) => setTimeout(r, 800));
  const browser = await chromium.launch({ channel: "chrome" });
  const risultati = [];
  const titoli = {};
  for (const p of pagine) {
    const ctx = await browser.newContext({ viewport: { width: 1280, height: 900 } });
    const page = await ctx.newPage();
    const errori = [];
    page.on("pageerror", (e) => errori.push("pageerror: " + e.message));
    page.on("console", (m) => { if (m.type() === "error") errori.push("console: " + m.text()); });
    const url = BASE + p + (p.includes("donazione.html") ? "?progetto=alveari-sani" : p.includes("cerca.html") ? "?q=api" : "");
    await page.goto(url);
    await page.waitForTimeout(150);
    const info = await page.evaluate(() => ({ h1: document.querySelectorAll("h1:not([hidden] h1)").length, title: document.title, lang: document.documentElement.lang }));
    await page.addScriptTag({ content: AXE });
    const axe = await page.evaluate(async () => {
      const r = await window.axe.run(document, { runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"] } });
      return r.violations.map((v) => ({ id: v.id, impact: v.impact, help: v.help, nodes: v.nodes.length, target: v.nodes.slice(0, 3).map((n) => n.target.join(" ")) }));
    });
    await page.setViewportSize({ width: 320, height: 800 });
    await page.waitForTimeout(100);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    (titoli[info.title] = titoli[info.title] || []).push(p);
    risultati.push({ pagina: p, errori, h1: info.h1, titolo: info.title, lunghezza_titolo: info.title.length, lang: info.lang, overflow320: overflow, axe });
    await ctx.close();
  }
  await browser.close();
  server.kill();

  const duplicati = Object.entries(titoli).filter(([t, ps]) => ps.length > 1 && !ps.some((x) => x.endsWith("404.html")));
  const tot = { pagine: risultati.length, errori_js: 0, h1_non_1: 0, overflow: 0, titoli_lunghi: 0, axe: { critical: 0, serious: 0, moderate: 0, minor: 0 } };
  risultati.forEach((r) => {
    tot.errori_js += r.errori.length; if (r.h1 !== 1) tot.h1_non_1++; if (r.overflow320 > 0) tot.overflow++; if (r.lunghezza_titolo > 60) tot.titoli_lunghi++;
    r.axe.forEach((v) => { tot.axe[v.impact] = (tot.axe[v.impact] || 0) + 1; });
  });
  const out = path.join(SITE, "docs/verifiche");
  fs.mkdirSync(out, { recursive: true });
  fs.writeFileSync(path.join(out, "axe.json"), JSON.stringify({ data: new Date().toISOString(), tot, duplicati, risultati }, null, 2));
  let md = `# Verifica automatica delle pagine\n\nGenerato da \`tools/verifica-pagine.js\` il ${new Date().toLocaleString("it-IT")} con Google Chrome (Playwright) e axe-core ${require("axe-core/package.json").version}, regole WCAG 2.0, 2.1 e 2.2 livello A e AA.\n\n`;
  md += `## Sintesi\n\n| Controllo | Esito |\n|---|---|\n| Pagine controllate (IT + EN) | ${tot.pagine} |\n| Errori JavaScript o di console | ${tot.errori_js} |\n| Pagine senza esattamente un \`h1\` | ${tot.h1_non_1} |\n| Pagine con scorrimento orizzontale a 320 px | ${tot.overflow} |\n| Titoli di pagina oltre 60 caratteri | ${tot.titoli_lunghi} |\n| Titoli duplicati (esclusa la 404) | ${duplicati.length} |\n| Violazioni axe critiche / gravi / moderate / minori | ${tot.axe.critical} / ${tot.axe.serious} / ${tot.axe.moderate} / ${tot.axe.minor} |\n\n`;
  md += `## Dettaglio per pagina\n\n| Pagina | Titolo | h1 | Overflow 320 px | Errori JS | Violazioni axe |\n|---|---|---|---|---|---|\n`;
  risultati.forEach((r) => { md += `| \`${r.pagina}\` | ${r.titolo} | ${r.h1} | ${r.overflow320} px | ${r.errori.length} | ${r.axe.length ? r.axe.map((v) => `${v.id} (${v.impact}, ${v.nodes})`).join("; ") : "nessuna"} |\n`; });
  const errs = risultati.filter((r) => r.errori.length);
  if (errs.length) { md += `\n## Errori\n\n`; errs.forEach((r) => { md += `- \`${r.pagina}\`: ${r.errori.join(" · ")}\n`; }); }
  const viol = risultati.filter((r) => r.axe.length);
  if (viol.length) { md += `\n## Violazioni axe\n\n`; viol.forEach((r) => r.axe.forEach((v) => { md += `- \`${r.pagina}\` · **${v.id}** (${v.impact}): ${v.help} → ${v.target.join(", ")}\n`; })); }
  fs.writeFileSync(path.join(out, "axe.md"), md);
  console.log(JSON.stringify(tot), "duplicati:", duplicati.length);
  viol.forEach((r) => r.axe.forEach((v) => console.log(r.pagina, v.id, v.impact, v.target.join(" | "))));
  errs.forEach((r) => console.log(r.pagina, r.errori.join(" · ")));
  risultati.filter((r) => r.overflow320 > 0 || r.h1 !== 1).forEach((r) => console.log("LAYOUT", r.pagina, "overflow", r.overflow320, "h1", r.h1));
})();
