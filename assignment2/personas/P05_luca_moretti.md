---
documento: persona_journey_prompts
persona: P05
journey: J05
nome: Luca Moretti
descrizione: donatore abituale e metodico
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P05, J05]
---

# P05 · J05 · Luca Moretti, donatore abituale e metodico

Questo file contiene i due prompt della persona P05 e del suo journey J05. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P05**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J05**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P05 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J05; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P05" tipo="persona" persona="P05" richiede="C00" -->
````text
<prompt id="P05" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P05 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Luca Moretti
- Età: 52
- Città: Asti
- Occupazione: elettricista, titolare di una piccola impresa con due dipendenti
- Famiglia: sposato, due figli adolescenti; il maggiore studia a UniTo
- Ruolo: donatore abituale e metodico
- Dispositivo principale: PC desktop in ufficio con monitor da 24 pollici; smartphone per controlli veloci
- Canali: sito da desktop, email, smartphone
- Familiarità digitale: 3/5. Fatturazione elettronica, home banking, acquisti online; lento ma meticoloso; usa fogli di calcolo semplici e prende appunti su carta
- Accessibilità: daltonismo (deuteranopia): distingue con difficoltà verde, rosso e arancione
- Frequenza d'uso: ricorrente; 2–3 donazioni l'anno su piattaforme di crowdfunding; visite lunghe di confronto (30–40 minuti) e poi controlli periodici
- Motivazione: vuole dare 100 € al progetto UniTo «che ne ha più bisogno», possibilmente con ricadute sul territorio piemontese
- Archetipo suggerito: «il donatore che confronta prima di scegliere»
</scheda_vincolante>

<problemi_assegnati>
- [S16 · H4 · G2] Le barre di avanzamento si distinguono solo per colore e il contatore «18 progetti» non dice quanti sono attivi.
- [S10 · H1 · G3] I progetti oltre il 100% non hanno un badge testuale: con il daltonismo non distingue lo stato affidato al colore.
- [S29 · H1 · G3] Sui progetti conclusi lo stato è un pallino rosso senza legenda.
- [S23 · H8 · G4] Pulsanti verdi con testo bianco e titoli arancioni poco contrastati.
- [S11 · H2 · G2] «-36 giorni» rende ambiguo quanto tempo resta.
- [S18 · H6 · G2] Le card non dicono il tema del progetto: deve aprirli tutti e ricordarli.
- [S21 · H7 · G3] Non può filtrare né ordinare per scadenza o per quanto manca all'obiettivo.
- [S22 · H7 · G3] «ALTRI» carica pochi progetti alla volta senza dire quanti ne restano.
- [S24 · H9 · G2] A fine elenco «ALTRI» sparisce senza messaggio.
- [S15 · H3 · G4] Tornando da un progetto perde la posizione e i progetti caricati.
- [S37 · H6 · G3] Il raddoppio UniTo non è rappresentato vicino al punto in cui si dona: non sa che per i progetti vicini all'obiettivo la sua donazione «vale doppio».
- [X08 · analisi preliminare, da verificare] I progetti oltre il 100% mostrano un «nuovo obiettivo» senza dire rispetto a quale cifra.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S08 · positivo] Ogni card riassume percentuale, importo su obiettivo e numero di donatori: è proprio il dato che gli serve per confrontare.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Mostra il suo metodo: confronta i progetti annotando cifre su carta o in un foglio di calcolo. Collegalo al carico sulla memoria e al principio «riconoscimento anziché ricordo».
- Il daltonismo è un tratto, non il centro della persona: emerge solo dove il sito affida informazioni al colore.
- Il suo criterio di scelta («chi ha più bisogno») è in conflitto con come il sito mostra lo stato delle campagne.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P05" -->

<!-- BEGIN PROMPT id="J05" tipo="journey_map" persona="P05" richiede="C00" -->
````text
<prompt id="J05" tipo="journey_map" persona="P05" richiede="C00">

<obiettivo>
Genera la journey map J05 della persona P05 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P05 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Luca Moretti, 52 anni, Asti. Elettricista titolare di una piccola impresa, figlio studente UniTo. PC desktop in ufficio, smartphone per controlli. Familiarità digitale 3/5, meticoloso, prende appunti su carta. Daltonismo (deuteranopia). Donatore ricorrente su piattaforme di crowdfunding. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Sabato mattina, in ufficio, a impresa chiusa. Luca ha deciso di dare 100 € alla ricerca UniTo e apre la scheda «Progetti» della pagina partner. Vuole confrontare le campagne e scegliere quella che ne ha più bisogno; nelle settimane successive tornerà a controllare come procede. Obiettivo: scegliere in modo informato e verificare che la sua donazione abbia fatto la differenza.
</scenario>

<fasi>
1. Esplorazione dell'elenco UniTo. Canale: sito da desktop. Problemi: [S16 · H4 · G2], [S23 · H8 · G4]. Positivo: [S08 · positivo].
2. Confronto tra i progetti. Problemi: [S18 · H6 · G2], [S21 · H7 · G3], [S22 · H7 · G3], [S24 · H9 · G2], [S15 · H3 · G4].
3. Verifica dello stato e del bisogno. Problemi: [S10 · H1 · G3], [S11 · H2 · G2], [S29 · H1 · G3], [X08 · analisi preliminare, da verificare].
4. Decisione. Problema: [S37 · H6 · G3].
5. Donazione. Nessun problema assegnato: puoi usare «—» oppure aggiungere al massimo un problema coerente del catalogo, spiegandolo nelle note.
6. Monitoraggio nelle settimane successive. Canali: smartphone, email [IPOTESI per eventuali email di aggiornamento]. Problemi: ritorno sull'elenco con [S15 · H3 · G4] e [S11 · H2 · G2].
</fasi>

<indicazioni_specifiche>
- Mostra la ricerca di tipo esaustivo e il modello del berrypicking: Luca costruisce la decisione per passi, raccogliendo informazioni da più progetti.
- Momento critico: fase 3, quando il colore non basta a capire quali campagne hanno raggiunto l'obiettivo. Collega il punto alle WCAG (l'informazione non deve essere trasmessa solo dal colore) senza inventare numeri di criteri che non conosci con certezza.
- Indicatore HEART da usare nei momenti critici: Retention (tornerà a donare?) e Task success.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J05" -->
