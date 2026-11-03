# ideaBlume · assignment 2 (HCI, Gruppo A)

**ideaBlume** è il sito di crowdfunding per i progetti di ricerca dell'Università di Torino. Comprende un **programma di cofinanziamento dell'Ateneo**: i progetti selezionati ricevono dall'Università una cifra pari all'obiettivo, se lo raggiungono.

Il progetto riparte dai 90 problemi di usabilità trovati su IdeaGinger in assignment1 e dalle 12 personas e dai 12 journey dell'assignment 2. Ogni scelta è tracciata in `docs/05_tracciabilita.md`.

## Come aprirlo

- **Senza server** (come richiesto da `assignment2/Istruzioni.md`): aprire **`index.html`** con un doppio clic. Tutto funziona da `file://`: filtri, ricerca, donazione, moduli, tema chiaro e scuro, versione inglese.
- **Con un server locale** (facoltativo): `python3 -m http.server` nella cartella `website/`, poi <http://localhost:8000/>.
- **Versione inglese**: link «English» in alto a destra in ogni pagina, oppure `en/index.html`.

Percorso principale consigliato per provarlo: Home → «Scopri i progetti in corso» → un progetto (per esempio «Proteggere i neonati dai virus respiratori») → «Sostieni il progetto» → 5 passi → «Paga ora» → conferma.

### Pubblicazione su GitHub Pages

La pubblicazione è automatica con la GitHub Action `.github/workflows/sito.yml` (nella radice del repository): a ogni push sul branch `main` che tocca `assignment2/website/` esegue `tools/build.py`, lancia `verifica-dati.py` e `verifica-link.py` e pubblica il sito (senza `tools/` e `docs/`). Sulle pull request esegue solo build e verifiche. Si può avviare anche a mano da «Actions → Run workflow».

Le pagine inglesi (`en/*.html`) **non sono nel repository** (sono in `.gitignore`): le genera la build, in locale con `python3 tools/build.py` e online nell'Action. Prima di aprire il sito da `file://` o di creare lo zip bisogna quindi lanciare la build.

Configurazione una tantum: Settings → Pages → Source «GitHub Actions»; in Settings → Environments → `github-pages` consentire il deploy dal branch `main`. Il file `.nojekyll` evita l'elaborazione di Jekyll. La pagina `404.html` funziona a qualunque profondità dell'indirizzo e mostra la versione inglese per gli indirizzi sotto `/en/`.

### Archivio per la consegna

Per lo zip richiesto (`assignment2_gruppox.zip`) bisogna prima rigenerare le pagine (così è presente anche `en/`), poi comprimere la cartella `website/` escludendo `tools/node_modules/`:

```bash
cd assignment2 && python3 website/tools/build.py && zip -r assignment2_gruppoA.zip website -x "website/tools/node_modules/*" "*.DS_Store"
```

## Pagine (17 tipi, in italiano e in inglese: 58 file HTML)

| Pagina | File | Funzione |
|---|---|---|
| Home | `index.html` | Che cos'è e chi lo gestisce, ricerca, progetti in corso, come funziona in 3 passi, numeri, aggiornamenti |
| Progetti | `progetti.html` | Elenco con filtri e ordinamento salvati nella URL, conteggio, ritorno nella stessa posizione |
| Ricerca | `cerca.html` | Risultati e caso «nessun risultato» con alternative |
| Pagina progetto (×13) | `progetto-<slug>.html` | Stato, obiettivo e raddoppio, indice, sezioni in ordine fisso, ricompense, scrivi al gruppo |
| Donazione | `donazione.html?progetto=…` | 5 passi con validazione in linea, dati conservati, commissioni nel riepilogo |
| Conferma | `donazione-conferma.html` | Codice di riferimento, riepilogo stampabile, che cosa succede adesso |
| Programma dell'Ateneo | `programma.html` | Stato del bando, fasi, regole del raddoppio, requisiti, costi, edizioni in numeri |
| Come funziona | `come-funziona.html` | Passi per chi sostiene, chi propone, gruppi con una campagna in corso |
| Proponi un progetto | `proponi.html` | Chi può proporre, costi in evidenza, due percorsi |
| Candidatura | `candidatura.html` | Modulo per ricercatori UniTo |
| Collaborazione | `collabora.html` | Modulo per associazioni ed enti esterni |
| Domande frequenti | `faq.html` | Per destinatario e argomento, ricerca interna, ancore |
| Glossario | `glossario.html` | Termini spiegati in modo semplice |
| Chi siamo | `chi-siamo.html` | Chi gestisce il servizio, dove vanno i soldi |
| Contatti | `contatti.html` | Recapiti, orari, modulo «Scrivici» |
| Accessibilità | `accessibilita.html` | Dichiarazione con verifiche e limiti |
| Pagina non trovata | `404.html` | Messaggio, ricerca e link utili |

## Struttura delle cartelle

```
website/
├── index.html, progetti.html, …          pagine italiane (generate)
├── en/                                   pagine inglesi (generate)
├── css/ideablume.css                     design system (token dei temi chiaro e scuro, componenti)
├── css/font.css, font-locali.css         font per server e per file:// (il secondo è generato)
├── fonts/                                Inter e Bricolage Grotesque (woff2) con licenze OFL
├── js/ideablume.js                       interazioni (miglioramento progressivo)
├── data/
│   ├── progetti.json                     i 13 progetti (fonte unica dei dati)
│   ├── sito.json                         contatti, regole, metodi di pagamento, dipartimenti, categorie
│   ├── ib-dati.js, testi-it.js, testi-en.js   generati per il JavaScript (non modificare a mano)
├── i18n/it.json, i18n/en.json            tutti i testi dell'interfaccia e delle pagine
├── img/                                  segno del marchio e illustrazioni SVG dei progetti (generate)
├── tools/                                generatore e script di verifica
└── docs/                                 documentazione di progetto (01–09, decisioni, verifiche)
```

## Stack e motivazioni

- **HTML, CSS e JavaScript senza framework e senza CDN.** Motivi: la consegna chiede pagine che funzionino nel browser senza server; le prestazioni su mobile erano un problema grave di IdeaGinger (LCP 34 s in laboratorio sulla pagina progetto). Tailwind e Bootstrap sono stati valutati per il redesign e scartati (D-35).
- **Design system v3** (D-35–D-41): palette calda (prugna bruna, arancio terracotta, verde bosco su crema), font open source **Inter** e **Bricolage Grotesque** (Fontsource, SIL OFL 1.1) ospitati nel sito, **tema chiaro predefinito e tema scuro a scelta** con un interruttore, intestazione con menu fisso da 900 px. Da `file://` i font sono caricati da `css/font-locali.css` (incorporati), su un server dai file `.woff2`. Risultato: Lighthouse mobile 95–98 per le prestazioni (CLS 0) e 100 per accessibilità, best practices e SEO su home, elenco, progetto e donazione.
- **Pagine statiche generate** da `tools/build.py` (Python, solo libreria standard) a partire da un unico file di dati e da un JSON di traduzioni per lingua. Motivi: numeri sempre coerenti tra elenco, pagina e contatori (P-036); inglese completo senza copiare a mano le pagine (P-043); contenuti leggibili anche senza JavaScript.
- **JavaScript come miglioramento progressivo**: tema, menu mobile, date relative, filtri, ricerca, FAQ, spiegazioni a comparsa, donazione, validazione. I dati sono in file `.js` e non in `.json` letti con `fetch()`, perché da `file://` i browser bloccano `fetch()`.
- **Date relative**: le campagne in corso hanno date calcolate a partire da oggi (`"rel:N"` nei dati), così il sito resta provabile anche dopo la consegna (D-24). Le campagne concluse hanno date fisse.

Tutte le scelte sono motivate in `docs/decisioni.md` (D-01–D-42).

## Come modificare il sito

Dopo ogni modifica a dati o testi:

```bash
python3 tools/build.py          # rigenera le 58 pagine, le illustrazioni, i file dati JS e css/font-locali.css
```

La build si ferma con un errore se manca una traduzione o una variabile.

- **Aggiungere un progetto**: aggiungere un oggetto a `data/progetti.json`, copiando un progetto esistente. Campi in due lingue `{"it": …, "en": …}`; le voci di `fondi` devono sommare all'`obiettivo`. Per una campagna in corso usare `"inizio": "rel:-10", "scadenza": "rel:30"`; per una conclusa date `"AAAA-MM-GG"` e il campo `esito`. `immagine.tema` è uno dei temi in `TEMI` di `build.py`. Poi rigenerare e lanciare `python3 tools/verifica-dati.py`.
- **Cambiare testi o contatti**: testi in `i18n/it.json` e `i18n/en.json` (stesse chiavi); contatti, orari, regole e metodi di pagamento in `data/sito.json`, un unico punto per tutto il sito.
- **Aggiungere una lingua**: creare `i18n/xx.json` con le stesse chiavi, aggiungerla a `LINGUE` in `tools/build.py` e assegnarle una cartella di uscita (come `en/`).
- **Cambiare la palette**: i colori sono solo nei token di `css/ideablume.css` (un blocco per il tema chiaro, uno per quello scuro), più i colori delle illustrazioni in `TEMI` di `tools/build.py`. Dopo ogni modifica: `python3 tools/contrasto.py`.

## Verifiche

Gli script di verifica richiedono Node.js e Google Chrome. Una volta sola: `cd tools && npm install`.

| Script | Che cosa controlla | Ultimo risultato |
|---|---|---|
| `python3 tools/contrasto.py` | Contrasti di 90 coppie di colori, tema chiaro e scuro | 180/180 conformi |
| `python3 tools/verifica-link.py` | Link interni, ancore, nuove schede, risorse esterne | 0 problemi |
| `python3 tools/verifica-dati.py` | Coerenza dei numeri, stati, ordine delle sezioni, lessico, nessun testo provvisorio | 394/394 |
| `node tools/verifica-pagine.js` | axe-core (WCAG 2.2 A/AA) in entrambi i temi, errori JS, `h1`, titoli, 320 px | 0 violazioni su 58 pagine |
| `node tools/percorsi.js` | Percorsi da tastiera, interazioni, cambio di tema | 66/66 |
| `node tools/verifica-file.js` | Funzionamento da `file://` | 8/8 |
| `node tools/responsive.js` | 320/375/768/1280 px, zoom 200%, daltonismo, aree cliccabili | nessun problema |
| `node tools/prestazioni.js` | Lighthouse mobile su 4 pagine | prestazioni 95–98, CLS 0; accessibilità 100 |
| `python3 tools/genera-tracciabilita.py` | Rigenera `docs/05_tracciabilita.md` | 87 risolti, 3 n/a |

Dettagli in `docs/verifiche/README.md`.

## Documentazione

| Documento | Contenuto |
|---|---|
| `docs/01_inventario_fonti.md` | File del repository, strumenti, versioni di riferimento di personas e journey, metriche Core Web Vitals di IdeaGinger |
| `docs/02_problemi_consolidati.md` | 90 problemi di assignment1 deduplicati, con fonti |
| `docs/03_bisogni_personas.md` | Bisogni delle 12 personas e 64 punti di dolore dei journey |
| `docs/04_requisiti.md` | 102 requisiti con priorità, criterio di accettazione e verifica |
| `docs/05_tracciabilita.md` | Problema → requisito → soluzione → verifica, matrice personas × aree, copertura |
| `docs/06_architettura.md` | Mappa del sito, menu, percorsi, URL, wireframe |
| `docs/07_design_system.md` | Colori, contrasti, tipografia, componenti |
| `docs/08_verifica_personas.md` | Ogni punto di dolore ripercorso sul nuovo sito, con prove |
| `docs/09_valutazione_euristica.md` | Valutazione euristica del nuovo sito e confronto con assignment1 |
| `docs/decisioni.md` | Registro delle decisioni |
| `docs/verifiche/` | Report e screenshot delle verifiche |

## Limiti tecnici

- Il sito è statico, senza backend: donazione, candidatura, collaborazione e contatti si completano nel browser (`sessionStorage`) e non inviano dati a un server; non ci sono account né area riservata.
- I dati di una donazione iniziata restano solo nella scheda del browser: non si può riprendere da un altro dispositivo (V-03).
- Ricerca, filtri e donazione richiedono JavaScript; progetti, FAQ e pagine informative funzionano anche senza. Senza JavaScript il tema è quello chiaro e l'interruttore è nascosto.
- Test automatici solo con Google Chrome; da fare: Safari (iPhone), Firefox, screen reader reali (NVDA, VoiceOver) e test con utenti.
- Le personas sono proto-personas: le soluzioni vanno validate con persone reali.
- Con le date relative, l'anno delle campagne in corso resta «2026» anche se il sito viene aperto in un anno successivo.

## Informazioni istituzionali

Sono definite in un solo punto e valgono per tutto il sito (D-42):

- **Raddoppio**: cifra pari all'obiettivo, tetto di € 10.000 per progetto, nessun raddoppio oltre l'obiettivo.
- **Bando**: candidature per l'edizione 2027 dal 1° novembre 2026 al 31 marzo 2027 (`bando` in `data/sito.json`); obiettivo tra € 3.000 e € 10.000.
- **Costi**: nessuna quota per i gruppi selezionati; commissioni di pagamento 1,8% + € 0,35 (nessuna con il bonifico), non restituite in caso di rimborso.
- **Ricevuta**: ricevuta fiscale via email; donazione deducibile dal reddito.
- **Gestione**: Ufficio ideaBlume dell'Ateneo; fondi al dipartimento del gruppo, vincolati al progetto.
- **Tempi**: 10 giorni lavorativi per le risposte a candidature e collaborazioni, 2 per pubblicare gli aggiornamenti.
- **Recapiti** (`data/sito.json`): `aiuto@ideablume.it`, `programma@ideablume.it`, `collaborazioni@ideablume.it`, `<progetto>@ideablume.it`, telefono `011 019 4250`, «Corso della Ricerca 12, Torino».
