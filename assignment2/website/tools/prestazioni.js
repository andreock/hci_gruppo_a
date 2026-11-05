#!/usr/bin/env node
/* Lighthouse (mobile, throttling simulato predefinito: Moto G Power, 4G lento) sulle quattro pagine
   del percorso del donatore, come in assignment1 (slide 72-78). Confronta con i valori di IdeaGinger.
   Uso (dalla cartella website/tools):  node prestazioni.js   → docs/verifiche/prestazioni.md */
const fs = require("fs");
const path = require("path");
const { spawn, execFileSync } = require("child_process");

const SITE = path.resolve(__dirname, "..");
const PORTA = 8768;
const BASE = `http://127.0.0.1:${PORTA}/website/`;
const CHROME = process.env.CHROME_PATH || (fs.existsSync("/usr/bin/chromium") ? "/usr/bin/chromium" : "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome");
const PAGINE = [
  ["Home", "index.html", null],
  ["Elenco dei progetti", "progetti.html", ["Progetti (scheda partner)", 50, 71, "16,6 s", "0,003", "60 ms"]],
  ["Pagina progetto", "progetto-neonati-virus.html", ["Mind the Climate", 41, 73, "34,1 s", "0,165", "440 ms"]],
  ["Donazione", "donazione.html?progetto=neonati-virus&ricompensa=r25", ["Donazione (di fatto la home)", 39, 74, "72,1 s", "0,478", "170 ms"]],
];
const it = (x, d = 1) => x.toFixed(d).replace(".", ",");

(async () => {
  const server = spawn("python3", ["-m", "http.server", String(PORTA), "--bind", "127.0.0.1", "--directory", path.resolve(SITE, "..")], { stdio: "ignore" });
  await new Promise((r) => setTimeout(r, 800));
  const righe = [];
  for (const [nome, url, ginger] of PAGINE) {
    const out = path.join(require("os").tmpdir(), "lh-" + url.replace(/\W/g, "_") + ".json");
    execFileSync(path.join(__dirname, "node_modules/.bin/lighthouse"), [BASE + url, "--quiet", "--output=json", "--output-path=" + out,
      "--only-categories=performance,accessibility,best-practices,seo", "--chrome-flags=--headless=new"], { env: { ...process.env, CHROME_PATH: CHROME }, stdio: "ignore" });
    const r = JSON.parse(fs.readFileSync(out, "utf8"));
    const a = r.audits, c = r.categories;
    const v = {
      nome, url, perf: Math.round(c.performance.score * 100), acc: Math.round(c.accessibility.score * 100),
      bp: Math.round(c["best-practices"].score * 100), seo: Math.round(c.seo.score * 100),
      fcp: a["first-contentful-paint"].numericValue / 1000, lcp: a["largest-contentful-paint"].numericValue / 1000,
      tbt: a["total-blocking-time"].numericValue, cls: a["cumulative-layout-shift"].numericValue, si: a["speed-index"].numericValue / 1000,
      peso: a["total-byte-weight"].numericValue / 1024, ginger,
    };
    righe.push(v);
    console.log(nome, JSON.stringify(v));
  }
  server.kill();
  let md = `# Prestazioni (Lighthouse mobile)\n\nGenerato da \`tools/prestazioni.js\` il ${new Date().toLocaleString("it-IT")} con Lighthouse ${require("lighthouse/package.json").version} e Google Chrome, impostazioni mobile predefinite (Moto G Power emulato, rete 4G lenta e CPU rallentata simulate), server statico locale.\n\n`;
  md += `| Pagina | Prestazioni | Accessibilità | Best practice | SEO | FCP | LCP | TBT | CLS | Speed Index | Peso trasferito |\n|---|---|---|---|---|---|---|---|---|---|---|\n`;
  righe.forEach((v) => { md += `| ${v.nome} | **${v.perf}** | ${v.acc} | ${v.bp} | ${v.seo} | ${it(v.fcp)} s | **${it(v.lcp)} s** | ${Math.round(v.tbt)} ms | **${it(v.cls, 3)}** | ${it(v.si)} s | ${Math.round(v.peso)} KB |\n`; });
  md += `\n## Confronto con IdeaGinger (assignment1, report del 15/10/2026, smartphone)\n\n| Pagina ideaBlume | Pagina IdeaGinger | Prestazioni | Accessibilità | LCP | CLS | TBT |\n|---|---|---|---|---|---|---|\n`;
  righe.filter((v) => v.ginger).forEach((v) => { const g = v.ginger; md += `| ${v.nome} | ${g[0]} | ${g[1]} → **${v.perf}** | ${g[2]} → **${v.acc}** | ${g[3]} → **${it(v.lcp)} s** | ${g[4]} → **${it(v.cls, 3)}** | ${g[5]} → **${Math.round(v.tbt)} ms** |\n`; });
  md += `\nObiettivi (R-122): LCP ≤ 2,5 s, CLS ≤ 0,1, INP ≤ 200 ms. Lighthouse in laboratorio non misura l'INP: si usa il TBT come indicatore (≤ 200 ms). Il server locale non comprime i file (su GitHub Pages i file sono serviti con compressione gzip), quindi i valori pubblicati possono solo migliorare.\n`;
  fs.writeFileSync(path.join(SITE, "docs/verifiche/prestazioni.md"), md);
})();
