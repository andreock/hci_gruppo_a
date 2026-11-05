---
Titolo: Relazione sulla realizzazione del sito di crowdfunding ideaBlume
Sottotitolo: Come abbiamo costruito e rivisto le personas, user journey e sito di crowdfunding per la ricerca
Gruppo: Gruppo A
Componenti: Andrea Canale · Antonio Fallea · Alexandru Ioan Chindris · Lorenzo Rizzolo
Corso: Human-Computer Interaction · a.a. 2026/27
Data: 5 novembre 2026
Sito pubblicato: https://andreock.github.io/hci_gruppo_a/
---

[[INDICE]]

## Introduzione

Con assignment 2 abbiamo progettato **ideaBlume**, un sito di crowdfunding per i progetti di ricerca dell'Università di Torino, ripartendo dalla valutazione euristica di IdeaGinger svolta in assignment 1 e sulla base dell'iniziativa Funds TOgether. Il lavoro ha avuto due fasi: prima 12 proto-personas per un servizio generico di crowdfunding e 12 user journey, che mostrano le difficoltà su IdeaGinger (As-is) e i miglioramenti su ideaBlume (To-be), poi un sito statico di 25 pagine, di cui 10 schede di progetto, in italiano e in inglese.

Il sito è stato creato mettendo nel contesto dell'IA, oltre alle personas e agli user journey, anche le problematiche relative al sito che abbiamo trovato nell'assignment 1.

Il sito è pubblicato su https://andreock.github.io/hci_gruppo_a/.

## Le personas

Dopo l'analisi di IdeaGinger abbiamo costruito 12 **proto-personas** pensate per un **servizio generico di crowdfunding**, non per IdeaGinger: descrivono persone con obiettivi ed esigenze proprie, e i problemi trovati nella valutazione euristica entrano come loro difficoltà, senza citare il sito. P10–P12 restano generiche nei bisogni, ma sono collocate sul sito di crowdfunding dell'Ateneo. Le personas non derivano da interviste o osservazioni con utenti, ma dallo studio dei potenziali utenti del servizio. Riportiamo il testo delle schede compilate sui template del corso, con un'impaginazione uniforme. Dati, nomi e scenari sono fittizi. La matrice che ne mostra la differenziazione è in §5.6.

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
| Claude Code (Claude Opus 5.5) | {{Personas}} {{Journey}} | Compilazione di P04–P12 e J04–J12, confronto con la consegna e revisione tramite prompt di verifica | Documentato |
| Claude Code (Claude Opus 5.5) | {{Sito}} | Inventario delle fonti, requisiti, architettura, codice, verifiche, tracciabilità | Documentato |
| Codex | {{Sito}} | Scrittura del codice del sito e vari raffinamenti | Dichiarato dal gruppo |
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
«GENERICITÀ ASSOLUTA. Non nominare mai piattaforme, app, siti, enti, università, programmi o progetti reali, né marchi. Non citare la valutazione del gruppo, slide, euristiche numerate, gravità o gli ID del catalogo (Sxx, Xxx). […]» Regola 2: «Persona: racconta la persona, non l'app. Profilo, attività, obiettivi, bisogni, contesto e competenze descrivono la sua vita e il suo rapporto con il crowdfunding in generale. […]»
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
«Esterna all'Università: non può proporre una campagna da sola, ma vuole costruire un progetto insieme ad altre persone.» «Si allarma quando scopre i costi tardi o scritti in piccolo: “che cos'altro non mi hanno detto?”.»
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
«Se la pagina iniziale non chiarisce lo scopo dell'iniziativa, teme di essere nel posto sbagliato.» «Trova faticosi titoli incompleti, etichette ambigue e parole tecniche non spiegate.»
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
| {{Personas}} {{Journey}} P10–P12: mancavano bisogni informativi, fiducia, familiarità con il crowdfunding, obiettivo e informazioni per fase | Confronto con la consegna | Aggiunte due righe ai journey e sottogruppi alle personas | Righe presenti in J10–J12; i sottogruppi delle personas sono stati tolti il 04/11/2026 (§5.5, §5.8) |
| {{Personas}} P10: «ogni euro vale doppio» contraddiceva la regola del cofinanziamento | Revisione delle schede | Motivazione e dubbio riformulati | Corretto |
| {{Personas}} P12: due affermazioni sul sito assenti dalla presentazione (FAQ, logo UniTo) | Confronto con la presentazione | Rimosse | Corretto |
| {{Personas}} P10, P11: fiducia del promotore confusa con quella dei donatori | Revisione delle schede | Ogni voce dice di chi è la fiducia | Corretto |
| {{Personas}} P12: aiuto del figlio e ansia, possibile stereotipo; dati familiari inutili in P10–P12 | Revisione delle schede | Ridotto a strategia di accessibilità; dati rimossi | Corretto |
| {{Journey}} J07–J09: IdeaGinger e riferimenti alle slide | Controllo rispetto alla regola 1 di C00 | Riscritti come J01–J06: nessun codice di slide, criticità in frasi complete, servizio generico | Corretto |
| {{Journey}} J10–J12: descrivevano criticità ancora da risolvere, con emozioni fino a −2 | Confronto con il sito realizzato | Riscritti sul percorso reale di ideaBlume, con confronto con IdeaGinger e criticità residue | Corretto |

**Controllo con V00.** Il prompt V00 (Appendice A) era facoltativo e non lo abbiamo eseguito mentre generavamo le schede. Il 05/11/2026 abbiamo applicato i suoi sette criteri alle 24 schede con Claude Code, in un'unica conversazione. Abbiamo adattato il criterio 2: V00 chiede citazioni con ID e gravità, che C00 versione 3 vieta, quindi abbiamo controllato che ogni problema assegnato emergesse. V00 non riscrive i documenti ma elenca che cosa correggere.

Tabella: Esito del controllo V00 sulle 24 schede
| Criterio | Esito | Che cosa è emerso |
|---|---|---|
| 1. Struttura | Da correggere | Campo «Frase rappresentativa e provenienza» ridotto a «Frase rappresentativa» in tutte le personas; P07 e P09 superano le 12 parole; J10–J12 senza momenti critici, HEART e continuità; J04–J06 senza la nota sulla base delle emozioni |
| 2. Problemi assegnati | Da correggere | Tutti presenti in J01–J09; ne mancano alcuni nelle difficoltà di P04, P07, P08, P09 e P10 |
| 3. Fedeltà | Da correggere | Tolti i marcatori `[IPOTESI]`: alcuni passaggi di J04, J05 e J06 ora sembrano fatti; P07–P09 riportano le fonti di P05; J10 e J11 usano nomi di campagna diversi da quelli del sito |
| 4. Scheda vincolante | Da correggere | Familiarità digitale diversa dal prompt in P02, P05, P08, P10 e P12; frequenza d'uso assente in P11 e P12 |
| 5. Journey | Da correggere | Curve coerenti con i prompt; touchpoint e canali confusi in singole celle di J04, J08, J09, J10 e J12 |
| 6. Terminologia HCI | Da correggere | Una sola metrica impropria: J08 usa dati di comportamento per HEART Happiness |
| 7. Rispetto | OK | Nessuno stereotipo nelle schede; resta l'archetipo del prompt P01 (§7) |

Le correzioni puntuali sono elencate nel registro `04_verifica_V00.md`. Il controllo è arrivato dopo la realizzazione del sito, quindi non ha influito sulle sue scelte.

### Richieste di modifica e interventi

Abbiamo fatto quattro tipi di intervento.

- **Revisioni dei prompt, prima di generare.** Abbiamo allineato C00 ai template e poi lo abbiamo reso generico: sono interventi sulle istruzioni date all'IA, non sui singoli output.
- **Richieste di revisione sugli output.** Per P01–P03 e J01–J03 abbiamo fatto sei richieste, una per documento. Per esempio, per P02: «Rendere visibili pause, una mano, interruzione e ripresa serale». Un controllo finale ha verificato la coerenza tra persona e journey.
- **Riscritture di una versione già salvata.** Il 27/10/2026 P10–P12 e J10–J12 sono passati in poche ore dal servizio esistente al nuovo sito, e i journey sono diventati To-be. Il 05/11/2026, a sito finito, abbiamo chiesto di togliere i riferimenti alle slide da J07–J09 e di far riflettere a J10–J12 «i miglioramenti che sono stati fatti in ideaBlume rispetto ad ideaGinger».
- **Revisione delle schede per la relazione.** Il 04/11/2026 abbiamo alleggerito le personas: via le intestazioni, i marcatori `[IPOTESI]` e i sottogruppi «Bisogni informativi» e «Fiducia» di P10–P12.


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

**Coerenza.** La scheda vincolante ha tenuto fermi età, dispositivo e ruolo tra persona e journey. Dove una persona contraddiceva una regola, abbiamo corretto il testo: è il caso di P10 e del raddoppio. La matrice riporta i valori del prompt: la familiarità digitale nelle schede finali è diversa per P02 (3,5), P05 (4), P08 (4), P10 (2,5) e P12 (2,5). Resta anche un'incoerenza tra prompt e output: il prompt di P12 descrive ancora Forlì e il lancio di una campagna, mentre la scheda finale descrive una partner a Torino.

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
| {{Journey}} J02 | Pausa breve, rete debole, una mano | Da «Riprende sul laptop» a percorso multicanale; dati da reinserire dichiarati come ipotesi in «Fonti e ipotesi»; abbandono legato a lentezza ed errore tardivo |
| {{Journey}} J12 | Tremore, ansia da moduli, decide dopo aver parlato con qualcuno | La registrazione è sostituita dal modulo «Proponi una collaborazione», seguito dalla telefonata dell'ufficio e dal direttivo |
| {{Journey}} J07–J09 | Piccola donazione da iPhone; ricerca esaustiva con interruzioni; candidatura in più sere | Codici delle slide sostituiti da difficoltà descritte per esteso, nel contesto di ciascuna persona |
| {{Journey}} J10–J12 | Pochi minuti (Franco); tastiera e pubblico estero (Amir); tremore e bisogno di parlare con qualcuno (Maria) | Le emozioni salgono a livelli medio-alti dove il sito risolve il problema; restano le criticità di ciascuno, come le tendine del modulo per Maria |

### Motivazioni delle scelte finali

- **Dodici personas invece di cinque.** Il minimo per quattro persone è 5. Le 12 personas sono costruite per far emergere i problemi di assignment 1. Il rischio è una maturità disomogenea, che si è verificata.
- **Proto-personas dichiarate.** Non derivano da ricerca con utenti, e le schede lo riportano.
- **To-be per P10–P12, As-is per gli altri.** I nove journey As-is documentano le difficoltà su IdeaGinger; i tre To-be mostrano, sul sito realizzato, come ideaBlume le affronta. Non abbiamo scritto un To-be per ogni persona: per le altre, la verifica del sito è nel confronto con i punti di dolore.
- **Niente area riservata.** Il prototipo non prevede account, quindi gli aggiornamenti passano dall'Ufficio di ideaBlume, come riportato in «Fonti e ipotesi» di J10 e J11.
- **Template e consegna.** La consegna chiede elementi che il template non ha. J10–J12 aggiungono le righe «Obiettivo della fase» e «Informazioni necessarie»; J01–J09 restano sul template, e nelle personas bisogni informativi e fiducia sono distribuiti nei campi esistenti. Non abbiamo uniformato le 24 schede.

## Fase 2 · Uso dell'IA per il sito

### Strumenti e attività

Abbiamo costruito il sito per fasi, con checkpoint in cui il gruppo ha confermato o cambiato le proposte dell'agente.

Tabella: Fasi di lavoro del sito (31/10–03/11/2026)
| Fase | Attività dell'agente | Controllo del gruppo |
|---|---|---|
| Fonti e requisiti | Inventario delle fonti, 90 problemi consolidati, bisogni, 102 requisiti, 19 decisioni proposte | Checkpoint 1: conferma con indicazioni (§6.5) |
| Architettura | Mappa del sito, design system, controllo dei contrasti | Checkpoint 2: date delle campagne |
| Implementazione | Prima versione di 58 pagine statiche, donazione in 5 passi | — |
| Verifiche | Script di verifica e correzioni | — |
| Chiusura | Verifica con le personas, valutazione euristica, tracciabilità | — |
| Redesign | Nuovo aspetto grafico | Richiesta di «un design più moderno» |
| Versione finale | Palette calda, tema, contenuti definitivi | Richieste del gruppo; ritocchi a mano (§6.7) |

### Prompt principali e informazioni fornite

**Informazioni fornite.** L'agente ha ricevuto la presentazione di assignment 1, i registri dei problemi, i report Core Web Vitals, i prompt di personas e journey e tutte le schede. A queste si aggiungono i nostri appunti e i vincoli della consegna: niente server, almeno 10 pagine distinte, versione desktop, nessun account né pagamento reale. Il lavoro è organizzato in una catena tracciabile: problema, requisito, soluzione, verifica.

**Prompt.** Il prompt iniziale, SITO-01, non è stato salvato: ne restano i frammenti citati nel registro delle decisioni. Abbiamo invece conservato due richieste di modifica, riportate qui in estratto e in Appendice A per la parte salvata. L'appendice contiene anche un prompt di esempio scritto a posteriori e indicato come tale.

:::prompt | Frammenti del prompt iniziale, citati nel registro delle decisioni | {{Sito}}
il prompt chiede un sito statico «consultabile con un semplice server locale» e dati letti da `data/progetti.json`
[…]
Il prompt dice che la valutazione ha trovato errori 404 «dalle pagine FAQ e Come funziona».
:::

:::prompt | Richieste di modifica (estratti) | {{Sito}}
Nella sezione dei progetti, quando si filtra rimuovi la didascalia legata ai progetti in corso e ai conclusi, mettila solo nella pagina progetti principale. Poi unisci la search box con la parte dei filtri rimuovendola dalla navbar.
[…]
Rifattorizza il sito cambiando la palette dei colori e introducendo il tema chiaro oltre il tema scuro. […]
:::

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

Provando il sito a mano abbiamo trovato due difetti nelle versioni generate dall'agente:

- La prima versione non mostrava solo i progetti filtrati, perché il filtro cercava anche sottostringhe all'interno delle parole.
- La seconda versione duplicava la ricerca nella navbar.

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
Su nostra richiesta sono stati tolti avvisi, FAQ «Questo sito è reale?» e 41 segnaposto, sostituiti da informazioni stabilite. La pagina è più pulita, ma il sito ha perso la dichiarazione della propria natura: ne discutiamo in §7.
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

### Richieste di modifica e interventi

Il nostro registro delle decisioni distingue le proposte dell'agente dalle scelte del gruppo.

Tabella: Che cosa ha proposto l'agente e che cosa abbiamo deciso
| Tema | Proposta dell'agente | Decisione del gruppo |
|---|---|---|
| Nome | «Sostieni la Ricerca» | **ideaBlume** |
| Pagine | Almeno 10, come da consegna | 25 pagine, di cui 10 progetti e una pagina 404 |
| Contatti | Dominio `example.org` | Fittizi ma credibili: `@ideablume.it`, numero di Torino |
| Pubblicazione | Sito apribile senza server | Anche pubblicato online |
| Date delle campagne | Date relative a oggi | Confermate al checkpoint 2 |
| Design | Prugna, «lontano dall'arancione» | Prima «più moderno», poi palette calda |
| Tema | Automatico dal sistema | Chiaro predefinito con interruttore |
| Contenuti | Segnaposto e avvisi | Eliminati, informazioni stabilite |
| Ricerca | Campo nella navbar | Tolto dalla navbar e unito ai filtri in «Progetti» |

### Revisione di contenuti, struttura, navigazione e interazioni

#### Contenuti

Le informazioni istituzionali non presenti nelle fonti erano inizialmente segnate come da verificare e sono state poi fissate da noi (§7). Il lessico è controllato da uno script: niente gergo, importi in una sola forma. I numeri vengono da un'unica fonte di dati, per evitare l'incoerenza di contatori trovata in assignment 1.

#### Struttura

Il principio guida è «prima i progetti da sostenere, poi le regole, poi i servizi per chi propone», l'opposto di quanto osservato su IdeaGinger. Il programma dell'Ateneo diventa una voce di primo livello. La versione 2 di P12 ha portato a una sezione per enti esterni e al modulo «Proponi una collaborazione»: è un caso in cui la revisione delle personas ha cambiato il sito. La versione inglese è completa, generata dagli stessi modelli; restano in lingua originale solo i commenti dei sostenitori, marcati con `lang`.

#### Navigazione

Il menu passa dalle oltre 70 voci di IdeaGinger a 8 voci senza tendine, Home compresa, con un menu mobile gestibile da tastiera. La ricerca non è più nella navbar: si trova in home, nell'elenco dei progetti e nella pagina dei risultati. L'ordine finale è Home, Progetti, Chi siamo, Come funziona, Il programma dell'Ateneo, Proponi un progetto, Domande frequenti, Contatti, diverso da quello della nostra richiesta in Appendice A, che non prevedeva Home e metteva Progetti al terzo posto. Tornando dall'elenco, filtri e posizione restano. Su telefono l'intestazione è stata compattata perché andava su tre righe a 375 px.

:::figure2 | stretta
![Home a 375 pixel: intestazione su una riga, ricerca, titolo e frase che spiega il servizio.](home-375.jpg){Home a 375 px.}
![Menu mobile aperto a 375 pixel con sette voci in un elenco e il campo di ricerca in alto.](menu-mobile-375.png){Menu mobile a 375 px, prima delle ultime modifiche: 7 voci e ricerca in alto.}
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
| Menu con oltre 70 voci (G2) | Slide 67 | J03, J11, J12 | 8 voci senza tendine; `aria-expanded`, Esc | Test da tastiera | Risolto |
| Oltre il 100% senza etichetta (G3) | Slide 10 | J01, J05, J10 | Badge con icona e testo | Test dei percorsi e dei dati | Risolto |
| Card che non sembrano cliccabili (G4) | Slide 17 | J03 | Titolo come unico link esteso alla card | Test da tastiera | Risolto |
| Il promotore riceve i dati anche con l'anonimato | Prompt C00 | J06 | Il sito lo dichiara prima dell'invio | Verifica con le personas | Risolto |

## Uso responsabile dell'IA

Riteniamo di aver usato l'IA in modo responsabile. In questa sezione mettiamo alla prova questa affermazione sul lavoro svolto: indichiamo dove regge e dove no.

:::responsabile | Supervisione umana
L'IA ha prodotto bozze e proposte; le scelte di progetto sono passate dal gruppo. Per le personas: l'iterazione di revisione sui primi output (§5.5) e le note con le decisioni da prendere insieme. Per il sito: i checkpoint, con proposte che abbiamo cambiato (§6.5), e gli script di verifica. Il limite è dichiarato nella nostra valutazione euristica: «chi valuta ha anche progettato il sito». V00 è stato eseguito solo il 05/11/2026, a sito finito (§5.4).
:::

:::responsabile | Fondamento nei dati
Le personas derivano dal catalogo dei problemi di assignment 1 e i requisiti dai 90 problemi consolidati, con la fonte per ciascuno. Le personas sono **proto-personas**, senza ricerca con utenti, e lo dichiariamo. La verifica con le personas è un cognitive walkthrough, non un test con utenti. Progetti, persone, recapiti e importi del sito sono inventati, e lo dichiariamo in questa relazione.
:::

:::responsabile | Errori e allucinazioni
Abbiamo trovato affermazioni senza fondamento in entrambe le direzioni.
- Dall'IA: Diverse frasi e affermazioni sono state riscritte e riviste per essere più generiche e scritte meglio.
- Dai nostri materiali, segnalate dall'agente: un problema del catalogo (l'anonimato) che non compare in nessun documento di assignment 1; il prompt attribuiva la pagina 404 a link rotti, mentre era stata ottenuta digitando un indirizzo errato.

:::

:::responsabile | Stereotipi e inclusione
C00 e i prompt chiedono di evitare stereotipi: per P07, «senza stereotipi: sui social è molto abile». Il controllo non si è fermato ai prompt: nonostante l'istruzione «Non descriverlo come incapace», abbiamo trovato e corretto «Giuseppe è poco capace con la tecnologia», e abbiamo ridotto l'aiuto del figlio di P12 a strategia di accessibilità. La matrice evita alcune associazioni scontate: Davide, cieco, ha familiarità 5/5; Elena, 58 anni, 4/5; Maria, 49 anni, 2/5. Restano però i due profili più anziani con familiarità 2/5 e l'archetipo «il nonno generoso ma prudente» nel prompt P01.
:::

:::responsabile | Privacy e proprietà intellettuale
Le personas sono fittizie e i nomi inventati. Il sito non invia dati a un server e non chiede numeri di carta: i moduli restano nel browser. Non usa loghi di IdeaGinger o dell'Università e i font sono open source. Le commissioni riprendono però le tariffe delle FAQ di IdeaGinger, e nessuno script controlla che non ci siano testi copiati.
:::

:::responsabile | Trasparenza
Questa relazione dichiara strumenti, prompt e limiti. È stata revisionata con **Claude Code (Claude Opus 5.5)**, a cui abbiamo chiesto di non inventare prompt, versioni o interventi: l'agente ha letto i nostri materiali e ha controllato il testo. Il limite maggiore riguarda il sito: dopo l'ultima revisione non dichiara più di essere un prototipo didattico e presenta come definitive informazioni inventate. Chi lo visita può saperlo solo da questa relazione.
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

## Conclusioni

**Che cosa ha funzionato.** Separare contesto comune e prompt singoli ci ha permesso di generare in parallelo documenti con lo stesso formato. La tracciabilità ha tenuto le soluzioni del sito agganciate ai problemi di assignment 1. Gli script hanno trovato difetti reali (§6.4). Il confronto ai checkpoint ha prodotto scelte diverse da quelle proposte dall'agente, e in più casi l'agente ha fatto emergere errori nelle nostre stesse fonti.

**Limiti.** Non abbiamo fatto test con utenti: personas e soluzioni restano ipotesi. La maturità delle personas è disomogenea, e J07–J09 sono stati rivisti solo a sito finito. Chi ha valutato il sito è anche chi lo ha progettato. Alcune decisioni aperte non sono state chiuse formalmente. Con l'ultima revisione dei contenuti il sito ha perso la trasparenza verso chi lo visita (§7).

**Che cosa faremmo diversamente.** Avremmo conservato fin dall’inizio una documentazione completa e versionata di prompt, output e decisioni, verificando ogni fase prima di procedere alla successiva. Avremmo inoltre mantenuto la trasparenza sulla natura didattica del prototipo, senza pubblicare informazioni istituzionali o fiscali non verificate, e ripetuto i controlli dopo ogni modifica significativa. Dal lavoro svolto emergono almeno tre indicazioni: salvare fin dall'inizio prompt e output grezzi, compresi quelli del sito; allineare tutte le schede prima di costruirci sopra; rigenerare insieme tutti i documenti di verifica quando una decisione li cambia.

## Appendice A · Prompt

Questa appendice raccoglie esempi di prompt per personas, journey e sito. Il contesto comune C00 e il prompt principale di P01–P03 sono in §5.2. Tutti i prompt riportati sono quelli che abbiamo usato, tranne il prompt di esempio per generare il sito, che abbiamo scritto a posteriori e che è indicato come tale.

### Prompt per personas e user journey

Ogni persona e ogni journey hanno un prompt proprio, da usare dopo C00. I prompt di persona fissano i tratti che non devono cambiare nella `<scheda_vincolante>`; quelli di journey definiscono scenario e fasi. Le chiavi tra parentesi quadre o nell'elenco delle fasi (S59, S41…) rimandano al catalogo dei problemi di C00 e non compaiono nelle schede.

:::prompt | Prompt · P01, Giuseppe Ferrero (estratto) | {{Personas}} · versione 3
<obiettivo>
Genera la scheda della persona P01 usando il formato <formato_persona> e le regole del contesto C00. Racconta la persona e il suo rapporto con il crowdfunding in generale, senza riferimenti ad app, piattaforme, enti o progetti reali.
</obiettivo>

<scheda_vincolante>
- Nome: Giuseppe Ferrero
- Età: 71
- Città: Moncalieri, nella prima cintura di Torino
- Occupazione: insegnante di scienze alle scuole medie, in pensione
[…]
- Ruolo: donatore alla prima esperienza di crowdfunding
- Dispositivo principale: tablet Android da 10 pollici regalato dal nipote, con carattere ingrandito; in casa non c'è un computer
- Familiarità digitale: 2/5. Usa WhatsApp, email, meteo e il giornale online; ha pagato online solo con l'aiuto della figlia; diffida dei siti che non conosce
- Accessibilità: presbiopia (occhiali da lettura), si affatica con testi piccoli e poco contrastati; tocchi imprecisi sui bersagli piccoli
- Frequenza d'uso: prima volta; al massimo una o due donazioni l'anno
- Motivazione: ha letto sul giornale di un progetto di ricerca universitaria per proteggere i neonati dai virus e, pensando alla nipote, vuole donare 50 €
</scheda_vincolante>

<frustrazioni_da_far_emergere>
- [S59] Non capisce subito «che cosa sia» il sito su cui è arrivato.
- [S23, S54] Testi piccoli e poco contrastati che lo costringono a ingrandire.
- [S12] Parole inglesi del crowdfunding che non conosce.
- [S10, S11] Numeri e percentuali che non sa interpretare (oltre il 100%, giorni con il segno meno).
- [S41] Paura di sbagliare quando paga online e l'errore arriva solo alla fine.
</frustrazioni_da_far_emergere>
:::

:::prompt | Prompt · J01, il journey di Giuseppe (estratto) | {{Journey}} · versione 3
<scenario>
Domenica mattina, a casa. Giuseppe ha letto sul giornale di un progetto di ricerca universitaria per proteggere i neonati dai virus, finanziato con il crowdfunding. Sul tablet cerca il progetto con il motore di ricerca. Obiettivo: donare 50 € ed essere sicuro che i soldi arrivino davvero alla ricerca.
</scenario>

<fasi>
Usa queste fasi come colonne. Per ogni fase sono indicati i problemi del catalogo di C00 da far emergere nella riga «Criticità e barriere» (con una soluzione in «Opportunità di miglioramento») e le esperienze positive da usare. Le chiavi non vanno riportate nel documento.
1. Scoperta: articolo sul giornale e ricerca online. Canali: giornale cartaceo, motore di ricerca. Problema facoltativo: S60.
2. Orientamento sulla homepage dell'app. Canale: sito da tablet. Problemi: S59, S23.
3. Capire come funziona la donazione (pagina «Come funziona»). Problemi: S54, S52, S12. Positivo: S44 (trova un numero di telefono).
4. Valutare il progetto: elenco dei progetti e pagina del progetto. Problemi: S10, S11, S14. Positivo: S27.
5. Donare: scelta dell'importo e modulo di donazione. Problema: S41.
6. Dopo la donazione: telefona alla figlia o all'assistenza per avere conferma; attende un'email [IPOTESI]. Canali: telefono, email.
</fasi>

<indicazioni_specifiche>
- Andamento emotivo atteso: motivazione alta all'inizio, calo nelle fasi 3–4, minimo nella fase 5, recupero nella fase 6 grazie al contatto umano.
- Nella fase 4 mostra il golfo della valutazione: Giuseppe interpreta male lo stato della campagna e rischia di rinunciare per un motivo sbagliato.
- Nella fase 5 evidenzia che dover scegliere una «ricompensa» non corrisponde al suo modello mentale.
</indicazioni_specifiche>
:::

:::prompt | Prompt · P11, Amir Haddad, un promotore (estratto) | {{Personas}} · versione 3
<scheda_vincolante>
- Nome: Amir Haddad
- Età: 27
- Origine e lingue: libanese, in Italia da cinque anni; arabo madrelingua, inglese C1, italiano B2
- Occupazione: dottorando in Informatica
[…]
- Ruolo: promotore; cura la comunicazione della campagna fittizia del suo gruppo («OpenAria», sensori open source per la qualità dell'aria)
- Dispositivo principale: laptop Linux con Firefox; smartphone Android
- Familiarità digitale: 5/5. Sviluppatore, usa molto la tastiera e le scorciatoie, ispeziona il codice delle pagine
- Motivazione: portare donatori anche dall'estero (colleghi internazionali, comunità libanese) e far sembrare la campagna professionale
</scheda_vincolante>

<indicazioni_specifiche>
- È un utente esperto: le sue difficoltà riguardano flessibilità ed efficienza d'uso e qualità tecnica, oltre alle lingue.
- Fa da ponte tra il gruppo di ricerca e i donatori: vede i problemi in prima persona e attraverso i messaggi che riceve.
- Distingui ciò che è previsto dal catalogo da ciò che riguarda l'area riservata dei promotori, da marcare [IPOTESI].
</indicazioni_specifiche>
:::

:::prompt | Richieste di revisione sulle prime bozze di P01–P03 e J01–J03 | {{Personas}} {{Journey}} · iterazione 1
P01: Descrivere competenze, strategie e contesto; attribuire le difficoltà all'interfaccia.
J01: Esplicitare percentuali oltre il 100%, giorni negativi e apertura inattesa dei link.
P02: Rendere visibili pause, una mano, interruzione e ripresa serale.
J02: Indicare dati da reinserire [IPOTESI] e collegarli a una soluzione di salvataggio.
P03: Specificare navigazione per H, landmark, elenco link e sintesi ad alta velocità.
J03: Descrivere lo stato non annunciato nel codice e il conseguente golfo della valutazione.
:::

:::prompt | Prompt · V00, verifica di un documento generato (estratto) | {{Personas}} {{Journey}}
1. Struttura: front matter completo; titoli e ordine delle sezioni identici a <formato_persona> o <formato_journey>.
2. Citazioni: ogni problema assegnato nel prompt originale è citato; ogni citazione esiste nel catalogo C00 con criterio e gravità corretti; problemi_citati coincide con gli ID presenti nel testo.
3. Fedeltà: nessun problema del sito inventato; le ipotesi sono marcate [IPOTESI]; nessun numero, URL o nome reale inventato.
4. Coerenza con la scheda vincolante: età, dispositivo, familiarità, accessibilità e frequenza rispettati.
5. Journey: fasi della tabella uguali al front matter; punteggi della curva emotiva uguali alla riga Emozioni; ogni difficoltà ha un'opportunità; touchpoint e canali non confusi.
6. Terminologia HCI corretta (usabilità e UX, affordance e signifier, touchpoint e canale, euristiche di Nielsen).
7. Rispetto nella descrizione delle esigenze di accessibilità, senza stereotipi.
:::

### Prompt per il sito

Questi sono due prompt con cui abbiamo chiesto di rifinire il sito già generato.

:::prompt | Richiesta di modifica · navigazione, ricerca e «Chi siamo» | {{Sito}}
Nella sezione dei progetti, quando si filtra rimuovi la didascalia legata ai progetti in corso e ai conclusi, mettila solo nella pagina progetti principale. Poi unisci la search box con la parte dei filtri rimuovendola dalla navbar.
Inoltre modifica l'ordine della navbar come segue: Chi siamo, Come funziona, Progetti, Proponi un progetto, Programma dell'ateneo, FAQ e contatti. Migliora anche la pagina chi siamo inventando una storia e aumentando un po' le didascalie.
:::

:::prompt | Richiesta di modifica · palette, tema e contenuti definitivi | {{Sito}} · la parte finale, un testo incollato, non è stata salvata
Rifattorizza il sito cambiando la palette dei colori e introducendo il tema chiaro oltre il tema scuro. Togli qualsiasi riferimento al fatto che il sito è simulato e che ci siano campagne/informazioni da decidere con l'università, tutto è deciso nulla deve essere ipotetico. […]
:::

### Prompt di esempio per generare il sito

Il prompt iniziale del sito non è stato salvato, quindi quello che segue **non è il prompt che abbiamo usato**. Lo abbiamo scritto a posteriori per mostrare come chiederemmo oggi un sito del genere: riunisce in un'unica richiesta le fonti, i vincoli e le correzioni emersi durante il lavoro (§6).

:::prompt | Prompt di esempio, scritto a posteriori · generazione di ideaBlume | {{Sito}}
<ruolo>
Sei un progettista UX e sviluppatore front-end esperto di accessibilità. Collabori con un gruppo di studenti del corso di Human-Computer Interaction e scrivi in italiano.
</ruolo>

<obiettivo>
Progetta e realizza ideaBlume, il sito di crowdfunding dei progetti di ricerca dell'Università di Torino. Chi arriva deve capire subito che cos'è il servizio e chi lo gestisce, trovare per primi i progetti da sostenere e poter donare senza incertezze. Il sito deve risolvere i problemi emersi dalla nostra valutazione euristica di IdeaGinger.
</obiettivo>

<fonti>
Prima di proporre qualsiasi cosa leggi: la consegna, la relazione di assignment 1 con i registri dei problemi, i report Core Web Vitals, le 12 personas e i 12 journey.
- Se due fonti sono in conflitto prevale la consegna: segnalami il conflitto.
- Se una fonte sembra sbagliata non correggerla in silenzio: segnalamelo.
- Ogni requisito deve indicare il problema o la persona da cui deriva.
</fonti>

<vincoli>
- Sito statico in HTML, CSS e JavaScript, senza framework: tutto deve funzionare senza server, anche aprendo i file da file://.
- Nessun account e nessun pagamento reale: i moduli restano nel browser e non si chiedono numeri di carta.
- Versione italiana e inglese complete, generate dagli stessi modelli.
- Una sola fonte di dati per progetti, importi e date, da cui uno script genera le pagine: lo stesso numero deve essere uguale ovunque.
- Font open source inclusi nel sito. Nessun logo di IdeaGinger o dell'Università e nessun nome di iniziative reali.
</vincoli>

<struttura>
Menu senza tendine: Home, Progetti, Chi siamo, Come funziona, Il programma dell'Ateneo, Proponi un progetto, Domande frequenti, Contatti.
Altre pagine: 10 pagine progetto, risultati di ricerca, donazione e conferma, candidatura per i ricercatori dell'Ateneo, collaborazione per gli enti esterni, accessibilità, pagina 404.
L'ordine di priorità è: prima i progetti da sostenere, poi le regole, poi i servizi per chi propone.
</struttura>

<interazioni>
- Elenco dei progetti: ricerca, filtri e ordinamento salvati nell'indirizzo; tornando da un progetto restano filtri e posizione.
- Ricerca: per inizio di parola e tollerante a singolare e plurale, maschile e femminile. «api» trova «apicoltori» ma non «capire»; «veterinaria» trova «Scienze Veterinarie». Se non ci sono risultati, proponi alternative.
- Stato delle campagne: sempre con testo e icona, mai con il solo colore, compreso «Obiettivo raggiunto · puoi ancora sostenerlo per N giorni». Le campagne concluse non hanno controlli di donazione attivi.
- Donazione in 5 passi: validazione all'uscita dal campo, riepilogo degli errori che riceve il focus, dati conservati tra i passi, «Modifica» nel riepilogo, commissioni visibili prima di pagare.
- Anonimato: spiega prima dell'invio quali dati riceve comunque il promotore.
</interazioni>

<design>
- Palette calda su fondo crema, tema chiaro predefinito e tema scuro con interruttore. Un solo colore di accento, riservato all'azione «Sostieni il progetto».
- WCAG 2.1 AA in entrambi i temi: testo almeno 4,5:1, componenti almeno 3:1. Calcola i contrasti con uno script.
- Tutto usabile da tastiera, con focus visibile; menu mobile con aria-expanded e chiusura con Esc; link con nomi distinguibili anche fuori contesto.
- Nessuno scorrimento orizzontale a 375 px, buone prestazioni su mobile e nessuno spostamento del layout durante il caricamento.
</design>

<contenuti>
Scrivi testi semplici, senza gergo, con gli importi in una sola forma e senza segnaposto. Progetti, persone, recapiti e importi sono inventati: elencali in un documento, così possiamo dichiararlo nella relazione. Non attribuire all'Ateneo regole, dati fiscali o dati reali che non si trovano nelle fonti: chiedici prima di fissarli.
</contenuti>

<processo>
Lavora per fasi e fermati ai checkpoint: non proseguire finché non abbiamo risposto.
1. Fonti e requisiti: inventario, problemi consolidati, bisogni per persona, requisiti, decisioni da prendere. CHECKPOINT.
2. Architettura: mappa del sito, design system, controllo dei contrasti. CHECKPOINT.
3. Implementazione a piccoli incrementi.
4. Verifiche: axe-core, Lighthouse, percorsi completi con Playwright e script su link, dati e lessico. Correggi e ripeti i controlli dopo ogni modifica significativa.
5. Chiusura: cognitive walkthrough per ogni persona, valutazione euristica e tabella di tracciabilità problema → requisito → soluzione → verifica.
In un registro delle decisioni distingui sempre ciò che proponi tu da ciò che decidiamo noi. Dichiara risolto un problema solo dopo averlo verificato e riporta i limiti rimasti.
</processo>
:::
