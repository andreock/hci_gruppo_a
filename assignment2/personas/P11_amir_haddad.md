---
documento: persona_journey_prompts
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
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P11**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J11**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P11 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J11; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P11" tipo="persona" persona="P11" richiede="C00" -->
````text
<prompt id="P11" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P11 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Amir Haddad
- Età: 27
- Città: Torino
- Origine e lingue: libanese, in Italia da cinque anni; arabo madrelingua, inglese C1, italiano B2
- Occupazione: dottorando in Informatica all'Università di Torino
- Famiglia: vive da solo
- Ruolo: promotore; cura la comunicazione della campagna del suo gruppo, la campagna fittizia «OpenAria» (sensori open source per la qualità dell'aria), in corso su Funds TOgether
- Dispositivo principale: laptop Linux con Firefox; smartphone Android
- Canali: area progettisti [IPOTESI], Instagram, LinkedIn, email, WhatsApp, sito da smartphone e da desktop
- Familiarità digitale: 5/5. Sviluppatore, usa molto la tastiera e le scorciatoie, ispeziona il codice delle pagine
- Accessibilità e contesto: lavora quasi solo da tastiera; scrive in italiano con qualche incertezza e preferisce scrivere i testi in inglese
- Frequenza d'uso: quotidiana durante la campagna
- Motivazione: portare donatori anche dall'estero (colleghi internazionali, comunità libanese) e far sembrare la campagna professionale
- Archetipo suggerito: «il dottorando che fa da social media manager»
</scheda_vincolante>

<problemi_assegnati>
- [S32 · H4 · G4] La versione inglese cambia solo la panoramica e rimanda alla sezione News: i suoi donatori stranieri trovano un sito a metà.
- [S40 · H8 · G2] Le ricompense ripetono ogni testo in due lingue: deve scrivere testi doppi e lunghi.
- [S36 · H4 · G2] Nel box «SOSTIENI» la disposizione delle lingue cambia da progetto a progetto.
- [S12 · H2 · G2] Etichette di piattaforma in inglese e italiano mescolati («Overfunding», «by»).
- [S41 · H9 · G4] Gli errori del modulo sono solo in italiano: riceve messaggi di donatori stranieri bloccati.
- [S74 · prestazioni] Il link condiviso sui social apre pagine lente da smartphone (pagina progetto 41/100, modulo 39/100).
- [S71 · Mobile · G3] Su smartphone i caroselli non mostrano di poter scorrere.
- [S28 · H1 · G3] «Contatta il progettista» resta senza feedback per secondi.
- [S33 · H4/H10 · G1] I tooltip sembrano link.
- [S39 · H7 · G1] La barra dell'obiettivo è cliccabile e ricarica la pagina.
- [S67 · LG9 · G2] Da tastiera le tendine del menu non si chiudono con Esc.
- [S20 · H7 · G3] Manca «Torna su» nelle pagine lunghe.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] «Copia link» e condivisione su vari canali; pulsanti con attributi ARIA.
- [S70 · positivo] Su smartphone la pagina progetto si adatta bene e «Sostieni il progetto» è visibile.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- È un utente esperto (power user): i suoi problemi riguardano flessibilità ed efficienza d'uso (H7) e la qualità tecnica, oltre all'internazionalizzazione.
- Fa da ponte tra il gruppo di ricerca e i donatori: vede i problemi del sito sia in prima persona sia attraverso i messaggi che riceve.
- Distingui chiaramente ciò che è verificato nella presentazione da ciò che riguarda l'area progettisti, da marcare [IPOTESI].
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P11" -->

<!-- BEGIN PROMPT id="J11" tipo="journey_map" persona="P11" richiede="C00" -->
````text
<prompt id="J11" tipo="journey_map" persona="P11" richiede="C00">

<obiettivo>
Genera la journey map J11 della persona P11 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P11 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Amir Haddad, 27 anni, dottorando in Informatica a UniTo, libanese, in Italia da cinque anni (italiano B2, inglese C1). Laptop Linux con Firefox, smartphone Android. Familiarità 5/5, lavora da tastiera. Cura la comunicazione della campagna fittizia «OpenAria». Uso quotidiano. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Una settimana tipo durante la campagna «OpenAria». Amir prepara un aggiornamento in due lingue, lo pubblica, lancia una promozione sui social rivolta anche ai colleghi all'estero, risponde ai donatori bloccati e il venerdì presenta un breve report al gruppo. Obiettivo: aumentare i donatori internazionali e ridurre le richieste di aiuto.
</scenario>

<fasi>
1. Preparazione dei contenuti bilingui. Problemi: [S40 · H8 · G2], [S36 · H4 · G2], [S12 · H2 · G2].
2. Pubblicazione di un aggiornamento. Canale: area progettisti [IPOTESI]. Problema: [S32 · H4 · G4] (la versione inglese finisce nella sezione News).
3. Promozione sui social. Canali: Instagram, LinkedIn, WhatsApp, sito da smartphone. Problemi: [S74 · prestazioni], [S71 · Mobile · G3]. Positivi: [S27 · positivo], [S70 · positivo].
4. Assistenza ai donatori stranieri. Canali: email, WhatsApp. Problemi: [S41 · H9 · G4], [S32 · H4 · G4].
5. Verifica dell'esperienza da tastiera e da mobile. Problemi: [S67 · LG9 · G2], [S20 · H7 · G3], [S33 · H4/H10 · G1], [S39 · H7 · G1], [S28 · H1 · G3].
6. Report settimanale al gruppo. Canale: riunione o documento condiviso. Sintesi dei problemi e proposte di segnalazione alla piattaforma.
</fasi>

<indicazioni_specifiche>
- Nella sezione «Momenti critici» usa gli indicatori HEART come li userebbe Amir nel report (es. Adoption dei donatori stranieri, Task success del modulo), proponendo metriche osservabili senza inventare valori.
- Momento critico: fase 4, donatori stranieri bloccati da messaggi solo in italiano.
- La curva emotiva alterna frustrazione tecnica e soddisfazione per la risposta della community.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J11" -->
