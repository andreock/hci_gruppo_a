---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P06
journey: J06
nome: Elena Conti
descrizione: commercialista attenta a fiducia e privacy
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P06, J06]
---

# P06 · J06 · Elena Conti, commercialista attenta a fiducia e privacy

Questo file contiene i due prompt della persona P06 e del suo journey J06. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P06**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J06**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P06 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J06; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P06" tipo="persona" persona="P06" richiede="C00" -->
````text
<prompt id="P06" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P06 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Elena Conti
- Età: 58
- Città: Torino, zona Crocetta
- Occupazione: commercialista con studio proprio
- Famiglia: divorziata, una figlia medico specializzando
- Vita quotidiana: lunghe giornate di lavoro, corso di yoga il giovedì, abbonata alla stagione del teatro, fa volontariato contabile per una piccola onlus
- Valori: rigore, trasparenza, riservatezza
- Ruolo: donatrice attenta a fiducia e privacy; prima volta con il crowdfunding
- Dispositivo principale: PC desktop con due monitor; smartphone solo per email e telefonate
- Familiarità digitale: 4/5. Software gestionali, portali fiscali, PEC; legge con attenzione condizioni e note
- Accessibilità: nessuna esigenza specifica; occhiali progressivi
- Frequenza d'uso: dona una volta l'anno, a dicembre, a enti di ricerca; visita lunga e accurata
- Motivazione: vuole destinare 300 € alla ricerca dell'università in cui si è laureata, che ha un programma su un'app di crowdfunding, ma solo se tutto è affidabile, trasparente, rispettoso della privacy e se ottiene una ricevuta
- Archetipo: «la donatrice che legge le condizioni»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S61, S09, X06] Servizi di cui non si capisce chi c'è dietro, con date mancanti e numeri che non tornano.
- [S48, S47, S53, X02] Regole e costi sparsi, con nomi diversi per la stessa cosa.
- [S42, X03] Dati personali resi pubblici o condivisi senza che sia chiaro.
- [X04] Nessuna indicazione su ricevute e detraibilità.
- [S13, S25] Non sapere chi contattare né chi c'è dietro un progetto.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- La sua prospettiva è la fiducia: ogni incoerenza (date, numeri, nomi) riduce la credibilità percepita.
- Legge davvero condizioni e FAQ: il problema non è la mancanza di informazioni ma la loro posizione e coerenza.
- La privacy è una priorità: collega anonimato e condivisione dei dati al senso di controllo dell'utente (regole di Shneiderman).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P06" -->

<!-- BEGIN PROMPT id="J06" tipo="journey_map" persona="P06" richiede="C00" -->
````text
<prompt id="J06" tipo="journey_map" persona="P06" richiede="C00">

<obiettivo>
Genera la scheda user journey J06 della persona P06 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P06 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Elena Conti, 58 anni, Torino. Commercialista. PC desktop con due monitor. Familiarità digitale 4/5, legge condizioni e note. Nessuna esigenza di accessibilità specifica. Dona una volta l'anno a enti di ricerca; prima volta con il crowdfunding. Priorità: affidabilità, trasparenza, privacy, ricevuta. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Metà dicembre, nello studio, a fine giornata. Elena ha saputo da un'ex compagna di università che la loro università raccoglie fondi per la ricerca su un'app di crowdfunding. Vuole destinare 300 € prima della fine dell'anno. Obiettivo: verificare che app e programma siano affidabili, capire le regole economiche, donare restando anonima e ottenere una ricevuta.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Verifica dell'affidabilità dell'app. Canale: sito da desktop. Problema: S61.
2. Verifica del programma dell'università. Canali: sito da desktop, sito dell'università. Problemi: S09, X06, S13, S25.
3. Comprensione delle regole economiche. Problemi: S53, S48, S47, X02.
4. Scelta del progetto e dell'importo. Positivo: S27.
5. Donazione e privacy. Problemi: S41 (regola «tutto o niente» non ricordata nel modulo), S42, X03.
6. Ricevuta e documentazione fiscale. Canali: email, telefono. Problema: X04. Positivo: S44 (telefona all'assistenza; esito [IPOTESI]).
</fasi>

<indicazioni_specifiche>
- La curva emotiva misura soprattutto la fiducia (es. «Sospetto (−1)», «Rassicurazione (+1)»).
- Momento critico: fase 2, dove date e numeri incoerenti mettono in dubbio l'intero programma (HEART Adoption).
- In «Continuità tra touchpoint» evidenzia i salti tra app, sito dell'università, FAQ e assistenza telefonica.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J06" -->
