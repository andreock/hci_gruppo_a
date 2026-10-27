---
documento: persona_journey_prompts
persona: P07
journey: J07
nome: Giulia Esposito
descrizione: studentessa che dona poco e condivide molto
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P07, J07]
---

# P07 · J07 · Giulia Esposito, studentessa che dona poco e condivide molto

Questo file contiene i due prompt della persona P07 e del suo journey J07. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P07**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J07**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P07 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J07; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P07" tipo="persona" persona="P07" richiede="C00" -->
````text
<prompt id="P07" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P07 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Giulia Esposito
- Età: 20
- Città: Torino (fuorisede, originaria di Salerno)
- Occupazione: studentessa al secondo anno di Biotecnologie all'Università di Torino
- Famiglia: vive in un appartamento condiviso con altre due studentesse
- Ruolo: donatrice alla prima esperienza, piccolo importo (5–10 €)
- Dispositivo principale: iPhone, usato quasi per tutto
- Canali: Instagram, Safari su iPhone, WhatsApp (gruppo di corso), PayPal
- Familiarità digitale: 4/5 su social e app; 2/5 con testi lunghi e moduli complessi
- Accessibilità: dislessia (DSA certificata): fatica con testi lunghi e densi, caratteri piccoli e parole inglesi; usa la funzione di lettura vocale dello schermo di iOS e cerca riassunti, grassetti e immagini
- Frequenza d'uso: prima visita; potrebbe tornare se coinvolta da amici o dall'Ateneo
- Motivazione: vede una storia Instagram dell'Ateneo su Funds TOgether e vuole sostenere un progetto vicino ai suoi studi, coinvolgendo il gruppo di studio
- Archetipo suggerito: «la studentessa che dona poco ma condivide molto»
</scheda_vincolante>

<problemi_assegnati>
- [S59 · LG1 · G4] La homepage non dice in una frase che cos'è Ginger: non capisce se è il sito giusto.
- [S62 · LG4 · G2] In alto vede Academy, podcast e servizi per progettisti, non i progetti da sostenere.
- [S64 · LG6 · G3] I titoli delle card sono troncati e «Per ispirarti» non dice che i progetti sono conclusi.
- [S63 · LG5 · G1] Cerca un campo di ricerca e trova solo una scritta e un elenco di categorie.
- [S71 · Mobile · G3] I caroselli scorrono di lato senza indicatori: non si accorge degli altri progetti.
- [S12 · H2 · G2] «Overfunding» e «100% SUCCESSO»: parole inglesi non spiegate, faticose da decifrare.
- [S38 · H7 · G4] La pagina del progetto è lunghissima e senza indice: perde il filo.
- [S52 · H7 · G3] «Come funziona» è un testo continuo senza titoli: la lettura vocale non le permette di saltare alla parte che le serve.
- [S41 · H9 · G4] Prova a donare 5 € e l'errore sul minimo compare solo dopo l'invio.
- [X05 · analisi preliminare, da verificare] «FAI TU» non dice che è un importo libero e il minimo cambia da progetto a progetto (10 € in MILK-ACT, 5 € in Mind the Climate).
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] Parole chiave in grassetto e infografiche nelle pagine progetto; «Copia link» e condivisione.
- [S70 · positivo] Su iPhone la pagina progetto è in una colonna leggibile e «Sostieni il progetto» è ben visibile.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Descrivi la dislessia in modo concreto (strategie, strumenti, che cosa la aiuta) e senza stereotipi; non confonderla con scarsa competenza: sui social è molto abile.
- La sua forza per il servizio è la condivisione: il suo valore come donatrice non sta nell'importo ma nella rete (indicatore HEART Engagement).
- Collega i problemi della homepage alla piega della pagina e alla gerarchia visiva.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P07" -->

<!-- BEGIN PROMPT id="J07" tipo="journey_map" persona="P07" richiede="C00" -->
````text
<prompt id="J07" tipo="journey_map" persona="P07" richiede="C00">

<obiettivo>
Genera la journey map J07 della persona P07 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P07 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Giulia Esposito, 20 anni, studentessa fuorisede di Biotecnologie a UniTo. iPhone, Instagram, WhatsApp. Familiarità 4/5 sulle app, 2/5 con testi lunghi. Dislessia (DSA): usa la lettura vocale di iOS. Budget 5–10 €. Prima visita. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Martedì pomeriggio, sul tram verso l'università. Giulia vede una storia Instagram dell'Ateneo su Funds TOgether e cerca «Ginger» per arrivare al sito: atterra sulla homepage di Ginger (scelta di scenario, non un'affermazione sul link dell'Ateneo). Obiettivo: trovare un progetto UniTo vicino ai suoi studi, donare un piccolo importo e farlo conoscere al suo gruppo di studio.
</scenario>

<fasi>
1. Scoperta su Instagram. Canale: Instagram.
2. Prima impressione sulla homepage. Canale: Safari su iPhone. Problemi: [S59 · LG1 · G4], [S62 · LG4 · G2], [S64 · LG6 · G3].
3. Ricerca dei progetti UniTo. Problemi: [S63 · LG5 · G1], [S71 · Mobile · G3], [S12 · H2 · G2].
4. Lettura del progetto e delle regole. Problemi: [S38 · H7 · G4], [S52 · H7 · G3]. Positivo: [S27 · positivo] grassetti e infografiche, [S70 · positivo].
5. Donazione di un piccolo importo: prova con 5 € su un progetto con minimo 10 €. Problemi: [S41 · H9 · G4], [X05 · analisi preliminare, da verificare].
6. Condivisione con il gruppo di studio. Canale: WhatsApp. Positivo: [S27 · positivo] «Copia link».
</fasi>

<indicazioni_specifiche>
- Nella riga Touchpoint indica dove usa la lettura vocale e dove la struttura della pagina la aiuta o la ostacola.
- Momento critico: fase 5, l'errore sul minimo che arriva tardi (rischio di rinuncia, HEART Task success). Secondo momento: fase 2, se la homepage non le conferma di essere nel posto giusto (HEART Adoption).
- La curva emotiva termina in positivo grazie alla condivisione.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J07" -->
