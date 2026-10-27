---
documento: persona_journey_prompts
persona: P02
journey: J02
nome: Sara Colombo
descrizione: donatrice occasionale da smartphone
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P02, J02]
---

# P02 · J02 · Sara Colombo, donatrice occasionale da smartphone

Questo file contiene i due prompt della persona P02 e del suo journey J02. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P02**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J02**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P02 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J02; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P02" tipo="persona" persona="P02" richiede="C00" -->
````text
<prompt id="P02" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P02 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Sara Colombo
- Età: 34
- Città: Torino
- Occupazione: infermiera turnista in pronto soccorso
- Famiglia: convive con il compagno, nessun figlio
- Ruolo: donatrice occasionale (ha già fatto due donazioni su altre piattaforme di raccolta fondi)
- Dispositivo principale: smartphone Android di fascia media di quattro anni, memoria quasi piena, connessione 4G spesso debole (tram, sotterranei dell'ospedale); la sera può usare il laptop di casa
- Canali: Instagram, WhatsApp, browser da smartphone, email, laptop di casa
- Familiarità digitale: 3/5. Social, home banking, app di consegne e dei turni; non legge le istruzioni, procede per tentativi
- Accessibilità e contesto: limitazioni situazionali: pause di 10 minuti, spesso una mano sola, attenzione divisa, stanchezza dopo il turno di notte
- Frequenza d'uso: occasionale; visite brevi (2–5 minuti) da link condivisi sui social
- Motivazione: un'amica dottoranda condivide il progetto Mind the Climate nelle storie di Instagram; Sara vuole donare 20 € prima che finisca la pausa
- Archetipo suggerito: «la donatrice d'impulso in pausa»
</scheda_vincolante>

<problemi_assegnati>
- [S74 · prestazioni] Da smartphone la pagina di Mind the Climate (41/100) e il modulo di donazione (39/100) sono le pagine più lente del percorso (LCP 3,4 s): con il 4G debole sembra tutto bloccato.
- [S38 · H7 · G4] La pagina del progetto è lunghissima e senza indice: col pollice scorre a lungo per arrivare alle ricompense.
- [S31 · H3 · G3] Le ricompense sono un elenco lungo che non si può comprimere né confrontare.
- [X05 · analisi preliminare, da verificare] «FAI TU» non dice che è un importo libero: non capisce subito che può donare 20 € senza ricompensa.
- [S28 · H1 · G3] Tocca «Contatta il progettista» per fare una domanda, non succede nulla per secondi e tocca di nuovo.
- [S41 · H9 · G4] Un errore del modulo compare solo dopo l'invio: deve tornare indietro e cercare il campo sbagliato.
- [S11 · H2 · G2] La sera, guardando gli altri progetti, legge «-36 giorni» e pensa che siano chiusi.
- [S71 · Mobile · G3] I caroselli dei progetti scorrono di lato senza indicatori: vede due progetti e pensa che siano gli unici.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S70 · positivo] Su smartphone la pagina è in una colonna leggibile e il pulsante «Sostieni il progetto» è ben visibile; la barra delle sezioni resta fissa.
- [S27 · positivo] «Copia link» le permette di mandarsi il progetto su WhatsApp per riprenderlo dopo.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Mostra che le sue difficoltà dipendono dal contesto d'uso (tempo, rete, una mano) più che da limiti personali: è un esempio di disabilità situazionale.
- Mostra il tipo di attenzione divisa: il sito deve competere con il cercapersone, i colleghi, la fine della pausa.
- Le sue aspettative sono modellate dalle app che usa ogni giorno (pagamento in pochi tocchi).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P02" -->

<!-- BEGIN PROMPT id="J02" tipo="journey_map" persona="P02" richiede="C00" -->
````text
<prompt id="J02" tipo="journey_map" persona="P02" richiede="C00">

<obiettivo>
Genera la journey map J02 della persona P02 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P02 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Sara Colombo, 34 anni, Torino. Infermiera turnista in pronto soccorso. Donatrice occasionale. Smartphone Android di fascia media con 4G spesso debole; la sera il laptop di casa. Familiarità digitale 3/5, procede per tentativi. Pause di 10 minuti, una mano sola, attenzione divisa. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Pausa di metà turno, in sala relax. Sara vede nelle storie di Instagram di un'amica dottoranda il link a Mind the Climate. Vuole donare 20 € prima che la pausa finisca. Il percorso si interrompe e riprende la sera, a casa. Obiettivo: completare la donazione con il minimo sforzo, anche passando da un dispositivo all'altro.
</scenario>

<fasi>
1. Scoperta sui social: storia Instagram con link. Canale: Instagram.
2. Primo caricamento da smartphone. Canale: browser da smartphone. Problema: [S74 · prestazioni].
3. Valutazione rapida del progetto. Problemi: [S38 · H7 · G4], [S28 · H1 · G3]. Positivo: [S70 · positivo].
4. Scelta della ricompensa. Problemi: [S31 · H3 · G3], [X05 · analisi preliminare, da verificare].
5. Tentativo di donazione e interruzione: il modulo è lento, compare un errore dopo l'invio, la pausa finisce. Problemi: [S41 · H9 · G4], [S74 · prestazioni]. Positivo: [S27 · positivo] si manda il link con «Copia link» su WhatsApp.
6. Ripresa la sera e conclusione: riapre il link sul laptop, curiosa tra gli altri progetti e completa la donazione. Canali: WhatsApp, sito da laptop, email. Problemi: [S11 · H2 · G2], [S71 · Mobile · G3] (ricordo di quanto visto su smartphone o nuova consultazione da telefono).
</fasi>

<indicazioni_specifiche>
- Questo journey è multicanale: evidenzia nella sezione «Note per il team» la mancanza di continuità tra smartphone e laptop (dati del modulo da reinserire) e marcala [IPOTESI] se non è verificata.
- Momento critico principale: fase 5, abbandono per lentezza e interruzione. Collegalo agli indicatori HEART Task success e Adoption.
- La curva emotiva parte positiva (fase 1), scende fino al minimo nella fase 5 e risale nella fase 6.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J02" -->
