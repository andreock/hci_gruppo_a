#!/usr/bin/env node
/* Il sito funziona aperto direttamente dal disco (file://), senza server (Istruzioni.md §7, R-130)?
   Uso (dalla cartella website/tools): node verifica-file.js → stampa gli esiti e li aggiunge a docs/verifiche/percorsi.md */
const fs = require("fs"); const path = require("path"); const { chromium } = require("playwright");
const SITE = path.resolve(__dirname, ".."); const F = (p) => "file://" + path.join(SITE, p);
const BROWSER = process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } :
  (fs.existsSync("/usr/bin/chromium") ? { executablePath: "/usr/bin/chromium" } : { channel: "chrome" });
const esiti = []; const ok = (n, c) => { esiti.push([n, !!c]); console.log((c ? "OK  " : "NO  ") + n); };
(async () => {
  const b = await chromium.launch(BROWSER); const page = await b.newPage(); const err = [];
  page.on("pageerror", (e) => err.push(e.message));
  await page.goto(F("progetti.html?stato=in-corso")); await page.waitForTimeout(150);
  ok("file:// · i filtri si applicano dalla URL", /Mostrati 4 di 10/.test(await page.textContent("[data-conteggio]")));
  await page.goto(F("cerca.html?q=clima"));
  ok("file:// · la ricerca funziona", /progett/.test(await page.textContent("[data-risultati-titolo]")));
  await page.goto(F("donazione.html?progetto=clima-giovani&ricompensa=r30"));
  ok("file:// · la donazione si apre con il progetto", await page.isVisible("[data-don-app]"));
  await page.click('[data-passo="1"] button[type=submit]'); await page.waitForSelector('[data-passo="2"]:not([hidden])');
  ok("file:// · si passa al passo 2 (history.pushState)", /passo=2/.test(page.url()));
  await page.fill("#nome", "Luca"); await page.goBack(); await page.waitForTimeout(150); await page.goForward(); await page.waitForTimeout(150);
  ok("file:// · i dati restano tornando avanti e indietro (sessionStorage)", (await page.inputValue("#nome")) === "Luca");
  await page.goto(F("en/faq.html#faq-anonimo")); await page.waitForTimeout(150);
  ok("file:// · versione inglese e FAQ aperta da ancora", await page.evaluate(() => document.getElementById("faq-anonimo").open));
  await page.goto(F("progetto-alveari-sani.html"));
  ok("file:// · le date relative sono ricalcolate", (await page.getAttribute("time[data-rel]", "datetime")) !== null);
  ok("file:// · nessun errore JavaScript", err.length === 0);
  await b.close();
  const md = path.join(SITE, "docs/verifiche/percorsi.md"); let t = fs.readFileSync(md, "utf8").replace(/\n## Senza server[\s\S]*$/, "");
  t += `\n## Senza server (file://)\n\nGenerato da \`tools/verifica-file.js\`: le stesse funzioni aprendo i file direttamente dal disco, come nello zip della consegna.\n\n| Controllo | Esito |\n|---|---|\n` + esiti.map(([n, c]) => `| ${n} | ${c ? "superato" : "**NON superato**"} |`).join("\n") + "\n";
  fs.writeFileSync(md, t);
})();
