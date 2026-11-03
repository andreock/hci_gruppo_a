# 06 · Architettura dell'informazione di ideaBlume

ideaBlume è il crowdfunding per i progetti di ricerca dell'Università di Torino. Dentro il sito, il **Programma di cofinanziamento dell'Ateneo** seleziona alcuni progetti e raddoppia la cifra raccolta se raggiungono l'obiettivo. Prototipo didattico: nessun pagamento reale.

Principio guida: **prima i progetti da sostenere, poi le regole, poi i servizi per chi propone**. Su IdeaGinger accadeva il contrario (P-004, P-007): il programma era nascosto in un menu «Partner» di 25 voci e i servizi per i promotori occupavano la prima schermata.

## 1. Mappa del sito

```
ideaBlume (index.html)                                   [en/index.html]
├── Progetti ─────────────── progetti.html  (elenco, filtri, ordinamento)
│   └── Pagina progetto ──── progetto-<slug>.html  (×10 progetti)
│       └── Donazione ────── donazione.html?progetto=<slug>[&ricompensa=<id>]
│           └── Conferma ─── donazione-conferma.html?codice=…
├── Cerca ────────────────── cerca.html?q=…  (risultati e «nessun risultato»)
├── Il programma dell'Ateneo programma.html  (stato del bando, regole del raddoppio, edizioni)
├── Come funziona ────────── come-funziona.html  (#sostenitori, #promotori)
├── Proponi un progetto ──── proponi.html  (chi può proporre, due percorsi, consigli, tempi e costi, #gruppi)
│   ├── Candidatura ──────── candidatura.html  (ricercatori UniTo, simulata)
│   └── Collaborazione ───── collabora.html  (enti esterni, simulata)
├── Chi siamo ────────────── chi-siamo.html
├── Aiuto
│   ├── Domande frequenti ── faq.html  (#sostenitori, #promotori, #generali, #parole)
│   └── Contatti ─────────── contatti.html  (recapiti, orari, modulo «Scrivici»)
├── Accessibilità ────────── accessibilita.html  (dichiarazione e segnalazioni)
└── Pagina non trovata ───── 404.html  [en/404.html]
```

Tutte le pagine esistono in italiano nella radice e in inglese in `en/` con lo stesso nome di file (D-21).

## 2. Pagine distinte (almeno 12, D-23 / R-133)

| # | Pagina | File | Funzione principale | Personas principali |
|---|---|---|---|---|
| 1 | Home | `index.html` | Dire che cos'è e chi lo gestisce; progetti in corso; ricerca; regole in breve; ingresso per chi propone | tutte; P01, P06, P07, P12 |
| 2 | Progetti | `progetti.html` | Elenco con filtri e ordinamento nella URL, conteggio, stato testuale | P05, P08, P03 |
| 3 | Risultati della ricerca | `cerca.html` | Risultati con conteggio; «nessun risultato» con alternative | P07, P03, P08 |
| 4 | Pagina progetto | `progetto-<slug>.html` | Riquadro di stato, soglie e raddoppio, indice, sezioni fisse, ricompense, contatto con il gruppo | P01, P02, P04, P05, P10 |
| 5 | Donazione | `donazione.html` | Percorso in 5 passi con validazione in linea e riepilogo | P01, P02, P03, P04, P06, P07 |
| 6 | Conferma della donazione | `donazione-conferma.html` | Codice di riferimento, riepilogo stampabile, ricevuta, contatti | P01, P06 |
| 7 | Il programma dell'Ateneo | `programma.html` | Stato del bando con date, fasi, regola del raddoppio con esempio, edizioni e numeri | P06, P08, P09, P10 |
| 8 | Come funziona | `come-funziona.html` | Passi numerati per sostenitori e per promotori, ognuno con il link all'azione | P01, P09 |
| 9 | Proponi un progetto | `proponi.html` | Chi può proporre (ricercatori, enti esterni), due percorsi passo per passo, consigli, tempi e costi, indicazioni per i gruppi con una campagna in corso | P09, P12 |
| 10 | Candidatura al programma | `candidatura.html` | Modulo simulato per ricercatori UniTo | P09 |
| 11 | Proponi una collaborazione | `collabora.html` | Modulo simulato per enti esterni, con «inviare non vi impegna» e riepilogo stampabile | P12 |
| 12 | Domande frequenti | `faq.html` | FAQ per destinatario e argomento, ricerca interna, accordion, ancore | P06, P09, P12, P04 |
| 14 | Chi siamo | `chi-siamo.html` | Chi gestisce il servizio, la sua storia, come lavora, dove vanno i soldi | P06, P12 |
| 15 | Contatti | `contatti.html` | Recapiti e orari da un'unica fonte, modulo «Scrivici» con conferma | P01, P06, P11 |
| 16 | Accessibilità | `accessibilita.html` | Stato di conformità verificato, limiti noti, come segnalare un problema | P03, P11 |
| 17 | Pagina non trovata | `404.html` | Spiega l'errore nella lingua giusta; ricerca, home, progetti, FAQ | tutte |

## 3. Navigazione globale

### Intestazione (uguale in tutte le pagine)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ [Salta al contenuto]  (visibile al focus)                                    │
│ ✿ ideaBlume                                                          EN ▸    │
│ Il crowdfunding per la ricerca                                               │
│   dell'Università di Torino                                                  │
├──────────────────────────────────────────────────────────────────────────────┤
│ Home · Progetti · Chi siamo · Come funziona · Il programma dell'Ateneo ·     │
│ Proponi un progetto · Domande frequenti · Contatti                           │
└──────────────────────────────────────────────────────────────────────────────┘
```

- **8 voci** di primo livello, compresa «Home» (D-44), senza tendine (P-008: oltre 70 voci su IdeaGinger). Le voci iniziano con la parola chiave (aspetto positivo S58).
- Il **programma dell'Ateneo** è una voce di primo livello con il suo nome (P-007).
- **Ricerca** in homepage e nella pagina Progetti, dove è unita ai filtri; non è più nell'intestazione (P-005, D-43).
- **Logo** e voce «Home» scritta per esteso portano alla home; nessuna icona senza etichetta (P-010, D-44). **Lingua**: «English» / «Italiano» scritto per esteso, con `lang` e `hreflang`, porta alla stessa pagina nell'altra lingua conservando filtri e ancora (R-112).
- **Voce corrente** con `aria-current="page"` e sottolineatura spessa (P-009).
- **Mobile (< 900 px)**: pulsante «Menu» con testo e icona, `aria-expanded`, apertura con Invio/Spazio, chiusura con Esc e con il pulsante; a menu chiuso le voci non ricevono il focus (`hidden`), il focus torna al pulsante (P-008, P-085). Voci alte 48 px per tocchi imprecisi (P01, P12).

### Piè di pagina (uguale in tutte le pagine)

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ Hai bisogno di aiuto?                Esplora           Per chi propone        │
│ ☎ 011 019 4250 (lun–ven 9:30–13,     Progetti          Proponi un progetto    │
│   14–17)                             Il programma      Candidatura            │
│ ✉ aiuto@ideablume.it                 Come funziona     Collaborazioni         │
│ Rispondiamo entro 2 giorni lavorativi Domande frequenti                       │
│ [Scrivici]                                                                    │
│ ────────────────────────────────────────────────────────────────────────────  │
│ Prototipo didattico realizzato per il corso di HCI: nessun pagamento reale.   │
│ Chi siamo · Accessibilità · Privacy (simulata)              English           │
└──────────────────────────────────────────────────────────────────────────────┘
```

Il blocco «Aiuto» è nella stessa posizione in ogni pagina (WCAG 3.2.6, R-085) con orari e tempi di risposta da un'unica fonte (`data/sito.json`), telefono e mail cliccabili (P-080, P-081). Il piè di pagina ha contrasto ≥ 7:1 (P-034: 2:1 su IdeaGinger) e titoli di sezione in corpo normale.

### Altri elementi comuni

- **Briciole di pane** sotto l'intestazione in tutte le pagine interne (P-016).
- **«Torna su»** in fondo alle pagine lunghe (progetto, elenco, FAQ, come funziona), come link con testo (P-015).
- **Titolo della finestra**: «Pagina – ideaBlume», unico per pagina, ≤ 60 caratteri (P-002). Pagina progetto: «Titolo breve – ideaBlume».

## 4. Percorsi principali per tipo di utente

### Sostenitore (donatore)

```
Home ──► Progetti (filtri) ──► Pagina progetto ──► Donazione (5 passi) ──► Conferma
  │          ▲      │                │  ▲
  │          └──────┘ Indietro:      │  └─ «Modifica importo» / «Torna al progetto»
  │        filtri e posizione        └─► «Scrivi al gruppo» (conferma immediata)
  │        conservati (P-027)
  └─► Cerca ──► Risultati (o «nessun risultato» con alternative) ──► Pagina progetto
Ingressi diretti: link condiviso a progetto-<slug>.html (P02, P04, P07, P11),
                  donazione.html?progetto=… aperta direttamente (P-061)
```

Personas: P01 (dal giornale alla ricerca), P02 (link dai social, interruzione e ripresa), P03 (solo tastiera), P04 (in inglese dall'inizio alla fine), P05 (confronto con filtri), P06 (verifica di affidabilità: Chi siamo → Programma → FAQ → Donazione), P07 (da smartphone, piccolo importo).

### Visitatore che si informa

```
Home ──► Il programma dell'Ateneo (stato, date, edizioni, numeri)
              ├─► Progetti?edizione=2024&stato=concluse ──► Pagina progetto (resoconto)
              └─► Contatti / Chi siamo
```

Persona: P08 (giornalista: edizioni, numeri coerenti con data, URL condivisibili).

### Promotore

```
Home («Hai un progetto di ricerca?») / menu «Proponi un progetto»
   └─► Proponi un progetto: chi può proporre · quanto costa · tempi
          ├─► Ricercatore UniTo ──► Il programma (requisiti, scadenze) ──► Candidatura (simulata) ──► conferma
          └─► Ente esterno ──► Collaborazione (simulata) ──► conferma con tempi e riepilogo stampabile
   Ogni passo cita il link a quello successivo (P-069). «Come funziona#promotori» e FAQ#promotori portano agli stessi due percorsi.
Gruppo con campagna in corso (P10, P11): Pagina progetto pubblica · Proponi#gruppi · Contatti («Segnala un problema»)
```

Personas: P09 (candidatura in più sessioni: ogni sezione ha un'ancora), P12 (contatto, non registrazione), P10–P11 (nessuna area riservata, D-17).

## 5. Schema delle URL

| Tipo | Italiano | Inglese | Note |
|---|---|---|---|
| Home | `index.html` | `en/index.html` | La radice è la pagina iniziale |
| Pagine statiche | `<nome>.html` | `en/<nome>.html` | Stessi nomi di file nelle due lingue |
| Progetto | `progetto-<slug>.html` | `en/progetto-<slug>.html` | `slug` stabile, ASCII (es. `alveari-sani`) |
| Elenco filtrato | `progetti.html?stato=in-corso&categoria=salute&dip=…&edizione=2026&ordina=scadenza` | idem | Filtri riflessi nella URL con `history.replaceState`; condivisibili |
| Ricerca | `cerca.html?q=api` | idem | Modulo `GET`; si apre dal campo di ricerca della home e della 404 |
| Donazione | `donazione.html?progetto=<slug>&ricompensa=<id>` | idem | Autosufficiente (P-061); senza parametri spiega che cosa fare |
| Ancore | `#presentazione`, `#fondi`, `#team`, `#ricompense`, `#aggiornamenti`, `#commenti`, `#sostenitori`; FAQ `#faq-<id>` e `#parola-<termine>` | idem (stessi id) | Gli id sono uguali nelle due lingue, così il selettore di lingua conserva l'ancora |
| Errore | `404.html` | `en/404.html` | Su GitHub Pages è servita la 404 della radice, che sceglie la lingua (D-21) |

Le URL sono relative: il sito funziona da `file://`, da un server locale e in una sottocartella di GitHub Pages.

## 6. Struttura delle pagine (wireframe testuali)

Larghezze: **mobile** una colonna; **desktop** (≥ 1024 px) contenitore di 1200 px al massimo, testo lungo a ~70 caratteri per riga.

### 6.1 Home

```
DESKTOP                                                   MOBILE
┌───────────────────────────────────────────────────┐     ┌─────────────────────┐
│ [intestazione]                                    │     │ ✿ ideaBlume  [Menu] │
├───────────────────────────────────────────────────┤     ├─────────────────────┤
│ H1 Sostieni la ricerca dell'Università di Torino  │     │ H1 Sostieni la      │
│ ideaBlume è il crowdfunding dei progetti di       │     │ ricerca dell'Univ.  │
│ ricerca dell'Università di Torino, gestito        │     │ di Torino           │
│ dall'Ufficio ideaBlume dell'Ateneo. Chi siamo ›   │     │ ideaBlume è … Chi   │
│ [Cerca un progetto…            ][Cerca]           │     │ siamo ›             │
│ [ Scopri i progetti in corso ]                    │     │ [Cerca…][Cerca]     │
├───────────────────────────────────────────────────┤     │ [Scopri i progetti] │
│ H2 Progetti in corso (5)          Tutti i progetti›│     ├─────────────────────┤
│ ┌────────┐ ┌────────┐ ┌────────┐                  │     │ H2 Progetti in corso│
│ │ card   │ │ card   │ │ card   │  (griglia, a capo│     │ ┌─────────────────┐ │
│ └────────┘ └────────┘ └────────┘   niente carosel.)│     │ │ card            │ │
├───────────────────────────────────────────────────┤     │ └─────────────────┘ │
│ H2 Come funziona in tre passi                     │     │ ┌─────────────────┐ │
│ 1 Scegli un progetto  2 Dona  3 Se l'obiettivo è  │     │ │ card            │ │
│ raggiunto, l'Ateneo raddoppia ›   Regola «tutto o │     │ └─────────────────┘ │
│ niente» in una frase › Come funziona              │     │ …                   │
├───────────────────────────────────────────────────┤     ├─────────────────────┤
│ H2 I numeri di ideaBlume (aggiornati al gg/mm/aa) │     │ H2 Come funziona    │
│ 5 campagne in corso · 8 concluse · € … raccolti · │     │ …                   │
│ … sostenitori  (calcolati dai dati, P-036)         │     ├─────────────────────┤
├───────────────────────────────────────────────────┤     │ H2 I numeri         │
│ H2 Ultimi aggiornamenti dai progetti (con date)   │     ├─────────────────────┤
├───────────────────────────────────────────────────┤     │ H2 Hai un progetto? │
│ H2 Hai un progetto di ricerca?  → Proponi ›       │     ├─────────────────────┤
├───────────────────────────────────────────────────┤     │ [piè di pagina]     │
│ [piè di pagina]                                   │     └─────────────────────┘
└───────────────────────────────────────────────────┘
```

Risolve: P-001 (frase iniziale e gestore), P-003 («Chi siamo» nella prima frase e nel menu), P-004 (progetti prima dei servizi), P-005 (ricerca visibile), P-013 (aggiornamenti datati), P-036 (numeri da un'unica fonte), P-037 (nessun carosello), P-038 (titoli interi).

### 6.2 Card di progetto (componente)

```
┌───────────────────────────────────────┐
│ [illustrazione SVG, alt=""]           │
│ SALUTE · Edizione 2026                │  ← categoria ed edizione (P-030)
│ H3 Alveari sani: monitorare la salute │  ← titolo intero, è l'unico link (P-029, P-038)
│    delle api del Piemonte             │
│ Gruppo ApiLab · Dipartimento di       │  ← formula unica (P-026)
│ Scienze Veterinarie, Università di T. │
│ ✔ Obiettivo raggiunto · puoi ancora   │  ← stato: icona + testo + colore (P-022, P-024)
│   sostenerlo per 20 giorni            │
│ ███████████████████████ 130%          │  ← barra non interattiva (P-028, P-050)
│ € 7.800 raccolti su € 6.000           │
│ 142 sostenitori                       │
└───────────────────────────────────────┘
hover/focus: bordo spesso e ombra; tutta la card è cliccabile tramite il link del titolo
```

### 6.3 Progetti (elenco)

```
[briciole: Home › Progetti]
H1 Progetti di ricerca
Paragrafo: «Se un progetto del programma raggiunge l'obiettivo, l'Ateneo raddoppia la cifra.
Vale la regola tutto o niente: se l'obiettivo non viene raggiunto, ti restituiamo la donazione.» (P-048)
I numeri: 5 in corso · 8 concluse (P-028)
┌ Filtri (form GET, funziona anche senza JS) ─────────────────────────────────┐
│ Stato [Tutti ▾] Categoria [Tutte ▾] Dipartimento [Tutti ▾] Edizione [Tutte ▾]│
│ Ordina per [Scadenza più vicina ▾]   [Applica] (senza JS)  [Azzera i filtri] │
└──────────────────────────────────────────────────────────────────────────────┘
«Mostrati 5 di 10 progetti» (role=status)                           (P-032)
[griglia di card: 1 colonna mobile, 2 tablet, 3 desktop]
«Hai visto tutti i progetti di questa selezione.»  [Torna su]       (P-033, P-015)
Nessun risultato con questi filtri → «Nessun progetto corrisponde. Azzera i filtri / vedi tutte le campagne in corso»
```

Comportamento: i filtri aggiornano la URL senza ricaricare; il conteggio è annunciato; prima di uscire verso un progetto la posizione di scorrimento viene salvata per quella URL e ripristinata al ritorno (P-027). Senza JS il modulo invia la query e la pagina mostra tutti i progetti (filtri applicati dallo script solo con JS: limite dichiarato).

### 6.4 Pagina progetto

```
DESKTOP                                                         
[briciole: Home › Progetti › Alveari sani]
┌──────────────────────────────────────────┬───────────────────────────────┐
│ SALUTE · Edizione 2026 · Programma       │ RIQUADRO DI STATO (P-030)     │
│ dell'Ateneo                              │ ✔ Obiettivo raggiunto ·       │
│ H1 Alveari sani: monitorare la salute    │ puoi ancora sostenerlo per    │
│ delle api del Piemonte                   │ 20 giorni (scade il 20/11/26) │
│ Sottotitolo in una frase                 │ € 7.800 raccolti              │
│ Gruppo ApiLab · Dip. di Scienze          │ obiettivo € 6.000 · 130%      │
│ Veterinarie · Resp. prof. Franco Gallo   │ ████████████████              │
│ [illustrazione con alt descrittivo]      │ 142 sostenitori               │
│                                          │ [ Sostieni il progetto ]      │
│ IN QUESTA PAGINA (indice, P-049)         │ ┌ Obiettivo e raddoppio ────┐ │
│ Presentazione · Uso dei fondi · Team ·   │ │ Obiettivo € 6.000 raggiunto│ │
│ Ricompense · Aggiornamenti (2) ·         │ │ → l'Ateneo aggiunge € 6.000│ │
│ Commenti (5) · Sostenitori (142)         │ │ Secondo obiettivo € 9.000: │ │
│                                          │ │ due apiari in più. Le dona-│ │
│ H2 Presentazione                         │ │ zioni oltre € 6.000 vanno  │ │
│ H2 Uso dei fondi (tabella in testo:      │ │ qui e non sono raddoppiate │ │
│    voci che sommano all'obiettivo)       │ │ [DA VERIFICARE] (P-053)    │ │
│ H2 Team                                  │ │ ⓘ Tutto o niente [?]       │ │
│ H2 Ricompense (lista compatta)           │ └────────────────────────────┘ │
│ H2 Aggiornamenti (datati)                │ [Copia link] [Scrivi al gruppo]│
│ H2 Commenti                              │ (riquadro fisso durante lo     │
│ H2 Sostenitori                           │  scorrimento, P-052)           │
│ [Torna su]                               │                               │
└──────────────────────────────────────────┴───────────────────────────────┘
MOBILE: titolo → riquadro di stato con «Sostieni» → indice → sezioni nello stesso ordine.
```

Ricompense (lista compatta e confrontabile, P-042, P-045, P-065):

```
┌────────────────────────────────────────────────────────────────────────┐
│ Donazione libera · da € 5                                              │
│ Scegli tu l'importo. Nessuna ricompensa.   [Dona un importo libero]    │
├────────────────────────────────────────────────────────────────────────┤
│ € 15 · Cartolina illustrata degli apiari                               │
│ 38 persone l'hanno scelta · senza limite        [Scegli € 15]          │
├────────────────────────────────────────────────────────────────────────┤
│ € 50 · Vasetto di miele del progetto + cartolina                       │
│ 21 persone l'hanno scelta · restano 9 posti su 30   [Scegli € 50]      │
├────────────────────────────────────────────────────────────────────────┤
│ € 250 · Visita guidata a un apiario di ricerca                         │
│ 0 persone l'hanno scelta · restano 10 posti su 10   [Scegli € 250]     │
└────────────────────────────────────────────────────────────────────────┘
Sempre in ordine crescente; sempre gli stessi quattro dati, anche con 0 (P-045).
```

Campagna conclusa (P-040): il riquadro di stato diventa «■ Conclusa · obiettivo raggiunto il 15/02/2025 · € 9.120 su € 8.000 · l'Ateneo ha aggiunto € 8.000» con i pulsanti «Leggi i risultati» (ancora all'ultimo aggiornamento) e «Scopri i progetti in corso»; le ricompense diventano un elenco in sola lettura «Ricompense assegnate», senza pulsanti né campi.

Spiegazioni a comparsa (P-044): un `button` «Che cosa significa “tutto o niente”?» con `aria-expanded` che apre un riquadro sotto il pulsante (si chiude con Esc o con lo stesso pulsante), con link alla risposta nelle FAQ. Nessun link a «#».

«Scrivi al gruppo» (P-039): l'email del gruppo è già visibile; il pulsante apre un piccolo modulo nella pagina; all'invio «Invio in corso…» e poi «Messaggio inviato (simulazione). Il gruppo risponde di solito entro 3 giorni lavorativi.» in `role="status"`.

### 6.5 Donazione

```
[briciole: Home › Progetti › Alveari sani › Donazione]
H1 Sostieni «Alveari sani»
⚠ Pagamento simulato: nessun addebito reale (R-058)
┌ Riepilogo (sempre in alto, anche su mobile, P-057) ─────────────────────┐
│ Progetto: Alveari sani · Ricompensa: Vasetto di miele · € 50 [Modifica] │
└─────────────────────────────────────────────────────────────────────────┘
Passo 2 di 5 ─ ① Importo ✓ ─ ② I tuoi dati ─ ③ Privacy ─ ④ Pagamento ─ ⑤ Riepilogo
┌ Se ci sono errori (role=alert, riceve il focus) ───────────────────────┐
│ Correggi 2 campi: · Email › · Nome ›                                    │
└─────────────────────────────────────────────────────────────────────────┘
H2 I tuoi dati
Nome *            [                    ]   (autocomplete=given-name)
Cognome *         [                    ]   (family-name)
Email *           [                    ]   (type=email, autocomplete=email)
                  ⚠ Scrivi un indirizzo email completo, per esempio nome@esempio.it
Telefono (facolt.) [                   ]   (type=tel)
[← Indietro]                                         [Continua →]
«I dati restano salvati in questa scheda del browser finché non chiudi.» (P-051 / 3.3.7)
```

Passi:
1. **Importo o ricompensa** — lista compatta delle ricompense e «Donazione libera · da € 5»; frase «tutto o niente» accanto all'importo (P-035, P-054); esempio del raddoppio (P-048).
2. **I tuoi dati** — come sopra.
3. **Privacy e visibilità** — radio senza preselezione «Mostra il mio nome tra i sostenitori» / «Dona in forma anonima», con spiegazione di che cosa vedono il pubblico e il gruppo [DA VERIFICARE] (P-055, P-056); consenso privacy con casella nativa.
4. **Pagamento** — `fieldset` «Metodo di pagamento»: Carta di credito, debito o prepagata · PayPal · Satispay · Bonifico bancario (un'unica fonte, P-062); che cosa succede dopo per ciascuno; nessun numero di carta (R-058).
5. **Riepilogo** — progetto, ricompensa, importo, commissione stimata, totale, destino in caso di rimborso, ricevuta [DA VERIFICARE], regola «tutto o niente»; [Simula il pagamento].

→ **Conferma** (`donazione-conferma.html`): «Grazie! Donazione simulata registrata», codice di riferimento, riepilogo, [Stampa il riepilogo], che cosa succede alla scadenza, ricevuta e detraibilità [DA VERIFICARE], contatti.

Comportamento senza JS: la pagina mostra il messaggio «La donazione simulata richiede JavaScript» e i contatti; leggere progetti e regole resta possibile (R-135).

### 6.6 Il programma dell'Ateneo

```
[briciole]
H1 Il programma di cofinanziamento dell'Ateneo
┌ Stato attuale ────────────────────────────────────────────────────────────┐
│ Edizione 2026 · Fase 4 di 4: campagne in corso fino al 15/12/2026          │
│ Candidature per l'edizione 2027: [DA VERIFICARE con l'Ateneo]               │
│ ① Formazione ✓  ② Selezione ✓  ③ Accompagnamento ✓  ④ Raccolta e raddoppio │
│                                                       (in corso)           │
└────────────────────────────────────────────────────────────────────────────┘
H2 Come funziona il raddoppio — esempio numerico; caso oltre l'obiettivo
H2 Chi può candidarsi · H2 Requisiti · H2 Come e quando · H2 A chi scrivere
   [Candidati al programma] (→ candidatura.html, P-078)  Quanto costa (riquadro, P-071)
H2 Le edizioni in numeri (tabella: edizione, progetti, riusciti, raccolto, cofinanziato,
   sostenitori; calcolata dai dati, P-036) → link «Progetti dell'edizione 2025»
Ultimo aggiornamento: 31/10/2026
```

### 6.7 Proponi un progetto

```
H1 Proponi un progetto
┌ Quanto costa (in evidenza, primo blocco dopo l'introduzione, P-071) ─┐
│ Per i gruppi selezionati dal programma: [DA VERIFICARE con l'Ateneo]  │
│ Commissioni dei pagamenti: a carico dei sostenitori [DA VERIFICARE]   │
└───────────────────────────────────────────────────────────────────────┘
H2 Chi può proporre
  ┌ Sei una ricercatrice o un ricercatore UniTo? ┐  ┌ Sei un ente esterno? ───────────┐
  │ requisiti in breve, scadenza                 │  │ associazioni, scuole, imprese:   │
  │ [Candidati al programma]                     │  │ potete collaborare con un gruppo │
  └──────────────────────────────────────────────┘  │ UniTo [IPOTESI/DA VERIFICARE]     │
                                                    │ [Proponi una collaborazione]      │
                                                    └──────────────────────────────────┘
H2 Tempi e fasi (con segnaposto)  H2 Esempi: progetti con scuole e territorio (link filtrati)
H2 Per i gruppi con una campagna in corso (contenuti in due lingue, segnala un problema)
```

### 6.8 Candidatura e collaborazione (moduli simulati)

```
H1 Candidatura al programma (simulata)
«Prima di iniziare: ti servono titolo, obiettivo in euro, uso dei fondi, gruppo.
Tempo stimato: 10 minuti. I dati restano in questa scheda finché non invii.»
Campi con etichetta visibile sopra, indicazione «facoltativo» sui pochi facoltativi,
autocomplete (name, email, organization), select del dipartimento, textarea con conteggio
caratteri; consenso = casella nativa (P-067, P-072, P-073); errori in linea che spariscono
(P-077); riepilogo errori in testa.
[Invia la candidatura (simulazione)] → conferma: che cosa succede dopo, entro quando, chi
risponde, riepilogo stampabile.
```

`collabora.html` ha la stessa struttura con campi per enti esterni e la nota in evidenza «Inviare questo modulo non impegna la vostra associazione» (J12-F4).

### 6.9 Come funziona

```
H1 Come funziona ideaBlume
Indice: Per chi sostiene · Per chi propone un progetto · Quanto costa · Hai ancora dubbi?
H2 Per chi sostiene (ol)
  1 Scegli un progetto → [Vedi i progetti in corso]
  2 Scegli una ricompensa o una donazione libera da € 5 → [Che cos'è una ricompensa]
  3 Paga in modo sicuro (pagamento simulato) → [Metodi di pagamento]
  4 Alla scadenza: obiettivo raggiunto → i fondi vanno al gruppo e l'Ateneo raddoppia;
    non raggiunto → ti restituiamo la donazione (tutto o niente) → [Il raddoppio]
H2 Per chi propone un progetto (ol) — ogni passo con il link all'azione
H2 Quanto costa (stesso testo di Proponi e FAQ)
H2 Hai ancora dubbi? → FAQ · Contatti
```

### 6.10 Domande frequenti

```
H1 Domande frequenti
[Cerca nelle domande…]   «12 domande corrispondono» (role=status)
Vai a: Per chi sostiene · Per chi propone · Domande generali
H2 Per chi sostiene
  H3 Donazioni e pagamenti
    ▸ Posso donare senza scegliere una ricompensa?   (details/summary, id=faq-…)
    ▸ Che cosa succede se il progetto non raggiunge l'obiettivo?
    ▸ Il pagamento non è andato a buon fine: che cosa faccio?
  H3 Ricevuta, privacy e dati
  …
H2 Per chi propone un progetto
H2 Domande generali
Non hai trovato la risposta? → Contatti (telefono, email, orari)
Ultimo aggiornamento: …
```

Ogni risposta inizia con la risposta in una frase, poi i dettagli (P-082). Il link «Copia il link a questa risposta» usa l'ancora; aprendo `faq.html#faq-rimborso` la risposta è aperta e evidenziata.

### 6.11 Pagina 404

```
[intestazione]
H1 Pagina non trovata
L'indirizzo potrebbe essere scritto male o la pagina è stata spostata.
[Cerca un progetto…][Cerca]
Puoi andare a: Home · Tutti i progetti · Domande frequenti · Contatti
[piè di pagina]
```

## 7. Come la struttura risolve i problemi di navigazione

| Problema su IdeaGinger | Scelta di architettura | P-xxx |
|---|---|---|
| Menu e tendine con oltre 70 voci, senza Esc | 8 voci, nessuna tendina; menu mobile accessibile da tastiera | P-008 |
| Il programma UniTo si trova solo ricordando che è un «Partner» | Voce di primo livello «Il programma dell'Ateneo»; la ricerca trova anche il programma | P-007 |
| Servizi per promotori prima dei progetti | Home: progetti in corso subito dopo la frase iniziale; promotori in fondo | P-004 |
| Nessun campo di ricerca | Campo in home e nei filtri di Progetti; pagina risultati con «nessun risultato» | P-005, P-006 |
| «Chi siamo» solo nel footer | Nel menu principale e nella prima frase della home | P-003 |
| Pagine interne aperte in nuove schede, link esterni non segnalati | Stessa scheda; link esterni con «(sito esterno)» | P-014 |
| Posizione persa tornando indietro, «Altri» opaco | Tutti i progetti in una griglia con conteggio; filtri nella URL; posizione salvata | P-027, P-032, P-033 |
| Pagina progetto lunghissima senza indice | Indice iniziale, sezioni in ordine fisso, riquadro di stato fisso, «Torna su» | P-049, P-041, P-045, P-015 |
| Percorso del promotore che finisce nella registrazione generica | «Proponi un progetto» con due percorsi distinti e costi subito | P-078, P-071, P-035 |
| FAQ in un'unica lista, Come funziona senza titoli | FAQ per destinatario con ricerca; Come funziona diviso con passi linkati | P-075, P-074, P-069 |
| Due lingue mescolate | Due versioni complete con selettore che porta alla stessa pagina | P-043, P-051 |
| 404 fuori dal sito, in inglese | 404 nel modello del sito, nella lingua giusta, con ricerca | P-019, P-020 |

## 8. Contenuti previsti per i progetti (per coprire tutti gli stati)

10 progetti inventati, attribuiti a dipartimenti reali dell'Università di Torino (nomi dei gruppi e delle persone inventati). Date rispetto al 31/10/2026.

| Slug | Tema | Dipartimento | Edizione | Stato previsto | Persona che lo usa |
|---|---|---|---|---|---|
| `alveari-sani` | Salute delle api in Piemonte | Scienze Veterinarie | 2026 | In corso, **oltre l'obiettivo** (130%), 20 giorni | P10, P05 |
| `neonati-virus` | Proteggere i neonati dai virus respiratori | Scienze della Sanità Pubblica e Pediatriche | 2026 | In corso, **vicino alla scadenza** (5 giorni), 84% | P01 |
| `clima-giovani` | Clima e benessere psicologico dei giovani | Psicologia | 2026 | In corso, 61%, 26 giorni | P02, P04 |
| `aria-aperta` | Sensori open source per la qualità dell'aria | Informatica | 2026 | In corso, 47%, 33 giorni | P11 |
| `matematica-accessibile` | Formule matematiche leggibili con lo screen reader | Matematica «Giuseppe Peano» | 2025 | **Concluso, obiettivo raggiunto** | P03 |
| `plastica-batteri` | Batteri che degradano le microplastiche | Biotecnologie Molecolari e Scienze per la Salute | 2025 | Concluso, raggiunto con secondo obiettivo | P08 |
| `dialetti-archivio` | Archivio sonoro dei dialetti piemontesi | Studi Umanistici | 2025 | **Concluso, obiettivo non raggiunto** | P08 |
| `scienza-doposcuola` | Laboratori di scienze nei doposcuola di quartiere | Filosofia e Scienze dell'Educazione | 2024 | Concluso, raggiunto (progetto con il territorio) | P12 |
| `rifugi-frane` | Frane e rifugi alpini: una mappa del rischio | Scienze della Terra | 2024 | Concluso, non raggiunto | P08 |
| `robot-anziani` | Robot sociali per l'autonomia delle persone anziane | Informatica | 2023 | Concluso, raggiunto (edizione più vecchia) | P08 |

Ogni progetto avrà: titolo, sottotitolo, dipartimento, gruppo, team (3–4 persone inventate con ruoli realistici), categoria, descrizione divulgativa, uso dei fondi con voci che sommano all'obiettivo, 3–6 ricompense più la donazione libera, 1–3 aggiornamenti datati, alcuni commenti, scadenza. I giorni rimanenti saranno calcolati dalla data corrente. **Decisione aperta (D-24)**: come comportarsi quando il sito viene aperto dopo la scadenza delle campagne 2026 (vedi `decisioni.md`).
