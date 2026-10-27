---
documento: persona_journey_prompts
persona: P10
journey: J10
nome: Franco Gallo
descrizione: responsabile di una campagna in corso
richiede: 00_contesto_comune_C00.md
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
prompt_ids: [P10, J10]
---

# P10 · J10 · Franco Gallo, responsabile di una campagna in corso

Questo file contiene i due prompt della persona P10 e del suo journey J10. Il contesto comune non è ripetuto qui: si trova in [00_contesto_comune_C00.md](00_contesto_comune_C00.md).

**Come usarlo**
1. Apri una nuova conversazione con Opus 5.5 e incolla il prompt **C00** dal file del contesto comune.
2. Per la persona incolla il prompt **P10**; per il journey usa una nuova conversazione, incolla di nuovo C00 e poi il prompt **J10**. Puoi anche incollare C00 e il prompt singolo nello stesso messaggio.
3. Se la persona P10 è già stata generata, incolla il suo documento dentro `<persona_generata>` del prompt J10; altrimenti lascialo com'è.
4. Facoltativo: controlla l'output con il prompt V00 in [99_verifica_V00.md](99_verifica_V00.md).

Il testo da copiare è quello dentro ciascun blocco di codice.

<!-- BEGIN PROMPT id="P10" tipo="persona" persona="P10" richiede="C00" -->
````text
<prompt id="P10" tipo="persona" richiede="C00">

<obiettivo>
Genera la persona P10 usando il formato <formato_persona> e le regole del contesto C00.
</obiettivo>

<scheda_vincolante>
- Nome: Franco Gallo
- Età: 63
- Città: Torino
- Occupazione: professore ordinario in un dipartimento UniTo di area veterinaria
- Famiglia: sposato, tre figli adulti
- Ruolo: promotore; responsabile scientifico della campagna fittizia «AlveareSano» (salute delle api), in corso, selezionata da Funds TOgether, al 130% dell'obiettivo con 20 giorni rimasti: un andamento simile a quello di MILK-ACT e RePatch
- Dispositivo principale: PC fisso con monitor da 27 pollici nello studio; smartphone per email e telefonate
- Canali: sito da desktop, area progettisti [IPOTESI], email, telefono con il campaign manager di Ginger, ufficio comunicazione d'Ateneo, eventi pubblici
- Familiarità digitale: 2/5. Email, piattaforme per i bandi, presentazioni; delega gli aspetti tecnici a un dottorando; poca pazienza con le interfacce
- Accessibilità e contesto: presbiopia lieve; consulta il sito tra una riunione e l'altra, pochi minuti per volta (attenzione divisa)
- Frequenza d'uso: quotidiana durante la campagna (controlli di 2–3 minuti), quasi nulla dopo
- Motivazione: raggiungere il secondo obiettivo, far capire ai donatori che il cofinanziamento UniTo raddoppia i fondi e chiudere la campagna con una buona immagine del gruppo
- Archetipo suggerito: «il responsabile scientifico con poco tempo»
</scheda_vincolante>

<problemi_assegnati>
- [S10 · H1 · G3] La campagna è oltre il 100% ma la card non dice «obiettivo raggiunto, raccolta ancora aperta»: i potenziali donatori pensano che non serva più.
- [X08 · analisi preliminare, da verificare] Il «nuovo obiettivo» non dice rispetto a quale cifra: i donatori gli scrivono per chiedere chiarimenti.
- [S37 · H6 · G3] Il raddoppio UniTo non è rappresentato vicino al punto in cui si dona.
- [S11 · H2 · G2] «-20 giorni» sulla card: un collega gli chiede se la campagna è già finita.
- [S16 · H4 · G2] Le barre di avanzamento non si capiscono al primo sguardo.
- [S13 · H2 · G2] Il nome del gruppo sulla card non richiama l'Ateneo.
- [S18 · H6 · G2] La card non indica il tema del progetto.
- [S64 · LG6 · G3] In homepage il titolo della campagna è troncato.
- [S30 · H2 · G2] Teme di ripetere l'errore visto in BRIGHT: aggiornamenti messi prima della presentazione.
- [S34 · H4 · G1] Le ricompense più alte non mostrano il contatore: sembrano ignorate.
- [S28 · H1 · G3] I donatori gli dicono che «Contatta il progettista» non funziona (in realtà è lento e senza feedback).
- [S29 · H1 · G3] A campagna chiusa il box «SOSTIENI» resterà visibile e confonderà i visitatori.
</problemi_assegnati>

<aspetti_positivi_da_includere>
- [S27 · positivo] Box di stato completo con scadenza esplicita nella pagina progetto.
- [S08 · positivo] Le card mostrano percentuale, raccolto e donatori.
</aspetti_positivi_da_includere>

<indicazioni_specifiche>
- Il suo punto di vista è quello di chi è responsabile dell'esperienza dei donatori senza controllare l'interfaccia: subisce i problemi del sito attraverso le domande e le lamentele degli altri.
- La familiarità bassa non va resa con stereotipi: è un esperto nel suo campo e sa comunicare la ricerca, ma non ha tempo per imparare uno strumento.
- Il raddoppio UniTo è il suo argomento di comunicazione principale e il sito non lo aiuta a renderlo visibile.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) il front matter è completo e problemi_citati contiene esattamente gli ID citati nel testo; (2) ogni problema assegnato è citato almeno una volta; (3) i dati della scheda vincolante sono rispettati; (4) titoli e ordine delle sezioni sono identici a <formato_persona>.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="P10" -->

<!-- BEGIN PROMPT id="J10" tipo="journey_map" persona="P10" richiede="C00" -->
````text
<prompt id="J10" tipo="journey_map" persona="P10" richiede="C00">

<obiettivo>
Genera la journey map J10 della persona P10 usando il formato <formato_journey> e le regole del contesto C00.
</obiettivo>

<persona_generata>
[Se la persona P10 è già stata generata, sostituisci questa riga con il suo documento completo. Altrimenti lascia la riga così: userai la scheda sintetica.]
</persona_generata>

<scheda_sintetica_persona>
Franco Gallo, 63 anni, professore ordinario UniTo di area veterinaria. Responsabile scientifico della campagna fittizia «AlveareSano», in corso, al 130% con 20 giorni rimasti. PC fisso con monitor grande, smartphone. Familiarità 2/5, delega a un dottorando. Presbiopia lieve, poco tempo, controlli quotidiani di pochi minuti. Se il documento in <persona_generata> è presente, usa i suoi dettagli; in caso di conflitto valgono età, dispositivo, familiarità, accessibilità e frequenza di questa scheda.
</scheda_sintetica_persona>

<scenario>
Le ultime tre settimane della campagna «AlveareSano». Franco controlla ogni giorno la pagina pubblica tra una riunione e l'altra, risponde ai donatori, prepara la comunicazione con l'ufficio stampa e, a fine campagna, deve rendicontare. Obiettivo: superare il secondo obiettivo e far capire ai donatori che la raccolta è ancora utile grazie al cofinanziamento UniTo.
</scenario>

<fasi>
1. Controllo della pagina pubblica e della card. Canale: sito da desktop. Problemi: [S64 · LG6 · G3], [S13 · H2 · G2], [S18 · H6 · G2].
2. Monitoraggio quotidiano. Problemi: [S11 · H2 · G2], [S16 · H4 · G2]. Positivi: [S27 · positivo], [S08 · positivo].
3. Superamento dell'obiettivo. Problemi: [S10 · H1 · G3], [X08 · analisi preliminare, da verificare], [S37 · H6 · G3].
4. Comunicazione ai donatori e alla stampa. Canali: area progettisti [IPOTESI], email, ufficio comunicazione. Problemi: [S30 · H2 · G2], [S34 · H4 · G1].
5. Gestione delle domande dei donatori. Canali: email, telefono. Problema: [S28 · H1 · G3].
6. Chiusura della campagna e rendicontazione. Problema: [S29 · H1 · G3].
</fasi>

<indicazioni_specifiche>
- Molti touchpoint sono indiretti (donatori, colleghi, ufficio stampa che gli riportano problemi): rendilo esplicito nella riga Canali.
- Momento critico: fase 3, quando il successo della campagna diventa paradossalmente un ostacolo alla raccolta (HEART Engagement dei donatori).
- Nelle note per il team indica quali passaggi riguardano l'area progettisti, non analizzata nella presentazione.
</indicazioni_specifiche>

<controllo_finale>
Prima di rispondere verifica, senza scriverlo: (1) front matter completo e problemi_citati uguale agli ID citati; (2) tutti i problemi elencati nelle fasi sono citati; (3) le fasi della tabella coincidono con il front matter; (4) i punteggi della curva emotiva coincidono con la riga Emozioni; (5) ogni difficoltà ha un'opportunità corrispondente.
</controllo_finale>

</prompt>
````
<!-- END PROMPT id="J10" -->
