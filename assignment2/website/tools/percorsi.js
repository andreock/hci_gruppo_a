#!/usr/bin/env node
/* Percorsi interattivi di ideaBlume, eseguiti con Playwright su Google Chrome.
   Ogni controllo è un'asserzione: il risultato (superato / NON superato) va in docs/verifiche/percorsi.md,
   gli screenshot del focus in docs/verifiche/screenshot/.
   Uso (dalla cartella website/tools):  node percorsi.js */
const fs = require("fs");
const path = require("path");
const { spawn } = require("child_process");
const { chromium } = require("playwright");

const SITE = path.resolve(__dirname, "..");
const SHOT = path.join(SITE, "docs/verifiche/screenshot");
const PORTA = 8766;
const BROWSER = process.env.CHROME_PATH ? { executablePath: process.env.CHROME_PATH } :
  (fs.existsSync("/usr/bin/chromium") ? { executablePath: "/usr/bin/chromium" } : { channel: "chrome" });
const BASE = `http://127.0.0.1:${PORTA}/website/`;
const esiti = [];
function ok(nome, cond, nota = "") { esiti.push({ nome, ok: !!cond, nota }); console.log((cond ? "OK  " : "NO  ") + nome + (nota ? " · " + nota : "")); }
async function focusInfo(page) {
  return page.evaluate(() => { const a = document.activeElement; return { tag: a.tagName, text: (a.innerText || a.value || a.getAttribute("aria-label") || "").trim().slice(0, 60), id: a.id }; });
}
async function tabFino(page, pred, max = 60) {
  for (let i = 0; i < max; i++) { await page.keyboard.press("Tab"); const f = await focusInfo(page); if (pred(f)) return f; }
  return null;
}

(async () => {
  fs.mkdirSync(SHOT, { recursive: true });
  const server = spawn("python3", ["-m", "http.server", String(PORTA), "--bind", "127.0.0.1", "--directory", path.resolve(SITE, "..")], { stdio: "ignore" });
  await new Promise((r) => setTimeout(r, 800));
  const browser = await chromium.launch(BROWSER);
  const errori = [];
  const nuova = async (vp = { width: 1280, height: 900 }) => {
    const ctx = await browser.newContext({ viewport: vp });
    const page = await ctx.newPage();
    page.on("pageerror", (e) => errori.push(e.message));
    return page;
  };

  /* 1. Percorso completo da tastiera: ricerca → progetto → donazione → conferma */
  let page = await nuova();
  await page.goto(BASE + "index.html");
  await page.keyboard.press("Tab");
  let f = await focusInfo(page);
  ok("Il primo Tab porta a «Salta al contenuto»", /Salta al contenuto/.test(f.text));
  await page.screenshot({ path: path.join(SHOT, "tastiera-01-salta.png"), clip: { x: 0, y: 0, width: 1280, height: 200 } });
  f = await tabFino(page, (x) => x.id === "q-home");
  ok("Il campo di ricerca della home è raggiungibile da tastiera", !!f);
  await page.keyboard.type("api");
  await page.screenshot({ path: path.join(SHOT, "tastiera-02-ricerca.png") });
  await page.keyboard.press("Enter");
  await page.waitForURL(/cerca\.html\?q=api/);
  const titoloRis = await page.textContent("[data-risultati-titolo]");
  ok("La ricerca «api» trova il progetto sulle api (per inizio di parola, non «capire»)", /^1 progetto per «api»/.test(titoloRis.trim()), titoloRis);
  f = await tabFino(page, (x) => x.tag === "A" && /Alveari sani/.test(x.text));
  ok("Il risultato «Alveari sani» si raggiunge con Tab (link con nome significativo)", !!f, f && f.text);
  await page.screenshot({ path: path.join(SHOT, "tastiera-03-card-focus.png"), fullPage: false });
  await page.keyboard.press("Enter");
  await page.waitForURL(/progetto-alveari-sani/);
  f = await tabFino(page, (x) => /Sostieni il progetto/.test(x.text));
  ok("«Sostieni il progetto» si raggiunge da tastiera", !!f);
  await page.screenshot({ path: path.join(SHOT, "tastiera-04-sostieni.png") });
  // spiegazione a comparsa
  f = await tabFino(page, (x) => /tutto o niente/.test(x.text), 10);
  await page.keyboard.press("Enter");
  ok("La spiegazione «tutto o niente» si apre con Invio", await page.isVisible("#tt-regola"));
  await page.keyboard.press("Escape");
  ok("La spiegazione si chiude con Esc", !(await page.isVisible("#tt-regola")));
  // torna al pulsante Sostieni
  await page.focus("a.btn--block");
  await page.keyboard.press("Enter");
  await page.waitForURL(/donazione\.html\?progetto=alveari-sani/);
  ok("La donazione si apre con il progetto nella URL", true);
  ok("Indicatore dei passi: passo 1 di 5", /Passo 1 di 5/.test(await page.textContent("[data-passo-testo]")));
  // passo 1: donazione libera con importo troppo basso
  await page.focus("#sc-libera"); await page.keyboard.press("Space");
  await page.fill("#importo", "3");
  await page.keyboard.press("Tab");
  const errImp = await page.textContent("#importo-e").catch(() => "");
  ok("Importo sotto il minimo: errore in linea quando si lascia il campo", /minimo è €\s5/.test(errImp), errImp);
  ok("Il campo con errore ha aria-invalid e aria-describedby", (await page.getAttribute("#importo", "aria-invalid")) === "true" && /importo-e/.test(await page.getAttribute("#importo", "aria-describedby")));
  await page.screenshot({ path: path.join(SHOT, "donazione-errore-importo.png") });
  await page.focus("#importo"); await page.fill("#importo", "20");
  await page.dispatchEvent("#importo", "input");
  ok("L'errore sparisce appena l'importo è corretto", await page.isHidden("#importo-e"));
  await page.keyboard.press("Enter");
  await page.waitForSelector('[data-passo="2"]:not([hidden])');
  ok("Invio porta al passo 2 e il focus va al titolo del passo", (await focusInfo(page)).tag === "H2");
  ok("Il riepilogo mostra 20 €", /20/.test(await page.textContent("[data-sum-importo]")));
  // passo 2: invio con email errata → riepilogo degli errori
  await page.fill("#nome", "Anna"); await page.fill("#cognome", "Rossi"); await page.fill("#email", "anna.rossi@");
  await page.keyboard.press("Enter");
  ok("Con un errore compare il riepilogo in testa e riceve il focus", (await page.isVisible("[data-errori]")) && (await focusInfo(page)).tag === "DIV");
  ok("Il riepilogo contiene il link al campo Email", /Email/.test(await page.textContent("[data-errori-lista]")));
  await page.screenshot({ path: path.join(SHOT, "donazione-riepilogo-errori.png") });
  ok("Il campo email usa type=email e autocomplete=email", (await page.getAttribute("#email", "type")) === "email" && (await page.getAttribute("#email", "autocomplete")) === "email");
  await page.fill("#email", "anna.rossi@esempio.it");
  await page.keyboard.press("Enter");
  await page.waitForSelector('[data-passo="3"]:not([hidden])');
  ok("Nessuna scelta di visibilità preselezionata", !(await page.isChecked("#vis-si")) && !(await page.isChecked("#vis-no")));
  // torna indietro con il pulsante del browser: i dati restano (WCAG 3.3.7)
  await page.goBack();
  await page.waitForSelector('[data-passo="2"]:not([hidden])');
  ok("Con Indietro del browser si torna al passo 2 e i dati sono ancora lì", (await page.inputValue("#nome")) === "Anna" && (await page.inputValue("#email")) === "anna.rossi@esempio.it");
  await page.reload();
  ok("Anche dopo aver ricaricato la pagina i dati restano", (await page.inputValue("#cognome")) === "Rossi");
  await page.keyboard.press("Tab"); await page.focus("#email"); await page.keyboard.press("Enter");
  await page.waitForSelector('[data-passo="3"]:not([hidden])');
  await page.focus("#vis-no"); await page.keyboard.press("Space");
  await page.check("#privacy");
  await page.keyboard.press("Enter");
  await page.waitForSelector('[data-passo="4"]:not([hidden])');
  await page.focus("#m-paypal"); await page.keyboard.press("Space");
  ok("La commissione è mostrata accanto al metodo", /Commissione/.test(await page.textContent('[data-commissione="paypal"]')));
  await page.keyboard.press("Enter");
  await page.waitForSelector('[data-passo="5"]:not([hidden])');
  const rev = await page.textContent("[data-revisione]");
  ok("Il riepilogo finale mostra commissione e totale prima della conferma", /Commissione/.test(rev) && /Totale/.test(rev), rev.replace(/\s+/g, " ").slice(0, 160));
  ok("Nessun campo per numeri di carta", (await page.$$('[autocomplete^="cc-"]')).length === 0);
  await page.screenshot({ path: path.join(SHOT, "donazione-riepilogo.png"), fullPage: true });
  await page.focus("[data-paga]"); await page.keyboard.press("Enter");
  await page.waitForURL(/donazione-conferma\.html/, { timeout: 5000 });
  ok("La conferma mostra il codice di riferimento", /IB-\d{8}-/.test(await page.textContent("[data-codice]")));
  await page.screenshot({ path: path.join(SHOT, "donazione-conferma.png"), fullPage: true });
  await page.context().close();

  /* 2. Elenco: filtri nella URL, conteggio, ritorno nella stessa posizione */
  page = await nuova();
  await page.goto(BASE + "progetti.html");
  await page.selectOption("#f-stato", "conclusi");
  ok("Il filtro aggiorna la URL", /stato=conclusi/.test(page.url()));
  await page.waitForTimeout(150);
  const cnt = await page.textContent("[data-conteggio]");
  ok("Il conteggio dice quanti progetti sono mostrati", /Mostrati 6 di 10 progetti/.test(cnt), cnt);
  await page.selectOption("#f-ordina", "bisogno");
  /* Evita che scroll-behavior:smooth renda y0 dipendente dal momento del campionamento. */
  await page.evaluate(() => {
    document.documentElement.style.scrollBehavior = "auto";
    window.scrollTo(0, 900);
  });
  await page.waitForTimeout(50);
  const y0 = await page.evaluate(() => window.scrollY);
  const link = await page.$("[data-elenco] li:not([hidden]) .card__title a");
  /* Il click di Playwright scorre automaticamente l'elemento prima di attivarlo e
     cambierebbe la posizione che stiamo cercando di verificare. Un click DOM replica
     l'attivazione del link senza introdurre quello scroll artificiale. */
  await link.evaluate((el) => el.click());
  await page.waitForURL(/progetto-/);
  await page.goBack();
  await page.waitForTimeout(300);
  ok("Tornando indietro i filtri restano", (await page.inputValue("#f-stato")) === "conclusi" && (await page.inputValue("#f-ordina")) === "bisogno");
  const y1 = await page.evaluate(() => window.scrollY);
  ok("Tornando indietro la posizione nella pagina resta", Math.abs(y1 - y0) < 60, `${y0} → ${y1}`);
  await page.goto(BASE + "progetti.html?stato=raggiunto");
  ok("Una URL filtrata condivisa mostra solo le campagne in corso con obiettivo raggiunto", /Mostrati 1 di 10/.test(await page.textContent("[data-conteggio]")));
  await page.goto(BASE + "progetti.html?categoria=cultura&anno=2023");
  ok("Con filtri senza risultati compare un messaggio con alternative", await page.isVisible("[data-nessuno]"));
  await page.context().close();

  /* 3. Ricerca senza risultati */
  page = await nuova();
  await page.goto(BASE + "cerca.html?q=zxqw");
  ok("Ricerca senza risultati: messaggio e suggerimenti", /Nessun progetto per «zxqw»/.test(await page.textContent("[data-risultati-titolo]")) && (await page.isVisible("[data-nessun-risultato]")));
  await page.goto(BASE + "cerca.html?q=veterinaria");
  ok("La ricerca tollera singolare e plurale («veterinaria» trova Scienze Veterinarie)", /1 progetto per «veterinaria»/.test(await page.textContent("[data-risultati-titolo]")));
  await page.goto(BASE + "cerca.html?q=cofinanziamento");
  ok("La ricerca trova anche la pagina del programma", await page.isVisible('[data-pagine-elenco] a[href="programma.html"]'));
  await page.context().close();

  /* 4. Menu mobile a 375 px: Invio apre, Esc chiude, focus torna al pulsante */
  page = await nuova({ width: 375, height: 740 });
  await page.goto(BASE + "index.html");
  ok("A menu chiuso le voci non sono raggiungibili", await page.isHidden("#menu-principale a"));
  await page.focus("[data-nav-toggle]"); await page.keyboard.press("Enter");
  ok("Invio apre il menu e aria-expanded diventa true", (await page.getAttribute("[data-nav-toggle]", "aria-expanded")) === "true" && (await page.isVisible("#menu-principale a")));
  await page.screenshot({ path: path.join(SHOT, "menu-mobile-375.png") });
  await page.keyboard.press("Escape");
  ok("Esc chiude il menu e il focus torna al pulsante", (await page.isHidden("#menu-principale a")) && (await page.evaluate(() => document.activeElement.hasAttribute("data-nav-toggle"))));
  const t = await page.evaluate(() => { const r = document.querySelector("[data-nav-toggle]").getBoundingClientRect(); return [r.width, r.height]; });
  ok("Il pulsante del menu misura almeno 44×44 px", t[0] >= 44 && t[1] >= 44, t.join("×"));
  await page.context().close();

  /* 5. FAQ: ancora condivisibile e ricerca interna */
  page = await nuova();
  await page.goto(BASE + "faq.html#faq-tutto-o-niente");
  await page.waitForTimeout(200);
  ok("Aprendo faq.html#faq-tutto-o-niente la risposta è aperta", await page.evaluate(() => document.getElementById("faq-tutto-o-niente").open));
  await page.fill("[data-faq-cerca]", "anonim");
  await page.waitForTimeout(100);
  ok("La ricerca nelle FAQ filtra e annuncia il numero", /domand/.test(await page.textContent("[data-faq-conteggio]")));
  await page.context().close();

  /* 6. Versione inglese: errori in inglese e lingua conservata */
  page = await nuova();
  await page.goto(BASE + "en/donazione.html?progetto=neonati-virus&ricompensa=libera");
  await page.fill("#importo", "2"); await page.keyboard.press("Tab");
  ok("In inglese l'errore sull'importo è in inglese", /The minimum amount is €5/.test(await page.textContent("#importo-e")));
  await page.goto(BASE + "progetti.html?stato=in-corso");
  await page.click("[data-lang-switch]");
  await page.waitForURL(/en\/progetti\.html\?stato=in-corso/);
  ok("Il selettore di lingua porta alla stessa pagina in inglese con gli stessi filtri", true);
  ok("La pagina inglese ha lang=en", (await page.getAttribute("html", "lang")) === "en");
  await page.context().close();

  /* 7. Campagna conclusa: nessun controllo per donare */
  page = await nuova();
  await page.goto(BASE + "progetto-dialetti-archivio.html");
  ok("Campagna conclusa: nessun link per donare né campo importo", (await page.$$('a[href^="donazione.html"]')).length === 0 && (await page.$$("input#importo")).length === 0);
  ok("Campagna conclusa: stato scritto in testo", /Conclusa · obiettivo non raggiunto/.test(await page.textContent(".statusbox")));
  await page.goto(BASE + "donazione.html?progetto=dialetti-archivio");
  ok("Donazione su campagna conclusa aperta da URL: spiegazione invece del modulo", /conclusa/.test(await page.textContent("[data-don-assente]")));
  await page.goto(BASE + "donazione.html");
  ok("Donazione senza progetto: spiegazione e link, nessun reindirizzamento", /Non hai ancora scelto/.test(await page.textContent("[data-don-assente]")));
  await page.context().close();

  /* 8. Scrivi al gruppo: indicatore e conferma */
  page = await nuova();
  await page.goto(BASE + "progetto-neonati-virus.html");
  await page.click("[data-scrivi-apri]");
  await page.fill("#sc-nome", "Carlo"); await page.fill("#sc-email", "carlo@esempio.it"); await page.fill("#sc-msg", "Possiamo partecipare da Asti?");
  await page.click('[data-form="scrivi"] button[type=submit]');
  ok("«Scrivi al gruppo» mostra subito un indicatore di invio", (await page.getAttribute('[data-form="scrivi"] button[type=submit]', "aria-busy")) === "true");
  await page.waitForSelector("[data-scrivi-ok]:not([hidden])");
  await page.waitForTimeout(100);
  ok("…poi una conferma con i tempi di risposta", /entro 3 giorni lavorativi/.test(await page.textContent("[data-scrivi-ok]")));
  await page.context().close();

  /* 9. Candidatura: casella di consenso nativa ed errori che spariscono */
  page = await nuova();
  await page.goto(BASE + "candidatura.html");
  await page.click('[data-form="candidatura"] button[type=submit]');
  ok("Candidatura vuota: riepilogo errori", /campi da correggere/.test(await page.textContent("[data-errori-titolo]")));
  ok("I consensi sono caselle di spunta native", (await page.getAttribute("#c-consenso", "type")) === "checkbox");
  await page.check("#c-consenso");
  ok("Spuntando il consenso l'errore sparisce", await page.isHidden("#c-consenso-e"));
  await page.context().close();

  /* Tema chiaro e scuro: chiaro predefinito, interruttore, memoria della scelta */
  const temaDi = (pg) => pg.evaluate(() => document.documentElement.getAttribute("data-theme"));
  const fondo = (pg) => pg.evaluate(() => getComputedStyle(document.body).backgroundColor);
  let ctxTema = await browser.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: "dark" });
  page = await ctxTema.newPage();
  page.on("pageerror", (e) => errori.push(e.message));
  await page.goto(BASE + "index.html");
  ok("Senza una scelta salvata il tema è chiaro, anche con il sistema in scuro", (await temaDi(page)) === "light" && (await fondo(page)) === "rgb(251, 246, 238)", await fondo(page));
  const pulsanteTema = page.locator("[data-tema-toggle]");
  const nomeTema = async () => (await pulsanteTema.innerText()).trim();
  ok("L'interruttore dice verso quale tema si passa", /Tema scuro/.test(await nomeTema()), await nomeTema());
  await pulsanteTema.focus();
  await page.keyboard.press("Enter");
  ok("Da tastiera si passa al tema scuro", (await temaDi(page)) === "dark" && (await fondo(page)) === "rgb(28, 20, 18)", await fondo(page));
  ok("Il pulsante propone ora il tema chiaro", /Tema chiaro/.test(await nomeTema()), await nomeTema());
  ok("Il colore della barra del browser segue il tema", (await page.getAttribute('meta[name="theme-color"]', "content")) === "#1c1412");
  await page.goto(BASE + "progetti.html");
  ok("La scelta resta valida cambiando pagina", (await temaDi(page)) === "dark");
  await page.goto(BASE + "en/index.html");
  ok("La scelta resta valida cambiando lingua", (await temaDi(page)) === "dark" && /Light theme/.test(await page.locator("[data-tema-toggle]").innerText()));
  await page.reload();
  ok("Il tema scuro scelto resta valido dopo aver ricaricato la pagina", (await temaDi(page)) === "dark");
  await page.locator("[data-tema-toggle]").click();
  await page.reload();
  ok("Si può tornare al tema chiaro e la scelta resta", (await temaDi(page)) === "light" && (await fondo(page)) === "rgb(251, 246, 238)", await fondo(page));
  await ctxTema.close();
  const ctxNoJs = await browser.newContext({ viewport: { width: 1280, height: 900 }, colorScheme: "dark", javaScriptEnabled: false });
  page = await ctxNoJs.newPage();
  await page.goto(BASE + "index.html");
  ok("Senza JavaScript il tema è chiaro e l'interruttore è nascosto", (await page.locator("[data-tema-toggle]").isHidden()) && (await fondo(page)) === "rgb(251, 246, 238)", await fondo(page));
  await ctxNoJs.close();
  for (const larghezza of [320, 375]) {
    page = await nuova({ width: larghezza, height: 700 });
    await page.goto(BASE + "index.html");
    const altezze = await page.evaluate(() => ["[data-tema-toggle]", "[data-nav-toggle]", ".lang-switch", ".brand"].map((s) => { const r = document.querySelector(s).getBoundingClientRect(); return { sopra: r.top, sotto: r.bottom, largo: r.width, alto: r.height }; }));
    const [tema, menu] = altezze;
    const riga = altezze.every((a) => a.sopra < menu.sotto && a.sotto > menu.sopra);
    ok(`A ${larghezza} px marchio, lingua, tema e menu stanno su una riga`, riga, JSON.stringify(altezze.map((a) => Math.round(a.sopra))));
    ok(`A ${larghezza} px l'interruttore del tema è largo e alto almeno 44 px`, tema.largo >= 44 && tema.alto >= 44, `${Math.round(tema.largo)}×${Math.round(tema.alto)}`);
    await page.context().close();
  }

  /* Controlli aggiunti in fondo, per non cambiare i numeri citati in docs/05_tracciabilita.md: ricerca nei filtri, didascalia, ordine del menu */
  page = await nuova();
  await page.goto(BASE + "progetti.html");
  ok("Nessun campo di ricerca nell'intestazione", (await page.$(".site-header input[type=search]")) === null);
  ok("L'ordine del menu è quello richiesto", (await page.$$eval(".main-nav__list a", (a) => a.map((x) => x.getAttribute("href")).join(" "))) === "index.html progetti.html chi-siamo.html come-funziona.html programma.html proponi.html faq.html contatti.html");
  ok("La didascalia è visibile nell'elenco completo", await page.isVisible("[data-didascalia]"));
  await page.selectOption("#f-ordina", "bisogno");
  ok("Ordinare non nasconde la didascalia", await page.isVisible("[data-didascalia]"));
  await page.selectOption("#f-ordina", "");
  await page.fill("#f-q", "api");
  await page.waitForFunction(() => /q=api/.test(location.search));
  await page.waitForTimeout(150);
  const cntQ = await page.textContent("[data-conteggio]");
  ok("La ricerca nei filtri riduce l'elenco e va nella URL", /Mostrati 1 di 10 progetti/.test(cntQ), cntQ);
  ok("Con la ricerca la didascalia sparisce", !(await page.isVisible("[data-didascalia]")));
  await page.selectOption("#f-stato", "in-corso");
  ok("Ricerca e filtri si combinano", /q=api/.test(page.url()) && /stato=in-corso/.test(page.url()));
  await page.click("[data-reset]");
  await page.waitForTimeout(100);
  ok("«Azzera i filtri» svuota anche la ricerca e riporta la didascalia", (await page.inputValue("#f-q")) === "" && (await page.isVisible("[data-didascalia]")) && !/q=/.test(page.url()));
  await page.context().close();

  /* Glossario unito alle FAQ, indici «In questa pagina», descrizioni dei progetti */
  page = await nuova();
  await page.goto(BASE + "faq.html#parola-obiettivo");
  ok("Le parole dell'ex glossario sono nelle FAQ, con un'ancora che apre la voce", await page.evaluate(() => document.getElementById("parola-obiettivo").open));
  await page.goto(BASE + "faq.html");
  await page.fill("[data-faq-cerca]", "crowdfunding");
  await page.waitForTimeout(100);
  ok("La ricerca nelle FAQ trova anche le parole", await page.isVisible("#parola-crowdfunding"));
  ok("Durante la ricerca l'indice delle FAQ è nascosto", !(await page.isVisible("[data-faq-indice]")));
  await page.fill("[data-faq-cerca]", "");
  await page.waitForTimeout(100);
  ok("Svuotando la ricerca l'indice delle FAQ torna", await page.isVisible("[data-faq-indice]"));
  for (const pg of ["chi-siamo.html", "proponi.html", "faq.html", "en/chi-siamo.html", "en/proponi.html", "en/faq.html"]) {
    await page.goto(BASE + pg);
    const voci = await page.$$eval(".toc a", (a) => a.map((x) => !!document.querySelector(x.getAttribute("href"))));
    ok(`${pg}: «In questa pagina» presente e ogni voce porta a una sezione`, voci.length >= 2 && voci.every(Boolean), `${voci.length} voci`);
  }
  await page.goto(BASE + "progetto-alveari-sani.html");
  ok("La descrizione del progetto è divisa con sottotitoli", (await page.$$("#presentazione h3")).length === 3 && (await page.$$("#presentazione p")).length >= 4);
  ok("Il riquadro «tutto o niente» rimanda alle FAQ", (await page.$('a[href="faq.html#faq-tutto-o-niente"]')) !== null);
  ok("Nessun link al glossario nel piè di pagina", (await page.$('.site-footer a[href*="glossario"]')) === null);
  await page.context().close();

  /* Proponi: riquadri alla stessa altezza, pulsanti allineati, sezione per i gruppi; pagina progetto: gruppo, sede e responsabile */
  page = await nuova();
  await page.goto(BASE + "proponi.html");
  const riq = await page.$$eval("#chi-puo .statusbox", (b) => b.map((x) => { const r = x.getBoundingClientRect(), c = x.querySelector(".btn").getBoundingClientRect(); return { alto: Math.round(r.height), pulsante: Math.round(c.top) }; }));
  ok("Proponi: i due riquadri hanno la stessa altezza", riq.length === 2 && riq[0].alto === riq[1].alto, JSON.stringify(riq));
  ok("Proponi: i pulsanti dei due riquadri sono allineati", riq[0].pulsante === riq[1].pulsante);
  ok("Proponi: c'è la sezione per i gruppi con una campagna in corso", await page.isVisible("#gruppi h2"));
  await page.goto(BASE + "come-funziona.html");
  ok("Come funziona: la sezione per i gruppi non c'è più e il passo rimanda a Proponi", (await page.$("#gruppi")) === null && (await page.$('a[href="proponi.html#gruppi"]')) !== null);
  await page.goto(BASE + "progetto-alveari-sani.html");
  const info = await page.$$eval(".proj-info dt", (d) => d.map((x) => x.textContent));
  ok("Progetto: gruppo, sede e responsabile hanno ciascuno un'etichetta", info.length === 3 && info[2] === "Responsabile scientifica", info.join(" / "));
  ok("Progetto: le etichette in alto non hanno puntini di separazione", !(await page.textContent(".proj-head .card__meta")).includes("·"));
  await page.context().close();

  /* Nessuna frase introduttiva sotto il titolo nelle sezioni del menu; la home la conserva (R-001) */
  page = await nuova();
  for (const pg of ["progetti.html", "chi-siamo.html", "come-funziona.html", "programma.html", "proponi.html", "faq.html", "contatti.html"]) {
    await page.goto(BASE + pg);
    ok(`${pg}: nessuna frase introduttiva sotto il titolo`, (await page.$("main .lead")) === null);
  }
  await page.goto(BASE + "index.html");
  ok("La home dice ancora che cos'è il sito e chi lo gestisce", /Ufficio ideaBlume/.test(await page.textContent("main .lead")));
  await page.context().close();

  /* Dieci progetti: i tre tolti non hanno più pagina né link, e «sfoglia per tema» non propone temi vuoti */
  page = await nuova();
  await page.goto(BASE + "progetti.html");
  ok("L'elenco mostra 10 progetti, 4 in corso e 6 conclusi", /Mostrati 10 di 10/.test(await page.textContent("[data-conteggio]")) && /4 progetti in corso · 6 conclusi/.test(await page.textContent("[data-didascalia]")));
  const risposta = await page.goto(BASE + "progetto-vigneti-clima.html");
  ok("La pagina di un progetto tolto non esiste più", risposta.status() === 404);
  await page.goto(BASE + "cerca.html?q=zxqw");
  ok("«Sfoglia per tema» non propone temi senza progetti", (await page.$('a[href="progetti.html?categoria=agricoltura"]')) === null && (await page.$('a[href="progetti.html?categoria=salute"]')) !== null);
  await page.goto(BASE + "en/programma.html");
  ok("Inglese allineato all'italiano nel programma", /without being matched/.test(await page.textContent("#raddoppio")) && /Any other questions/.test(await page.textContent("#contatti")));
  await page.context().close();

  await browser.close();
  server.kill();
  ok("Nessun errore JavaScript durante i percorsi", errori.length === 0, errori.join(" | "));

  const sup = esiti.filter((e) => e.ok).length;
  let md = `# Percorsi interattivi\n\nGenerato da \`tools/percorsi.js\` il ${new Date().toLocaleString("it-IT")} (Playwright + Google Chrome, server statico locale con il sito in una sottocartella).\n\n**${sup} controlli superati su ${esiti.length}.**\n\n| # | Controllo | Esito | Nota |\n|---|---|---|---|\n`;
  esiti.forEach((e, i) => { md += `| ${i + 1} | ${e.nome} | ${e.ok ? "superato" : "**NON superato**"} | ${e.nota.replace(/\|/g, "/")} |\n`; });
  md += `\nScreenshot del percorso da tastiera e della donazione: \`docs/verifiche/screenshot/tastiera-*.png\`, \`donazione-*.png\`, \`menu-mobile-375.png\`.\n`;
  fs.writeFileSync(path.join(SITE, "docs/verifiche/percorsi.md"), md);
  console.log(`\n${sup}/${esiti.length} superati`);
  process.exit(sup === esiti.length ? 0 : 1);
})();
