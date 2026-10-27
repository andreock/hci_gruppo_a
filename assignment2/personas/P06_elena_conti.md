---
documento: persona_journey_prompts
persona: P06
journey: J06
nome: Elena Conti
descrizione: donatrice attenta a fiducia e privacy
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P06, J06]
---

# P06 · J06 · Elena Conti, donatrice attenta a fiducia e privacy

Questo file contiene i due prompt della persona P06 e del suo journey J06. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P06**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J06**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P06 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J06; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P06" tipo="persona" persona="P06" richiede="C00" -->
````text
<prompt id="P06" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P06 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Elena Conti
- Età: 58
- Città: Torino
- Occupazione: commercialista con studio proprio
- Famiglia: divorziata, una figlia medico specializzando
- Istruzione: laurea in Economia all'Università di Torino
- Ruolo: donatrice attenta a fiducia, trasparenza e privacy; prima volta su Ginger
- Dispositivo principale: PC desktop con due monitor; smartphone solo per email
- Canali: sito da desktop, sito unito.it, email, telefono
- Familiarità digitale: 4/5. Software gestionali, portali fiscali, PEC; legge con attenzione condizioni e note
- Accessibilità: nessuna esigenza specifica; occhiali progressivi
- Frequenza d'uso: dona una volta l'anno, a dicembre, a enti di ricerca; visita lunga e accurata
- Motivazione: vuole destinare 300 € alla ricerca della sua università, ma solo se l'iniziativa è affidabile, trasparente sull'uso dei fondi, rispettosa della privacy e se ottiene una ricevuta utilizzabile
- Archetipo suggerito: «la donatrice che legge le condizioni»
</scheda_vincolante>

<problemi_assegnati>
- [S61 · LG3 · G3] «Chi siamo» è solo nel footer: non capisce subito chi gestisce la piattaforma.
- [S09 · H1 · G3] Testi al futuro, nessuna data e blog fermo al 2021–2022: dubita che l'iniziativa sia ancora attiva.
- [X06 · analisi preliminare, da verificare] Nella stessa pagina i numeri dell'iniziativa non coincidono (13 o 18 progetti, 312.000 o 343.000 €).
- [S13 · H2 · G2] Dagli autori («by Team GaIA») non capisce che sono gruppi di ricerca UniTo.
- [S48 · H4 · G1] «Prende ciò che raccoglie» e «keep it all» per la stessa regola.
- [S47 · H3 · G2] Il link «commissioni» apre le Condizioni d'uso invece della spiegazione dei costi.
- [S53 · H7 · G3] Le 25 FAQ sono mescolate, senza gruppi né ricerca.
- [X02 · analisi preliminare, da verificare] Le commissioni restano a suo carico anche in caso di rimborso.
- [S41 · H9 · G4] La regola «tutto o niente» non è richiamata nel modulo di donazione.
- [S42 · H5 · G2] Il nome diventa pubblico se non spunta «donatore anonimo».
- [X03 · analisi preliminare, da verificare] Anche se anonima, il progettista riceve nome, email e importo.
- [X04 · analisi preliminare, da verificare] Nessuna indicazione su ricevuta e detraibilità fiscale.
- [S25 · H10 · G2] Nella pagina UniTo non c'è un contatto di riferimento.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] La descrizione del progetto anticipa le domande sull'uso dei fondi e sul team.
- [S44 · positivo] Telefono, email e orari dell'assistenza ben visibili.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- La sua prospettiva è quella della fiducia: ogni incoerenza (date, numeri, nomi) riduce la credibilità percepita.
- Mostra che legge davvero condizioni e FAQ, e che il problema non è la mancanza di informazioni ma la loro posizione e coerenza.
- La privacy è una sua priorità: collega [S42] e [X03] alla prevenzione degli errori e al senso di controllo dell'utente (regole di Shneiderman).
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P06" -->

<!-- BEGIN PROMPT id="J06" tipo="journey_map" persona="P06" richiede="C00" -->
````text
<prompt id="J06" tipo="journey_map" persona="P06" richiede="C00">

<obiettivo>
Genera la journey map J06 della persona P06 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P06 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Elena Conti, 58 anni, Torino. Commercialista, laureata a UniTo. PC desktop con due monitor. Familiarità digitale 4/5, legge condizioni e note. Nessuna esigenza di accessibilità specifica. Dona una volta l'anno a enti di ricerca; prima volta su Ginger. Priorità: affidabilità, trasparenza, privacy, ricevuta. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Metà dicembre, nello studio, a fine giornata. Elena ha sentito parlare di Funds TOgether da un'ex compagna di università e vuole destinare 300 € alla ricerca UniTo prima della fine dell'anno. Obiettivo: verificare che piattaforma e iniziativa siano affidabili, capire le regole economiche, donare restando anonima e ottenere una ricevuta.
</scenario>

<fasi>
1. Verifica dell'affidabilità della piattaforma. Canale: sito da desktop. Problema: [S61 · LG3 · G3].
2. Verifica dell'iniziativa UniTo. Canali: sito da desktop, unito.it. Problemi: [S09 · H1 · G3], [X06 · analisi preliminare, da verificare], [S13 · H2 · G2], [S25 · H10 · G2].
3. Comprensione delle regole economiche. Problemi: [S53 · H7 · G3], [S48 · H4 · G1], [S47 · H3 · G2], [X02 · analisi preliminare, da verificare].
4. Scelta del progetto e dell'importo. Positivo: [S27 · positivo].
5. Donazione e privacy. Problemi: [S41 · H9 · G4] (regola «tutto o niente» non richiamata), [S42 · H5 · G2], [X03 · analisi preliminare, da verificare].
6. Ricevuta e documentazione fiscale. Canali: email, telefono. Problema: [X04 · analisi preliminare, da verificare]. Positivo: [S44 · positivo] telefona all'assistenza [IPOTESI sull'esito della telefonata].
</fasi>

<indicazioni_specifiche>
- La curva emotiva qui misura soprattutto la fiducia: rendilo esplicito nella riga Emozioni (es. «Sospetto (−1)», «Rassicurazione (+1)»).
- Momento critico: fase 2, dove le incoerenze tra date e numeri mettono in dubbio l'intera iniziativa (indicatore HEART Adoption).
- Nella sezione «Continuità tra touchpoint» evidenzia i salti tra Ginger, unito.it, FAQ e assistenza telefonica.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J06" -->
