---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P11
journey: J11
nome: Amir Haddad
descrizione: dottorando che cura la comunicazione della campagna
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P11, J11]
---

# P11 · J11 · Amir Haddad, dottorando che cura la comunicazione della campagna

Questo file contiene i due prompt della persona P11 e del suo journey J11. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P11**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J11**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P11 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J11; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P11" tipo="persona" persona="P11" richiede="C00" -->
````text
<prompt id="P11" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P11 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Amir Haddad
- Età: 27
- Città: Torino
- Origine e lingue: libanese, in Italia da cinque anni; arabo madrelingua, inglese C1, italiano B2
- Occupazione: dottorando in Informatica
- Famiglia: vive da solo; sente la famiglia in videochiamata ogni domenica
- Vita quotidiana: programma anche nel tempo libero, contribuisce a progetti open source, gioca a scacchi online, frequenta l'associazione degli studenti libanesi
- Valori: apertura, condivisione della conoscenza, comunità
- Ruolo: promotore; cura la comunicazione della campagna fittizia del suo gruppo («OpenAria», sensori open source per la qualità dell'aria)
- Dispositivo principale: laptop Linux con Firefox; smartphone Android
- Familiarità digitale: 5/5. Sviluppatore, usa molto la tastiera e le scorciatoie, ispeziona il codice delle pagine
- Accessibilità e contesto: lavora quasi solo da tastiera; scrive in italiano con qualche incertezza e preferisce scrivere in inglese
- Frequenza d'uso: quotidiana durante la campagna
- Motivazione: portare donatori anche dall'estero (colleghi internazionali, comunità libanese) e far sembrare la campagna professionale
- Archetipo: «il dottorando che fa da social media manager»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S32, S40, S36, S12] Strumenti che non gestiscono bene due lingue.
- [S41] Donatori stranieri bloccati da messaggi solo in italiano.
- [S74, S71] Link condivisi sui social che si aprono lenti o poco chiari su smartphone.
- [S67, S20] Interfacce scomode da usare con la tastiera.
- [S28, S33, S39] Piccoli difetti tecnici che fanno sembrare poco professionale la campagna.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- È un utente esperto: le sue difficoltà riguardano flessibilità ed efficienza d'uso e qualità tecnica, oltre alle lingue.
- Fa da ponte tra il gruppo di ricerca e i donatori: vede i problemi in prima persona e attraverso i messaggi che riceve.
- Distingui ciò che è previsto dal catalogo da ciò che riguarda l'area riservata dei promotori, da marcare [IPOTESI].
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P11" -->

<!-- BEGIN PROMPT id="J11" tipo="journey_map" persona="P11" richiede="C00" -->
````text
<prompt id="J11" tipo="journey_map" persona="P11" richiede="C00">

<obiettivo>
Genera la scheda user journey J11 della persona P11 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P11 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Amir Haddad, 27 anni, dottorando in Informatica a Torino, libanese, in Italia da cinque anni (italiano B2, inglese C1). Laptop Linux con Firefox, smartphone Android. Familiarità 5/5, lavora da tastiera. Cura la comunicazione della campagna fittizia «OpenAria». Uso quotidiano. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una settimana tipo durante la campagna «OpenAria». Amir prepara un aggiornamento in due lingue, lo pubblica, lancia una promozione sui social rivolta anche a colleghi all'estero, risponde ai donatori bloccati e il venerdì presenta un breve report al gruppo. Obiettivo: aumentare i donatori dall'estero e ridurre le richieste di aiuto.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Preparazione dei contenuti in due lingue. Problemi: S40, S36, S12.
2. Pubblicazione di un aggiornamento. Canale: area riservata [IPOTESI]. Problema: S32 (la versione inglese è parziale).
3. Promozione sui social. Canali: Instagram, LinkedIn, WhatsApp, app da smartphone. Problemi: S74, S71. Positivi: S27, S70.
4. Assistenza ai donatori stranieri. Canali: email, WhatsApp. Problemi: S41, S32.
5. Verifica dell'esperienza da tastiera e da smartphone. Problemi: S67, S20, S33, S39, S28.
6. Report settimanale al gruppo. Canale: riunione o documento condiviso.
</fasi>

<indicazioni_specifiche>
- In «Momenti critici» usa gli indicatori HEART come li userebbe Amir nel report (Adoption dei donatori stranieri, Task success del modulo), con metriche osservabili e senza valori inventati.
- Momento critico: fase 4, donatori stranieri bloccati da messaggi solo in italiano.
- La curva emotiva alterna frustrazione tecnica e soddisfazione per la risposta della comunità.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J11" -->
