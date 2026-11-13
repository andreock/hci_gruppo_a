// Percorso «esperto» dei 4 task sul prototipo (file://): verifica che i task siano eseguibili,
// che le risposte attese siano quelle scritte nel piano e salva le schermate di partenza/arrivo.
// Uso: node pilota.js [cartella del sito] [--senza-schermate]   (predefinita: assignment2/website)
const path = require("path");
const pw = require(path.join(__dirname, "..", "..", "..", "assignment2", "website", "tools", "node_modules", "playwright"));
const ARG = process.argv.slice(2), SCHERMATE = !ARG.includes("--senza-schermate");
const SITO = path.resolve(ARG.filter((x) => !x.startsWith("--"))[0] || path.join(__dirname, "..", "..", "..", "assignment2", "website"));
const IMG = path.join(__dirname, "..", "img");
const u = (p) => "file://" + path.join(SITO, p);
(async () => {
  let b; try { b = await pw.chromium.launch(); } catch (e) { b = await pw.chromium.launch({ channel: "chrome" }); }
  const p = await b.newPage({ viewport: { width: 1280, height: 800 } });
  const esiti = [];
  const foto = (o) => (SCHERMATE ? p.screenshot(o) : null);
  const ok = (t, cond, nota) => { esiti.push((cond ? "OK  " : "KO  ") + t + " · " + nota); if (!cond) process.exitCode = 1; };
  let clic = 0; const c = async (loc) => { await loc.click(); clic++; };

  // T1: progetto in corso più lontano dall'obiettivo
  await p.goto(u("index.html")); await foto({ path: path.join(IMG, "t0-home.png") });
  clic = 0; await c(p.getByRole("navigation").getByRole("link", { name: "Progetti", exact: true }).first());
  await p.getByLabel("Stato").selectOption({ label: "In corso" }); clic++;
  await p.getByLabel("Ordina per").selectOption({ label: "Più lontani dall'obiettivo" }); clic++;
  const applica = p.getByRole("button", { name: "Applica i filtri" }); if (await applica.isVisible()) await c(applica);
  await p.waitForTimeout(300);
  const primo = await p.locator("main h2 a:visible, main h3 a:visible").first().innerText();
  await foto({ path: path.join(IMG, "t1-elenco.png") });
  ok("T1", /Aria aperta/.test(primo), `primo risultato: ${primo} · azioni ${clic}`);

  // T2: uso dei fondi e tutto o niente
  await p.goto(u("index.html")); clic = 0;
  await c(p.getByRole("link", { name: "Proteggere i neonati dai virus respiratori" }).first());
  await c(p.getByRole("link", { name: "Come useremo i fondi" }));
  const corpo = (await p.locator("main").textContent()).replace(/\s+/g, " ");
  await foto({ path: path.join(IMG, "t2-progetto.png") });
  ok("T2", /Reagenti per i test molecolari\s*€\s*3\.800/.test(corpo) && /ti restituiamo la donazione/.test(corpo), `azioni ${clic}`);

  // T3: donazione 30 € con ricompensa, anonima, Satispay
  await p.goto(u("progetto-alveari-sani.html")); clic = 0;
  await c(p.getByRole("link", { name: /Scegli € 30/ }));
  await p.waitForTimeout(300); await foto({ path: path.join(IMG, "t3-donazione.png") });
  const avanti = () => p.getByRole("button", { name: /Continua/ }).locator("visible=true").first();
  await c(avanti());
  await p.locator("#nome").fill("Maria"); await p.locator("#cognome").fill("Rossi");
  await p.locator("#email").fill("maria.rossi@example.com");
  await c(avanti());
  await c(p.locator('label[for="vis-no"]')); await c(p.locator('label[for="privacy"]'));
  await c(avanti());
  await c(p.locator('label[for="m-satispay"]'));
  await c(avanti());
  await p.waitForTimeout(300);
  const riep = await p.locator("main").innerText();
  await foto({ path: path.join(IMG, "t3-riepilogo.png"), fullPage: true });
  const tot = (riep.match(/Totale[^\n€]*\n?[^€]*€\s*([\d.,]+)/) || [])[1];
  await c(p.getByRole("button", { name: "Paga ora" })); await p.waitForURL(/conferma/, { timeout: 15000 });
  const conf = await p.locator("main").innerText();
  await foto({ path: path.join(IMG, "t3-conferma.png") });
  ok("T3", /30,89/.test(riep) && /conferma/i.test(p.url()), `totale ${tot} · url ${path.basename(p.url()).slice(0, 40)} · azioni ${clic}`);

  // T4: proposta di collaborazione da un'associazione
  await p.goto(u("index.html")); clic = 0;
  await c(p.getByRole("navigation").getByRole("link", { name: "Proponi un progetto" }).first());
  await foto({ path: path.join(IMG, "t4-proponi.png") });
  await c(p.getByRole("link", { name: "Proponi una collaborazione" }).first());
  await p.getByLabel("Nome dell'ente").fill("Associazione Acqua Chiara");
  await p.getByLabel("Tipo di ente").selectOption({ label: "Associazione" });
  await p.getByLabel(/Nome e cognome/).fill("Maria Rossi");
  await p.getByLabel("Email").locator("visible=true").first().fill("maria.rossi@example.com");
  await p.getByLabel("La vostra idea").locator("visible=true").last().fill("Analizzare con l'Università la qualità dell'acqua delle fontane del quartiere.");
  await p.getByLabel("Tema").selectOption({ label: "Ambiente" });
  await c(p.getByText(/Ho letto l'informativa/));
  await c(p.getByRole("button", { name: "Invia la proposta" })); await p.getByRole("heading", { name: "Proposta ricevuta" }).waitFor({ timeout: 15000 });
  const fine = await p.locator("main").innerText();
  await foto({ path: path.join(IMG, "t4-ricevuta.png") });
  ok("T4", /Proposta ricevuta/.test(fine) && /collabora/.test(p.url()), `azioni ${clic}`);
  console.log(esiti.join("\n"));
  await b.close();
})().catch((e) => { console.error(e); process.exit(1); });
