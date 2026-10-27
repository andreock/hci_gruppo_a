---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P05
journey: J05
nome: Luca Moretti
descrizione: artigiano daltonico che confronta prima di donare
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P05, J05]
---

# P05 · J05 · Luca Moretti, artigiano daltonico che confronta prima di donare

Questo file contiene i due prompt della persona P05 e del suo journey J05. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P05**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J05**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P05 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J05; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P05" tipo="persona" persona="P05" richiede="C00" -->
````text
<prompt id="P05" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P05 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Luca Moretti
- Età: 52
- Città: Asti
- Occupazione: elettricista, titolare di una piccola impresa con due dipendenti
- Famiglia: sposato, due figli adolescenti; il maggiore studia all'università
- Vita quotidiana: lavora molto, la domenica va in mountain bike, è nel direttivo della pro loco del paese, tiene i conti di casa su un foglio di calcolo
- Valori: concretezza, aiutare chi è più indietro, sostenere il territorio
- Ruolo: donatore abituale e metodico
- Dispositivo principale: PC desktop in ufficio con monitor da 24 pollici; smartphone per controlli veloci
- Familiarità digitale: 3/5. Fatturazione elettronica, home banking, acquisti online; lento ma meticoloso; prende appunti su carta
- Accessibilità: daltonismo (deuteranopia): distingue con difficoltà verde, rosso e arancione
- Frequenza d'uso: ricorrente; 2–3 donazioni l'anno su app di crowdfunding; visite lunghe di confronto (30–40 minuti) e controlli periodici
- Motivazione: vuole dare 100 € al progetto di ricerca «che ne ha più bisogno», possibilmente con ricadute sul suo territorio
- Archetipo: «il donatore che confronta prima di scegliere»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S16, S10, S29, S23] Informazioni affidate solo ai colori, che lui non distingue.
- [S21, S22, S24] Non poter ordinare o filtrare e dover caricare i progetti a gruppi.
- [S15] Perdere la posizione ogni volta che torna all'elenco.
- [S18] Dover aprire ogni progetto per capire di che cosa parla.
- [S11, X08] Cifre e scadenze ambigue che rendono difficile il confronto.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Mostra il suo metodo: confronta i progetti annotando cifre su carta o nel foglio di calcolo (carico sulla memoria, riconoscimento anziché ricordo).
- Il daltonismo è un tratto, non il centro della persona: emerge solo dove l'informazione è affidata al colore.
- Il suo criterio («chi ha più bisogno») si scontra con il modo in cui le app mostrano lo stato delle campagne.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P05" -->

<!-- BEGIN PROMPT id="J05" tipo="journey_map" persona="P05" richiede="C00" -->
````text
<prompt id="J05" tipo="journey_map" persona="P05" richiede="C00">

<obiettivo>
Genera la scheda user journey J05 della persona P05 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P05 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Luca Moretti, 52 anni, Asti. Elettricista titolare di una piccola impresa, figlio universitario. PC desktop in ufficio, smartphone per controlli. Familiarità digitale 3/5, meticoloso, prende appunti su carta. Daltonismo (deuteranopia). Donatore ricorrente. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Sabato mattina, in ufficio, a impresa chiusa. Luca ha deciso di dare 100 € a un progetto di ricerca di un'università che raccoglie fondi su un'app di crowdfunding. Vuole confrontare le campagne e scegliere quella che ne ha più bisogno; nelle settimane successive tornerà a controllare. Obiettivo: scegliere in modo informato e vedere che la sua donazione ha fatto la differenza.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Esplorazione dell'elenco dei progetti del programma. Canale: sito da desktop. Problemi: S16, S23. Positivo: S08.
2. Confronto tra i progetti. Problemi: S18, S21, S22, S24, S15.
3. Verifica dello stato e del bisogno. Problemi: S10, S11, S29, X08.
4. Decisione. Problema: S37 (non sa che vicino all'obiettivo la sua donazione verrebbe raddoppiata dal partner).
5. Donazione. Nessun problema assegnato: puoi usare «—».
6. Monitoraggio nelle settimane successive. Canali: smartphone, email [IPOTESI]. Problemi: S15, S11.
</fasi>

<indicazioni_specifiche>
- Mostra la ricerca esaustiva e il modello del berrypicking: la decisione si costruisce raccogliendo informazioni da più progetti.
- Momento critico: fase 3, quando il colore non basta a capire quali campagne hanno raggiunto l'obiettivo; collega il punto al principio di accessibilità per cui l'informazione non deve essere trasmessa solo dal colore.
- Indicatori HEART: Retention (tornerà a donare?) e Task success.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J05" -->
