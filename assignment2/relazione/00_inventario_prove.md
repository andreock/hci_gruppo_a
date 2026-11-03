# 00 · Inventario delle prove

Inventario per la relazione sull'uso dell'IA (prompt REL-AI-01), compilato il 03/11/2026 sul branch `main` (HEAD `dd07a0a`, poi `797fc7e`: vedi §6). Ogni riga è stata aperta e letta: file nella copia di lavoro oppure versione nella cronologia git.

I percorsi sono relativi alla radice del repository. Gli autori sono indicati con il nome della cartella o l'account git, senza indirizzi email. Il gruppo deve associarli ai nominativi (vedi `01_indice.md`, informazioni mancanti).

## 1. Come leggere la paternità dei commit

La riga `Co-Authored-By` è l'unica traccia oggettiva dell'uso di un agente. La sua assenza **non dimostra** che una modifica sia manuale: lo si può affermare solo con altre prove o con la conferma del gruppo.

| Categoria | Commit | Base dell'attribuzione |
|---|---|---|
| Agente dichiarato (`Co-Authored-By: Claude Opus 5.5`) | `d6feb95`, `1b2f2c9` (lorenzo); `4baa4e9`, `38a1910`, `56e2a95`, `e1ebd20`, `60712ad` (andreock) | Riga nel messaggio del commit |
| Modifica manuale dimostrabile | `dd07a0a` (una riga di `.github/workflows/sito.yml`) | Committer «GitHub»: modifica fatta dall'interfaccia web, nessuna riga di co-autore |
| Modifica manuale non applicata | stash `6a32c9f` (una riga di `i18n/it.json`) | È solo nello stash: la copia di lavoro conserva il testo precedente (`i18n/it.json:292`) |
| Caricamento di file dall'interfaccia web | `3bc8d33`, `b5012db`, `9f46b94` (template del corso) | Committer «GitHub» |
| **Non determinabile: serve il gruppo** | `fb0a77b`, `d4a7bcb`, `c264a64`, `2971d53`, `f547471`, `c67c067`, `f0988ba` (andreock); `a941518`, `d3e3440` (antofallea); `86536bf` (lorenzo); `6767c88`, `34ebd76` (Alex) | Nessuna riga di co-autore. Alex dichiara però Codex in `documentazione_uso_ai.md`; `f0988ba` contiene un redesign con decisioni registrate nel tono dell'agente (D-35–D-39) |
| Copia di lavoro non committata | 95 file in `assignment2/website/`, tra cui D-40, D-41, D-42, palette calda, interruttore del tema | Nessun hash citabile: stato del 03/11/2026 |

## 2. Personas e user journey

| Prova | Percorso o commit | Fase | Che cosa dimostra |
|---|---|---|---|
| Consegna della docente | `assignment2/Istruzioni.md` | Personas, journey, sito | Requisiti, minimi, criteri di valutazione e materiali da consegnare (§7) |
| Contesto comune C00, prima versione | `fb0a77b:assignment2/00_contesto_comune_C00.md` (27/10/2026) | Personas, journey | Contesto incentrato su IdeaGinger e Funds TOgether, citazioni `[Sxx · Hx · Gx]` obbligatorie |
| C00 adattato ai template del corso | `c264a64` (27/10/2026) | Personas, journey | Aggiunge `<template_del_corso>` e `<corrispondenze>`: i campi degli appunti vanno nei campi del template |
| C00 versione 3, «personas generiche» | `2971d53`; `assignment2/00_contesto_comune_C00.md` | Personas, journey | Rimuove `<contesto_sito>`, introduce `<servizio_generico>` e la regola «GENERICITÀ ASSOLUTA», riscrive il catalogo dei problemi senza nomi reali |
| Regole di rispetto e di fedeltà in C00 | `00_contesto_comune_C00.md`, `<regole>` 4, 5, 6, 7 | Personas, journey | Niente dati inventati presentati come reali, `[IPOTESI]`, niente pietismo né stereotipi, dichiarazione di proto-persona |
| Indice e matrice delle personas | `assignment2/README.md` (tabella «Indice e assegnazione», frase di copertura) | Personas | Differenziazione progettata: 8 donatori o visitatori e 4 promotori, 6 donne e 6 uomini, 20–71 anni. La colonna «Assegnato a» è vuota |
| Note del gruppo sulla presentazione | `assignment2/README.md`, «Note di revisione» | Personas | Incoerenze trovate in assignment1: conteggi delle slide 80–81, soglia WCAG errata a slide 23 |
| Motivazione del metodo a prompt paralleli | `assignment2/README.md`, introduzione e «Come usarlo» | Personas, journey | Un prompt autonomo per documento, per generare in parallelo con la stessa struttura. Prompt totali: 26 |
| Prompt singoli, prima versione | `fb0a77b:assignment2/personas/P01_giuseppe_ferrero.md` e seguenti | Personas, journey | Scheda vincolante e `<problemi_assegnati>` con riferimenti reali (MILK-ACT, Ginger) |
| Prompt singoli, versione 3 | `2971d53`; `assignment2/personas/P01…P12*.md` | Personas, journey | Stessa scheda, problemi come frustrazioni generiche, fasi del journey con chiavi. P01: «Non descriverlo come incapace» |
| Prompt di verifica V00 | `assignment2/99_verifica_V00.md` | Personas, journey | Sette criteri, tra cui fedeltà e rispetto. **È facoltativo: nessuna prova che sia stato eseguito** |
| Documentazione di Alex | `assignment2/alex/documentazione_uso_ai.md` | Personas, journey | Strumento (OpenAI Codex, modello GPT-5), prompt, iterazione 1 con sei problemi, iterazione 2, controllo finale |
| Sorgenti e HTML di Alex | `assignment2/alex/personas/`, `alex/journeys/`, `alex/output/html/`, `alex/scripts/genera_html.py` (`6767c88`, `34ebd76`) | Personas, journey | Versioni finali di P01–P03 e J01–J03. Le prime formulazioni **non sono in git**: esistono solo come citazioni nella documentazione |
| Note di revisione P10–P12 | `assignment2/personas/da_rivedere_P10-P12.md` (`d6feb95`, `86536bf`) | Personas, journey | Undici problemi con il relativo intervento, decisioni aperte con caselle non spuntate, tabella «Opportunità → elementi del prototipo» |
| P10–P12, J10–J12: prima versione salvata | `d6feb95:assignment2/lorenzo/*.html` (27/10/2026, 15:18) | Personas, journey | Già rivista rispetto a `Istruzioni.md`, ancora legata a IdeaGinger. Journey As-is, base Mista |
| P10–P12, J10–J12: versione 2 | `86536bf`; `assignment2/personas/personas/P1*`, `personas/journey/J1*` (27/10/2026, 22:35) | Personas, journey | Scollegate da IdeaGinger, journey To-be con base Ipotesi, P10 con resoconto ai donatori |
| P07–P09: prima versione | `a941518` (27/10/2026) | Personas, journey | «v1», citazioni `[Sxx]`, IdeaGinger |
| P07–P09: revisione | `d3e3440` (31/10/2026), **solo sul branch `assignment1-valutazione-euristica`, non su `main`** | Personas | «v2», nessuna chiave `Sxx` né «Ginger» nel testo, ma il servizio resta «Funds TOgether · Università di Torino». Su `main` e nella copia di lavoro le schede sono ancora v1 (16–22 righe con riferimenti per scheda) |
| J07–J09 | `assignment2/personas/journey/J0[7-9]*` (unico commit `a941518`) | Journey | **Mai rivisti**: «v1», As-is, IdeaGinger, chiavi `Sxx` ancora presenti |
| P04–P06, J04–J06 | `f547471` (29/10/2026) | Personas, journey | Versione unica già «v3». **Nessuna prima versione disponibile** |
| Template del corso | `assignment2/personas/scheda_persona.pdf`, `scheda_user_journey.pdf`, `personas_template.html`, `user_journey_template.html` | Personas, journey | Formato vincolante fornito all'IA |
| Collegamento con assignment1 | `assignment1/assignment1_gruppoA.pdf` (citato), `website/docs/01_inventario_fonti.md` §3 | Personas, journey, sito | Provenienza del catalogo dei problemi: le chiavi `Sxx` sono i numeri di slide (`README.md`). Il PDF non è stato riaperto: basta come fonte delle informazioni date all'IA |

## 3. Sito

| Prova | Percorso o commit | Fase | Che cosa dimostra |
|---|---|---|---|
| Prompt del sito | **Non salvato nel repository.** Citato come «prompt SITO-01» in `4baa4e9` e nominato in `decisioni.md` («regola generale 3», «regola 4 del prompt») | Sito | Si conoscono solo frammenti riportati indirettamente. Testo da fornire |
| Inventario delle fonti | `website/docs/01_inventario_fonti.md` (`4baa4e9`) | Sito | Informazioni fornite, versioni di riferimento e livelli di maturità di personas e journey, incoerenze segnalate |
| Problemi consolidati | `website/docs/02_problemi_consolidati.md` | Sito | 90 problemi deduplicati con fonte; X03 senza fonte |
| Bisogni e punti di dolore | `website/docs/03_bisogni_personas.md` | Sito, journey | Quadro delle 12 personas e 64 punti di dolore |
| Requisiti | `website/docs/04_requisiti.md`; diff `4baa4e9..38a1910` | Sito | 102 requisiti; R-071, R-120, R-130, R-133 cambiano dopo il checkpoint 1 |
| Tracciabilità | `website/docs/05_tracciabilita.md`, `tools/genera-tracciabilita.py`, `tools/soluzioni.py` | Sito | Problema → requisito → soluzione → verifica. Totali: 84/3/3 in `60712ad`, 87/0/3 nella copia di lavoro |
| Architettura | `website/docs/06_architettura.md` (`38a1910`) | Sito | Mappa, menu di 7 voci, percorsi, wireframe. Parla ancora di «prototipo didattico» |
| Design system | `website/docs/07_design_system.md` in `38a1910`, `f0988ba`, copia di lavoro | Sito | Tre versioni: prugna `#5a2d82`, redesign con font, palette calda |
| Registro delle decisioni | `website/docs/decisioni.md` | Sito | D-01–D-42, con checkpoint 1 e 2: distingue proposte e conferme del gruppo |
| Evoluzione dei checkpoint | diff `4baa4e9..38a1910` su `decisioni.md` | Sito | D-08 «Sostieni la Ricerca» superata da D-20 «ideaBlume»; `example.org` sostituito da D-22 |
| Verifica con le personas | `website/docs/08_verifica_personas.md` (`60712ad`) | Sito, journey | 64 punti di dolore: 58 risolti e 6 parziali. Cognitive walkthrough, non test con utenti. **Non aggiornato dopo D-42** |
| Valutazione euristica | `website/docs/09_valutazione_euristica.md` (`60712ad`) | Sito | V-01–V-10, limite «chi valuta ha anche progettato». **Non aggiornata dopo D-42** |
| Verifiche tecniche | `website/docs/verifiche/*.md`, `axe.json`, `website/tools/*` | Sito | Stato attuale: axe 0 violazioni su 58 pagine, 66/66 percorsi, 394/394 dati, 180/180 contrasti, Lighthouse 95–98 |
| Correzioni da verifica | diff `56e2a95..e1ebd20` e `e1ebd20..60712ad` su `js/ideablume.js`, `faq.html`, `tools/build.py` | Sito | Ricerca (due correzioni successive), link FAQ distinguibili, menu e CLS, link alle regole del raddoppio |
| Screenshot versione 1 | `e1ebd20:…/screenshot/home-1280.jpg`, `donazione-1280.jpg`, `progetto-1280.jpg` | Sito | Palette prugna; avviso «Pagamento simulato» visibile |
| Screenshot versione 2 | `f0988ba:…/screenshot/*` | Sito | Redesign con Inter e Bricolage Grotesque |
| Screenshot versione 3 | `website/docs/verifiche/screenshot/*` (03/11/2026) | Sito | Palette calda, interruttore del tema, nessun avviso |
| Decisione D-42 | `website/docs/decisioni.md`, `tools/soluzioni.py` (copia di lavoro) | Sito, uso responsabile | Tolti avvisi e segnaposto; informazioni istituzionali inventate presentate come stabilite; 3 problemi passano da «parziale» a «risolto» |
| Testi prima di D-42 | `f0988ba:assignment2/website/i18n/it.json` (`prototype`, `simulated`, `faq-prototipo`, 41 `{DV}`) | Sito, uso responsabile | Il sito dichiarava di essere un prototipo e marcava le informazioni non verificate |
| Pubblicazione | `.github/workflows/sito.yml`, `website/README.md`; `f0988ba`, `dd07a0a` | Sito | Build e deploy su GitHub Pages dal branch `main`. **Nessuna prova dell'URL pubblico** |
| README del sito | `website/README.md` | Sito | Avvio, struttura, stack, limiti tecnici, informazioni istituzionali |

## 4. Materiali esterni e prove mancanti

| Elemento | Stato |
|---|---|
| `MATERIALI_EXTRA` delle impostazioni | Ancora segnaposto: nessun estratto di conversazione indicato |
| Conversazioni di generazione di tutte le personas | Non presenti nel repository |
| Output grezzi di P01–P09 | Non salvati. Per P01–P03 restano solo le citazioni di Alex |
| Strumento usato per P04–P09 | Non documentato. `README.md` indica un modello **consigliato** (Claude Opus 5.5), che non prova l'uso effettivo |
| Prompt usato per il redesign e per D-40, D-41, D-42 | Non salvato: in `decisioni.md` c'è solo la sintesi delle richieste |
| Esecuzioni del prompt V00 | Nessuna traccia |
| Prompt di questa relazione (REL-AI-01) | Fornito nella conversazione del 03/11/2026, citabile in Appendice B |

## 5. Incoerenze tra le prove da non nascondere nella relazione

1. **Maturità diversa delle personas.** P01–P06 sono generiche (v3, As-is); P07–P09 e J07–J09 sono v1 su `main`, e la revisione delle sole schede P07–P09 (`d3e3440`) è rimasta su un altro branch; P10–P12 sono v2 sul nuovo sito con journey To-be. Il sito è stato costruito a partire dalle v1 (`decisioni.md` D-04), perché il suo branch si stacca da `c67c067`, prima di `d3e3440`.
2. **Prompt e output di P12 divergono.** Il prompt in `personas/P12_maria_lombardi.md` descrive ancora Forlì e una promotrice che lancia una campagna; l'output è una partner a Torino. L'approvazione del gruppo non risulta: in `da_rivedere_P10-P12.md` §2.2 le caselle sono vuote e D-04 chiede di riverificare.
3. **`08` e `09` non concordano con `05`.** `08` e `09` riportano ancora segnaposto, «parziale» e Lighthouse 100; `05`, il README del sito e le verifiche sono allineati alla copia di lavoro: nessun parziale, Lighthouse 95–98.
4. **Un miglioramento apparente.** I tre «parziali» di `60712ad` (P-021, P-064, P-079) risultano «risolti» nella copia di lavoro solo perché D-42 ha sostituito i segnaposto con informazioni stabilite dal gruppo, non verificate presso l'Ateneo. X03 resta «non trovato in nessun file» eppure P-056 è «risolto».
5. **Il sito non dichiara più di essere fittizio.** Vedi `01_indice.md`, decisione 1.

## 6. Aggiornamento dopo il checkpoint (03/11/2026)

- **Versione finale del sito:** i 95 file indicati come copia di lavoro sono ora nel commit `797fc7e` (senza riga di co-autore), già su `origin/main`. Dove sopra si legge «copia di lavoro», la versione finale è questa.
- **Dichiarazioni del gruppo:** componenti; Claude Code e Codex usati per tutto il progetto; materiali forniti: relazione di assignment 1 e appunti; uso responsabile dell'IA; modifiche manuali a didascalie e design. Sono citate come dichiarazioni, non come prove.
- **Sito pubblicato:** https://andreock.github.io/hci_gruppo_a/ risponde. Controllate il 03/11/2026 home, donazione, FAQ e chi siamo: nessun riferimento a prototipo, simulazione o contenuti inventati; compaiono «gestito dall'Ufficio ideaBlume dell'Ateneo», telefono e, in donazione e FAQ, «deducibile dal reddito».
- **Corrispondenza tra account e persone**, dedotta dai nomi e da confermare: andreock e Andrea Canale → Andrea Canale; Alex → Alexandru Ioan Chindris; antofallea → Antonio Fallea; lorenzorizzolo → Lorenzo Rizzolo.
- **Conversazioni locali:** non consultate, perché il gruppo non ha indicato di farlo. Il prompt SITO-01 resta da fornire.
