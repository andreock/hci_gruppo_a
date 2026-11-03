# 01 · Indice della relazione, passaggi scelti e informazioni mancanti

Documento per il checkpoint di REL-AI-01. Le prove sono descritte in `00_inventario_prove.md`.

> **Esito del checkpoint (03/11/2026).** Il gruppo ha fornito componenti, strumenti, materiali, URL e natura delle modifiche manuali, senza rispondere alle decisioni 1–4. La relazione è stata scritta così: decisione 1, descrive D-42 com'è, con un riquadro e un segnaposto in §5; decisione 2, cita `797fc7e`, già committato; decisione 3, dichiara i disallineamenti come limiti; decisione 4, copre solo la documentazione dell'IA. Quanto resta da fornire è in `03_da_completare.md`.

## 1. Passaggi scelti

Ogni passaggio indica il criterio che illustra e quanto è solida la prova della prima versione:

- **A**: prima versione recuperabile da git;
- **B**: prima versione nota solo da una citazione del gruppo;
- **C**: prima versione assente, si mostra il prompt confrontato con l'output.

### Fase 1 · Personas e user journey

| ID | Passaggio | Criterio | Prima → finale | Prova | Solidità |
|---|---|---|---|---|---|
| PJ1 | Il contesto comune C00: dal sito reale alla persona generica | Formato comune, genericità, nessun marchio | `<contesto_sito>` con IdeaGinger e citazioni → template del corso → `<servizio_generico>` e «GENERICITÀ ASSOLUTA» | `fb0a77b`, `c264a64`, `2971d53` | A (è un prompt, non un output) |
| PJ2 | P01 e J01: da «poco capace» a ex insegnante con strategie proprie | Stereotipi, specificità, base osservabile delle barriere | «Giuseppe è poco capace con la tecnologia» → competenze e strategie; «La pagina è confusa» → percentuali oltre il 100%, giorni negativi, Indietro | `alex/documentazione_uso_ai.md`, `alex/personas/P01…`, `alex/journeys/J01…` | B |
| PJ3 | P03 e J03: da «non vede il pallino» a stato non annunciato | Accessibilità, corrispondenza journey-persona | «Non vede il pallino rosso» → stato affidato a colore o simbolo, controlli attivi, golfo della valutazione. P02 e J02 come esempio breve di limite situazionale | `alex/documentazione_uso_ai.md`, `alex/journeys/J03…`, `J02…` | B |
| PJ4 | P12 e J12: da promotrice a Forlì a partner che cerca un contatto | Differenziazione da P09, coerenza con la consegna | Prompt (Forlì, lancia una campagna) → `d6feb95` (partner a Torino, ancora Ginger) → `86536bf` (To-be, percorso «contatto») | `personas/P12…md`, `d6feb95`, `86536bf`, `da_rivedere_P10-P12.md` §2.2 | A |
| PJ5 | P10 e J10: distinguere due promotori nella stessa fase | Differenziazione da P11, coerenza interna, journey fino al resoconto | Fase 6 «rendicontazione con l'ufficio comunicazione» → «Resoconto ai donatori»; regola del cofinanziamento e fiducia di chi | `d6feb95`, `86536bf`, `da_rivedere_P10-P12.md` §0, §2.4, §3 | A |
| PJ6 | P07: una revisione rimasta a metà | Uso critico, limiti: la v2 della scheda non è su `main`, J07 è rimasto v1 | `[S59 · LG1 · G4] …Ginger` → frase sulla persona, solo in `d3e3440`; il sito usa la v1 | `a941518`, `d3e3440`, D-04 | A |

P04–P06 compaiono solo nella matrice di differenziazione, perché non esiste una loro prima versione.

### Fase 2 · Il sito

| ID | Passaggio | Criterio | Prima → finale | Prova | Solidità |
|---|---|---|---|---|---|
| S1 | L'agente segnala errori nelle nostre richieste; il gruppo decide | Contenuti, fondamento nei dati | Prompt: server locale e `fetch` → D-01 senza server. «404 da FAQ e Come funziona» → D-07. X03 senza fonte → D-06 | `4baa4e9`, `decisioni.md`, `01_inventario_fonti.md` | A (il prompt è citato solo in forma indiretta) |
| S2 | Architettura e correzioni al checkpoint 1 | Struttura, navigazione, multilingua | Oltre 70 voci su IdeaGinger → 7 voci senza tendine. «Sostieni la Ricerca» → ideaBlume. `example.org` → contatti credibili. 10 → 12 pagine. IT nella radice, EN in `en/` | `38a1910`, diff di `decisioni.md` e `04_requisiti.md`, `06_architettura.md` | A |
| S3 | La ricerca, corretta due volte grazie alle verifiche | Interazioni, feedback | Sottostringa («api» trova «capire») → inizio di parola («veterinaria» non trova nulla) → tollerante | Diff di `js/ideablume.js` in `e1ebd20` e `60712ad`, D-33, V-01 | A |
| S4 | Accessibilità e stati verificati da script | Moduli, tastiera, feedback | Link FAQ con testo uguale → testo nascosto distintivo. CLS del menu → D-32. Colonna fissa irraggiungibile → D-31. Errori del modulo | Diff di `faq.html` in `e1ebd20`, `verifiche/*`, screenshot `donazione-errore-importo.png`, `tastiera-*` | A |
| S5 | Tre versioni grafiche con 2 screenshot a confronto | Coerenza visiva, scelte del gruppo | Prugna con font di sistema → Inter e Bricolage (framework scartati, D-35) → palette calda e interruttore del tema (D-40, D-41) | `e1ebd20`, `f0988ba`, copia di lavoro | A |
| S6 | Da prototipo dichiarato a «contenuti definitivi» | Contenuti, uso responsabile | «Pagamento simulato» e 41 segnaposto → nessun avviso, informazioni istituzionali stabilite | `f0988ba:i18n/it.json`, D-42, `tools/soluzioni.py`, screenshot `donazione-1280` | A (dipende dalla decisione 1) |

Modifiche dirette al codice (§4.7): `dd07a0a` con il diff di una riga. Lo stash `6a32c9f` è citato come non applicato. Il resto dipende da ciò che dichiarerà il gruppo.

## 2. Indice della relazione

| § | Sezione | Contenuto e prove |
|---|---|---|
| 0 | Copertina | Dati dalle impostazioni (da completare) |
| 1 | Introduzione | `Istruzioni.md`, `README.md`, legame con assignment1 (`01_inventario_fonti.md` §3) |
| 2 | Panoramica degli strumenti | Tabella strumento → fase → attività → chi; figura del flusso di lavoro |
| 3.1 | Strumenti e attività | Codex per P01–P03; Claude Opus 5.5 per P10–P12 (`d6feb95`); P04–P09 da completare |
| 3.2 | Prompt e informazioni fornite | C00, P01, V00, prompt di Alex, template, catalogo; motivazione dei prompt paralleli (PJ1) |
| 3.3 | Dalla prima versione alla finale | PJ2, PJ4, PJ6 a confronto |
| 3.4 | Problemi negli output | Tabella da `documentazione_uso_ai.md` e `da_rivedere_P10-P12.md` §3 |
| 3.5 | Richieste e interventi | Iterazioni di Alex, `86536bf`, `d3e3440` |
| 3.6 | Personas più specifiche, differenziate e coerenti | Matrice di `README.md` e `03_bisogni_personas.md` §2; PJ4, PJ5 |
| 3.7 | Journey e personas | PJ2, PJ3, PJ5; To-be e As-is; `<persona_generata>` |
| 3.8 | Motivazioni delle scelte | `da_rivedere_P10-P12.md` §2, proto-personas, limiti di maturità |
| 4.1 | Strumenti e attività | Claude Opus 5.5 dai commit; script di verifica |
| 4.2 | Prompt e informazioni | SITO-01 (da fornire), fonti, requisiti, vincoli |
| 4.3 | Dalla prima versione alla finale | S3, S5, S6 |
| 4.4 | Problemi negli output | Tabella da `decisioni.md`, `verifiche/README.md`, `09_valutazione_euristica.md` |
| 4.5 | Richieste e interventi | Checkpoint 1 e 2, richieste di redesign, D-40, D-41, D-42 |
| 4.6 | Contenuti, struttura, navigazione, interazioni | S1, S2, S3, S4; multilingua (D-21, D-28) |
| 4.7 | Modifiche dirette al codice | `dd07a0a` e dichiarazioni del gruppo |
| 4.8 | Motivazioni con tracciabilità | Estratto P-001, P-008, P-022, P-029, P-056 di `05_tracciabilita.md` |
| 5 | Uso responsabile | Supervisione, dati, errori, stereotipi, privacy, trasparenza, limiti; ogni punto rimanda a un passaggio |
| 6 | Contributo del gruppo | Paternità dei commit e `RUOLI` (da completare) |
| 7 | Conclusioni | Cosa ha funzionato, limiti (nessun test con utenti, valutatori e progettisti coincidono), cosa faremmo diversamente |
| A | Elenco delle prove | Da `00_inventario_prove.md` |
| B | Prompt | C00 e V00 per estratti e percorso, P01, prompt di Alex, REL-AI-01 |

## 3. Decisioni da prendere al checkpoint

### Decisione 1 · Il sito non dichiara più di essere fittizio

Secondo REL-AI-01, la relazione deve mostrare che «personas e progetti sono fittizi e lo dichiariamo» e che «pagamenti e dati» sono simulati. Le prove dicono questo:

- fino a `f0988ba` il sito lo dichiarava: `prototype`, «Pagamento simulato», FAQ «Questo sito è reale?», 41 segnaposto;
- nella copia di lavoro D-42 ha tolto tutto, e `tools/verifica-dati.py` controlla che quelle parole non ricompaiano;
- la home dice che il sito è «gestito dall'Ufficio ideaBlume dell'Ateneo»; le FAQ dicono che la donazione all'Università «è deducibile dal reddito»; il sito indica un telefono con prefisso di Torino e una sede inventata;
- `sito.yml` pubblica il sito da `main`, quindi a ogni push che tocca `website/` questi testi possono andare online.

Non posso quindi scrivere che il sito dichiara la propria natura fittizia. Le opzioni sono due:

- **(a) Consigliata: ripristinare un avviso breve e permanente** nel piè di pagina e nella donazione, e togliere dalle FAQ l'affermazione fiscale o riformularla. Va fatto prima di pubblicare, ed è una modifica al sito che spetta al gruppo: questo prompt mi vieta di toccarlo. La relazione racconterebbe D-42 e la correzione successiva come un esempio di revisione critica.
- **(b) Mantenere D-42.** La relazione dichiara la natura fittizia al posto del sito e riporta D-42 come scelta del gruppo con il relativo rischio. Non può presentarla come buona pratica, e il rischio di scambiare il sito per un servizio dell'Ateneo resta.

### Decisione 2 · Qual è la versione finale del sito

Palette calda, D-40–D-42 e i contenuti attuali sono in 95 file non committati. Consiglio di fare il commit prima che scriva la relazione, così potrò citare un hash. Altrimenti scriverò «copia di lavoro del 03/11/2026».

### Decisione 3 · Disallineamenti da correggere o dichiarare

- Su `main` P07–P09 e J07–J09 sono ancora v1 con chiavi `Sxx` e IdeaGinger. La revisione delle schede P07–P09 (`d3e3440`) è solo sul branch `assignment1-valutazione-euristica`, cita ancora Funds TOgether e non tocca i journey. Va unita a `main`?
- `08_verifica_personas.md` e `09_valutazione_euristica.md` non riflettono D-42.
- Il prompt P12 non coincide con l'output.

Se il gruppo non li corregge, la relazione li dichiara come limiti, in particolare in PJ6 e §3.8.

### Decisione 4 · Questa relazione basta per la consegna?

`Istruzioni.md` §7 chiede **un solo PDF** con personas, journey, documentazione dell'IA e link al prototipo, chiamato `assignment2_gruppox.pdf`. La struttura di REL-AI-01 copre solo la documentazione dell'IA. Propongo di tenere questo PDF come parte documentale e di indicare nella relazione che personas e journey sono allegati. Se preferite un PDF unico, posso aggiungere le 24 schede in appendice, ma la lunghezza supererebbe di molto le 25 pagine.

## 4. Informazioni mancanti che solo il gruppo può fornire

| # | Informazione | Dove serve |
|---|---|---|
| 1 | Nomi e cognomi, numero del gruppo («Gruppo A» basta per il nome del file?), nome del corso | Copertina |
| 2 | Corrispondenza tra account git e persone: andreock, Andrea Canale, Alex, antofallea, lorenzo. Dati dalla cronologia: stessa email per i primi due | §2, §6 |
| 3 | Ruoli: chi ha generato e rivisto P04–P06 e P07–P09 (`README.md`, colonna «Assegnato a», è vuota) | §2, §3.1, §6 |
| 4 | Strumento effettivamente usato per P04–P09. È stato usato Claude Code per il sito, oppure un'altra interfaccia? | §2, §3.1, §4.1 |
| 5 | **Testo del prompt SITO-01** ed eventuali richieste del redesign e di D-40, D-41, D-42 | §4.2, Appendice B |
| 6 | Estratti di conversazioni, prime bozze di P04–P09 se salvate | §3.3, §3.5 |
| 7 | Modifiche fatte **a mano** al codice o ai testi. In particolare: `86536bf`, `d3e3440`, `f0988ba` sono manuali o generate? | §3.5, §4.7 |
| 8 | Perché C00 è passato alla v3 «generica» (`2971d53` si intitola solo «Update prompts») | §3.2, §3.8 |
| 9 | V00 è stato eseguito? Su quali documenti e con quale esito? | §3.4, §5 |
| 10 | Esito delle decisioni aperte di `da_rivedere_P10-P12.md`: P12 approvata? Template o Istruzioni? | §3.8 |
| 11 | Conferma che all'IA non sono stati forniti dati personali reali e controlli fatti su stereotipi di età, genere, provenienza, oltre a quelli documentati | §5 |
| 12 | URL del sito pubblicato, se esiste | §1 |
| 13 | Chi ha provato il sito di persona e che cosa ha trovato: le prove riguardano solo script e walkthrough | §4.4, §6 |
| 14 | Cosa fareste diversamente | §7 |

Quello che resta senza risposta diventa un segnaposto «[DA COMPLETARE: …]» nella relazione e un elemento di `03_da_completare.md`. Nessuna di queste informazioni verrà dedotta.
