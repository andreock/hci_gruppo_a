# Assignment 4 · Test di usabilità di ideaBlume (Gruppo A)

Test «in svendita» alla Krug sul prototipo: **8 utenti × 4 task**, pensiero ad alta voce, metriche per utente e task, SUS, classificazione dei problemi e re-design.

## Stato

| Parte | Stato |
|---|---|
| Materiali del test (kit, task, schede) | pronti |
| Ispezione dei 4 percorsi: 8 problemi con misure sulla versione provata | fatta (`dati/problemi.csv`, `dati/misure.json`) |
| **Re-design** del prototipo per gli 8 problemi, con misure e schermate prima/dopo | **fatto** in `assignment2/website/` su questo branch |
| Sessioni con gli 8 utenti | **da fare**: i file `sessioni`, `sus`, `intervista`, `partecipanti` sono vuoti di proposito |
| Relazione | bozza: la parte su task, metodo, problemi e re-design è scritta; i risultati compaiono quando i CSV sono compilati |

Gli 8 problemi vengono da un'**ispezione** (difetti reali, misurati sul sito), non da osservazioni di utenti. Nelle colonne `utenti` ed `evidenza` di `problemi.csv` va scritto **che cosa è successo davvero nelle sessioni**; finché sono vuote, nella relazione la gravità è indicata come «stima» e la frequenza come «da rilevare».

## Che cosa c'è

| Cartella / file | Contenuto |
|---|---|
| `kit/kit_test.pdf` | Da stampare: preparazione, copione del facilitatore, consenso, questionario iniziale, cartoncini dei 4 task, scheda dell'osservatore (una pagina per task, con le ipotesi P1–P8 da verificare), SUS, intervista |
| `dati/*.csv` | I dati del test: `partecipanti`, `sessioni` (32 righe: utente × task), `sus`, `intervista`, `problemi`, `task` (tempi limite e tempo dell'esperto) |
| `dati/misure.json` | Misure prima/dopo scritte da `prima_dopo.py` (non modificare a mano) |
| `relazione/modello.html` | Il testo della relazione. Le parti `{{COSÌ}}` sono calcolate dai dati, quelle `<span class="todo">` sono da scrivere a mano |
| `relazione/tools/task.py` | Testo dei 4 task, criteri di successo, affermazioni SUS, regole di conteggio (fonte unica per kit e relazione) |
| `relazione/tools/genera.py` | Calcola tabelle, punteggi SUS, grafici e indice → `relazione/relazione.html` e `relazione/assignment4_gruppoA.pdf` |
| `relazione/tools/genera_kit.py` | Rigenera il kit |
| `relazione/tools/prima_dopo.py` | Ricostruisce la versione provata (branch `assignment3`), esegue i 4 task su entrambe le versioni, misura gli aspetti legati a P1–P8 e salva le schermate `relazione/img/p*-prima.png` e `p*-dopo.png` |

## I 4 task

| | Percorso | Risposta attesa |
|---|---|---|
| T1 | Esplorare le campagne: trovare la raccolta aperta più lontana dall'obiettivo | «Aria aperta», € 2.350 su € 5.000 |
| T2 | Approfondire un progetto: uso dei fondi e che cosa succede se l'obiettivo non è raggiunto | Tabella «Come useremo i fondi»; donazione restituita («tutto o niente») |
| T3 | Donare € 30 al progetto sulle api con la ricompensa, in forma anonima, con Satispay | Pagina di conferma; totale € 30,89 |
| T4 | Proporre un'idea come associazione | Modulo di collaborazione inviato; risposta entro 10 giorni lavorativi |

## Il re-design in breve

| N. | Problema (versione provata) | Intervento | Prima → dopo |
|---|---|---|---|
| P1 | Su telefono il riepilogo della donazione esce dallo schermo | Layout | pagina larga 416 px su 375, 8 valori tagliati → 375 px, 0 |
| P2 | Il costo totale si scopre solo all'ultimo passo | Riquadro «La tua donazione» sempre visibile | totale leggibile dal passo 5 → dal passo 1 |
| P3 | La regola «tutto o niente» è nascosta dietro un pulsante | Frase visibile sotto «Sostieni il progetto» | 1 clic → 0 clic |
| P4 | Nelle schede la percentuale si legge a fatica | Percentuale accanto alla barra | 15 px grigio tra parentesi → 18 px grassetto |
| P5 | In «Progetti» i filtri occupano la prima schermata | Ricerca e ordinamento in vista, filtri compatti | prima scheda a 1047 px (telefono) e 758 px (computer) → 583 e 577 px |
| P6 | I moduli per chi propone non dicono a chi sono riservati | Avviso «Per chi è questo modulo», suggerimento in Contatti | rimando assente → presente nei 3 punti |
| P7 | Su telefono titolo e indicatore dei passi spingono giù il modulo | Indicatore su una riga, titolo breve | indicatore 136 px → 40 px |
| P8 | Errore generico per l'email mancante | Messaggio specifico | «Compila questo campo.» → «Scrivi la tua email.» |

Dopo le modifiche: 4 task ancora completabili, 0 violazioni axe-core su 50 pagine nei due temi, 105/105 percorsi, nessuno scorrimento orizzontale a 320–1280 px.

## Come procedere

1. **Prima delle sessioni.** Un componente esegue i 4 task cronometrandosi e scrive i secondi in `dati/task.csv` (`tempo_esperto_s`). Stampare il kit. Fare una sessione di prova tra di noi.
2. **Sessioni.** Gli utenti provano la **versione dell'Assignment 3**: <https://andreock.github.io/hci_gruppo_a/anteprime/assignment3/>. Quell'indirizzo cambia solo se si fa un push sul branch `assignment3`: non farlo finché le 8 sessioni non sono finite. Il push di `assignment4` pubblica il re-design a un indirizzo diverso (`…/anteprime/assignment4/`) e non tocca la versione provata. I turni facilitatore/osservatore proposti sono in `dati/partecipanti.csv` (2 sessioni condotte e 2 osservate a testa): cambiarli se diversi.
3. **Dopo ogni sessione.** Copiare la scheda dell'osservatore nei CSV (si aprono con Excel/Numbers/LibreOffice; salvare sempre come CSV UTF-8 con la virgola come separatore).
   - `sessioni.csv`: `esito` = `S`, `A` o `F`; `tempo_s` in secondi oppure `min:sec`; più frasi in `citazioni` separate da ` | `.
   - `sus.csv`: risposte da 1 a 5 così come sono sul foglio (il punteggio lo calcola lo script).
4. **Riunione di sintesi.** In `problemi.csv`:
   - per P1–P8 compilare `utenti` (per esempio `U1;U3;U6`) ed `evidenza` (che cosa hanno fatto e detto), poi **rivedere** `impatto_1_3`, `persistenza_1_3` e `gravita_0_4`: i valori presenti sono la nostra stima dall'ispezione;
   - aggiungere i problemi nuovi emersi dalle sessioni con `origine` = `test`; se li correggete, `stato` = `fatto` e le colonne del re-design, altrimenti il motivo in `soluzione`.
5. **Se il re-design cambia ancora.** Modificare il sito in `assignment2/website/` (testi in `i18n/`, dati in `data/`, poi `python3 tools/build.py` e le verifiche del suo README), quindi rilanciare `python3 relazione/tools/prima_dopo.py` per aggiornare misure e schermate.
6. **Relazione.** Completare i testi `todo` in `relazione/modello.html`, poi:

```bash
cd assignment4
python3 relazione/tools/genera.py        # stampa che cosa manca ancora ed eventuali errori nei dati
```

7. **Prototipo da consegnare:**

```bash
cd assignment2 && python3 website/tools/build.py && zip -r ../assignment4/assignment4_gruppoA.zip website -x "website/tools/node_modules/*" "*.DS_Store" "website/.idea/*"
```

Requisiti degli script: Python 3, Node.js con le dipendenze di `assignment2/website/tools` (`npm --prefix assignment2/website/tools ci`), Google Chrome, `pdfinfo` e `pdftotext` (poppler).
