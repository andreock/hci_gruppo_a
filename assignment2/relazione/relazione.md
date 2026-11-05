---
Titolo: Relazione sulla realizzazione del sito di crowdfunding ideaBlume
Sottotitolo: Come abbiamo costruito e rivisto le personas, user journey e sito di crowdfunding per la ricerca
Gruppo: Gruppo A
Componenti: Andrea Canale · Antonio Fallea · Alexandru Ioan Chindris · Lorenzo Rizzolo
Corso: Human-Computer Interaction · a.a. 2026/27
Data: 3 novembre 2026
Sito pubblicato: https://andreock.github.io/hci_gruppo_a/
---

[[INDICE]]

## Introduzione

Con assignment 2 abbiamo progettato **ideaBlume**, un sito di crowdfunding per i progetti di ricerca dell'Università di Torino, ripartendo dalla valutazione euristica di IdeaGinger svolta in assignment 1 e sulla base dell'iniziativa Funds TOgether. Il lavoro ha avuto due fasi: prima 12 proto-personas per un servizio generico di crowdfunding e 12 user journey, che mostrano le difficoltà su IdeaGinger (As-is) e i miglioramenti su ideaBlume (To-be), poi un sito statico di 17 tipi di pagina in italiano e in inglese.

Il sito è stato creato mettendo nel contesto dell'IA, oltre alle personas e agli user journey, anche le problematiche relative al sito che abbiamo trovato nell'assignment 1.

Il sito è pubblicato su https://andreock.github.io/hci_gruppo_a/.

## Le personas

Dopo l'analisi di IdeaGinger abbiamo costruito 12 **proto-personas** pensate per un **servizio generico di crowdfunding**, non per IdeaGinger: descrivono persone con obiettivi ed esigenze proprie, e i problemi trovati nella valutazione euristica entrano come loro difficoltà, senza citare il sito. P10–P12 restano generiche nei bisogni, ma sono collocate sul sito di crowdfunding dell'Ateneo. Le personas non derivano da interviste o osservazioni con utenti, ma dallo studio dei potenziali utenti del servizio. Riportiamo il testo delle schede compilate sui template del corso, con un'impaginazione uniforme. Dati, nomi e scenari sono fittizi. La matrice che ne mostra la differenziazione è in §5.6.

<!-- Le schede non hanno tutte lo stesso grado di maturità, e lo dichiariamo: P01–P06 descrivono un'app di crowdfunding generica; P07–P09 sono state riviste il 31/10/2026 ma nominano ancora Funds TOgether, e hanno una struttura leggermente diversa; P10–P12 descrivono il nuovo sito dell'Università di Torino. I motivi sono in §5.8. -->

[[INCLUDI schede/personas.md]]

## Gli user journey

Ogni persona ha un journey di sei fasi, che considera anche ciò che avviene prima e dopo l'uso del sito. La riga «Emozioni e loro base» usa punteggi da −2 a +2, tutti ipotizzati.

Abbiamo costruito i journey sulle personas, seguendo questo ordine:

- **Punto di partenza: IdeaGinger.** L'analisi di assignment 1 ha fornito i problemi di usabilità e di accessibilità del sito esistente.
- **Personas generiche.** A partire da quei problemi abbiamo definito persone che userebbero un generico servizio di crowdfunding.
- **J01–J09, journey As-is: le difficoltà su IdeaGinger.** Mostrano che cosa incontrerebbero queste persone usando il servizio così com'è. Le schede lo indicano come «servizio generico» e non nominano IdeaGinger, per coerenza con le personas, ma le criticità sono quelle riscontrate su IdeaGinger. Le righe «Criticità» e «Opportunità» sono diventate un punto di partenza per ideaBlume.
- **J10–J12, journey To-be: i miglioramenti su ideaBlume.** Mostrano il percorso sul sito realizzato, con una riga in più che confronta ogni fase con IdeaGinger. Le righe «Criticità» e «Opportunità» riportano ciò che resta da migliorare.

Il confronto si vede nelle emozioni: le curve As-is scendono fino a −2 nei momenti critici, mentre in J10–J12 i livelli di soddisfazione sono medio-alti, da +1 a +2. Questi livelli sono attesi e non misurati, perché il sito non è stato provato con utenti reali.

[[INCLUDI schede/journeys.md]]

## Panoramica degli strumenti

Abbiamo usato **Claude Code e Codex in tutto il progetto**. La tabella riporta le attività e che cosa risulta dalla nostra documentazione.

Tabella: Strumenti e attività
| Strumento | Fase | Attività | Che cosa risulta |
|---|---|---|---|
| Codex (OpenAI Codex, modello GPT-5) | {{Personas}} {{Journey}} | Generazione e revisione di P01–P03 e J01–J03, controllo di coerenza, schede HTML | Documentato nelle nostre note sulle revisioni |
| Claude Code (Claude Opus 5.5) | {{Personas}} {{Journey}} | Compilazione di P10–P12 e J10–J12, confronto con la consegna | Documentato |
| Claude Code e Codex | {{Personas}} {{Journey}} | P04–P09 e J04–J09 |  |
| Claude Code (Claude Opus 5.5) | {{Journey}} | Revisione di J07–J09 e J10–J12 del 05/11/2026, dopo la realizzazione del sito | Documentato |
| Claude Code (Claude Opus 5.5) | {{Sito}} | Inventario delle fonti, requisiti, architettura, codice, verifiche, tracciabilità | Documentato |
| Codex | {{Sito}} | [Abbiamo usato Codex per fargli scrivere il codice del sito,e per vari raffinamenti.] | Dichiarato dal gruppo |
| Script scritti con l'agente | {{Sito}} | axe-core, Lighthouse, Playwright, controlli su contrasti, link e dati | Risultati nelle verifiche del sito |

:::html
<figure class="flusso">
<svg viewBox="0 0 760 190" role="img" aria-labelledby="flusso-t flusso-d" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">
<title id="flusso-t">Flusso di lavoro con l'IA</title>
<desc id="flusso-d">Le fonti del gruppo alimentano i prompt; i prompt producono gli output dell'IA; il gruppo li rivede e ottiene la versione finale. Dalla revisione una freccia torna ai prompt con le richieste di modifica.</desc>
<defs><marker id="fr" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#3b1d2a"/></marker></defs>
<g font-size="12.5" fill="#3b1d2a">
<rect x="4" y="30" width="132" height="92" rx="6" fill="#fbf6ee" stroke="#3b1d2a"/><text x="70" y="52" text-anchor="middle" font-weight="700">Fonti del gruppo</text><text x="70" y="72" text-anchor="middle" font-size="10.5">relazione 1, appunti,</text><text x="70" y="87" text-anchor="middle" font-size="10.5">template, consegna,</text><text x="70" y="102" text-anchor="middle" font-size="10.5">personas per il sito</text>
<rect x="160" y="30" width="132" height="92" rx="6" fill="#fbf6ee" stroke="#3b1d2a"/><text x="226" y="52" text-anchor="middle" font-weight="700">Prompt</text><text x="226" y="72" text-anchor="middle" font-size="10.5">C00, Pxx, Jxx, V00</text><text x="226" y="87" text-anchor="middle" font-size="10.5">SITO-01 e richieste</text><text x="226" y="102" text-anchor="middle" font-size="10.5">ai checkpoint</text>
<rect x="316" y="30" width="132" height="92" rx="6" fill="#e2eff4" stroke="#1d5b73"/><text x="382" y="52" text-anchor="middle" font-weight="700">Output dell'IA</text><text x="382" y="72" text-anchor="middle" font-size="10.5">bozze, codice,</text><text x="382" y="87" text-anchor="middle" font-size="10.5">documenti e proposte</text><text x="382" y="102" text-anchor="middle" font-size="10.5">Claude Code, Codex</text>
<rect x="472" y="30" width="132" height="92" rx="6" fill="#fbeadd" stroke="#bf4a12" stroke-width="1.6"/><text x="538" y="52" text-anchor="middle" font-weight="700">Revisione del gruppo</text><text x="538" y="72" text-anchor="middle" font-size="10.5">note, scelte ai</text><text x="538" y="87" text-anchor="middle" font-size="10.5">checkpoint, verifiche</text><text x="538" y="102" text-anchor="middle" font-size="10.5">e ritocchi a mano</text>
<rect x="628" y="30" width="128" height="92" rx="6" fill="#e3f2e6" stroke="#24603f"/><text x="692" y="60" text-anchor="middle" font-weight="700">Versione finale</text><text x="692" y="82" text-anchor="middle" font-size="10.5">schede e sito</text><text x="692" y="97" text-anchor="middle" font-size="10.5">pubblicato</text>
</g>
<g stroke="#3b1d2a" stroke-width="1.6" fill="none">
<path d="M136 76 H157" marker-end="url(#fr)"/><path d="M292 76 H313" marker-end="url(#fr)"/><path d="M448 76 H469" marker-end="url(#fr)"/><path d="M604 76 H625" marker-end="url(#fr)"/>
<path d="M538 122 V160 H226 V125" marker-end="url(#fr)" stroke-dasharray="5 3"/>
</g>
<text x="382" y="178" text-anchor="middle" font-size="11" fill="#3b1d2a">richieste di modifica: più iterazioni, documentate solo in parte</text>
</svg>
<figcaption><b>Figura {FIG}.</b> Il flusso di lavoro seguito in entrambe le fasi.</figcaption>
</figure>
:::

## Fase 1 · Uso dell'IA per personas e user journey

### Strumenti e attività

Abbiamo generato ogni persona e ogni journey in una conversazione separata, lavorando in parallelo. Gli strumenti hanno prodotto le schede e, per P01–P03, anche il generatore delle schede HTML. Il gruppo ha fornito il catalogo dei problemi e i template, ha controllato gli output e ha chiesto le modifiche.

### Prompt principali e informazioni fornite

**Informazioni fornite.** Abbiamo dato agli strumenti la relazione di assignment 1 sotto forma di catalogo dei problemi, i nostri appunti del corso, i due template ufficiali e una scheda vincolante per ogni persona.

**Perché questa struttura.** Dovendo lavorare in parallelo, abbiamo separato un contesto comune da un prompt singolo per documento: così più persone del gruppo potevano generare i documenti, ciascuna nella propria conversazione, ottenendo la stessa struttura. I 26 prompt sono C00, una coppia Pxx e Jxx per persona, e il prompt di verifica V00. Il tag `<persona_generata>` di ogni Jxx permette di incollare la persona già pronta, per tenere allineato il journey. I tratti che non dovevano cambiare (età, dispositivo, familiarità, accessibilità, frequenza) sono fissati nella `<scheda_vincolante>`.

:::prompt | Prompt · C00, contesto comune (estratto) | {{Personas}} {{Journey}} · versione 3
Il gruppo sta producendo 12 personas (P01–P12) e 12 journey map (J01–J12) per una GENERICA app di crowdfunding (sito web e versione mobile). Ogni documento viene generato da una persona diversa in una conversazione separata: per questo tutti i documenti devono seguire esattamente gli stessi formati, definiti più sotto.
[…]
4. Non inventare dati presentati come reali (statistiche, URL, citazioni). Se aggiungi comportamenti dell'app non previsti dal catalogo, marcali con [IPOTESI].
[…]
6. Le esigenze di accessibilità vanno descritte con rispetto e precisione (strumenti usati, strategie), senza pietismo e senza stereotipi.
:::

:::prompt | Prompt · P01, indicazioni specifiche (estratto) | {{Personas}} · versione 3
- Il suo modello mentale della donazione è l'offerta o il bonifico: si aspetta di dare una somma, non di scegliere una «ricompensa».
- Mostra le sue strategie: chiede conferma alla figlia per telefono, fotografa lo schermo, preferisce chiamare un numero di assistenza. Non descriverlo come incapace: è un ex insegnante curioso e attento.
:::

:::prompt | Prompt principale di P01–P03 | {{Personas}} {{Journey}}
Genera e raffina la scheda della proto-persona indicata usando esclusivamente i campi del template ufficiale. Mantieni invariati età, ruolo, dispositivo, familiarità digitale, accessibilità e frequenza. Trasforma i problemi assegnati in esperienze personali, senza citare ID interni o servizi reali. Costruisci poi un journey as-is coerente, con azioni, touchpoint, pensieri, emozioni motivate, barriere e opportunità concrete. Segnala come ipotesi tutto ciò che non deriva dal catalogo.
:::

**Come è cambiato il contesto comune.** Il 27/10/2026 abbiamo riscritto C00 due volte. Con la prima revisione abbiamo reso vincolanti i template del corso, con una tabella `<corrispondenze>` tra gli appunti e i campi. Con la seconda abbiamo tolto ogni riferimento al sito valutato.

:::confronto
:::prima | Prima versione | C00, regola 1, 27/10/2026
«Fai emergere tutti i problemi elencati nel prompt singolo, ciascuno citato almeno una volta nel formato [Sxx · criterio · Gx] (es. [S17 · H4 · G4], [S59 · LG1 · G4], [S74 · prestazioni]) o [X0n · analisi preliminare, da verificare]. […]»
:::
:::dopo | Versione finale | C00, regola 1, versione 3
«GENERICITÀ ASSOLUTA. Non nominare mai piattaforme, app, siti, enti, università, programmi o progetti reali, né marchi. Non citare la valutazione del gruppo, slide, euristiche numerate, gravità o gli ID del catalogo (Sxx, Xxx). […]»
:::
:::cambio
Le personas non descrivono più l'interfaccia di IdeaGinger ma persone con esigenze proprie; il legame con la valutazione resta nelle chiavi interne dei prompt. 
:::
:::

### Dalla prima versione alla versione finale

:::confronto
:::prima | Prima versione · P01 {{Personas}} | Citata nella nostra documentazione delle revisioni (output grezzo non salvato)
«Giuseppe è poco capace con la tecnologia.»
:::
:::dopo | Versione finale · P01 {{Personas}} | Scheda P01, §2
«Sa cercare informazioni e confrontarle, ma non riconosce sempre le convenzioni dei moduli online.» «Si insospettisce se non comprende subito che cosa offre un sito.» Frase rappresentativa: «Aiuto volentieri, ma prima voglio capire dove vanno i soldi.»
:::
:::cambio
Abbiamo giudicato la prima formulazione «stereotipata e centrata sul deficit» e abbiamo chiesto di «descrivere competenze, strategie e contesto; attribuire le difficoltà all'interfaccia». Giuseppe è passato da «anziano inesperto» a ex insegnante curioso e prudente.
:::
:::

:::confronto
:::prima | Prompt e prima versione salvata · P12 {{Personas}} | Prompt iniziale e prima scheda, 27/10/2026
Prompt: «Città: Forlì»; «promotrice esterna a UniTo; vuole lanciare la prima campagna dell'associazione su Ginger».

Prima scheda: Torino; «una volontaria le manda su WhatsApp il link di Ginger»; «[S49 · H5 · G4] Trova in fondo a un paragrafo la quota di 350 € + IVA e si allarma».
:::
:::dopo | Versione finale · P12 {{Personas}} | Scheda P12, versione 2, §2
«Esterna all'Università: non può proporre una campagna da sola, ma vuole costruire un progetto insieme a un gruppo di ricerca UniTo [IPOTESI].» «Si allarma quando scopre i costi tardi o scritti in piccolo: “che cos'altro non mi hanno detto?”.»
:::
:::cambio
Il sito è dedicato alle campagne dell'Ateneo: lì una campagna lanciata in autonomia non esiste, e una ricercatrice UniTo sarebbe stata quasi uguale a P09. Maria resta esterna e segue il percorso «contatto», mentre Chiara segue la candidatura. La versione 2 toglie i riferimenti a IdeaGinger.
:::
:::

:::confronto
:::prima | Prima versione · P07 {{Personas}} | Versione 1, 27/10/2026
«[S59 · LG1 · G4] La homepage non spiega che cos'è Ginger: teme di essere sul sito sbagliato.» «[S64 · LG6 · G3] Titoli troncati e stato “Per ispirarti” ambiguo.»
:::
:::dopo | Versione rivista · P07 {{Personas}} | Versione 2, 31/10/2026, §2
«Se la pagina iniziale non chiarisce lo scopo dell'iniziativa, teme di essere nel posto sbagliato.» «Trova faticosi titoli incompleti, etichette ambigue e parole inglesi non spiegate.»
:::
:::cambio
La revisione porta le difficoltà dall'interfaccia alla persona. È però **arrivata tardi**: il sito è stato costruito sulla prima versione di P07–P09, e J07–J09 sono stati allineati solo il 05/11/2026, a sito già realizzato.
:::
:::

### Problemi individuati negli output

Tabella: Problemi trovati negli output di personas e journey
| Problema nell'output | Come ce ne siamo accorti | Richiesta o intervento | Esito |
|---|---|---|---|
| {{Personas}} P01: «Giuseppe è poco capace con la tecnologia» | Revisione: stereotipo, centrato sul deficit | Descrivere competenze e strategie; difficoltà attribuite all'interfaccia | Corretto |
| {{Personas}} P03: «Davide ha bisogno di un sito semplice» | Revisione: paternalistico | Specificare navigazione per H, landmark, elenco link, sintesi ad alta velocità | Corretto |
| {{Journey}} J01: «La pagina è confusa» | Revisione: generico, non osservabile, senza soluzione | Esplicitare percentuali oltre il 100%, giorni negativi, apertura inattesa dei link | Corretto |
| {{Journey}} J03: «Non vede il pallino rosso» | Revisione: descrizione visiva impropria per chi usa uno screen reader | Descrivere lo stato non annunciato e il golfo della valutazione | Corretto |
| {{Personas}} {{Journey}} P10–P12: mancavano bisogni informativi, fiducia, familiarità con il crowdfunding, obiettivo e informazioni per fase | Confronto con la consegna | Aggiunte righe e sottogruppi | Corretto per P10–P12; decisione generale rimasta aperta (§5.8) |
| {{Personas}} P10: «ogni euro vale doppio» contraddiceva la regola del cofinanziamento | Revisione delle schede | Motivazione e dubbio riformulati | Corretto |
| {{Personas}} P12: due affermazioni sul sito assenti dalla presentazione (FAQ, logo UniTo) | Confronto con la presentazione | Rimosse | Corretto |
| {{Personas}} P10, P11: fiducia del promotore confusa con quella dei donatori | Revisione delle schede | Ogni voce dice di chi è la fiducia | Corretto |
| {{Personas}} P12: aiuto del figlio e ansia, possibile stereotipo; dati familiari inutili in P10–P12 | Revisione delle schede | Ridotto a strategia di accessibilità; dati rimossi | Corretto |
| {{Journey}} J07–J09: IdeaGinger e riferimenti alle slide | Controllo rispetto alla regola 1 di C00 | Riscritti come J01–J06: nessun codice di slide, criticità in frasi complete, servizio generico | Corretto |
| {{Journey}} J10–J12: descrivevano criticità ancora da risolvere, con emozioni fino a −2 | Confronto con il sito realizzato | Riscritti sul percorso reale di ideaBlume, con confronto con IdeaGinger e criticità residue | Corretto |

Il prompt V00 prevedeva sette criteri, tra cui fedeltà e rispetto (Appendice A), ma era facoltativo. Prompt usato per revisionare la relazione, in modo tale da ottenere un opinione critica e basata su criteri predefiniti nel prompt.

### Richieste di modifica e interventi

Abbiamo fatto tre tipi di intervento.

- **Revisioni dei prompt, prima di generare.** Abbiamo allineato C00 ai template e poi lo abbiamo reso generico: sono interventi sulle istruzioni date all'IA, non sui singoli output.
- **Richieste di revisione sugli output.** Per P01–P03 e J01–J03 abbiamo fatto sei richieste, una per documento. Per esempio, per P02: «Rendere visibili pause, una mano, interruzione e ripresa serale». Un controllo finale ha verificato la coerenza tra persona e journey.
- **Riscritture di una versione già salvata.** Il 27/10/2026 P10–P12 e J10–J12 sono passati in poche ore dal servizio esistente al nuovo sito, e i journey sono diventati To-be. Il 05/11/2026, a sito finito, abbiamo chiesto di togliere i riferimenti alle slide da J07–J09 e di far riflettere a J10–J12 «i miglioramenti che sono stati fatti in ideaBlume rispetto ad ideaGinger».


### Come abbiamo reso le personas più specifiche, differenziate e coerenti

**Specificità.** Abbiamo sostituito i tratti generici con comportamenti osservabili. Davide non ha bisogno di «un sito semplice»: usa NVDA con H, landmark ed elenco dei link. Gli scenari vaghi («nelle ultime settimane…») sono diventati momenti concreti: Franco ha tre minuti, un martedì tra una seduta di laurea e il consiglio di dipartimento, e tre email di donatori da leggere.

**Differenziazione.** La matrice è stata decisa prima di generare, nella scheda vincolante di ogni prompt. Copre 8 donatori o visitatori e 4 promotori, 6 donne e 6 uomini, 20–71 anni. Le differenze riguardano obiettivi ed esigenze, non solo nome ed età, come chiede la consegna.

Tabella: Matrice delle personas nella versione usata per il sito
| ID | Persona | Ruolo | Dispositivo | Fam. digitale | Esigenza o contesto |
|---|---|---|---|---|---|
| P01 | Giuseppe, 71 | Donatore, prima volta | Tablet Android 10" | 2/5 | Presbiopia, tocchi imprecisi |
| P02 | Sara, 34 | Donatrice occasionale | Android di 4 anni, 4G debole; laptop | 3/5 | Pause brevi, una mano, attenzione divisa |
| P03 | Davide, 39 | Donatore | PC con NVDA; iPhone con VoiceOver | 5/5 con tecnologie assistive | Cieco dalla nascita |
| P04 | Tomás, 31 | Donatore dall'estero | Laptop, Android | 5/5 | Italiano A2, inglese C1 |
| P05 | Luca, 52 | Donatore metodico | PC desktop 24" | 3/5 | Deuteranopia |
| P06 | Elena, 58 | Attenta a fiducia e privacy | PC con due monitor | 4/5 | Occhiali progressivi, ingrandisce |
| P07 | Giulia, 20 | Studentessa, piccolo importo | iPhone, Safari | 4/5 social, 2/5 moduli | Dislessia, lettura vocale |
| P08 | Roberta, 47 | Giornalista scientifica | Laptop, molte schede | 5/5 | Ricerca esaustiva, interruzioni |
| P09 | Chiara, 32 | Ricercatrice che si candida | MacBook, iPhone | 4/5 | Tempo frammentato |
| P10 | Franco, 63 | Responsabile di campagna | PC fisso 27" | 2/5 | Presbiopia lieve, pochi minuti |
| P11 | Amir, 27 | Comunicazione della campagna | Linux, Android | 5/5 | Usa la tastiera, italiano B2 |
| P12 | Maria, 49 | Partner esterna | Android, vecchio PC | 2/5 | Tremore lieve alle mani |

Due casi mostrano dove la differenziazione è stata corretta dopo la generazione. P12 si distingue da P09 per il percorso «contatto». P10 e P11 erano entrambi promotori nella stessa fase: nella versione 2 Franco arriva fino al resoconto ai donatori, che copre anche il percorso «Seguire un progetto già sostenuto», mentre Amir cura diffusione e pubblico internazionale.

**Coerenza.** La scheda vincolante mantiene costanti i dati principali tra persona e journey. Dove una persona contraddiceva una regola, abbiamo corretto il testo: è il caso di P10 e del raddoppio. Resta un'incoerenza non risolta tra prompt e output: il prompt di P12 descrive ancora Forlì e il lancio di una campagna, mentre la scheda finale descrive una partner a Torino.

### Come abbiamo migliorato la corrispondenza tra journey e personas

:::confronto
:::prima | Prima versione · J03 {{Journey}} | Citata nella nostra documentazione delle revisioni
«Non vede il pallino rosso.»
:::
:::dopo | Versione finale · J03 {{Journey}} | Fase 3, §3
«Stato affidato a colore o simbolo; ricompense e importo restano attivi nella campagna conclusa.» Opportunità: «Etichetta “Campagna conclusa” annunciata; controlli di donazione disabilitati e spiegazione dell'esito.»
:::
:::cambio
Il journey ora usa il modo di interagire di Davide: la barriera è lo stato non annunciato, non qualcosa che lui «non vede». Azioni e touchpoint nominano tastiera e NVDA in ogni fase sul sito.
:::
:::

:::confronto
:::prima | Prima versione salvata · J10 {{Journey}} | 27/10/2026, As-is, base Mista
Fase 1: «Controllo della pagina pubblica e della card». Fase 6: «Chiusura della campagna e rendicontazione», con la fine del percorso «rendicontazione con l'ufficio comunicazione». Azione: «Risponde a email e telefonate di donatori che non riescono a contattarlo dal sito».
:::
:::dopo | Versione finale · J10 {{Journey}} | Versione 3, To-be, base Ipotesi, §3
Fase 1: «Controllo della pagina pubblica». Fase 6: «Resoconto ai donatori». Azione: «Due mesi dopo scrive con il dottorando il resoconto, con spese e foto degli apiari; l'ufficio lo pubblica e lo invia ai sostenitori». Fase 2: da «Preoccupazione (−2)» a «Sollievo (+1) · il successo non sembra più una chiusura».
:::
:::cambio
Il percorso rispetta la persona: Franco delega le attività tecniche e ha pochi minuti, quindi il resoconto passa dal dottorando e dall'ufficio. La versione 3 descrive il sito realizzato: le opportunità della versione 2 sono diventate elementi di ideaBlume, una nuova riga le confronta con IdeaGinger e criticità e opportunità riportano ciò che resta da migliorare.
:::
:::

Tabella: Altri adattamenti del journey alle caratteristiche della persona
| Journey | Caratteristica della persona | Intervento |
|---|---|---|
| {{Journey}} J01 | Tablet, modello mentale dell'offerta, ricorso alla figlia | La curva scende su comprensione e pagamento e risale con conferma e contatto umano; «La pagina è confusa» diventa dati osservabili |
| {{Journey}} J02 | Pausa breve, rete debole, una mano | Da «Riprende sul laptop» a percorso multicanale; dati da reinserire marcati `[IPOTESI]`; abbandono legato a lentezza ed errore tardivo |
| {{Journey}} J12 | Tremore, ansia da moduli, decide dopo aver parlato con qualcuno | La registrazione è sostituita dal modulo «Proponi una collaborazione», seguito dalla telefonata dell'ufficio e dal direttivo |
| {{Journey}} J07–J09 | Piccola donazione da iPhone; ricerca esaustiva con interruzioni; candidatura in più sere | Codici delle slide sostituiti da difficoltà descritte per esteso, nel contesto di ciascuna persona |
| {{Journey}} J10–J12 | Pochi minuti (Franco); tastiera e pubblico estero (Amir); tremore e bisogno di parlare con qualcuno (Maria) | Le emozioni salgono a livelli medio-alti dove il sito risolve il problema; restano le criticità di ciascuno, come le tendine del modulo per Maria |

### Motivazioni delle scelte finali

- **Dodici personas invece di cinque.** Il minimo per quattro persone è 5. Le 12 personas sono costruite per far emergere i problemi di assignment 1. Il rischio è una maturità disomogenea, che si è verificata.
- **Proto-personas dichiarate.** Non derivano da ricerca con utenti, e le schede lo riportano.
- **To-be per P10–P12, As-is per gli altri.** I nove journey As-is documentano le difficoltà su IdeaGinger; i tre To-be mostrano, sul sito realizzato, come ideaBlume le affronta. Non abbiamo scritto un To-be per ogni persona: per le altre, la verifica del sito è nel confronto con i punti di dolore.
- **Niente area riservata.** Il prototipo non prevede account, quindi gli aggiornamenti passano da un ufficio d'Ateneo, marcato `[IPOTESI]`.


## Fase 2 · Uso dell'IA per il sito

### Strumenti e attività

Abbiamo costruito il sito per fasi, con checkpoint in cui il gruppo ha confermato o cambiato le proposte dell'agente.

Tabella: Fasi di lavoro del sito (31/10–03/11/2026)
| Fase | Attività dell'agente | Controllo del gruppo |
|---|---|---|
| Fonti e requisiti | Inventario delle fonti, 90 problemi consolidati, bisogni, 102 requisiti, 19 decisioni proposte | Checkpoint 1: conferma con indicazioni (§6.5) |
| Architettura | Mappa del sito, design system, controllo dei contrasti | Checkpoint 2: date delle campagne |
| Implementazione | 58 pagine statiche, donazione in 5 passi | — |
| Verifiche | Script di verifica e correzioni | — |
| Chiusura | Verifica con le personas, valutazione euristica, tracciabilità | — |
| Redesign | Nuovo aspetto grafico | Richiesta di «un design più moderno» |
| Versione finale | Palette calda, tema, contenuti definitivi | Richieste del gruppo; ritocchi a mano (§6.7) |

### Prompt principali e informazioni fornite



:::prompt | Frammenti del prompt citati nel registro delle decisioni | {{Sito}}
il prompt chiede un sito statico «consultabile con un semplice server locale» e dati letti da `data/progetti.json`
[…]
Il prompt dice che la valutazione ha trovato errori 404 «dalle pagine FAQ e Come funziona».
:::

**Informazioni fornite.** L'agente ha ricevuto la presentazione di assignment 1, i registri dei problemi, i report Core Web Vitals, i prompt di personas e journey e tutte le schede. A queste si aggiungono i nostri appunti e i vincoli della consegna: niente server, almeno 10 pagine distinte, versione desktop, nessun account né pagamento reale. Il lavoro è organizzato in una catena tracciabile: problema, requisito, soluzione, verifica.

### Dalla prima versione alla versione finale

#### La grafica

Le tre versioni condividono la struttura; cambiano palette, caratteri e gerarchia.

:::figure2 | stretta
![Home della prima versione: fascia lilla, titolo in nero, pulsanti viola, font di sistema, card sotto la prima schermata.](home-1280-v1.jpg){Versione 1, 31/10/2026. Palette prugna e font di sistema.}
![Home della seconda versione: fondo chiaro violaceo, titolo grande, ricerca arrotondata, scheda di un progetto in evidenza a destra.](home-1280-v2.jpg){Versione 2, 01/11/2026. Inter e Bricolage Grotesque.}
![Home della terza versione: stessa impaginazione su fondo crema, testi prugna bruna, pulsante terracotta, interruttore «Tema scuro».](home-1280-v3.jpg){Versione 3, 03/11/2026. Palette calda e tema a scelta.}
:::

:::cambio
La richiesta di redesign ammetteva framework CSS: Tailwind e Bootstrap sono stati valutati e scartati perché avrebbero richiesto di riscrivere il markup o contrastavano con l'uso senza server. La palette calda è stata una nostra richiesta. Il terracotta è stato scurito finché il bianco non ha raggiunto 5,00:1, contro i 2,46:1 dei titoli arancioni di IdeaGinger. Il prezzo del redesign è misurato: Lighthouse mobile è passato da 100 a 95–98 per le prestazioni.
:::

#### Una funzione: la ricerca

L'agente ha prodotto una prima versione che le verifiche hanno trovato difettosa due volte.

:::diff | Script di ricerca del sito, dalla prima versione alla finale | {{Sito}}
- return parole.every(function (w) { return testo.indexOf(w) >= 0; });
+ // seconda versione: «api» trova «apicoltori», non «capire»
+ var voci = testo.split(/[^a-z0-9]+/);
+ return parole.every(function (w) { return voci.some(function (v) { return v.indexOf(w) === 0; }); });
+ // versione finale: «veterinaria» trova «veterinarie»
+ var r = w.length >= 5 ? w.slice(0, -1) : w;
+ return voci.some(function (v) { return v.indexOf(r) === 0; });
:::

:::cambio
La ricerca per sottostringa dava risultati sbagliati (7 per «api»). Quella per inizio di parola ne dava 2 pertinenti, ma «veterinaria» non trovava «Scienze Veterinarie» (gravità 2). La versione finale tollera singolare e plurale, maschile e femminile.
:::

#### I contenuti: da prototipo dichiarato a sito «definitivo»

:::figure2
![Primo passo della donazione nella versione 1, con il riquadro giallo «Pagamento simulato. Questo è un prototipo didattico» sopra il riepilogo.](donazione-1280-v1.jpg){Versione 1, 31/10/2026. Avviso di pagamento simulato in cima.}
![Primo passo della donazione nella versione 3: titolo, indicatore dei cinque passi e scelta della ricompensa, senza alcun avviso.](donazione-1280-v3.jpg){Versione 3, 03/11/2026. L'avviso non c'è più.}
:::

:::cambio
Su nostra richiesta sono stati tolti avvisi, FAQ «Questo sito è reale?» e 41 segnaposto «[DA VERIFICARE con l'Ateneo]», sostituiti da informazioni stabilite. La pagina è più pulita, ma il sito ha perso la dichiarazione della propria natura: ne discutiamo in §7.
:::

### Problemi individuati negli output

Tabella: Problemi trovati negli output del sito
| Problema nell'output | Come ce ne siamo accorti | Richiesta o intervento | Esito |
|---|---|---|---|
| FAQ: 21 link identici «Link a questa risposta» | Script di controllo dei link | Testo nascosto con la domanda | Corretto |
| CLS 0,30 su elenco e progetto, 0,59 sulla donazione | Lighthouse | Menu nascosto da CSS; spazio riservato | CLS 0 |
| FAQ e progetto senza testi per i messaggi: errori vuoti, modulo inviabile senza controlli | Test dei percorsi | Testi dell'interfaccia separati | Corretto |
| Ricerca: «api» trova «capire»; poi «veterinaria» non trova nulla | Screenshot dei test; valutazione euristica | Due correzioni | Corretto |
| Colonna fissa più alta dello schermo: contatto irraggiungibile | Verifiche tecniche | Colonna non più fissa | Corretto |
| Riquadro del raddoppio senza link alle regole | Valutazione euristica | Aggiunto il link | Corretto |
| Transizioni animate: errori in console | Test dei percorsi | Scartate | Corretto |
| Ripresa della donazione su un altro dispositivo impossibile (J02) | Valutazione euristica | Richiederebbe account, esclusi | **Aperto** |
| Verifica con le personas e valutazione euristica riportano ancora segnaposto e Lighthouse 100 | Rilettura per questa relazione | Da aggiornare | **Aperto** |
| Tre problemi (stato del programma, detraibilità, informazioni per candidarsi) passano da «parziale» a «risolto» senza nuove fonti | Confronto tra le versioni della tracciabilità | Da riconsiderare (§7) | **Aperto** |

### Richieste di modifica e interventi

Il nostro registro delle decisioni distingue le proposte dell'agente dalle scelte del gruppo.

Tabella: Che cosa ha proposto l'agente e che cosa abbiamo deciso
| Tema | Proposta dell'agente | Decisione del gruppo |
|---|---|---|
| Nome | «Sostieni la Ricerca» | **ideaBlume** |
| Pagine | Almeno 10, come da consegna | Almeno 12 |
| Contatti | Dominio `example.org` | Fittizi ma credibili: `@ideablume.it`, numero di Torino |
| Pubblicazione | Sito apribile senza server | Anche pubblicato online |
| Date delle campagne | Date relative a oggi | Confermate al checkpoint 2 |
| Design | Prugna, «lontano dall'arancione» | Prima «più moderno», poi palette calda |
| Tema | Automatico dal sistema | Chiaro predefinito con interruttore |
| Contenuti | Segnaposto e avvisi | Eliminati, informazioni stabilite |

### Revisione di contenuti, struttura, navigazione e interazioni

#### Contenuti

Le informazioni istituzionali non presenti nelle fonti erano inizialmente segnate come da verificare e sono state poi fissate da noi (§7). Il lessico è controllato da uno script: niente gergo, importi in una sola forma. I numeri vengono da un'unica fonte di dati, per evitare l'incoerenza di contatori trovata in assignment 1.

#### Struttura

Il principio guida è «prima i progetti da sostenere, poi le regole, poi i servizi per chi propone», l'opposto di quanto osservato su IdeaGinger. Il programma dell'Ateneo diventa una voce di primo livello. La versione 2 di P12 ha portato a una sezione per enti esterni e al modulo «Proponi una collaborazione»: è un caso in cui la revisione delle personas ha cambiato il sito. La versione inglese è completa, generata dagli stessi modelli; restano in lingua originale solo i commenti dei sostenitori, marcati con `lang`.

#### Navigazione

Il menu passa dalle oltre 70 voci di IdeaGinger a 7 voci senza tendine, con la ricerca sempre visibile e un menu mobile gestibile da tastiera. Tornando dall'elenco, filtri e posizione restano. Su telefono l'intestazione è stata compattata perché andava su tre righe a 375 px.

:::figure2 | stretta
![Home a 375 pixel: intestazione su una riga, ricerca, titolo e frase che spiega il servizio.](home-375.jpg){Home a 375 px.}
![Menu mobile aperto a 375 pixel con le sette voci in un elenco.](menu-mobile-375.png){Menu mobile a 375 px con le 7 voci.}
![Pagina di un progetto a 375 pixel: tema, titolo, gruppo, responsabile e riquadro dello stato.](progetto-375.jpg){Pagina progetto a 375 px.}
:::

#### Interazioni

La donazione è un percorso in 5 passi con validazione all'uscita dal campo, riepilogo degli errori con focus, dati conservati e «Modifica» nel riepilogo. Le campagne concluse non hanno controlli attivi. Il badge «Obiettivo raggiunto · puoi ancora sostenerlo per N giorni» risponde direttamente al dubbio di Franco e Giuseppe.

:::figure2
![Passo 2 della donazione: riquadro rosso con il focus, «C'è 1 campo da correggere», e link al campo Email.](donazione-riepilogo-errori.png){Riepilogo degli errori con focus e correzione proposta.}
![Risultati della ricerca «api»: due progetti pertinenti e anello di focus sulla prima card.](ricerca-api-focus.png){Ricerca «api» da tastiera: 2 risultati e focus visibile sulla card.}
:::

### Modifiche apportate direttamente al codice dal gruppo

Abbiamo modificato a mano **didascalie e design**, oltre alla configurazione della pubblicazione del sito. Le altre modifiche sono state fatte attraverso l'agente.

### Motivazioni delle scelte finali

- **Sito statico senza server e senza framework.** Lo impone la consegna, che ha prevalso sul prompt. Serve anche alle prestazioni su mobile, un problema grave di IdeaGinger: LCP della pagina progetto da 34,1 s a 2,3 s in laboratorio.
- **Pagine generate da un'unica fonte**, per avere numeri coerenti e inglese completo.
- **Nessun nome reale per il programma.** «Funds TOgether» è stato evitato per «non presentare come reali informazioni inventate» sotto il nome di un'iniziativa vera. Vale anche per i marchi: nessun logo di IdeaGinger o dell'Università.
- **Un solo accento per l'azione di donare**, perché «Sostieni il progetto» resti il punto più visibile.

Tabella: Estratto della tracciabilità problema → soluzione
| Problema | Fonte | Journey | Soluzione | Verifica | Stato |
|---|---|---|---|---|---|
| Nessuna frase che dica che cos'è il servizio (G4) | Slide 59 | J01, J07, J12 | Frase iniziale in home e nel programma | Screenshot a 1280 e 375 px | Risolto |
| Menu con oltre 70 voci (G2) | Slide 67 | J03, J11, J12 | 7 voci senza tendine; `aria-expanded`, Esc | Test da tastiera | Risolto |
| Oltre il 100% senza etichetta (G3) | Slide 10 | J01, J05, J10 | Badge con icona e testo | Test dei percorsi e dei dati | Risolto |
| Card che non sembrano cliccabili (G4) | Slide 17 | J03 | Titolo come unico link esteso alla card | Test da tastiera | Risolto |
| Il promotore riceve i dati anche con l'anonimato | **Solo catalogo di C00: nessuna fonte** | J06 | Il sito lo dichiara prima dell'invio | Verifica con le personas | «Risolto», ma non verificato |

La copertura dichiarata è di 87 problemi risolti e 3 non applicabili su 90. Prima della versione finale era 84, 3 parziali e 3 non applicabili: il dato più prudente è il secondo, per i motivi di §7. Le verifiche attuali danno 0 violazioni axe su 58 pagine, 66/66 percorsi da tastiera, 394/394 controlli sui dati e Lighthouse mobile 95–98 per le prestazioni e 100 per l'accessibilità. Sono controlli automatici in Chrome, non una prova di usabilità con persone.

## Uso responsabile dell'IA

Riteniamo di aver usato l'IA in modo responsabile. In questa sezione mettiamo alla prova questa affermazione sul lavoro svolto: indichiamo dove regge e dove no.

:::responsabile | Supervisione umana
L'IA ha prodotto bozze e proposte; le scelte di progetto sono passate dal gruppo. Per le personas: l'iterazione di revisione sui primi output (§5.5) e le note con le decisioni da prendere insieme. Per il sito: i checkpoint, con proposte che abbiamo cambiato (§6.5), e gli script di verifica. Il limite è dichiarato nella nostra valutazione euristica: «chi valuta ha anche progettato il sito». Non abbiamo documentato l'esecuzione di V00.
:::

:::responsabile | Fondamento nei dati
Le personas derivano dal catalogo dei problemi di assignment 1 e i requisiti dai 90 problemi consolidati, con la fonte per ciascuno. Le personas sono **proto-personas**, senza ricerca con utenti, e lo dichiariamo. La verifica con le personas è un cognitive walkthrough, non un test con utenti. Progetti, persone, recapiti e importi del sito sono inventati, e lo dichiariamo in questa relazione.
:::

:::responsabile | Errori e allucinazioni
Abbiamo trovato affermazioni senza fondamento in entrambe le direzioni.
- Dall'IA: due affermazioni su P12 assenti dalla presentazione, rimosse; «ogni euro vale doppio» in P10, corretto; ricerca che sembrava funzionare, corretta dopo i test.
- Dai nostri materiali, segnalate dall'agente: un problema del catalogo (l'anonimato) che non compare in nessun documento di assignment 1; il prompt attribuiva la pagina 404 a link rotti, mentre era stata ottenuta digitando un indirizzo errato.
- Nella nostra presentazione: la soglia di contrasto errata a slide 23 e un conteggio sbagliato a slide 80.
:::

:::responsabile | Stereotipi e inclusione
C00 e i prompt chiedono di evitare stereotipi: per P07, «senza stereotipi: sui social è molto abile». Il controllo non si è fermato ai prompt: nonostante l'istruzione «Non descriverlo come incapace», abbiamo trovato e corretto «Giuseppe è poco capace con la tecnologia», e abbiamo ridotto l'aiuto del figlio di P12 a strategia di accessibilità. La matrice evita alcune associazioni scontate: Davide, cieco, ha familiarità 5/5; Elena, 58 anni, 4/5; Maria, 49 anni, 2/5. Restano però i due profili più anziani con familiarità 2/5 e l'archetipo «il nonno generoso ma prudente» nel prompt P01.
:::

:::responsabile | Privacy e proprietà intellettuale
Le personas sono fittizie e i nomi inventati. Il sito non invia dati a un server e non chiede numeri di carta: i moduli restano nel browser. Non usa loghi di IdeaGinger o dell'Università e i font sono open source. Le commissioni riprendono però le tariffe delle FAQ di IdeaGinger, e nessuno script controlla che non ci siano testi copiati. [DA VERIFICARE: conferma esplicita che agli strumenti non siano stati forniti dati personali reali, compresi quelli eventualmente presenti negli appunti]
:::

:::avviso | Il punto critico: il sito pubblicato non dichiara di essere fittizio
Le prime versioni del sito dicevano di essere un prototipo didattico, avvisavano che il pagamento era simulato e marcavano le informazioni non verificate. Nella versione finale, su nostra richiesta, tutto questo è stato tolto, e il nostro script di controllo dei dati verifica che quelle parole non ricompaiano.

Il 03/11/2026 abbiamo controllato https://andreock.github.io/hci_gruppo_a/ (home, donazione, FAQ, chi siamo). Il sito si presenta come «gestito dall'Ufficio ideaBlume dell'Ateneo», afferma che la donazione all'Università «è deducibile dal reddito», indica un telefono di Torino e una sede inventati, e nessuna di queste pagine dice che si tratta di un'esercitazione. Queste informazioni non vengono da fonti: le abbiamo stabilite noi, e riguardano un ente reale.

Di conseguenza non possiamo presentare questa scelta come buona pratica: i tre problemi passati a «risolto» non hanno nuovi riscontri, e un visitatore potrebbe scambiare il sito per un servizio dell'Università. [DA VERIFICARE: ripristiniamo un avviso e togliamo l'affermazione fiscale, oppure confermiamo la scelta motivandola; aggiornare questo riquadro di conseguenza]
:::

:::responsabile | Trasparenza
Questa relazione dichiara strumenti, prompt e limiti. È stata revisionata tramite **Claude Code (Claude Opus 5.5)** , che chiedeva di non inventare prompt, versioni o interventi. L'agente ha letto i nostri materiali e ha controllato il testo.
:::

:::responsabile | Limiti dell'IA e del nostro uso
- La conformità alle istruzioni non è garantita: la prima formulazione di P01 contraddiceva l'indicazione del prompt.
- Gli indicatori generati possono sembrare migliori dei fatti: 87 «risolti» su 90.
- La documentazione generata invecchia: verifica con le personas e valutazione euristica non sono state aggiornate dopo l'ultima revisione dei contenuti.
- Gli strumenti non sostituiscono le persone: Safari, Firefox, NVDA e VoiceOver reali e test con utenti restano da fare.
- Non abbiamo salvato le conversazioni, quindi non possiamo documentare molte richieste. È un limite nostro, non degli strumenti.
:::

## Contributo del gruppo

Tabella: Che cosa ha fatto l'IA e che cosa ha fatto il gruppo
| Attività | IA | Gruppo |
|---|---|---|
| Analisi di partenza | — | Valutazione euristica di assignment 1, appunti del corso |
| Personas e journey | Generazione delle schede, secondo template e scheda vincolante | Prompt, revisione degli output, richieste di modifica, ridefinizione dei profili |
| Struttura e contenuti del sito | Inventario, requisiti, architettura, testi, proposte | Conferma o modifica ai checkpoint, scelte finali |
| Codice del sito | Pagine, stili, interazioni, script di verifica | Ritocchi a mano a didascalie e design, pubblicazione |
| Verifica | Esecuzione degli script, prima stesura dei documenti di verifica | il sito è stato provato a mano e raffinato tramite prompt successivi, basati su un opinione critica e basata sui criteri visti a lezione|

**Decisioni che sono state solo del gruppo.** Ridefinizione di P12 e differenza tra P10 e P11; nome ideaBlume; almeno 12 pagine; contatti credibili; pubblicazione online; palette calda; interruttore del tema; rimozione di avvisi e segnaposto; ritocchi manuali a didascalie e design.

## Conclusioni

**Che cosa ha funzionato.** Separare contesto comune e prompt singoli ci ha permesso di generare in parallelo documenti con lo stesso formato. La tracciabilità ha tenuto le soluzioni del sito agganciate ai problemi di assignment 1. Gli script hanno trovato difetti reali (§6.4). Il confronto ai checkpoint ha prodotto scelte diverse da quelle proposte dall'agente, e in più casi l'agente ha fatto emergere errori nelle nostre stesse fonti.

**Limiti.** Non abbiamo fatto test con utenti: personas e soluzioni restano ipotesi. La maturità delle personas è disomogenea, e J07–J09 sono stati rivisti solo a sito finito. Chi ha valutato il sito è anche chi lo ha progettato. Alcune decisioni aperte non sono state chiuse formalmente. Con l'ultima revisione dei contenuti il sito ha perso la trasparenza verso chi lo visita (§7).

**Che cosa faremmo diversamente.** Avremmo conservato fin dall’inizio una documentazione completa e versionata di prompt, output e decisioni, verificando ogni fase prima di procedere alla successiva. Avremmo inoltre mantenuto la trasparenza sulla natura didattica del prototipo, senza pubblicare informazioni istituzionali o fiscali non verificate, e ripetuto i controlli dopo ogni modifica significativa. Dal lavoro svolto emergono almeno tre indicazioni: salvare fin dall'inizio prompt e output grezzi, compresi quelli del sito; allineare tutte le schede prima di costruirci sopra; rigenerare insieme tutti i documenti di verifica quando una decisione li cambia.

## Appendice A · Prompt

Riportiamo i criteri di V00 e un estratto del prompt di questa relazione. I prompt di C00, P01 e P01–P03 sono in §5.2.

:::prompt | Prompt · V00, verifica di un documento generato (estratto) | {{Personas}} {{Journey}}
1. Struttura: front matter completo; titoli e ordine delle sezioni identici a <formato_persona> o <formato_journey>.
2. Citazioni: ogni problema assegnato nel prompt originale è citato; ogni citazione esiste nel catalogo C00 con criterio e gravità corretti; problemi_citati coincide con gli ID presenti nel testo.
3. Fedeltà: nessun problema del sito inventato; le ipotesi sono marcate [IPOTESI]; nessun numero, URL o nome reale inventato.
4. Coerenza con la scheda vincolante: età, dispositivo, familiarità, accessibilità e frequenza rispettati.
5. Journey: fasi della tabella uguali al front matter; punteggi della curva emotiva uguali alla riga Emozioni; ogni difficoltà ha un'opportunità; touchpoint e canali non confusi.
6. Terminologia HCI corretta (usabilità e UX, affordance e signifier, touchpoint e canale, euristiche di Nielsen).
7. Rispetto nella descrizione delle esigenze di accessibilità, senza stereotipi.
:::

:::prompt | Prompt · REL-AI-01, relazione sull'uso dell'IA (estratto) | {{Trasversale}} · conversazione con Claude Code del 03/11/2026
3. Non inventare prompt, conversazioni, prime versioni, problemi o interventi. Se una prova manca (per esempio la prima versione di una persona non è stata salvata), scrivi un segnaposto evidente «Ci assumiamo la responsabilità delle scelte finali e dei loro effetti: l’uso dell’IA non giustifica le informazioni inesatte né le verifiche incomplete.» che dica al gruppo cosa serve, e raccoglilo nell'elenco finale delle informazioni mancanti.
4. Distingui sempre il contributo dell'IA da quello del gruppo: cosa ha proposto lo strumento, cosa il gruppo ha controllato, scartato, corretto o deciso.
:::
