---
Titolo: Uso dell'intelligenza artificiale nel progetto ideaBlume
Sottotitolo: Come abbiamo costruito e rivisto con l'IA personas, user journey e sito di crowdfunding per la ricerca
Gruppo: Gruppo A
Componenti: Andrea Canale · Antonio Fallea · Alexandru Ioan Chindris · Lorenzo Rizzolo
Corso: Human-Computer Interaction · a.a. 2026/27
Data: 3 novembre 2026
Sito pubblicato: https://andreock.github.io/hci_gruppo_a/
---

[[INDICE]]

## Introduzione

Con assignment 2 abbiamo progettato **ideaBlume**, un sito di crowdfunding per i progetti di ricerca dell'Università di Torino, ripartendo dalla valutazione euristica di IdeaGinger e Funds TOgether svolta in assignment 1 (`assignment1/assignment1_gruppoA.pdf`). Il lavoro ha avuto due fasi: prima 12 proto-personas e 12 user journey, poi un sito statico di 17 tipi di pagina in italiano e in inglese. In entrambe abbiamo usato l'IA generativa come richiesto da `Istruzioni.md`.

Il legame con assignment 1 è diretto. Il catalogo dei problemi dato all'IA per personas e journey usa come chiavi i numeri di slide della nostra presentazione (`README.md`). I requisiti del sito partono dai 90 problemi consolidati di `website/docs/02_problemi_consolidati.md`.

**Come leggere la relazione.** I percorsi sono relativi a `assignment2/`, salvo quelli che iniziano con `assignment1/` o `.github/`. I codici come `2971d53` sono commit del repository. Le etichette {{Personas}} {{Journey}} {{Sito}} indicano la fase. Abbiamo selezionato i passaggi più utili a capire l'evoluzione del lavoro, non l'intera cronologia. Distinguiamo sempre ciò che ha proposto lo strumento da ciò che il gruppo ha controllato, corretto o deciso. Dove una prova manca lo diciamo, con un segnaposto evidente.

Questo documento copre la documentazione dell'uso dell'IA richiesta da `Istruzioni.md` §5. Le 24 schede di personas e journey sono in `personas/personas/` e `personas/journey/`.

:::avviso | Che cosa non è stato conservato
Non abbiamo salvato le conversazioni con gli strumenti né gli output grezzi di P01–P09. Per P01–P03 la prima versione è nota solo dalle citazioni di `alex/documentazione_uso_ai.md`; per P04–P06 esiste una sola versione. Il prompt principale del sito non è nel repository. I confronti che seguono si limitano a ciò che possiamo dimostrare.
:::

## Panoramica degli strumenti

Il gruppo dichiara di aver usato **Claude Code e Codex in tutto il progetto**. La tabella riporta, per ogni attività, che cosa risulta anche dalle prove.

Tabella: Strumenti, attività e persone, con la prova disponibile
| Strumento | Fase | Attività | Chi | Prova |
|---|---|---|---|---|
| Codex (OpenAI Codex, modello GPT-5) | {{Personas}} {{Journey}} | Generazione e revisione di P01–P03 e J01–J03, controllo di coerenza, schede HTML | Alexandru Ioan Chindris | `alex/documentazione_uso_ai.md` |
| Claude Code (Claude Opus 5.5) | {{Personas}} {{Journey}} | Compilazione di P10–P12 e J10–J12, confronto con `Istruzioni.md` | Lorenzo Rizzolo | `Co-Authored-By` in `d6feb95`, `1b2f2c9` |
| Claude Code e Codex | {{Personas}} {{Journey}} | P04–P06 e J04–J06 | Commit di Andrea Canale | `f547471`. [DA COMPLETARE: chi le ha generate e con quale strumento] |
| Claude Code e Codex | {{Personas}} {{Journey}} | P07–P09 e J07–J09 | Commit di Antonio Fallea | `a941518`, `d3e3440`. [DA COMPLETARE: quale strumento per ciascun documento] |
| Claude Code (Claude Opus 5.5) | {{Sito}} | Inventario, requisiti, architettura, codice, verifiche, tracciabilità | Commit di Andrea Canale | `Co-Authored-By` in `4baa4e9`, `38a1910`, `56e2a95`, `e1ebd20`, `60712ad` |
| Codex | {{Sito}} | Dichiarato dal gruppo, senza traccia nei commit | [DA COMPLETARE: chi e per quali attività del sito] | Dichiarazione del gruppo |
| Script scritti con l'agente | {{Sito}} | axe-core, Lighthouse, Playwright, controlli su contrasti, link e dati | Eseguiti sul sito | `website/tools/`, `website/docs/verifiche/` |

:::html
<figure class="flusso">
<svg viewBox="0 0 760 190" role="img" aria-labelledby="flusso-t flusso-d" xmlns="http://www.w3.org/2000/svg" font-family="Inter, Arial, sans-serif">
<title id="flusso-t">Flusso di lavoro con l'IA</title>
<desc id="flusso-d">Le fonti del gruppo alimentano i prompt; i prompt producono gli output dell'IA; il gruppo li rivede e ottiene la versione finale. Dalla revisione una freccia torna ai prompt con le richieste di modifica.</desc>
<defs><marker id="fr" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#3b1d2a"/></marker></defs>
<g font-size="12.5" fill="#3b1d2a">
<rect x="4" y="30" width="132" height="92" rx="6" fill="#fbf6ee" stroke="#3b1d2a"/><text x="70" y="52" text-anchor="middle" font-weight="700">Fonti del gruppo</text><text x="70" y="72" text-anchor="middle" font-size="10.5">relazione 1, appunti,</text><text x="70" y="87" text-anchor="middle" font-size="10.5">template, Istruzioni,</text><text x="70" y="102" text-anchor="middle" font-size="10.5">personas per il sito</text>
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

## Fase 1 · Personas e user journey

### Strumenti e attività

Ogni componente ha lavorato su tre personas e sui relativi journey, in conversazioni separate. La suddivisione risulta dalle cartelle e dai commit: P01–P03 Alexandru Ioan Chindris («Alex» nelle cartelle del repository), P07–P09 Antonio Fallea, P10–P12 Lorenzo Rizzolo. P04–P06 sono state caricate da Andrea Canale, che ha caricato anche i prompt comuni (`fb0a77b`). Gli strumenti hanno generato le schede e, per P01–P03, anche il generatore delle schede HTML (`alex/scripts/genera_html.py`). La colonna «Assegnato a» di `README.md` è rimasta vuota. [DA VERIFICARE: conferma della suddivisione, in particolare P04–P06]

### Prompt principali e informazioni fornite

**Informazioni fornite.** Abbiamo dato agli strumenti la relazione di assignment 1 sotto forma di catalogo dei problemi, i nostri appunti del corso (`<riferimenti_teorici_dagli_appunti>` in C00), i due template ufficiali (`personas/scheda_persona.pdf`, `personas/scheda_user_journey.pdf`) e una scheda vincolante per ogni persona.

**Perché questa struttura.** Dovendo lavorare in parallelo, abbiamo separato un contesto comune da un prompt singolo per documento: `README.md` spiega che così «più persone del gruppo possono generarli in parallelo, ciascuna nella propria conversazione, ottenendo documenti con la stessa struttura». I 26 prompt sono C00, una coppia Pxx e Jxx per persona, e il prompt di verifica V00. Il tag `<persona_generata>` di ogni Jxx permette di incollare la persona già pronta, per tenere allineato il journey. I tratti che non dovevano cambiare (età, dispositivo, familiarità, accessibilità, frequenza) sono fissati nella `<scheda_vincolante>`.

:::prompt | Prompt · C00, contesto comune (estratto) | {{Personas}} {{Journey}} · `00_contesto_comune_C00.md`, versione `2971d53`
Il gruppo sta producendo 12 personas (P01–P12) e 12 journey map (J01–J12) per una GENERICA app di crowdfunding (sito web e versione mobile). Ogni documento viene generato da una persona diversa in una conversazione separata: per questo tutti i documenti devono seguire esattamente gli stessi formati, definiti più sotto.
[…]
4. Non inventare dati presentati come reali (statistiche, URL, citazioni). Se aggiungi comportamenti dell'app non previsti dal catalogo, marcali con [IPOTESI].
[…]
6. Le esigenze di accessibilità vanno descritte con rispetto e precisione (strumenti usati, strategie), senza pietismo e senza stereotipi.
:::

:::prompt | Prompt · P01, indicazioni specifiche (estratto) | {{Personas}} · `personas/P01_giuseppe_ferrero.md`, versione `2971d53`
- Il suo modello mentale della donazione è l'offerta o il bonifico: si aspetta di dare una somma, non di scegliere una «ricompensa».
- Mostra le sue strategie: chiede conferma alla figlia per telefono, fotografa lo schermo, preferisce chiamare un numero di assistenza. Non descriverlo come incapace: è un ex insegnante curioso e attento.
:::

:::prompt | Prompt principale di P01–P03 | {{Personas}} {{Journey}} · Alexandru Ioan Chindris · `alex/documentazione_uso_ai.md`
Genera e raffina la scheda della proto-persona indicata usando esclusivamente i campi del template ufficiale. Mantieni invariati età, ruolo, dispositivo, familiarità digitale, accessibilità e frequenza. Trasforma i problemi assegnati in esperienze personali, senza citare ID interni o servizi reali. Costruisci poi un journey as-is coerente, con azioni, touchpoint, pensieri, emozioni motivate, barriere e opportunità concrete. Segnala come ipotesi tutto ciò che non deriva dal catalogo.
:::

**Come è cambiato il contesto comune.** C00 è stato riscritto due volte nella stessa giornata del 27/10/2026. Il primo passo (`c264a64`) ha reso vincolanti i template del corso, con una tabella `<corrispondenze>` tra gli appunti e i campi. Il secondo (`2971d53`) ha tolto ogni riferimento al sito valutato.

:::confronto
:::prima | Prima versione | C00, regola 1, `fb0a77b`
«Fai emergere tutti i problemi elencati nel prompt singolo, ciascuno citato almeno una volta nel formato [Sxx · criterio · Gx] (es. [S17 · H4 · G4], [S59 · LG1 · G4], [S74 · prestazioni]) o [X0n · analisi preliminare, da verificare]. […]»
:::
:::dopo | Versione finale | C00, regola 1, `2971d53`
«GENERICITÀ ASSOLUTA. Non nominare mai piattaforme, app, siti, enti, università, programmi o progetti reali, né marchi. Non citare la valutazione del gruppo, slide, euristiche numerate, gravità o gli ID del catalogo (Sxx, Xxx). […]»
:::
:::cambio
Le personas non descrivono più l'interfaccia di IdeaGinger ma persone con esigenze proprie; il legame con la valutazione resta nelle chiavi interne dei prompt. Il messaggio del commit dice solo «Update prompts». [DA COMPLETARE: perché il gruppo ha scelto la versione generica]
:::
:::

### Dalla prima versione alla versione finale

:::confronto
:::prima | Prima versione · P01 {{Personas}} | citata in `alex/documentazione_uso_ai.md`, iterazione 1 (output grezzo non salvato)
«Giuseppe è poco capace con la tecnologia.»
:::
:::dopo | Versione finale · P01 {{Personas}} | `alex/personas/P01_giuseppe_ferrero.md`
«Sa cercare informazioni e confrontarle, ma non riconosce sempre le convenzioni dei moduli online.» «Si insospettisce se non comprende subito che cosa offre un sito.» Frase rappresentativa: «Aiuto volentieri, ma prima voglio capire dove vanno i soldi.»
:::
:::cambio
Alex ha giudicato la prima formulazione «stereotipata e centrata sul deficit» e ha chiesto di «descrivere competenze, strategie e contesto; attribuire le difficoltà all'interfaccia». Giuseppe è passato da «anziano inesperto» a ex insegnante curioso e prudente.
:::
:::

:::confronto
:::prima | Prompt e versione salvata · P12 {{Personas}} | Prompt `fb0a77b`; prima scheda salvata `d6feb95`
Prompt: «Città: Forlì»; «promotrice esterna a UniTo; vuole lanciare la prima campagna dell'associazione su Ginger».

Scheda `d6feb95`: Torino; «una volontaria le manda su WhatsApp il link di Ginger»; «[S49 · H5 · G4] Trova in fondo a un paragrafo la quota di 350 € + IVA e si allarma».
:::
:::dopo | Versione finale · P12 {{Personas}} | `86536bf`, `personas/personas/P12_maria_lombardi_persona.html`
«Esterna all'Università: non può proporre una campagna da sola, ma vuole costruire un progetto insieme a un gruppo di ricerca UniTo [IPOTESI].» «Si allarma quando scopre i costi tardi o scritti in piccolo: “che cos'altro non mi hanno detto?”.»
:::
:::cambio
Il sito è dedicato alle campagne dell'Ateneo: lì una campagna lanciata in autonomia non esiste, e una ricercatrice UniTo sarebbe stata quasi uguale a P09. Maria resta esterna e segue il percorso «contatto», mentre Chiara segue la candidatura (`da_rivedere_P10-P12.md` §2.2). La v2 toglie i riferimenti a IdeaGinger.
:::
:::

:::confronto
:::prima | Prima versione · P07 {{Personas}} | `a941518`, 27/10/2026, v1
«[S59 · LG1 · G4] La homepage non spiega che cos'è Ginger: teme di essere sul sito sbagliato.» «[S64 · LG6 · G3] Titoli troncati e stato “Per ispirarti” ambiguo.»
:::
:::dopo | Versione rivista · P07 {{Personas}} | `d3e3440`, 31/10/2026, v2 (non è su `main`)
«Se la pagina iniziale non chiarisce lo scopo dell'iniziativa, teme di essere nel posto sbagliato.» «Trova faticosi titoli incompleti, etichette ambigue e parole inglesi non spiegate.»
:::
:::cambio
La revisione porta le difficoltà dall'interfaccia alla persona. È però **rimasta a metà**: `d3e3440` è solo sul branch `assignment1-valutazione-euristica`, il servizio resta «Funds TOgether» e J07–J09 non sono stati toccati. Su `main` le schede P07–P09 sono ancora v1, e il sito le ha usate così (`website/docs/decisioni.md`, D-04).
:::
:::

### Problemi individuati negli output

Tabella: Problemi trovati negli output di personas e journey
| Problema nell'output | Come ce ne siamo accorti | Richiesta o intervento | Esito |
|---|---|---|---|
| {{Personas}} P01: «Giuseppe è poco capace con la tecnologia» | Revisione di Alex: stereotipo, centrato sul deficit | Descrivere competenze e strategie; difficoltà attribuite all'interfaccia | Corretto |
| {{Personas}} P03: «Davide ha bisogno di un sito semplice» | Revisione di Alex: paternalistico | Specificare navigazione per H, landmark, elenco link, sintesi ad alta velocità | Corretto |
| {{Journey}} J01: «La pagina è confusa» | Revisione di Alex: generico, non osservabile, senza soluzione | Esplicitare percentuali oltre il 100%, giorni negativi, apertura inattesa dei link | Corretto |
| {{Journey}} J03: «Non vede il pallino rosso» | Revisione di Alex: descrizione visiva impropria per chi usa uno screen reader | Descrivere lo stato non annunciato e il golfo della valutazione | Corretto |
| {{Personas}} {{Journey}} P10–P12: mancavano bisogni informativi, fiducia, familiarità con il crowdfunding, obiettivo e informazioni per fase | Confronto con `Istruzioni.md` | Aggiunte righe e sottogruppi | Corretto per P10–P12; decisione generale rimasta aperta (§3.8) |
| {{Personas}} P10: «ogni euro vale doppio» contraddiceva la regola del cofinanziamento | Note di Lorenzo Rizzolo, `da_rivedere_P10-P12.md` §3 | Motivazione e dubbio riformulati | Corretto |
| {{Personas}} P12: due affermazioni sul sito assenti dalla presentazione (FAQ, logo UniTo) | Confronto con la presentazione | Rimosse | Corretto |
| {{Personas}} P10, P11: fiducia del promotore confusa con quella dei donatori | Note di Lorenzo Rizzolo | Ogni voce dice di chi è la fiducia | Corretto |
| {{Personas}} P12: aiuto del figlio e ansia, possibile stereotipo; dati familiari inutili in P10–P12 | Note di Lorenzo Rizzolo | Ridotto a strategia di accessibilità; dati rimossi | Corretto |
| {{Personas}} {{Journey}} P07–P09, J07–J09: IdeaGinger e chiavi `Sxx` | `website/docs/01_inventario_fonti.md` §5, in contrasto con la regola 1 di C00 | `d3e3440` solo per le schede | **Aperto** su `main` |

Il prompt V00 prevedeva sette criteri, tra cui fedeltà e rispetto (Appendice B), ma era facoltativo. [DA COMPLETARE: se V00 è stato eseguito, su quali documenti e con quale esito]

### Richieste di modifica e interventi

Nel repository restano tre tipi di intervento.

- **Revisioni dei prompt, prima di generare.** `c264a64` allinea C00 ai template e `2971d53` lo rende generico: intervengono sulle istruzioni date all'IA, non sui singoli output.
- **Richieste di revisione sugli output.** La tabella «Iterazione 1» di `alex/documentazione_uso_ai.md` riporta sei richieste, una per documento. Per esempio, per P02: «Rendere visibili pause, una mano, interruzione e ripresa serale». Il controllo finale elenca anche le verifiche di coerenza tra persona e journey.
- **Riscritture di una versione già salvata.** Tra `d6feb95` e `86536bf`, a sette ore di distanza, P10–P12 e J10–J12 passano al nuovo sito e i journey diventano To-be. Le scelte sono registrate da Lorenzo Rizzolo in `da_rivedere_P10-P12.md` §0.

Le note di revisione sono del gruppo; il testo delle schede è stato prodotto con gli strumenti. Non sappiamo dire, dalle sole prove, quanto di `86536bf` e `d3e3440` sia stato scritto a mano. [DA COMPLETARE: estratti di richieste reali, se recuperabili dagli appunti, e natura di questi due commit]

### Come abbiamo reso le personas più specifiche, differenziate e coerenti

**Specificità.** Abbiamo sostituito i tratti generici con comportamenti osservabili. Davide non ha bisogno di «un sito semplice»: usa NVDA con H, landmark ed elenco dei link (`alex/journeys/J03_davide_rinaldi.md`). Gli scenari vaghi («nelle ultime settimane…», `da_rivedere_P10-P12.md` §3) sono diventati momenti concreti: Franco ha tre minuti, un martedì tra una seduta di laurea e il consiglio di dipartimento, e tre email di donatori da leggere.

**Differenziazione.** La matrice è stata decisa prima di generare, nella scheda vincolante di ogni prompt. Copre 8 donatori o visitatori e 4 promotori, 6 donne e 6 uomini, 20–71 anni (`README.md`). Le differenze riguardano obiettivi ed esigenze, non solo nome ed età, come chiede `Istruzioni.md` §2.

Tabella: Matrice delle personas nella versione usata per il sito (`website/docs/03_bisogni_personas.md` §2)
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

Due casi mostrano dove la differenziazione è stata corretta dopo la generazione. P12 si distingue da P09 per il percorso «contatto». P10 e P11 erano «entrambi promotori nella stessa fase» (`da_rivedere_P10-P12.md` §2.4): nella v2 Franco arriva fino al resoconto ai donatori, che copre anche «Seguire un progetto già sostenuto», mentre Amir cura diffusione e pubblico internazionale (§0).

**Coerenza.** La scheda vincolante mantiene costanti i dati principali tra persona e journey. Dove una persona contraddiceva una regola, abbiamo corretto il testo: è il caso di P10 e del raddoppio. Resta un'incoerenza non risolta tra prompt e output: `personas/P12_maria_lombardi.md` descrive ancora Forlì e il lancio di una campagna, mentre la scheda finale descrive una partner a Torino.

### Come abbiamo migliorato la corrispondenza tra journey e personas

:::confronto
:::prima | Prima versione · J03 {{Journey}} | citata in `alex/documentazione_uso_ai.md`
«Non vede il pallino rosso.»
:::
:::dopo | Versione finale · J03 {{Journey}} | `alex/journeys/J03_davide_rinaldi.md`, fase 3
«Stato affidato a colore o simbolo; ricompense e importo restano attivi nella campagna conclusa.» Opportunità: «Etichetta “Campagna conclusa” annunciata; controlli di donazione disabilitati e spiegazione dell'esito.»
:::
:::cambio
Il journey ora usa il modo di interagire di Davide: la barriera è lo stato non annunciato, non qualcosa che lui «non vede». Azioni e touchpoint nominano tastiera e NVDA in ogni fase sul sito.
:::
:::

:::confronto
:::prima | Prima versione salvata · J10 {{Journey}} | `d6feb95`, As-is, base Mista
Fase 1: «Controllo della pagina pubblica e della card». Fase 6: «Chiusura della campagna e rendicontazione», con la fine del percorso «rendicontazione con l'ufficio comunicazione». Azione: «Risponde a email e telefonate di donatori che non riescono a contattarlo dal sito».
:::
:::dopo | Versione finale · J10 {{Journey}} | `86536bf`, To-be, base Ipotesi
Fase 1: «Controllo della pagina pubblica». Fase 6: «Resoconto ai donatori». Azione: «Due mesi dopo scrive con il dottorando il resoconto, con foto degli apiari; l'ufficio lo pubblica e lo invia ai sostenitori».
:::
:::cambio
Il percorso rispetta la persona: Franco delega le attività tecniche e ha pochi minuti, quindi il resoconto passa dal dottorando e dall'ufficio. Le opportunità diventano elementi del prototipo (`da_rivedere_P10-P12.md` §0).
:::
:::

Tabella: Altri adattamenti del journey alle caratteristiche della persona
| Journey | Caratteristica della persona | Intervento | Prova |
|---|---|---|---|
| {{Journey}} J01 | Tablet, modello mentale dell'offerta, ricorso alla figlia | La curva scende su comprensione e pagamento e risale con conferma e contatto umano; «La pagina è confusa» diventa dati osservabili | `alex/documentazione_uso_ai.md`, `alex/journeys/J01…` |
| {{Journey}} J02 | Pausa breve, rete debole, una mano | Da «Riprende sul laptop» a percorso multicanale; dati da reinserire marcati `[IPOTESI]`; abbandono legato a lentezza ed errore tardivo | `alex/documentazione_uso_ai.md` |
| {{Journey}} J12 | Tremore, ansia da moduli, decide dopo aver parlato con qualcuno | La registrazione è sostituita dal modulo «Proponi una collaborazione», seguito dalla telefonata dell'ufficio e dal direttivo | `d6feb95`, `86536bf` |
| {{Journey}} J07–J09 | — | Nessuna revisione: restano v1 | `a941518` |

### Motivazioni delle scelte finali

- **Dodici personas invece di cinque.** Il minimo per quattro persone è 5 (`Istruzioni.md` §2). Le 12 personas sono costruite per far emergere i problemi di assignment 1 (`README.md`, tabella di copertura). Il rischio è una maturità disomogenea, che si è verificata.
- **Proto-personas dichiarate.** Non derivano da ricerca con utenti: `README.md` lo dice nella «Nota di metodo» e le schede lo riportano.
- **To-be per P10–P12, As-is per gli altri.** Lorenzo Rizzolo ha scelto il To-be per collegare le opportunità al prototipo. La scelta non è stata estesa alle altre schede (`da_rivedere_P10-P12.md` §2.5).
- **Niente area riservata.** Il prototipo non prevede account (`Istruzioni.md` §4), quindi gli aggiornamenti passano da un ufficio d'Ateneo, marcato `[IPOTESI]`.

Le decisioni di gruppo elencate in `da_rivedere_P10-P12.md` §2 hanno ancora le caselle vuote. [DA COMPLETARE: esito sull'approvazione di P12, sulla precedenza tra template e Istruzioni e sulla revisione di P07–P09 rimasta fuori da main]

## Fase 2 · Il sito

### Strumenti e attività

Il sito è stato costruito per fasi, con un checkpoint del gruppo tra una fase e l'altra. Le fasi e il nome del prompt risultano dai messaggi di commit.

Tabella: Fasi di lavoro del sito (31/10–03/11/2026)
| Commit | Attività dell'agente | Controllo del gruppo |
|---|---|---|
| `4baa4e9` | Inventario delle fonti, 90 problemi consolidati, bisogni, 102 requisiti, 19 decisioni proposte | Checkpoint 1: conferma con indicazioni (§4.5) |
| `38a1910` | Architettura, design system, controllo dei contrasti | Checkpoint 2: D-24 |
| `56e2a95` | Implementazione: 58 pagine statiche, donazione in 5 passi | — |
| `e1ebd20` | Script di verifica e correzioni | — |
| `60712ad` | Verifica con le personas, valutazione euristica, tracciabilità | — |
| `f0988ba` | Redesign, GitHub Action (senza riga di co-autore) | Richiesta «un design più moderno» (D-35) |
| `dd07a0a` | — | Modifica manuale del trigger di pubblicazione |
| `797fc7e` | Palette calda, tema, contenuti definitivi (senza riga di co-autore) | Richieste D-40, D-41, D-42; ritocchi a mano (§4.7) |

### Prompt principali e informazioni fornite

Il prompt principale, «SITO-01», non è stato salvato nel repository. [DA COMPLETARE: testo o estratti del prompt SITO-01] Ne conosciamo solo i frammenti riportati nel registro delle decisioni.

:::prompt | Frammenti del prompt citati indirettamente | {{Sito}} · `website/docs/decisioni.md`, D-01 e D-07
il prompt chiede un sito statico «consultabile con un semplice server locale» e dati letti da `data/progetti.json`
[…]
Il prompt dice che la valutazione ha trovato errori 404 «dalle pagine FAQ e Come funziona».
:::

**Informazioni fornite.** Secondo `website/docs/01_inventario_fonti.md`, l'agente ha letto per intero o in estratto la presentazione di assignment 1, i registri dei singoli componenti, i report Core Web Vitals, C00, V00, i prompt delle personas e tutte le schede. A queste si aggiungono i nostri appunti, indicati dal gruppo come fonte, e i vincoli di `Istruzioni.md`: niente server, almeno 10 pagine distinte, versione desktop, nessun account né pagamento reale. Il lavoro è organizzato in una catena tracciabile: problema (P-xxx), requisito (R-xxx), soluzione, verifica.

### Dalla prima versione alla versione finale

#### La grafica

Le tre versioni condividono la struttura; cambiano palette, caratteri e gerarchia.

:::figure2 | stretta
![Home della prima versione: fascia lilla, titolo in nero, pulsanti viola, font di sistema, card sotto la prima schermata.](home-1280-v1.jpg){Versione 1, `e1ebd20`. Palette prugna e font di sistema.}
![Home della seconda versione: fondo chiaro violaceo, titolo grande, ricerca arrotondata, scheda di un progetto in evidenza a destra.](home-1280-v2.jpg){Versione 2, `f0988ba`. Inter e Bricolage Grotesque.}
![Home della terza versione: stessa impaginazione su fondo crema, testi prugna bruna, pulsante terracotta, interruttore «Tema scuro».](home-1280-v3.jpg){Versione 3, `797fc7e`. Palette calda e tema a scelta.}
:::

:::cambio
La richiesta di redesign ammetteva framework CSS: Tailwind e Bootstrap sono stati valutati e scartati perché avrebbero richiesto di riscrivere il markup o contrastavano con l'uso senza server (D-35). La palette calda è stata una richiesta del gruppo (D-40). Il terracotta è stato scurito finché il bianco non ha raggiunto 5,00:1, contro i 2,46:1 dei titoli arancioni di IdeaGinger. Il prezzo del redesign è misurato: Lighthouse mobile è passato da 100 a 95–98 per le prestazioni.
:::

#### Una funzione: la ricerca

L'agente ha prodotto una prima versione che gli script di verifica hanno trovato difettosa due volte.

:::diff | Modifica in `js/ideablume.js`, dalla prima versione alla finale | {{Sito}} · `56e2a95` → `e1ebd20` → `60712ad`
- return parole.every(function (w) { return testo.indexOf(w) >= 0; });
+ // e1ebd20: «api» trova «apicoltori», non «capire»
+ var voci = testo.split(/[^a-z0-9]+/);
+ return parole.every(function (w) { return voci.some(function (v) { return v.indexOf(w) === 0; }); });
+ // 60712ad: «veterinaria» trova «veterinarie»
+ var r = w.length >= 5 ? w.slice(0, -1) : w;
+ return voci.some(function (v) { return v.indexOf(r) === 0; });
:::

:::cambio
La ricerca per sottostringa dava risultati sbagliati (7 per «api»). Quella per inizio di parola ne dava 2 pertinenti, ma «veterinaria» non trovava «Scienze Veterinarie» (V-01, gravità 2). La versione finale tollera singolare e plurale, maschile e femminile (D-33).
:::

#### I contenuti: da prototipo dichiarato a sito «definitivo»

:::figure2
![Primo passo della donazione nella versione 1, con il riquadro giallo «Pagamento simulato. Questo è un prototipo didattico» sopra il riepilogo.](donazione-1280-v1.jpg){Versione 1, `e1ebd20`. Avviso di pagamento simulato in cima.}
![Primo passo della donazione nella versione 3: titolo, indicatore dei cinque passi e scelta della ricompensa, senza alcun avviso.](donazione-1280-v3.jpg){Versione 3, `797fc7e`. L'avviso non c'è più.}
:::

:::cambio
Su richiesta del gruppo (D-42) sono stati tolti avvisi, FAQ «Questo sito è reale?» e 41 segnaposto «[DA VERIFICARE con l'Ateneo]», sostituiti da informazioni stabilite. La pagina è più pulita, ma il sito ha perso la dichiarazione della propria natura: ne discutiamo in §5.
:::

### Problemi individuati negli output

Tabella: Problemi trovati negli output del sito
| Problema nell'output | Come ce ne siamo accorti | Richiesta o intervento | Esito |
|---|---|---|---|
| FAQ: 21 link identici «Link a questa risposta» | `tools/verifica-link.py` | Testo nascosto con la domanda | Corretto, `e1ebd20` |
| CLS 0,30 su elenco e progetto, 0,59 sulla donazione | Lighthouse | Menu nascosto da CSS; spazio riservato (D-32) | CLS 0 |
| FAQ e progetto senza testi per i messaggi: errori vuoti, modulo inviabile senza controlli | `tools/percorsi.js` | Testi dell'interfaccia separati (D-30) | Corretto |
| Ricerca: «api» trova «capire»; poi «veterinaria» non trova nulla | Screenshot di `percorsi.js`; valutazione euristica V-01 | Due correzioni (D-33) | Corretto |
| Colonna fissa più alta dello schermo: contatto irraggiungibile | Verifiche della Fase 4 | Colonna non più fissa (D-31) | Corretto, con R-042 parziale per scelta |
| Riquadro del raddoppio senza link alle regole | Valutazione euristica V-02 | Aggiunto il link | Corretto, `60712ad` |
| Transizioni animate: errori in console | `tools/percorsi.js` | Scartate (D-39) | Corretto |
| Ripresa della donazione su un altro dispositivo impossibile (V-03, J02) | Valutazione euristica | Richiederebbe account, esclusi | **Aperto** |
| `08_verifica_personas.md` e `09_valutazione_euristica.md` riportano ancora segnaposto e Lighthouse 100 | Rilettura per questa relazione, 03/11/2026 | Da aggiornare | **Aperto** |
| P-021, P-064, P-079 passano da «parziale» a «risolto» senza nuove fonti | Confronto di `tools/soluzioni.py` tra `f0988ba` e `797fc7e` | Da riconsiderare (§5) | **Aperto** |

Lo screenshot `donazione-errore-importo.png`, citato come prova in `08_verifica_personas.md`, nella versione attuale mostra il passo 1 senza il messaggio d'errore, che resta fuori dall'inquadratura. La prova è il controllo automatico di `percorsi.md`.

### Richieste di modifica e interventi

Il registro `website/docs/decisioni.md` distingue le proposte dell'agente dalle scelte del gruppo. Le richieste sono note da questa sintesi, non dalle conversazioni. [DA COMPLETARE: testo delle richieste per redesign, D-40, D-41 e D-42, se disponibile]

Tabella: Che cosa ha proposto l'agente e che cosa ha deciso il gruppo
| Tema | Proposta dell'agente | Decisione del gruppo | Prova |
|---|---|---|---|
| Nome | «Sostieni la Ricerca» | **ideaBlume** | D-08, D-20 |
| Pagine | Almeno 10, come da consegna | Almeno 12 | D-23, R-133 |
| Contatti | Dominio `example.org` | Fittizi ma credibili: `@ideablume.it`, numero di Torino | D-16, D-22 |
| Pubblicazione | Sito apribile da `file://` (D-01) | Anche pubblicato su GitHub Pages | D-21 |
| Date delle campagne | Date relative a oggi | Confermate al checkpoint 2 | D-24 |
| Design | Prugna «lontano dall'arancione» (`38a1910`) | Prima «più moderno», poi palette calda | D-35, D-40 |
| Tema | Automatico dal sistema (D-38) | Chiaro predefinito con interruttore | D-41 |
| Contenuti | Segnaposto e avvisi | Eliminati, informazioni stabilite | D-42 |

### Revisione di contenuti, struttura, navigazione e interazioni

#### Contenuti

Le informazioni istituzionali non presenti nelle fonti erano inizialmente segnate come da verificare (D-10, D-12–D-15) e sono state poi fissate da D-42. Il lessico è controllato da `tools/verifica-dati.py`: niente gergo, importi in una sola forma (D-34). I numeri vengono da un'unica fonte, `data/progetti.json`, per evitare l'incoerenza di contatori trovata in assignment 1.

#### Struttura

Il principio guida di `website/docs/06_architettura.md` è «prima i progetti da sostenere, poi le regole, poi i servizi per chi propone», l'opposto di quanto osservato su IdeaGinger. Il programma dell'Ateneo diventa una voce di primo livello. La v2 di P12 ha portato a una sezione per enti esterni e al modulo «Proponi una collaborazione» (R-076): è un caso in cui la revisione delle personas ha cambiato il sito. La versione inglese è completa, generata dagli stessi modelli in `en/` (D-21); restano in lingua originale solo i commenti dei sostenitori, marcati con `lang` (D-28).

#### Navigazione

Il menu passa dalle oltre 70 voci di IdeaGinger a 7 voci senza tendine, con la ricerca sempre visibile (D-25) e un menu mobile gestibile da tastiera. Tornando dall'elenco, filtri e posizione restano (P-027). Su telefono l'intestazione è stata compattata perché andava su tre righe a 375 px (D-36).

:::figure2 | stretta
![Home a 375 pixel: intestazione su una riga, ricerca, titolo e frase che spiega il servizio.](home-375.jpg){Home a 375 px.}
![Menu mobile aperto a 375 pixel con le sette voci in un elenco.](menu-mobile-375.png){Menu mobile a 375 px con le 7 voci.}
![Pagina di un progetto a 375 pixel: tema, titolo, gruppo, responsabile e riquadro dello stato.](progetto-375.jpg){Pagina progetto a 375 px.}
:::

#### Interazioni

La donazione è un percorso in 5 passi con validazione all'uscita dal campo, riepilogo degli errori con focus, dati conservati e «Modifica» nel riepilogo. Le campagne concluse non hanno controlli attivi. Il badge «Obiettivo raggiunto · puoi ancora sostenerlo per N giorni» risponde direttamente al dubbio di Franco e Giuseppe.

:::figure2
![Passo 2 della donazione: riquadro rosso con il focus, «C'è 1 campo da correggere», e link al campo Email.](donazione-riepilogo-errori.png){Riepilogo degli errori con focus e correzione proposta (`percorsi.js`).}
![Risultati della ricerca «api»: due progetti pertinenti e anello di focus sulla prima card.](ricerca-api-focus.png){Ricerca «api» da tastiera: 2 risultati e focus visibile sulla card.}
:::

### Modifiche apportate direttamente al codice dal gruppo

Il gruppo dichiara di aver modificato a mano **didascalie e design**. Queste modifiche sono confluite in `797fc7e` insieme al lavoro dell'agente e non si possono separare dalla sola cronologia. [DA COMPLETARE: una o due modifiche concrete a didascalie e design, con file e riga, da mostrare come diff] La modifica manuale che possiamo dimostrare è una riga fatta dall'interfaccia web di GitHub.

:::diff | Codice modificato a mano | `.github/workflows/sito.yml`, commit `dd07a0a`, 01/11/2026
 on:
   push:
-    branches: [assignment2-sito]
+    branches: [main]
:::

Serve a pubblicare il sito dal branch che abbiamo scelto. Lo stash `6a32c9f` conserva inoltre un tentativo manuale di accorciare un suggerimento in `i18n/it.json` («Minimo {min} per la scelta fatta. Puoi donare di più.»), non applicato: il testo attuale è quello originale.

### Motivazioni delle scelte finali

- **Sito statico senza server e senza framework.** Lo impone `Istruzioni.md` §7 B, che ha prevalso sul prompt (D-01). Serve anche alle prestazioni su mobile, un problema grave di IdeaGinger: LCP della pagina progetto da 34,1 s a 2,3 s in laboratorio (`verifiche/prestazioni.md`).
- **Pagine generate da un'unica fonte** (`tools/build.py`), per avere numeri coerenti e inglese completo.
- **Nessun nome reale per il programma.** «Funds TOgether» è stato evitato per «non presentare come reali informazioni inventate» sotto il nome di un'iniziativa vera (D-09). Vale anche per i marchi: nessun logo di IdeaGinger o dell'Università (D-20).
- **Un solo accento per l'azione di donare**, perché «Sostieni il progetto» resti il punto più visibile (D-40).

Tabella: Estratto della tracciabilità problema → soluzione (`website/docs/05_tracciabilita.md`)
| Problema | Fonte | Personas | Soluzione | Verifica | Stato |
|---|---|---|---|---|---|
| P-001 Nessuna frase che dica che cos'è il servizio (G4) | Slide 59 | J01, J07, J12 | Frase iniziale in home e nel programma | Screenshot `home-1280`, `home-375` | Risolto |
| P-008 Menu con oltre 70 voci (G2) | Slide 67 | J03, J11, J12 | 7 voci senza tendine; `aria-expanded`, Esc | `percorsi` #34–37 | Risolto |
| P-022 Oltre il 100% senza etichetta (G3) | Slide 10 | J01, J05, J10 | Badge con icona e testo | `dati.md`, `percorsi` #29 | Risolto |
| P-029 Card che non sembrano cliccabili (G4) | Slide 17 | J03 | Titolo come unico link esteso alla card | `percorsi` #4 | Risolto |
| P-056 Il promotore riceve i dati anche con l'anonimato (X03) | **Solo C00: nessuna fonte** | J06 | Il sito lo dichiara prima dell'invio | `08`, J06-F5 | «Risolto», ma non verificato |

La copertura dichiarata è di 87 problemi risolti e 3 non applicabili su 90. Fino a `f0988ba` era 84, 3 parziali e 3 non applicabili: il dato più prudente è il secondo, per i motivi di §5. Le verifiche attuali danno 0 violazioni axe su 58 pagine, 66/66 percorsi da tastiera, 394/394 controlli sui dati e Lighthouse mobile 95–98 per le prestazioni e 100 per l'accessibilità (`website/docs/verifiche/README.md`). Sono controlli automatici in Chrome, non una prova di usabilità con persone.

## Uso responsabile dell'IA

Il gruppo dichiara di aver usato l'IA in modo responsabile. In questa sezione controlliamo quella dichiarazione sulle prove: indichiamo dove regge e dove no.

:::responsabile | Supervisione umana
L'IA ha prodotto bozze e proposte; le scelte di progetto sono passate dal gruppo. Per le personas: l'iterazione di revisione di Alex (§3.5) e le note di Lorenzo Rizzolo con le decisioni da prendere insieme. Per il sito: i checkpoint (`decisioni.md`), con proposte che il gruppo ha cambiato (§4.5), e gli script di verifica. Il limite è dichiarato in `09_valutazione_euristica.md`: «chi valuta ha anche progettato il sito». Non abbiamo prove dell'esecuzione di V00.
:::

:::responsabile | Fondamento nei dati
Le personas derivano dal catalogo dei problemi di assignment 1 e i requisiti dai 90 problemi consolidati, con la fonte per ciascuno. Le personas sono **proto-personas**, senza ricerca con utenti, e lo dichiariamo. La verifica `08_verifica_personas.md` è un cognitive walkthrough, non un test con utenti. Progetti, persone, recapiti e importi del sito sono inventati, e lo dichiariamo in questa relazione.
:::

:::responsabile | Errori e allucinazioni
Abbiamo trovato affermazioni senza fondamento in entrambe le direzioni.
- Dall'IA: due affermazioni su P12 assenti dalla presentazione, rimosse; «ogni euro vale doppio» in P10, corretto; ricerca che sembrava funzionare, corretta dopo i test.
- Dai nostri materiali, segnalate dall'agente: X03 non compare in nessun file di assignment 1 (D-06); il prompt attribuiva la pagina 404 a link rotti, mentre era stata ottenuta digitando un indirizzo errato (D-07).
- Nella nostra presentazione: la soglia di contrasto errata a slide 23 e un conteggio sbagliato a slide 80, nelle note di revisione di `README.md`.
:::

:::responsabile | Stereotipi e inclusione
C00 (regola 6) e i prompt chiedono di evitare stereotipi: per P07, «senza stereotipi: sui social è molto abile». Il controllo non si è fermato ai prompt: nonostante l'istruzione «Non descriverlo come incapace», Alex ha trovato e corretto «Giuseppe è poco capace con la tecnologia»; Lorenzo Rizzolo ha ridotto l'aiuto del figlio di P12 a strategia di accessibilità. La matrice evita alcune associazioni scontate: Davide, cieco, ha familiarità 5/5; Elena, 58 anni, 4/5; Maria, 49 anni, 2/5. Restano però i due profili più anziani con familiarità 2/5 e l'archetipo «il nonno generoso ma prudente» nel prompt P01. [DA COMPLETARE: quali controlli su genere e provenienza, per esempio su P04 e P11]
:::

:::responsabile | Privacy e proprietà intellettuale
Le personas sono fittizie e i nomi inventati. Il sito non invia dati a un server e non chiede numeri di carta: i moduli restano nel browser (`website/README.md`, «Limiti tecnici»). Non usa loghi di IdeaGinger o dell'Università (D-20) e i font sono open source con licenza inclusa (D-35). Le commissioni riprendono però le tariffe delle FAQ di IdeaGinger (D-12, D-42), e nessuno script controlla che non ci siano testi copiati. [DA VERIFICARE: conferma esplicita che agli strumenti non siano stati forniti dati personali reali, compresi quelli eventualmente presenti negli appunti]
:::

:::avviso | Il punto critico: il sito pubblicato non dichiara di essere fittizio
Fino a `f0988ba` il sito diceva di essere un prototipo didattico, avvisava che il pagamento era simulato e marcava le informazioni non verificate. Con D-42, su richiesta del gruppo, tutto questo è stato tolto, e `tools/verifica-dati.py` ora controlla che quelle parole non ricompaiano.

Il 03/11/2026 abbiamo controllato https://andreock.github.io/hci_gruppo_a/ (home, donazione, FAQ, chi siamo). Il sito si presenta come «gestito dall'Ufficio ideaBlume dell'Ateneo», afferma che la donazione all'Università «è deducibile dal reddito», indica un telefono di Torino e una sede inventati, e nessuna di queste pagine dice che si tratta di un'esercitazione. Queste informazioni non vengono da fonti: le ha stabilite il gruppo in D-42, e riguardano un ente reale.

Di conseguenza non possiamo presentare questa scelta come buona pratica: i tre problemi passati a «risolto» non hanno nuove prove, e un visitatore potrebbe scambiare il sito per un servizio dell'Università. [DA VERIFICARE: il gruppo ripristina un avviso e toglie l'affermazione fiscale, oppure conferma D-42 motivandola; aggiornare questo riquadro di conseguenza]
:::

:::responsabile | Trasparenza
Questa relazione dichiara strumenti, prompt e limiti. È stata scritta con **Claude Code (Claude Opus 5.5)** a partire dal prompt REL-AI-01 (Appendice B), che imponeva di citare una prova per ogni affermazione e di non inventare prompt o versioni. L'agente ha letto il repository e scritto testo e script; il gruppo ha fornito nominativi, strumenti, link e dichiarazioni. [DA COMPLETARE: chi ha riletto la relazione e che cosa ha modificato]
:::

:::responsabile | Limiti dell'IA e del nostro uso
- La conformità alle istruzioni non è garantita: la prima formulazione di P01 contraddiceva l'indicazione del prompt.
- Gli indicatori generati possono sembrare migliori dei fatti: 87 «risolti» su 90.
- La documentazione generata invecchia: `08` e `09` non sono stati aggiornati dopo D-42.
- Gli strumenti non sostituiscono le persone: Safari, Firefox, NVDA e VoiceOver reali e test con utenti restano da fare (`website/README.md`).
- Non abbiamo salvato le conversazioni, quindi non possiamo documentare molte richieste. È un limite nostro, non degli strumenti.
:::

## Contributo del gruppo

Tabella: Contributi risultanti dalle prove (corrispondenza tra account git e persone da confermare)
| Persona | Personas e journey | Sito e altro |
|---|---|---|
| Andrea Canale | Commit dei prompt C00, Pxx, Jxx, V00 e di `README.md` (`fb0a77b`, `c264a64`, `2971d53`); template HTML (`b5012db`, `9f46b94`); caricamento di P04–P06 (`f547471`) | Lavoro con l'agente sul sito (`4baa4e9`…`60712ad`, `f0988ba`, `797fc7e`), pubblicazione (`dd07a0a`) |
| Alexandru Ioan Chindris | P01–P03, J01–J03, generatore HTML, `alex/documentazione_uso_ai.md` (`6767c88`, `34ebd76`) | [DA COMPLETARE: contributo al sito] |
| Antonio Fallea | P07–P09, J07–J09 (`a941518`), revisione delle schede (`d3e3440`) | [DA COMPLETARE: contributo al sito] |
| Lorenzo Rizzolo | P10–P12, J10–J12, `Istruzioni.md` nel repository, note di revisione (`d6feb95`, `1b2f2c9`, `86536bf`) | [DA COMPLETARE: contributo al sito] |

**Decisioni che sono state solo del gruppo.** Ridefinizione di P12 e differenza tra P10 e P11, proposte da Lorenzo Rizzolo e ancora da ratificare; nome ideaBlume; almeno 12 pagine; contatti credibili; pubblicazione su GitHub Pages; palette calda; interruttore del tema; rimozione di avvisi e segnaposto (D-42); ritocchi manuali a didascalie e design.

## Conclusioni

**Che cosa ha funzionato.** Separare contesto comune e prompt singoli ha permesso di generare in parallelo documenti con lo stesso formato. La tracciabilità ha tenuto le soluzioni del sito agganciate ai problemi di assignment 1. Gli script hanno trovato difetti reali (§4.4). Il confronto ai checkpoint ha prodotto scelte diverse da quelle proposte dall'agente, e in più casi l'agente ha fatto emergere errori nelle nostre stesse fonti.

**Limiti.** Non ci sono test con utenti: personas e soluzioni restano ipotesi. La maturità delle personas è disomogenea, con J07–J09 mai rivisti e la revisione di P07–P09 fuori da `main`. Chi ha valutato il sito è anche chi lo ha progettato. Le decisioni aperte non sono state chiuse formalmente. Con D-42 il sito ha perso la trasparenza verso chi lo visita (§5).

**Che cosa faremmo diversamente.** [DA COMPLETARE: riflessione del gruppo] Dalle prove emergono almeno tre indicazioni: salvare fin dall'inizio prompt e output grezzi, compresi quelli del sito; unire le revisioni in un solo branch prima di costruirci sopra; rigenerare insieme tutti i documenti di verifica quando una decisione li cambia.

## Appendice A · Prove citate

Tabella: Commit citati
| Commit | Data | Autore | Contenuto |
|---|---|---|---|
| `fb0a77b` | 27/10/2026 | Andrea Canale | Prima versione di C00, Pxx, Jxx, V00 |
| `c264a64` | 27/10/2026 | Andrea Canale | C00 allineato ai template del corso |
| `b5012db`, `9f46b94` | 27/10/2026 | Andrea Canale | Template HTML (interfaccia web) |
| `a941518` | 27/10/2026 | Antonio Fallea | P07–P09, J07–J09, «Bozza 07 a 09» |
| `d6feb95`, `1b2f2c9` | 27/10/2026 | Lorenzo Rizzolo | P10–P12, J10–J12, `Istruzioni.md`, note |
| `2971d53` | 27/10/2026 | Andrea Canale | C00 e prompt v3 generici |
| `86536bf` | 27/10/2026 | Lorenzo Rizzolo | P10–P12, J10–J12 v2 |
| `f547471` | 29/10/2026 | Andrea Canale | P04–P06, J04–J06 |
| `6767c88`, `34ebd76` | 30/10/2026 | Alexandru Ioan Chindris | P01–P03, J01–J03, documentazione |
| `c67c067` | 30/10/2026 | Andrea Canale | Schede di Alex nelle cartelle comuni |
| `d3e3440` | 31/10/2026 | Antonio Fallea | P07–P09 v2 (solo su `assignment1-valutazione-euristica`) |
| `4baa4e9`, `38a1910`, `56e2a95`, `e1ebd20`, `60712ad` | 31/10/2026 | Andrea Canale con Claude Opus 5.5 | Sito: fonti, architettura, codice, verifiche, chiusura |
| `f0988ba`, `dd07a0a` | 01/11/2026 | Andrea Canale | Redesign e Action; trigger modificato a mano |
| `6a32c9f` | 01/11/2026 | Andrea Canale | Stash non applicato |
| `797fc7e` | 03/11/2026 | Andrea Canale | Versione finale del sito |

**File principali.** `Istruzioni.md`; `README.md`; `00_contesto_comune_C00.md`; `99_verifica_V00.md`; `personas/`; `alex/documentazione_uso_ai.md`; `personas/da_rivedere_P10-P12.md`; `website/README.md`; `website/docs/01`–`09`; `website/docs/decisioni.md`; `website/docs/verifiche/`; `.github/workflows/sito.yml`. L'elenco completo, con ciò che ogni prova dimostra, è in `relazione/00_inventario_prove.md`.

## Appendice B · Prompt

I prompt completi di personas e journey sono in `00_contesto_comune_C00.md` e `personas/P01…P12*.md`. Quelli di P01–P03 sono in §3.2. Riportiamo V00 per i criteri e un estratto del prompt di questa relazione.

:::prompt | Prompt · V00, verifica di un documento generato (estratto) | {{Personas}} {{Journey}} · `99_verifica_V00.md`
1. Struttura: front matter completo; titoli e ordine delle sezioni identici a <formato_persona> o <formato_journey>.
2. Citazioni: ogni problema assegnato nel prompt originale è citato; ogni citazione esiste nel catalogo C00 con criterio e gravità corretti; problemi_citati coincide con gli ID presenti nel testo.
3. Fedeltà: nessun problema del sito inventato; le ipotesi sono marcate [IPOTESI]; nessun numero, URL o nome reale inventato.
4. Coerenza con la scheda vincolante: età, dispositivo, familiarità, accessibilità e frequenza rispettati.
5. Journey: fasi della tabella uguali al front matter; punteggi della curva emotiva uguali alla riga Emozioni; ogni difficoltà ha un'opportunità; touchpoint e canali non confusi.
6. Terminologia HCI corretta (usabilità e UX, affordance e signifier, touchpoint e canale, euristiche di Nielsen).
7. Rispetto nella descrizione delle esigenze di accessibilità, senza stereotipi.
:::

:::prompt | Prompt · REL-AI-01, relazione sull'uso dell'IA (estratto) | {{Trasversale}} · conversazione con Claude Code del 03/11/2026
2. Ogni affermazione sull'evoluzione del lavoro deve poggiare su una prova che hai aperto: un file, una versione nella cronologia git, un commit, un documento di decisioni o di verifica. Cita la prova (percorso del file, hash breve del commit, data).
3. Non inventare prompt, conversazioni, prime versioni, problemi o interventi. Se una prova manca (per esempio la prima versione di una persona non è stata salvata), scrivi un segnaposto evidente «[DA COMPLETARE: …]» che dica al gruppo cosa serve, e raccoglilo nell'elenco finale delle informazioni mancanti.
4. Distingui sempre il contributo dell'IA da quello del gruppo: cosa ha proposto lo strumento, cosa il gruppo ha controllato, scartato, corretto o deciso.
:::
