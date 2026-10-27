---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P12
journey: J12
nome: Maria Lombardi
descrizione: presidente di un'associazione che lancia la prima campagna
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P12, J12]
---

# P12 · J12 · Maria Lombardi, presidente di un'associazione che lancia la prima campagna

Questo file contiene i due prompt della persona P12 e del suo journey J12. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P12**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J12**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P12 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J12; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P12" tipo="persona" persona="P12" richiede="C00" -->
````text
<prompt id="P12" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P12 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Maria Lombardi
- Età: 49
- Città: Forlì
- Occupazione: impiegata part-time in un'agenzia assicurativa; presidente volontaria di un'associazione che gestisce un doposcuola
- Famiglia: sposata, due figli (il maggiore ha 16 anni e la aiuta con il telefono)
- Vita quotidiana: organizza turni di volontari, cene di raccolta fondi e lotterie in parrocchia; coro il mercoledì; usa molto WhatsApp e Facebook per l'associazione
- Valori: comunità, attenzione ai ragazzi, concretezza
- Ruolo: promotrice; vuole lanciare la prima campagna online dell'associazione
- Dispositivo principale: smartphone Android; vecchio PC Windows dell'associazione con schermo piccolo
- Familiarità digitale: 2/5. WhatsApp, Facebook, email; i moduli online la mettono in ansia
- Accessibilità: tremore essenziale lieve alle mani: fatica con bersagli piccoli, menu a tendina e gesti precisi
- Frequenza d'uso: prima volta; se lancia la campagna, uso intensivo per circa due mesi
- Motivazione: raccogliere 5.000 € per rinnovare l'aula del doposcuola (arredi e computer); una volontaria le ha parlato del crowdfunding
- Archetipo: «la volontaria che si lancia nel crowdfunding»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S59, S61] Non capire subito che cos'è il servizio e chi c'è dietro.
- [S49, S54] Costi scoperti tardi e scritti in piccolo.
- [S46, S53, S48] Parole tecniche e FAQ infinite.
- [S67, S19] Menu e icone troppo piccoli da toccare con precisione.
- [S51, S50, S45, S55] Moduli che la confondono e le fanno credere di sbagliare.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Il tremore riguarda la precisione motoria: collega le difficoltà ai bersagli piccoli e ai gesti precisi (legge di Fitts come concetto, senza calcoli).
- Sa organizzare persone e raccogliere fondi offline; la difficoltà è tradurre questa competenza nel linguaggio delle app.
- Mostra che i servizi pensati per i promotori, che in homepage ostacolano i donatori (S62), per lei sono utili.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P12" -->

<!-- BEGIN PROMPT id="J12" tipo="journey_map" persona="P12" richiede="C00" -->
````text
<prompt id="J12" tipo="journey_map" persona="P12" richiede="C00">

<obiettivo>
Genera la scheda user journey J12 della persona P12 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P12 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Maria Lombardi, 49 anni, Forlì. Impiegata part-time e presidente volontaria di un'associazione che gestisce un doposcuola. Smartphone Android e vecchio PC dell'associazione. Familiarità 2/5, i moduli online la mettono in ansia. Tremore lieve alle mani. Vuole lanciare una campagna da 5.000 €. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Dopo una riunione dell'associazione, una volontaria le parla di un'app di crowdfunding. Maria la apre sullo smartphone la sera stessa e prosegue nei giorni successivi dal PC dell'associazione. Obiettivo: capire se il servizio fa al caso loro, quanto costa, registrarsi e parlare con qualcuno prima di decidere.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta tramite passaparola e primo accesso. Canali: passaparola, app da smartphone. Problemi: S59, S62. Positivo: S58.
2. Capire chi gestisce il servizio e se è affidabile. Canali: smartphone e PC. Problemi: S61, S67, S19, S63.
3. Capire costi e regole. Canale: sito da PC. Problemi: S54, S49, S46, S53, S48, S47.
4. Registrazione da smartphone. Problemi: S51, S50, S45, S55.
5. Primo contatto con la piattaforma. Canali: telefono, videochiamata. Positivo: S44. Problema: S46 («call di consulenza»). Esito [IPOTESI].
6. Decisione di lanciare la campagna. Canali: riunione dell'associazione, email. [IPOTESI].
</fasi>

<indicazioni_specifiche>
- Mostra il passaggio tra smartphone e PC e i punti in cui manca continuità.
- Momenti critici: fase 3, la scoperta tardiva della quota (HEART Adoption dei promotori); fase 4, ansia nel modulo.
- La curva emotiva risale nella fase 5 grazie al contatto umano: il canale telefonico recupera l'esperienza.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J12" -->
