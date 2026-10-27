---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P07
journey: J07
nome: Giulia Esposito
descrizione: studentessa con dislessia che dona poco e condivide molto
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P07, J07]
---

# P07 · J07 · Giulia Esposito, studentessa con dislessia che dona poco e condivide molto

Questo file contiene i due prompt della persona P07 e del suo journey J07. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P07**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J07**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P07 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J07; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P07" tipo="persona" persona="P07" richiede="C00" -->
````text
<prompt id="P07" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P07 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Giulia Esposito
- Età: 20
- Città: Torino, fuorisede (originaria di Salerno)
- Occupazione: studentessa al secondo anno di Biotecnologie
- Famiglia: vive in un appartamento condiviso con altre due studentesse; la famiglia le passa un budget mensile ridotto
- Vita quotidiana: lezioni e laboratorio, lavoretto da babysitter, pallavolo con la squadra universitaria, crea reel su Instagram per il suo gruppo di studio
- Valori: fiducia nella scienza, condivisione, attivismo «dal basso»
- Ruolo: donatrice alla prima esperienza, piccolo importo (5–10 €)
- Dispositivo principale: iPhone, usato quasi per tutto
- Familiarità digitale: 4/5 su social e app; 2/5 con testi lunghi e moduli complessi
- Accessibilità: dislessia (DSA certificata): fatica con testi lunghi e densi, caratteri piccoli e parole inglesi; usa la lettura vocale dello schermo di iOS e cerca riassunti, grassetti e immagini
- Frequenza d'uso: prima volta; potrebbe tornare se coinvolta da amici o dall'università
- Motivazione: vede una storia Instagram della sua università su un programma di crowdfunding per la ricerca e vuole sostenere un progetto vicino ai suoi studi, coinvolgendo il gruppo di studio
- Archetipo: «la studentessa che dona poco ma condivide molto»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S38, S52] Testi lunghi e senza titoli in cui perde il filo.
- [S12] Parole inglesi del crowdfunding che deve decifrare.
- [S59, S62, S64] Homepage che non dicono subito che cosa sono e titoli tagliati a metà.
- [S41, X05] Importi minimi scoperti solo dopo aver provato a pagare.
- [S71] Caroselli che non mostrano di poter scorrere.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Descrivi la dislessia in modo concreto (strategie, strumenti, che cosa la aiuta) e senza stereotipi: sui social è molto abile.
- Il suo valore come donatrice non è l'importo ma la rete che può coinvolgere (HEART Engagement).
- Collega le difficoltà sulla homepage alla piega della pagina e alla gerarchia visiva.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P07" -->

<!-- BEGIN PROMPT id="J07" tipo="journey_map" persona="P07" richiede="C00" -->
````text
<prompt id="J07" tipo="journey_map" persona="P07" richiede="C00">

<obiettivo>
Genera la scheda user journey J07 della persona P07 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P07 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Giulia Esposito, 20 anni, studentessa fuorisede di Biotecnologie a Torino. iPhone, Instagram, WhatsApp. Familiarità 4/5 sulle app, 2/5 con testi lunghi. Dislessia (DSA): usa la lettura vocale di iOS. Budget 5–10 €. Prima volta. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Martedì pomeriggio, sul tram verso l'università. Giulia vede una storia Instagram della sua università su un programma di crowdfunding per la ricerca e cerca l'app con il nome indicato nella storia: arriva sulla homepage. Obiettivo: trovare un progetto vicino ai suoi studi, donare un piccolo importo e farlo conoscere al gruppo di studio.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta su Instagram. Canale: Instagram.
2. Prima impressione sulla homepage. Canale: browser su iPhone. Problemi: S59, S62, S64.
3. Ricerca dei progetti del programma. Problemi: S63, S71, S12.
4. Lettura del progetto e delle regole. Problemi: S38, S52. Positivi: S27 (grassetti e infografiche), S70.
5. Donazione di un piccolo importo: prova con 5 € su un progetto con minimo 10 €. Problemi: S41, X05.
6. Condivisione con il gruppo di studio. Canale: WhatsApp. Positivo: S27 («Copia link»).
</fasi>

<indicazioni_specifiche>
- Indica dove usa la lettura vocale e dove la struttura della pagina la aiuta o la ostacola.
- Momenti critici: fase 5 (errore sul minimo che arriva tardi, HEART Task success) e fase 2 (non capire di essere nel posto giusto, HEART Adoption).
- La curva emotiva termina in positivo grazie alla condivisione.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J07" -->
