# Da fare prima della consegna

La pipeline dell'Assignment 4 è completa e collaudata con dati sintetici. Questa checklist riguarda le attività che richiedono persone reali o una decisione finale del gruppo. Lo ZIP non è incluso perché verrà preparato separatamente.

## 1. Preparazione del test reale

- Un componente ripete i quattro task con il cronometro. Se i tempi differiscono sensibilmente da 60, 80, 140 e 120 secondi, aggiorna `dati/task.csv` e controlla che i limiti restino motivati.
- Il gruppo svolge almeno una sessione pilota interna usando il kit completo.
- Si confermano turni, luoghi, strumenti di registrazione e disponibilità degli otto partecipanti.
- La versione `assignment3` resta invariata fino alla fine di tutte le sessioni.

## 2. Sessioni con partecipanti reali

- Raccogliere il consenso prima di avviare qualsiasi registrazione.
- Usare solo le etichette U1–U8 nei dati e nella relazione.
- Applicare le stesse definizioni di errore, aiuto, blocco ed esito presenti nel kit.
- Dopo ogni sessione, facilitatore e osservatore ricontrollano insieme scheda e registrazione.

## 3. Sostituzione del dataset sintetico

- Sostituire tutti i profili in `dati/partecipanti.csv`.
- Sostituire tutte le 32 righe di `dati/sessioni.csv`.
- Sostituire le 80 risposte di `dati/sus.csv`.
- Sostituire tutte le risposte in `dati/intervista.csv`.
- Non conservare citazioni simulate, anche se sembrano plausibili.

## 4. Riunione di sintesi e re-design finale

- Per P1–P7 riscrivere `utenti` ed `evidenza` in `dati/problemi.csv` usando soltanto ciò che è accaduto davvero.
- Rivedere impatto, persistenza e gravità; abbassare la gravità dei problemi non incontrati.
- Aggiungere eventuali problemi nuovi con `origine=test`.
- Se emerge un problema nuovo rilevante, implementare la correzione nel prototipo e documentare file modificati, soluzione e misura prima/dopo.
- Valutare un secondo giro rapido sul re-design con tre persone nuove.

## 5. Chiusura della relazione

- In `relazione/modello.html` rimuovere l'avviso «Dataset sintetico di collaudo» e sostituire tutti i paragrafi che descrivono risultati simulati.
- Cercare nel modello e nei CSV le parole `sintetico`, `simulato` e `prova generale`: nella versione finale devono restare solo se servono a dichiarare l'uso dell'IA, non per descrivere i risultati.
- Inserire data effettiva, contesto reale, modalità di reclutamento, strumenti e limiti realmente incontrati.
- Rigenerare la relazione con `python3 relazione/tools/genera.py`.
- Il comando deve terminare con `0 valori nei CSV, 0 testi nel modello`.
- Renderizzare il PDF e controllare copertina, indice, tabelle 3–15, grafici, citazioni, confronti prima/dopo e numerazione delle pagine.
- Consegnare soltanto `relazione/assignment4_gruppoA.pdf`; il vecchio `relazione/relazione.pdf` non è il documento finale.

## 6. Presentazione

- Preparare i transcript del video usando i dati reali e la versione definitiva del re-design.
- Nel video distinguere chiaramente problemi emersi dai test, problemi trovati con l'ispezione e modifiche effettivamente implementate.
