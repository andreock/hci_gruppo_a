---
documento: persona_journey_prompts
persona: P12
journey: J12
nome: Maria Lombardi
descrizione: promotrice di un'associazione
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P12, J12]
---

# P12 · J12 · Maria Lombardi, promotrice di un'associazione

Questo file contiene i due prompt della persona P12 e del suo journey J12. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P12**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J12**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P12 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J12; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P12" tipo="persona" persona="P12" richiede="C00" -->
````text
<prompt id="P12" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P12 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Maria Lombardi
- Età: 49
- Città: Forlì
- Occupazione: impiegata part-time in un'agenzia assicurativa; presidente volontaria di un'associazione che gestisce un doposcuola per ragazzi
- Famiglia: sposata, due figli (il maggiore ha 16 anni e la aiuta con il telefono)
- Ruolo: promotrice esterna a UniTo; vuole lanciare la prima campagna dell'associazione su Ginger
- Dispositivo principale: smartphone Android; vecchio PC Windows dell'associazione con schermo piccolo
- Canali: passaparola, sito da smartphone, sito da PC, telefono, email, videochiamata
- Familiarità digitale: 2/5. WhatsApp, Facebook, email; i moduli online la mettono in ansia
- Accessibilità: tremore essenziale lieve alle mani: fatica con bersagli piccoli, menu a tendina e gesti precisi
- Frequenza d'uso: prima visita; se lancia la campagna, uso intensivo per circa due mesi
- Motivazione: raccogliere 5.000 € per rinnovare l'aula del doposcuola (arredi e computer); una volontaria le ha parlato di Ginger
- Archetipo suggerito: «la volontaria che si lancia nel crowdfunding»
</scheda_vincolante>

<problemi_assegnati>
- [S59 · LG1 · G4] La homepage non spiega in una frase che cos'è Ginger.
- [S62 · LG4 · G2] I blocchi per progettisti in cima alla homepage, problema per i donatori, per lei sono utili: mostra che la priorità dei compiti dipende dal pubblico.
- [S61 · LG3 · G3] «Chi siamo» è solo nel footer: vuole sapere chi c'è dietro prima di fidarsi.
- [S67 · LG9 · G2] Menu e tendine con oltre 70 voci: con il tremore le tendine sono difficili da usare.
- [S19 · H6 · G1] La piccola icona «casetta» senza etichetta è un bersaglio minuscolo e poco riconoscibile.
- [S63 · LG5 · G1] Non trova un campo di ricerca per cercare campagne simili alla sua.
- [S54 · H8 · G4] In «Come funziona» i testi sono piccoli, comprese le informazioni sui costi.
- [S49 · H5 · G4] La quota di 350 € + IVA è nascosta: la scopre tardi ed è una cifra importante per l'associazione.
- [S46 · H2 · G2] «Campaign manager», «call di consulenza», «fee di accesso»: parole che non usa.
- [S53 · H7 · G3] Le FAQ sono una lista unica e lunghissima.
- [S48 · H4 · G1] Due nomi diversi per la stessa modalità di raccolta.
- [S47 · H3 · G2] Il link «commissioni» apre le Condizioni d'uso.
- [S51 · H6 · G3] Nel modulo di registrazione le etichette spariscono mentre scrive: non ricorda quale campo sta compilando.
- [S50 · H5 · G2] Su smartphone non compare la tastiera per l'email e l'autocompletamento è disattivato.
- [S45 · H1 · G2] Il consenso obbligatorio sembra una casella di spunta ma non mostra chiaramente il suo stato.
- [S55 · H9 · G2] L'errore resta visibile anche dopo la correzione: pensa di sbagliare ancora.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S58 · positivo] «LANCIA UNA CAMPAGNA» è ben visibile nel menu.
- [S44 · positivo] Telefono e orari dell'assistenza ben visibili e tre modi per iniziare: preferisce parlare con una persona.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Il tremore riguarda la precisione motoria: collega i problemi ai bersagli piccoli e ai gesti che richiede l'interfaccia (puoi richiamare la legge di Fitts come concetto, senza calcoli).
- Mostra la sua competenza: sa organizzare persone e raccogliere fondi offline; la difficoltà è tradurre questa competenza nel linguaggio della piattaforma.
- Per [S45] chiarisci nelle note per il team che la presentazione l'ha rilevato soprattutto per gli screen reader: qui è usato come ipotesi di effetto sul piano visivo.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P12" -->

<!-- BEGIN PROMPT id="J12" tipo="journey_map" persona="P12" richiede="C00" -->
````text
<prompt id="J12" tipo="journey_map" persona="P12" richiede="C00">

<obiettivo>
Genera la journey map J12 della persona P12 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P12 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Maria Lombardi, 49 anni, Forlì. Impiegata part-time e presidente volontaria di un'associazione che gestisce un doposcuola. Smartphone Android e vecchio PC dell'associazione. Familiarità 2/5, i moduli online la mettono in ansia. Tremore lieve alle mani. Prima visita; vuole lanciare una campagna da 5.000 €. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Dopo una riunione dell'associazione, una volontaria le parla di Ginger. Maria apre il sito sullo smartphone la sera stessa e prosegue nei giorni successivi dal PC dell'associazione. Obiettivo: capire se Ginger fa al caso dell'associazione, quanto costa, registrarsi e parlare con qualcuno prima di decidere se lanciare la campagna.
</scenario>

<fasi>
1. Scoperta tramite passaparola e primo accesso. Canali: passaparola, sito da smartphone. Problemi: [S59 · LG1 · G4], [S62 · LG4 · G2]. Positivo: [S58 · positivo].
2. Capire chi è Ginger e se è affidabile. Canali: sito da smartphone e da PC. Problemi: [S61 · LG3 · G3], [S67 · LG9 · G2], [S19 · H6 · G1], [S63 · LG5 · G1].
3. Capire costi e regole. Canale: sito da PC. Problemi: [S54 · H8 · G4], [S49 · H5 · G4], [S46 · H2 · G2], [S53 · H7 · G3], [S48 · H4 · G1], [S47 · H3 · G2].
4. Registrazione da smartphone. Problemi: [S51 · H6 · G3], [S50 · H5 · G2], [S45 · H1 · G2], [S55 · H9 · G2].
5. Primo contatto con la piattaforma. Canali: telefono, videochiamata. Positivo: [S44 · positivo]. Problema: [S46 · H2 · G2] («call di consulenza»). Esito della chiamata [IPOTESI].
6. Decisione di lanciare la campagna. Canali: riunione dell'associazione, email. [IPOTESI] sulla decisione finale.
</fasi>

<indicazioni_specifiche>
- Mostra il passaggio tra smartphone e PC e i punti in cui manca continuità (dati da reinserire, pagine da ritrovare).
- Momento critico: fase 3, la scoperta tardiva della quota (HEART Adoption dei promotori); secondo momento: fase 4, ansia nel modulo.
- La curva emotiva risale nella fase 5 grazie al contatto umano: evidenzia il ruolo del canale telefonico come recupero dell'esperienza.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J12" -->
