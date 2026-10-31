# 09 · Valutazione euristica di ideaBlume

Valutazione rapida del nuovo sito con le 10 euristiche di Nielsen e la **stessa scala di gravità di assignment1** (`assignment1/assignment1_gruppoA.pdf`, slide 3): 0 nessun problema · 1 superficiale · 2 minore · 3 importante · 4 grave.

- **Data**: 31/10/2026. **Dispositivi**: Chrome 156 a 1280 × 900 e 375 × 780 (emulazione), zoom 200%, solo tastiera.
- **Task**: gli stessi T1–T8 di assignment1 (slide 5): capire il programma, trovare e scegliere un progetto, capire obiettivi e uso dei fondi, capire lo stato, donare, chiarire dubbi, candidare un progetto, recuperare da un indirizzo errato.
- **Limite**: chi valuta ha anche progettato il sito. Una valutazione indipendente, fatta da un altro gruppo o da chi non ha partecipato alla progettazione, sarebbe più affidabile.

## 1. Problemi trovati

| ID | Euristica | Problema | Dove | Gravità | Esito |
|---|---|---|---|---|---|
| V-01 | H9 · Riconoscere e correggere gli errori | La ricerca confrontava l'inizio esatto delle parole: «veterinaria» non trovava «Scienze Veterinarie» e mostrava «nessun risultato» | `cerca.html` | 2 | **Corretto**: tollera singolare/plurale e maschile/femminile (`percorsi.md`, controllo «veterinaria») |
| V-02 | H10 · Aiuto e documentazione | Il riquadro «Obiettivo e raddoppio» della pagina progetto non portava alle regole complete del raddoppio | `progetto-*.html` | 2 | **Corretto**: link «Come funziona il raddoppio» → `programma.html#raddoppio` |
| V-03 | H3 · Controllo e libertà | Chi inizia la donazione sullo smartphone non può riprenderla sul laptop con i dati già inseriti (J02-F6): la bozza resta nella scheda del browser | `donazione.html` | 2 | **Aperto**: richiede account o un link con i dati, esclusi dal prototipo (D-17). Mitigazione: si può copiare il link della pagina e i dati sono pochi |
| V-04 | H8 · Design estetico e minimalista | A 375 px intestazione, selettore di lingua, menu e ricerca occupano circa 215 px prima del contenuto | tutte, su mobile | 1 | **Aperto**: scelta consapevole (ricerca sempre visibile, P-005). Possibile miglioramento: ricerca a scomparsa con un pulsante «Cerca» etichettato |
| V-05 | H4 · Coerenza e standard | Le card dicono «Anno 2026», la pagina del programma «Edizione 2026» | card, `programma.html` | 1 | **Aperto**: due concetti vicini ma diversi (i progetti fuori dal programma non hanno un'edizione); il glossario li spiega insieme («Anno (edizione)») |
| V-06 | H8 · Design estetico e minimalista | I segnaposto «[DA VERIFICARE con l'Ateneo]» sono molti (41 contesti) e appesantiscono la lettura | regole, FAQ, donazione | 1 | **Aperto per scelta**: richiesti dal prompt per non presentare come vere informazioni non documentate; spariscono quando il gruppo inserisce i dati veri |
| V-07 | H7 · Flessibilità ed efficienza | Non c'è un confronto affiancato tra progetti né un'esportazione dei dati (utile a P05 e P08) | `progetti.html` | 1 | **Aperto**: i filtri e l'ordinamento «Più lontani dall'obiettivo» coprono il bisogno principale |
| V-08 | H5 · Prevenzione degli errori | L'importo della donazione non ha un massimo né una richiesta di conferma per cifre molto alte (es. 10.000 € digitato al posto di 100) | `donazione.html` | 1 | **Aperto**: il riepilogo prima della conferma mostra l'importo in grande; un avviso sopra una soglia è un possibile miglioramento |
| V-09 | H2 · Corrispondenza con il mondo reale | I commenti dei sostenitori non sono tradotti | pagine progetto | 1 | **Aperto per scelta** (D-28): dichiarato e marcato con la lingua |
| V-10 | H1 · Visibilità dello stato | Senza server la 404 non compare per gli indirizzi sbagliati: dipende dall'hosting | `404.html` | 0–1 | Non applicabile da `file://`; su GitHub Pages è servita a qualunque profondità (D-21), da provare dopo la pubblicazione |

**Nessun problema di gravità 3 o 4.** I due problemi di gravità 2 correggibili nel prototipo (V-01, V-02) sono stati corretti; V-03 resta aperto per un limite di ambito dichiarato.

## 2. Euristiche: che cosa funziona

| Euristica | Valutazione | Evidenze principali |
|---|---|---|
| H1 Visibilità dello stato | Buona | Stato delle campagne in testo con data; passo corrente della donazione; conteggi annunciati; indicatori di invio; voce di menu corrente |
| H2 Corrispondenza con il mondo reale | Buona | Lessico controllato senza gergo («donazione libera», «tutto o niente», «raddoppio dell'Ateneo»); glossario; date e importi nel formato della lingua |
| H3 Controllo e libertà | Buona, con V-03 | Indietro del browser funziona anche nella donazione; dati conservati; «Modifica» nel riepilogo; filtri azzerabili; menu e spiegazioni chiudibili con Esc |
| H4 Coerenza e standard | Buona, con V-05 | Stessa struttura in tutti i progetti (verificata da script); componenti nativi (caselle, radio, `details`); un solo nome del marchio |
| H5 Prevenzione degli errori | Buona, con V-08 | Minimo scritto accanto al campo; `type` e `autocomplete`; nessuna preselezione nascosta; campagne concluse senza controlli attivi |
| H6 Riconoscimento anziché ricordo | Buona | Tema, gruppo, dipartimento e stato sulle card; riepilogo sempre visibile nella donazione; raddoppio spiegato dove si dona |
| H7 Flessibilità ed efficienza | Buona, con V-07 | Ricerca, filtri e ordinamento condivisibili; indice e ancore; «Torna su»; link alle singole risposte delle FAQ |
| H8 Design estetico e minimalista | Buona, con V-04 e V-06 | Una lingua per volta; ricompense compatte; nessun carosello; contrasti alti |
| H9 Riconoscere e correggere gli errori | Buona | Errori vicino al campo, con la correzione da fare, nella lingua della pagina, che spariscono appena il valore è corretto; ricerca e filtri vuoti con alternative; 404 nel modello del sito |
| H10 Aiuto e documentazione | Buona | FAQ per destinatario con ricerca; «Come funziona» per passi con link; blocco «Aiuto» nella stessa posizione in ogni pagina |

## 3. Confronto con la valutazione di assignment1

| | IdeaGinger (assignment1) | ideaBlume |
|---|---|---|
| Problemi di gravità 4 | 9 | 0 |
| Problemi di gravità 3 | 30 | 0 |
| Problemi di gravità 2 | 33 | 3 trovati, 2 corretti |
| Problemi di gravità 1 | 15 | 6 (3 per scelta dichiarata) |
| Lighthouse mobile, prestazioni (progetto / donazione) | 41 / 39 | 100 / 100 |
| Lighthouse mobile, accessibilità | 64–77 | 100 |

Il confronto non è simmetrico: IdeaGinger è un servizio reale con molte più funzioni e contenuti, ideaBlume è un prototipo valutato da chi lo ha progettato. Il dato utile è che **84 dei 90 problemi consolidati risultano risolti con una verifica, 3 parziali e 3 non applicabili**, e che la valutazione del nuovo sito non trova problemi di gravità 3 o 4. I 3 parziali (date del bando, ricevuta e detraibilità, tempi della formazione) dipendono da informazioni che le fonti non contengono (vedi `05_tracciabilita.md` §4).

## 4. Prossimi passi consigliati

1. **Test di usabilità con utenti reali**, almeno 5 persone simili alle personas: una persona anziana alla prima donazione (P01), una persona che usa NVDA (P03), una persona con italiano A2 (P04), una ricercatrice (P09). Task: trovare un progetto, donare, capire che cosa succede se l'obiettivo non viene raggiunto, candidarsi. Metriche HEART già proposte nei journey (task success, tempo, errori).
2. **Valutazione euristica indipendente** fatta da un altro gruppo.
3. **Sostituire i segnaposto** con le informazioni vere dell'Ateneo (`docs/verifiche/segnaposto.md`).
