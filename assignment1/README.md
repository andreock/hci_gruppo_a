# Assignment 1 – Valutazione euristica di IdeaGinger × Università di Torino

Valutazione con le 10 euristiche di Nielsen della sezione di IdeaGinger dedicata all'Università di Torino
(pagina di partenza: <https://www.ideaginger.it/partner/universita-di-torino.html>).

Il lavoro è diviso in quattro parti, una per componente. Ogni componente analizza le proprie pagine e
consegna la sua parte in `parti/<nome>/`; il documento finale del gruppo si assembla da lì.

## Struttura

```
assignment1/
├── README.md                     questo file
├── assignment1_gruppoX.pdf       consegna finale del gruppo (da creare unendo le parti)
└── parti/
    ├── antofallea/               parte 1 – completata
    │   ├── valutazione_antofallea.pdf
    │   ├── problemi_antofallea.csv
    │   └── src/                  sorgente HTML + screenshot
    ├── antofallea2/              approfondimento di antofallea – completato (stessa struttura)
    └── <nome>/                   parti 2, 3, 4 – stessa struttura
```

## Stato delle parti

| Parte | Componente | Pagine analizzate | Stato |
|---|---|---|---|
| 1 | antofallea | Pagina partner UniTo (schede «Partnership» e «Progetti») · Fai Brillare la Ricerca! · BRIGHT · Pagina 404 | Completata: 22 problemi |
| 1 bis | antofallea | Menu «Partner» · Servizi · Come funziona (cartella `antofallea2`) | Completata: 16 problemi |
| 2 | _da compilare_ | _da compilare_ | Da fare |
| 3 | _da compilare_ | _da compilare_ | Da fare |
| 4 | _da compilare_ | _da compilare_ | Da fare |

## Convenzioni comuni (per poter unire le parti)

- **Scheda di ogni problema**: ID, pagina/URL e task, descrizione e conseguenze, euristica con motivazione,
  severità (0–4) con giustificazione e indicatori di frequenza, impatto e persistenza, proposta, screenshot numerato. Le colonne di
  `parti/antofallea/problemi_antofallea.csv` sono il modello (separatore `;`, UTF-8, si apre in Excel o Fogli Google).
- **Una sola euristica prevalente per problema**; un problema che si ripete su più pagine si descrive una volta
  elencando le pagine.
- **ID**: ogni parte numera i propri problemi da `P01`. Nel documento finale vanno rinumerati in sequenza
  (oppure prefissati con l'iniziale del componente) per evitare doppioni.
- **Problemi trasversali** (header, menu «Cerca progetti» e «Partner», footer, banner cookie, ricerca, checkout):
  la parte 1 li ha già registrati (P03, P06, P08, P11, P12, P17, P18). Prima di aggiungerne uno uguale,
  controllare il CSV e, se serve, aggiungere solo la pagina in cui ricompare.
- **Dichiarare sempre** data della valutazione e dispositivi/browser usati: contenuti e stato delle campagne cambiano.

## Parte 1 in breve

- Data: 12 ottobre 2026 · Chrome 155 su Windows 10 (1366 × 768) e emulazione mobile 390 × 844.
- 8 task, 22 problemi: 4 gravi (severità 3), 15 minori, 3 cosmetici, nessuno critico.
- Oltre il richiesto: confronto desktop/mobile, percorso di donazione su una campagna attiva (senza pagamento),
  tre proposte di riprogettazione illustrate.

Per rigenerare il PDF dopo una modifica: aprire `parti/antofallea/src/presentazione.html` in Chrome e stampare
in PDF (formato 1280 × 720 px, senza margini, grafica di sfondo attiva).

## Approfondimento (cartella `antofallea2`) in breve

- Data: 13 ottobre 2026 · stessi dispositivi della parte 1.
- 6 task, 16 problemi: 1 grave (severità 3), 11 minori, 4 cosmetici, nessuno critico.
- Non ripete i problemi della parte 1: dove un tema era già stato registrato, la scheda lo richiama.
- Oltre il richiesto: confronto desktop/mobile e tre proposte di riprogettazione illustrate.

## Consegna finale

Formato PDF, nome `assignment1_gruppox.pdf` con il numero del gruppo al posto di «x», una sola consegna per gruppo.
Nel documento unito servono un'unica introduzione (obiettivo, metodo, task, pagine), i problemi di tutte le parti
raggruppati per euristica e una sintesi comune dei problemi prioritari.
