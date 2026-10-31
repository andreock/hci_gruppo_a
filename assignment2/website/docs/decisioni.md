# Decisioni di progetto

Registro delle scelte prese quando le fonti erano ambigue, in conflitto o mancanti. Ogni decisione indica il motivo e, se serve, che cosa deve confermare il gruppo. Stato: **proposta** (da confermare al checkpoint), **confermata**, **superata**.

## Vincoli della consegna

### D-01 · Il prototipo deve funzionare senza server · proposta
- **Conflitto**: il prompt chiede un sito statico «consultabile con un semplice server locale» e dati letti da `data/progetti.json`; `assignment2/Istruzioni.md` §7 B dice: «Non devono essere richiesti server per testare le pagine, devono funzionare sul client usando un browser». Le istruzioni della docente prevalgono (regola generale 3 del prompt).
- **Conseguenze**:
  - niente `fetch()` di file JSON (da `file://` i browser lo bloccano). Le pagine sono **generate in anticipo** da uno script Python a partire da `data/progetti.json` e dai file di traduzione; per le funzioni dinamiche (filtri, ricerca, stato calcolato dalla data) lo script produce anche `data/progetti.js`, caricato con un normale `<script>`;
  - tutti i link puntano a file espliciti (`progetti.html`, `it/index.html`), mai a cartelle, perché da `file://` una cartella non apre `index.html`;
  - la conservazione dei dati del modulo usa `sessionStorage` (funziona anche da `file://`).
- Il sito funzionerà comunque anche con un server locale e su GitHub Pages.

### D-02 · Versione desktop obbligatoria e numero di pagine · proposta
- `Istruzioni.md` §4 richiede la **versione desktop** e, per un gruppo di 4, **almeno 10 pagine distinte** per contenuti o funzioni. Il prompt chiede una progettazione mobile first: le due cose sono compatibili. Il sito sarà mobile first ma la verifica principale sarà a 1280 px; le pagine distinte previste sono elencate in `06_architettura.md` (Fase 2).

### D-03 · Stack · proposta
- HTML5 semantico, CSS e JavaScript senza framework né CDN; uno script di build in Python con la sola libreria standard (`tools/build.py`) genera le pagine `it/` ed `en/` da modelli, dati e traduzioni. Le pagine generate sono versionate, così chi apre lo zip non deve eseguire nulla.
- Motivo: evita la duplicazione tra italiano e inglese (requisito R-110) e mantiene i numeri coerenti da un'unica fonte (R-131), rispettando D-01. Le pagine restano leggibili senza JavaScript (R-135).
- Da definire nella Fase 2: se la pagina iniziale sarà `index.html` nella radice con l'italiano (e l'inglese in `en/`) o un `index.html` di ingresso che rimanda a `it/index.html`.

## Fonti e loro uso

### D-04 · Versione di riferimento di personas e journey · proposta
- Si usano `assignment2/personas/personas/*.html` e `assignment2/personas/journey/*.html`: sono le uniche cartelle complete; le copie di Alex (`assignment2/alex/output/html/`) sono identiche byte per byte. Dettagli in `01_inventario_fonti.md` §5.
- P07–P09 sono in **v1** (citano IdeaGinger e le chiavi `Sxx`), P10–P12 in **v2** con decisioni ancora aperte (`da_rivedere_P10-P12.md`). Il sito tiene conto di tutti i punti di dolore; per **P12** si adotta la versione v2 (partner esterna che chiede un contatto), che richiede una sezione «enti esterni» e un modulo «Proponi una collaborazione» (R-076). **Da confermare dal gruppo**, perché la v2 di P12 non è ancora approvata (§2.2 del file di revisione).

### D-05 · Consolidamento dei problemi e scala di gravità · proposta
- La presentazione di gruppo (`assignment1_gruppoA.pdf`) è la fonte consolidata; le parti individuali sono state confrontate con essa e i doppioni uniti (90 problemi, `02_problemi_consolidati.md`).
- Le scale non coincidono (GA: 3 = importante, 4 = grave; alex: 3 = grave, 4 = critico; andre usa anche 5). Regola adottata: gravità consolidata = valore della slide di GA, se esiste; altrimenti il massimo dei valori validi; i valori fuori scala sono riportati ma non usati.

### D-06 · Chiavi X01–X08 del catalogo C00 · proposta
- Le chiavi `Xxx` non hanno una slide. Per ognuna è stata cercata la fonte nei file di assignment1; **X03** («anche con l'anonimato il promotore riceve nome ed email») non compare in nessun file: resta come problema P-056 con fonte «solo C00» e il sito lo tratta come informazione **[DA VERIFICARE]**.

### D-07 · Pagina 404 nelle fonti · confermata
- Il prompt dice che la valutazione ha trovato errori 404 «dalle pagine FAQ e Come funziona». Le fonti dicono un'altra cosa: la 404 è stata ottenuta **digitando un indirizzo sbagliato** (`/faqs.html`, `assignment1/lorenzo/Pagina_FAQ.md:130`), non seguendo link rotti. Il requisito resta (R-014, R-015), con questa precisazione.

## Contenuti istituzionali (segnaposto)

### D-08 · Nome della piattaforma · proposta
- `NOME_PIATTAFORMA` è «[da definire]». Proposta: **«Sostieni la Ricerca»**, nome descrittivo e neutro, uguale in italiano e in inglese (un solo nome del marchio, R-013), con il sottotitolo «Il crowdfunding per i progetti di ricerca dell'Università di Torino» / «Crowdfunding for research projects at the University of Turin». Non è il nome di IdeaGinger né del programma reale. **Da confermare.**

### D-09 · Nome del programma con l'Ateneo · proposta
- Il programma reale si chiama «Funds TOgether». Per non presentare come reali informazioni inventate (date, importi) sotto il nome di un'iniziativa vera, il sito usa un nome descrittivo: **«Programma di cofinanziamento dell'Ateneo»** (voce di menu «Il programma dell'Ateneo»; in inglese «University co-funding programme»), con una nota che dichiara che il prototipo si ispira a Funds TOgether. **Da confermare.**

### D-10 · Regola del cofinanziamento · proposta
- Documentato nelle fonti: «Se una campagna raggiunge l'obiettivo, l'Ateneo raddoppia i fondi fino a 10.000 €» (`valutazione_antofallea.pdf` p. 32, schema di riprogettazione che riprende la pagina partner); in Mind the Climate l'obiettivo è 7.000 € nel riquadro e 14.000 € nel testo (`Pagina_MindTheClimate.md:32, :49`), coerente con un raddoppio dell'obiettivo.
- Interpretazione adottata: **se la raccolta raggiunge l'obiettivo, l'Ateneo aggiunge una somma pari all'obiettivo, fino a un massimo di 10.000 € per progetto; le donazioni oltre l'obiettivo non vengono raddoppiate e vanno al secondo obiettivo**. Nel sito la regola è marcata **[DA VERIFICARE con l'Ateneo]**, in particolare il caso oltre il 100% (dubbio esplicito di P10).

### D-11 · Donazione libera: nome e minimo · proposta
- Fonti: «FAI TU» con minimo 5 € in Mind the Climate (`Pagina_MindTheClimate.md:60`, scheda progetto); nel checkout MILK-ACT il minimo è legato alla ricompensa (15 €). Scelta: **«Donazione libera»** con minimo **5 €** uguale in tutti i progetti (R-037).

### D-12 · Metodi di pagamento e commissioni · proposta
- Metodi osservati nel checkout reale: PayPal o carta, Satispay, bonifico (`problemi_antofallea.csv` P03); «PayWay» compare solo nelle FAQ ed è un nome tecnico (P-062). Scelta: un unico elenco con nomi comprensibili: **Carta di credito, debito o prepagata · PayPal · Satispay · Bonifico bancario**, definito una sola volta nei dati.
- Commissioni: le fonti riportano quelle di IdeaGinger (PayPal 1,8% + 0,35 €, `Pagina_FAQ.md:74`) e il fatto che in caso di rimborso le spese di transazione vengono trattenute (`Pagina_FAQ.md:84`). Il prototipo mostra nel riepilogo una **commissione stimata** con queste percentuali, dichiarata come esempio, e la frase sul rimborso, entrambe **[DA VERIFICARE]**.

### D-13 · Visibilità del nome e dati al team · proposta
- Due scelte obbligatorie senza preselezione (R-054). Per spiegare che cosa riceve il team si scrive: «Il gruppo di ricerca riceve nome ed email per inviarti la ricompensa e ringraziarti [DA VERIFICARE con l'Ateneo]», perché X03 non è documentato (D-06).

### D-14 · Ricevuta e detraibilità · proposta
- Le fonti dicono solo che l'informazione manca (`Pagina_FAQ.md:139`). Il sito spiega che dopo la donazione si riceve una conferma via email con il riepilogo e che ricevuta fiscale e detraibilità sono **[DA VERIFICARE con l'Ateneo]**.

### D-15 · Costi per il promotore · proposta
- Documentato: quota di 350 € + IVA per pubblicare una campagna generica su IdeaGinger (`assignment1_gruppoA.pdf` s49); non si sa se vale per i progetti selezionati dall'Ateneo (dubbio di P09 in J09). Il sito mostra il riquadro «Quanto costa» con **[DA VERIFICARE con l'Ateneo]** e nessuna cifra inventata.

### D-16 · Date, orari e contatti · proposta
- Data di sviluppo: 31/10/2026. Le campagne dell'edizione 2026 sono in corso con scadenze a novembre–dicembre 2026, come quelle reali osservate (scadenze 10–18/11/2026 in assignment1). Le date di candidatura della prossima edizione sono **[DA VERIFICARE]**.
- Contatti fittizi sul dominio riservato `example.org` (es. `crowdfunding@example.org`, telefono `+39 011 000 0000`), con orari scritti in un solo punto dei dati (P-080).
- I giorni rimanenti sono calcolati nel browser dalla data corrente; il testo generato dallo script (per chi non ha JavaScript) usa la data di generazione e lo dichiara.

## Ambito

### D-17 · Niente account né area riservata · proposta
- `Istruzioni.md` §4: non sono richiesti account reali. La «registrazione simulata» del prompt diventa un **modulo di candidatura al programma** (per ricercatori UniTo, P09) e un modulo **«Proponi una collaborazione»** (per enti esterni, P12), entrambi simulati. I requisiti sulla password del prompt non si applicano perché non c'è una password; se il gruppo vuole una registrazione con password, il modulo seguirà R-077 e indicherà i requisiti della password prima del campo.

### D-18 · Elenco senza «Carica altri» · proposta
- Con 10–14 progetti l'elenco li mostra tutti insieme, con il conteggio «Mostrati N di M progetti» aggiornato dai filtri (R-025). La paginazione è prevista solo se i progetti superano i 24.

### D-19 · Git · confermata
- Commit locali piccoli e descrittivi su un branch locale dedicato (`assignment2-sito`), creato a partire da `assignment1-valutazione-euristica`; nessun push.
