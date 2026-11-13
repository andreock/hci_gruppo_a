// Confronto «prima / dopo» del re-design: per ogni problema P1–P8 misura lo stesso aspetto sulle due versioni
// del sito e salva le schermate. Non va lanciato a mano: lo usa prima_dopo.py, che prepara la versione «prima».
// Uso: node prima_dopo.js <sito prima> <sito dopo> <cartella immagini> <misure.json>
const fs = require("fs");
const path = require("path");
const pw = require(path.join(__dirname, "..", "..", "..", "assignment2", "website", "tools", "node_modules", "playwright"));
const [PRIMA, DOPO, IMG, OUT] = process.argv.slice(2).map((p) => path.resolve(p));
const TEL = { width: 375, height: 740 }, PC = { width: 1280, height: 800 };

async function versione(b, sito, nome) {
  const u = (p) => "file://" + path.join(sito, p);
  const m = {};
  const img = (n) => path.join(IMG, `${n}-${nome}.png`);
  const yDi = (p, sel) => p.evaluate((s) => { const e = document.querySelector(s); return e ? Math.round(e.getBoundingClientRect().top + scrollY) : null; }, sel);
  const avanti = (p) => p.getByRole("button", { name: /Continua/ }).locator("visible=true").first();
  const finoAlPasso = async (p, n) => {           // percorre la donazione con i dati del task T3
    await p.goto(u("donazione.html?progetto=alveari-sani&ricompensa=r30")); await p.waitForSelector("#importo");
    if (n >= 2) await avanti(p).click();
    if (n >= 3) { await p.locator("#nome").fill("Maria"); await p.locator("#cognome").fill("Rossi"); await p.locator("#email").fill("maria.rossi@example.com"); await avanti(p).click(); }
    if (n >= 4) { await p.locator("#vis-no").setChecked(true); await p.locator("#privacy").setChecked(true); await avanti(p).click(); }
    if (n >= 5) { await p.locator("#m-satispay").setChecked(true); await avanti(p).click(); }
    await p.waitForTimeout(250);
  };
  const testoVisibile = (p) => p.evaluate(() => document.querySelector("main").innerText);

  // ---------- telefono (375 × 740)
  let p = await b.newPage({ viewport: TEL });
  // P1: riepilogo al passo 5 e nella conferma
  await finoAlPasso(p, 5);
  const fuori = () => p.evaluate(() => {
    const d = [...document.querySelectorAll("main .summary dl")].find((x) => x.offsetParent && x.querySelector("dd")); const c = d.closest(".summary").getBoundingClientRect();
    return { larghezza_pagina: document.documentElement.scrollWidth, valori_fuori_dal_riquadro: [...d.querySelectorAll("dd")].filter((x) => x.getBoundingClientRect().right > c.right + 1).length };
  });
  m.p1 = { schermo: "375 px", passo5: await fuori() };
  const yRev = await yDi(p, "#h-p5");
  await p.screenshot({ path: img("p1"), fullPage: true, clip: { x: 0, y: yRev - 12, width: 375, height: 560 } });
  await p.getByRole("button", { name: "Paga ora" }).click(); await p.waitForURL(/conferma/); await p.waitForTimeout(250);
  m.p1.conferma = await fuori();
  await p.setViewportSize({ width: 320, height: 640 }); await finoAlPasso(p, 5);
  m.p1.passo5_320 = await fuori();
  await p.setViewportSize(TEL);
  // P7: indicatore dei passi e posizione del primo campo
  await finoAlPasso(p, 1);
  m.p7 = await p.evaluate(() => { const s = document.querySelector(".steps").getBoundingClientRect(), h = document.querySelector("main h1"), lh = parseFloat(getComputedStyle(h).lineHeight);
    return { altezza_indicatore_px: Math.round(s.height), righe_del_titolo: Math.round(h.getBoundingClientRect().height / lh), y_prima_scelta_px: Math.round(document.querySelector("[data-scelte] label").getBoundingClientRect().top + scrollY) }; });
  await p.screenshot({ path: img("p7") });
  // P5: elenco dei progetti su telefono
  await p.goto(u("progetti.html"));
  const elenco = () => p.evaluate(() => { const li = [...document.querySelectorAll("main li[data-slug]")].filter((e) => e.offsetParent);
    return { y_prima_scheda_px: Math.round(li[0].getBoundingClientRect().top + scrollY), schede_che_iniziano_nella_prima_schermata: li.filter((e) => e.getBoundingClientRect().top + scrollY < innerHeight).length, altezza_schermo_px: innerHeight }; });
  m.p5 = { telefono: await elenco() };
  await p.screenshot({ path: img("p5m") });
  await p.close();

  // ---------- computer (1280 × 800)
  p = await b.newPage({ viewport: PC });
  await p.goto(u("progetti.html"));
  m.p5.computer = await elenco();
  await p.screenshot({ path: img("p5d") });
  // P4: percentuale nelle schede
  m.p4 = await p.evaluate(() => {
    const li = document.querySelector('main li[data-slug="aria-aperta"]'); const nuovo = li.querySelector(".card__perc strong");
    if (nuovo) { const s = getComputedStyle(nuovo); return { dove: "accanto alla barra", corpo_px: parseFloat(s.fontSize), peso: +s.fontWeight, tra_parentesi: false }; }
    const f = li.querySelector(".card__figures"), s = getComputedStyle(f); return { dove: "in coda alla riga delle cifre", corpo_px: parseFloat(s.fontSize), peso: +s.fontWeight, tra_parentesi: /\(\d+%\)/.test(f.textContent) };
  });
  await p.locator('main li[data-slug="aria-aperta"]').screenshot({ path: img("p4") });
  // P3: regola «tutto o niente» nella pagina del progetto
  await p.goto(u("progetto-neonati-virus.html"));
  m.p3 = await p.evaluate(() => { const a = document.querySelector(".layout-aside__aside"); const vis = /restituiamo la donazione/.test(a.innerText);
    return { frase_sulla_restituzione_visibile_senza_clic: vis, clic_necessari: vis ? 0 : 1 }; });
  const a = await p.locator(".layout-aside__aside").boundingBox();
  await p.screenshot({ path: img("p3"), fullPage: true, clip: { x: a.x - 12, y: a.y - 12, width: a.width + 24, height: Math.min(a.height + 24, 760) } });
  // P2: quando compaiono commissione e totale
  m.p2 = { passo_in_cui_si_legge_il_totale: null, passo_in_cui_si_legge_la_commissione: null };
  for (let n = 1; n <= 5; n++) {
    await finoAlPasso(p, n); const t = await testoVisibile(p);
    if (m.p2.passo_in_cui_si_legge_la_commissione === null && /0,89/.test(t)) m.p2.passo_in_cui_si_legge_la_commissione = n;
    if (m.p2.passo_in_cui_si_legge_il_totale === null && /30,89/.test(t)) m.p2.passo_in_cui_si_legge_il_totale = n;
    if (n === 1) await p.screenshot({ path: img("p2") });
    if (n === 4) { await p.locator("#m-satispay").setChecked(true); await p.waitForTimeout(150); await p.evaluate(() => scrollTo(0, 0)); await p.screenshot({ path: img("p2b") }); }
  }
  // P8: messaggio per l'email vuota
  await finoAlPasso(p, 2);
  for (const id of ["#nome", "#cognome", "#email"]) await p.locator(id).fill("");   // i dati dei passaggi precedenti restano salvati: qui servono i campi vuoti
  await avanti(p).click(); await p.waitForTimeout(200);
  m.p8 = { errore_email_vuota: (await p.locator("#email-e").innerText()).trim(), errore_nome_vuoto: (await p.locator("#nome-e").innerText()).trim() };
  const e = await p.evaluate(() => { const r = document.querySelector("[data-errori]").getBoundingClientRect(); return { x: r.left + scrollX, y: r.top + scrollY, h: r.height }; });
  await p.screenshot({ path: img("p8"), fullPage: true, clip: { x: e.x - 12, y: e.y - 12, width: 760, height: e.h + 24 } });
  // P6: a chi è riservato il modulo
  const avviso = (file, dest) => p.goto(u(file)).then(() => p.evaluate((d) => { const f = document.querySelector("form[data-form]"); const prima = [...document.querySelectorAll(`main a[href="${d}"]`)].filter((x) => x.offsetParent && (f.compareDocumentPosition(x) & Node.DOCUMENT_POSITION_PRECEDING)); return prima.length > 0; }, dest));
  m.p6 = { candidatura_rimanda_alla_collaborazione: await avviso("candidatura.html", "collabora.html") };
  await p.screenshot({ path: img("p6") });
  m.p6.collaborazione_rimanda_alla_candidatura = await avviso("collabora.html", "candidatura.html");
  await p.goto(u("contatti.html")); await p.locator("#ct-argomento").selectOption({ index: 2 }); await p.waitForTimeout(150);
  m.p6.contatti_suggerisce_i_moduli = await p.evaluate(() => [...document.querySelectorAll('#scrivici a[href="collabora.html"]')].some((x) => x.offsetParent));
  const sc = await yDi(p, "#scrivici");
  await p.screenshot({ path: img("p6b"), fullPage: true, clip: { x: 0, y: sc - 8, width: 1280, height: 620 } });
  await p.close();
  return m;
}

(async () => {
  fs.mkdirSync(IMG, { recursive: true });
  let b; try { b = await pw.chromium.launch(); } catch (e) { b = await pw.chromium.launch({ channel: "chrome" }); }
  const misure = { prima: await versione(b, PRIMA, "prima"), dopo: await versione(b, DOPO, "dopo") };
  await b.close();
  fs.writeFileSync(OUT, JSON.stringify(misure, null, 2) + "\n");
  console.log(JSON.stringify(misure, null, 1));
})().catch((e) => { console.error(e); process.exit(1); });
