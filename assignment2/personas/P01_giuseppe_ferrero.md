---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P01
journey: J01
nome: Giuseppe Ferrero
descrizione: pensionato alla prima donazione online
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P01, J01]
---

# P01 · J01 · Giuseppe Ferrero, pensionato alla prima donazione online

Questo file contiene i due prompt della persona P01 e del suo journey J01. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P01**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J01**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P01 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J01; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P01" tipo="persona" persona="P01" richiede="C00" -->
````text
<prompt id="P01" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P01 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Giuseppe Ferrero
- Età: 71
- Città: Moncalieri, nella prima cintura di Torino
- Occupazione: insegnante di scienze alle scuole medie, in pensione
- Famiglia: vedovo; una figlia e due nipoti, la più piccola nata prematura due anni fa
- Vita quotidiana: orto, bocciofila, volontariato in parrocchia, legge il quotidiano locale cartaceo ogni mattina
- Valori: generosità concreta, fiducia nella scienza, prudenza con i soldi
- Ruolo: donatore alla prima esperienza di crowdfunding
- Dispositivo principale: tablet Android da 10 pollici regalato dal nipote, con carattere ingrandito; in casa non c'è un computer
- Familiarità digitale: 2/5. Usa WhatsApp, email, meteo e il giornale online; ha pagato online solo con l'aiuto della figlia; diffida dei siti che non conosce
- Accessibilità: presbiopia (occhiali da lettura), si affatica con testi piccoli e poco contrastati; tocchi imprecisi sui bersagli piccoli
- Frequenza d'uso: prima volta; al massimo una o due donazioni l'anno
- Motivazione: ha letto sul giornale di un progetto di ricerca universitaria per proteggere i neonati dai virus e, pensando alla nipote, vuole donare 50 €
- Archetipo: «il nonno generoso ma prudente»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S59] Non capisce subito «che cosa sia» il sito su cui è arrivato.
- [S23, S54] Testi piccoli e poco contrastati che lo costringono a ingrandire.
- [S12] Parole inglesi del crowdfunding che non conosce.
- [S10, S11] Numeri e percentuali che non sa interpretare (oltre il 100%, giorni con il segno meno).
- [S41] Paura di sbagliare quando paga online e l'errore arriva solo alla fine.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Il suo modello mentale della donazione è l'offerta o il bonifico: si aspetta di dare una somma, non di scegliere una «ricompensa».
- Mostra le sue strategie: chiede conferma alla figlia per telefono, fotografa lo schermo, preferisce chiamare un numero di assistenza. Non descriverlo come incapace: è un ex insegnante curioso e attento.
- La frase rappresentativa deve esprimere insieme generosità e prudenza.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P01" -->

<!-- BEGIN PROMPT id="J01" tipo="journey_map" persona="P01" richiede="C00" -->
````text
<prompt id="J01" tipo="journey_map" persona="P01" richiede="C00">

<obiettivo>
Genera la scheda user journey J01 della persona P01 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P01 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Giuseppe Ferrero, 71 anni, insegnante di scienze in pensione, vedovo, nonno di una bambina nata prematura. Tablet Android con carattere ingrandito, nessun computer. Familiarità digitale 2/5. Presbiopia e tocchi imprecisi. Prudente, preferisce telefonare e chiede conferma alla figlia. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Domenica mattina, a casa. Giuseppe ha letto sul giornale di un progetto di ricerca universitaria per proteggere i neonati dai virus, finanziato con il crowdfunding. Sul tablet cerca il progetto con il motore di ricerca. Obiettivo: donare 50 € ed essere sicuro che i soldi arrivino davvero alla ricerca.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta: articolo sul giornale e ricerca online. Canali: giornale cartaceo, motore di ricerca. Problema facoltativo: S60.
2. Orientamento sulla homepage dell'app. Canale: sito da tablet. Problemi: S59, S23.
3. Capire come funziona la donazione (pagina «Come funziona»). Problemi: S54, S52, S12. Positivo: S44 (trova un numero di telefono).
4. Valutare il progetto: elenco dei progetti e pagina del progetto. Problemi: S10, S11, S14. Positivo: S27.
5. Donare: scelta dell'importo e modulo di donazione. Problema: S41.
6. Dopo la donazione: telefona alla figlia o all'assistenza per avere conferma; attende un'email [IPOTESI]. Canali: telefono, email.
</fasi>

<indicazioni_specifiche>
- Andamento emotivo atteso: motivazione alta all'inizio, calo nelle fasi 3–4, minimo nella fase 5, recupero nella fase 6 grazie al contatto umano.
- Nella fase 4 mostra il golfo della valutazione: Giuseppe interpreta male lo stato della campagna e rischia di rinunciare per un motivo sbagliato.
- Nella fase 5 evidenzia che dover scegliere una «ricompensa» non corrisponde al suo modello mentale.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J01" -->
