---
documento: persona_journey_prompts
persona: P01
journey: J01
nome: Giuseppe Ferrero
descrizione: donatore alla prima esperienza
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P01, J01]
---

# P01 · J01 · Giuseppe Ferrero, donatore alla prima esperienza

Questo file contiene i due prompt della persona P01 e del suo journey J01. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P01**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J01**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P01 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J01; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P01" tipo="persona" persona="P01" richiede="C00" -->
````text
<prompt id="P01" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P01 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Giuseppe Ferrero
- Età: 71
- Città: Moncalieri (TO)
- Occupazione: insegnante di scienze alle scuole medie, in pensione
- Famiglia: vedovo; una figlia e due nipoti, la più piccola nata prematura due anni fa
- Ruolo: donatore alla prima esperienza di crowdfunding
- Dispositivo principale: tablet Android da 10 pollici regalato dal nipote, con carattere di sistema ingrandito; in casa non c'è un computer
- Canali: quotidiano locale cartaceo, motore di ricerca, sito da tablet, email, telefono
- Familiarità digitale: 2/5. Usa WhatsApp, email, meteo e il giornale online; ha pagato online solo con l'aiuto della figlia; diffida dei siti che non conosce
- Accessibilità: presbiopia (occhiali da lettura), si affatica con testi piccoli e poco contrastati; tocchi imprecisi sui bersagli piccoli
- Frequenza d'uso: prima visita; al massimo una o due donazioni l'anno
- Motivazione: ha letto sul quotidiano locale un articolo su un progetto UniTo per proteggere i neonati dai virus (MILK-ACT) e, pensando alla nipote, vuole donare 50 €
- Archetipo suggerito: «il nonno generoso ma prudente»
</scheda_vincolante>

<problemi_assegnati>
- [S59 · LG1 · G4] Arrivato in homepage dal motore di ricerca, non trova una frase che dica che cos'è Ginger né che cosa c'entri con l'Università.
- [S23 · H8 · G4] Titoli arancioni e footer poco contrastati: deve avvicinare il tablet e ingrandire con due dita.
- [S54 · H8 · G4] In «Come funziona» i testi sono piccoli e di dimensione diversa: si stanca presto.
- [S52 · H7 · G3] «Come funziona» non ha titoli né indice: perde il segno e rinuncia a leggere fino in fondo.
- [S12 · H2 · G2] «Overfunding», «100% SUCCESSO»: parole che non conosce e che non vengono spiegate.
- [S10 · H1 · G3] MILK-ACT risulta al 181%: deduce che i soldi bastano già e che la sua donazione non serve.
- [S11 · H2 · G2] «-36 giorni» sulla card: pensa che la campagna sia scaduta da più di un mese.
- [S14 · H3 · G3] Un pulsante apre una nuova scheda: sul tablet non capisce perché il tasto Indietro non lo riporta dove era.
- [S41 · H9 · G4] L'errore del modulo compare solo dopo l'invio: teme di aver sbagliato qualcosa con il pagamento.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] La descrizione del progetto è scritta a domande e risposte e la scadenza è esplicita («Scade il …»): lo rassicura.
- [S44 · positivo] Numero di telefono e orari dell'assistenza ripetuti in «Come funziona»: preferisce telefonare piuttosto che scrivere.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Il suo modello mentale della donazione è quello dell'offerta o del bonifico: si aspetta di dare una somma e basta, non di scegliere una «ricompensa».
- Mostra le sue strategie: chiede conferma alla figlia per telefono, fotografa lo schermo, preferisce chiamare l'assistenza. Non descriverlo come incapace: è un ex insegnante di scienze, curioso e capace di capire la ricerca.
- Il motto deve esprimere insieme generosità e prudenza.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P01" -->

<!-- BEGIN PROMPT id="J01" tipo="journey_map" persona="P01" richiede="C00" -->
````text
<prompt id="J01" tipo="journey_map" persona="P01" richiede="C00">

<obiettivo>
Genera la journey map J01 della persona P01 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P01 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Giuseppe Ferrero, 71 anni, Moncalieri. Insegnante di scienze in pensione, vedovo, una nipote nata prematura. Prima esperienza di crowdfunding. Tablet Android con carattere ingrandito, nessun computer. Familiarità digitale 2/5. Presbiopia e tocchi imprecisi. Prudente, preferisce telefonare; chiede conferma alla figlia. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Domenica mattina, a casa. Giuseppe ha letto sul quotidiano locale cartaceo un articolo su un progetto UniTo per proteggere i neonati dai virus (MILK-ACT). Sul tablet cerca con il motore di ricerca le parole che ricorda dell'articolo. Obiettivo: donare 50 € a MILK-ACT ed essere sicuro che i soldi arrivino davvero alla ricerca.
</scenario>

<fasi>
1. Scoperta: articolo cartaceo e ricerca sul motore di ricerca. Canali: giornale, motore di ricerca. Facoltativo: [S60 · LG2 · G1] titolo della pagina troncato nei risultati e marchio con due nomi.
2. Orientamento sulla homepage di Ginger. Canale: sito da tablet. Problemi: [S59 · LG1 · G4], [S23 · H8 · G4].
3. Capire come funziona la donazione: pagina «Come funziona». Problemi: [S54 · H8 · G4], [S52 · H7 · G3], [S12 · H2 · G2]. Positivo: [S44 · positivo] trova il numero di telefono.
4. Valutare MILK-ACT: elenco dei progetti UniTo e pagina del progetto. Problemi: [S10 · H1 · G3], [S11 · H2 · G2], [S14 · H3 · G3]. Positivo: [S27 · positivo].
5. Donare: scelta dell'importo e modulo di donazione. Problema: [S41 · H9 · G4].
6. Dopo la donazione: telefona alla figlia o all'assistenza per avere conferma; attende un'email di conferma [IPOTESI]. Canali: telefono, email.
</fasi>

<indicazioni_specifiche>
- Andamento emotivo atteso: motivazione alta all'inizio, calo nelle fasi 3–4, minimo nella fase 5, recupero parziale nella fase 6 grazie al contatto umano.
- Nella fase 4 mostra il golfo della valutazione: Giuseppe interpreta male lo stato della campagna (181%, «-36 giorni») e rischia di rinunciare per un motivo sbagliato.
- Nella fase 5 evidenzia il bisogno di prevenzione degli errori e di feedback immediato (regole di Shneiderman).
- Indica nella sezione «Note per il team» che il passaggio dalla pagina progetto al modulo richiede di scegliere una ricompensa, cosa che non corrisponde al suo modello mentale.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati (il facoltativo solo se usato); (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J01" -->
