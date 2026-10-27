---
documento: persona_journey_prompts
versione: 3 (personas generiche)
persona: P02
journey: J02
nome: Sara Colombo
descrizione: infermiera che dona dallo smartphone in pausa
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P02, J02]
---

# P02 · J02 · Sara Colombo, infermiera che dona dallo smartphone in pausa

Questo file contiene i due prompt della persona P02 e del suo journey J02. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5, incolla il prompt **C00** dal file del contesto comune e allega il template del corso: [scheda_persona.pdf](template/scheda_persona.pdf) per la persona, [scheda_user_journey.pdf](template/scheda_user_journey.pdf) per il journey.
2. Per la persona incolla il prompt **P02**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J02**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P02 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J02; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P02" tipo="persona" persona="P02" richiede="C00" -->
````text
<prompt id="P02" tipo="persona" richiede="C00">

<obiettivo>
Genera la scheda della persona P02 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Sara Colombo
- Età: 34
- Città: Torino
- Occupazione: infermiera turnista in pronto soccorso
- Famiglia: convive con il compagno, nessun figlio, un gatto
- Vita quotidiana: turni di notte, corsa al parco quando riesce, serie TV, segue molti profili di divulgazione su Instagram
- Valori: solidarietà pratica, attenzione all'ambiente
- Ruolo: donatrice occasionale (ha già fatto due donazioni a raccolte fondi online)
- Dispositivo principale: smartphone Android di fascia media di quattro anni, memoria quasi piena, connessione 4G spesso debole; la sera il laptop di casa
- Familiarità digitale: 3/5. Social, home banking, app di consegne e dei turni; non legge le istruzioni, procede per tentativi
- Accessibilità e contesto: limitazioni situazionali: pause di 10 minuti, spesso una mano sola, attenzione divisa, stanchezza dopo il turno di notte
- Frequenza d'uso: occasionale; visite brevi (2–5 minuti) da link condivisi sui social
- Motivazione: un'amica dottoranda condivide nelle storie di Instagram un progetto di ricerca sul clima; Sara vuole donare 20 € prima che finisca la pausa
- Archetipo: «la donatrice d'impulso in pausa»
</scheda_vincolante>

<frustrazioni_da_far_emergere>
Frustrazioni con le app di crowdfunding da trasformare in 3–5 punti personali di «Difficoltà e frustrazioni», senza dettagli tecnici dell'interfaccia (le chiavi tra parentesi quadre rimandano al catalogo di C00 e non vanno riportate):
- [S74] App e siti lenti quando la rete è debole.
- [S38, S31] Pagine e liste lunghissime da scorrere con il pollice.
- [X05] Non capisce se può donare una cifra libera senza scegliere una ricompensa.
- [S41] Errori che compaiono solo alla fine, quando il tempo è già finito.
- [S28] Pulsanti che sembrano non rispondere.
</frustrazioni_da_far_emergere>

<indicazioni_specifiche>
- Le sue difficoltà dipendono dal contesto d'uso (tempo, rete, una mano) più che da limiti personali: è un esempio di disabilità situazionale.
- Mostra l'attenzione divisa: il telefono deve competere con colleghi, chiamate e la fine della pausa.
- Le sue aspettative sono modellate dalle app che usa ogni giorno (pagamento in pochi tocchi).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) campi, etichette e ordine identici a <formato_persona>; (3) dati della scheda vincolante rispettati; (4) il profilo descrive la vita della persona, non un'interfaccia.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P02" -->

<!-- BEGIN PROMPT id="J02" tipo="journey_map" persona="P02" richiede="C00" -->
````text
<prompt id="J02" tipo="journey_map" persona="P02" richiede="C00">

<obiettivo>
Genera la scheda user journey J02 della persona P02 usando il formato <formato_journey> e le regole del contesto C00. Il percorso si svolge in una generica app di crowdfunding, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<persona_generata>
[Se la persona P02 è già stata generata, sostituisci questa riga con la sua scheda completa. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Sara Colombo, 34 anni, infermiera turnista in pronto soccorso. Donatrice occasionale. Smartphone Android di fascia media con 4G spesso debole; la sera il laptop di casa. Familiarità digitale 3/5, procede per tentativi. Pause di 10 minuti, una mano sola, attenzione divisa. Se la scheda in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Pausa di metà turno, in sala relax. Sara vede nelle storie di Instagram di un'amica il link a un progetto di ricerca sul clima su un'app di crowdfunding. Vuole donare 20 € prima che la pausa finisca. Il percorso si interrompe e riprende la sera, a casa. Obiettivo: completare la donazione con il minimo sforzo, anche passando da un dispositivo all'altro.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta sui social: storia Instagram con link. Canale: Instagram.
2. Primo caricamento da smartphone. Canale: app o sito da smartphone. Problema: S74.
3. Valutazione rapida del progetto. Problemi: S38, S28. Positivo: S70.
4. Scelta della ricompensa. Problemi: S31, X05.
5. Tentativo di donazione e interruzione: il modulo è lento, compare un errore dopo l'invio, la pausa finisce. Problemi: S41, S74. Positivo: S27 (si manda il link su WhatsApp con «Copia link»).
6. Ripresa la sera e conclusione: riapre il link sul laptop, guarda anche altri progetti e completa la donazione. Canali: WhatsApp, sito da laptop, email. Problemi: S11, S71 (ricordo di quanto visto sullo smartphone).
</fasi>

<indicazioni_specifiche>
- Journey multicanale: in «Fonti e ipotesi» evidenzia la mancanza di continuità tra smartphone e laptop (dati del modulo da reinserire) e marcala [IPOTESI].
- Momento critico principale: fase 5, abbandono per lentezza e interruzione (HEART Task success e Adoption).
- La curva emotiva parte positiva, scende fino al minimo nella fase 5 e risale nella fase 6.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) nessun nome di app, piattaforma, ente, università o progetto reale e nessuna chiave Sxx o Xxx nel testo; (2) tutti i problemi indicati nelle fasi emergono come criticità vissute; (3) le colonne coincidono con le fasi del front matter; (4) ogni cella di «Emozioni e loro base» ha emozione, punteggio e base; (5) ogni criticità ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J02" -->
