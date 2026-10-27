---
documento: persona_journey_prompts
prompt_ids: [C00]
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
---

# C00 · Contesto comune

Questo è il contesto condiviso da tutti i prompt delle 12 personas e dei 12 journey. Va incollato **all'inizio di ogni conversazione**, prima del prompt singolo (Pxx, Jxx o V00). Contiene il contesto del sito, la terminologia degli appunti, il catalogo dei problemi della presentazione (con ID = numero di slide), gli aspetti positivi, i fatti integrativi, le regole e i formati di output.

**Template obbligatori.** Persone e journey vanno prodotti con i template del corso: la «Scheda persona» ([template/scheda_persona.pdf](template/scheda_persona.pdf)) e la «Scheda user journey» ([template/scheda_user_journey.pdf](template/scheda_user_journey.pdf)). **Allega il PDF giusto alla conversazione** insieme al prompt: la scheda persona per i prompt Pxx, la scheda user journey per i prompt Jxx. Se non puoi allegarlo, il contesto riproduce comunque la struttura dei due template.

Il testo da copiare è quello dentro il blocco di codice.

<!-- BEGIN PROMPT id="C00" tipo="contesto_comune" richiede="" -->
````text
<prompt id="C00" tipo="contesto_comune">

<ruolo>
Sei un ricercatore UX esperto di Human-Computer Interaction che collabora con un gruppo di studenti universitari del corso di HCI. Scrivi in italiano, con stile accademico, preciso e concreto. Mantieni i termini tecnici inglesi diffusi nella letteratura HCI (persona, journey map, touchpoint, feedback, screen reader…).
</ruolo>

<compito_generale>
Il gruppo sta producendo 12 personas (P01–P12) e 12 journey map (J01–J12) per il sito di crowdfunding IdeaGinger, nel contesto dell'iniziativa Funds TOgether dell'Università di Torino. Ogni documento viene generato da una persona diversa in una conversazione separata: per questo tutti i documenti devono seguire esattamente gli stessi formati, definiti più sotto.
In questa conversazione genererai UN SOLO documento: quello indicato dal prompt Pxx o Jxx che riceverai dopo questo contesto.
Le personas e i journey servono a far emergere, in modo realistico e motivato, i problemi di usabilità rilevati dal gruppo nella sua valutazione euristica (catalogo qui sotto).
</compito_generale>

<contesto_sito>
- IdeaGinger (ideaginger.it, marchio «Ginger») è una piattaforma italiana di crowdfunding per progetti sociali, culturali e di ricerca. In homepage mostra 29 progetti reali, le sezioni «Scelti per te», «SOSTIENILI ORA», «Per ispirarti» (progetti conclusi, ma non indicato), il blog «Il Gingerino», l'Academy, un podcast, il servizio di campaign manager, il menu «Partner», «CERCA PROGETTI» e «LANCIA UNA CAMPAGNA».
- Funds TOgether è l'iniziativa di crowdfunding dell'Università di Torino su Ginger: i ricercatori UniTo candidano progetti, l'Ateneo ne seleziona alcuni (fino a 5 nel 2026, quarta edizione) e li accompagna; se un progetto raggiunge l'obiettivo, UniTo cofinanzia raddoppiando la cifra fino a 10.000 € per progetto. I cittadini sostengono i progetti con donazioni.
- La pagina partner UniTo ha due schede: «Partnership» (descrizione dell'iniziativa, fasi, contatori, pulsanti «Scopri tutti i progetti!» e «Scopri la guida dell'iniziativa», che porta su unito.it) e «Progetti» (18 campagne divise in «in corso» e «conclusi», con pulsante «ALTRI»).
- Progetti in corso citati nella presentazione: MILK-ACT (181% raccolto), Mind the Climate (scadenza 17/11/2026), RePatch (109%), NanoStop, VIBE. Progetti conclusi analizzati: BRIGHT, MatematIcA senza barriere, Fai Brillare la Ricerca!
- Pagina progetto: box di stato con percentuale, raccolto, obiettivo, sostenitori e scadenza; formula «O tutto o niente!»; categorie e obiettivi ONU (SDG); schede Progetto, News, Commenti, Sostenitori, Condividi; «Conosci il progettista» e «Contatta il progettista»; colonna «SOSTIENI» con le ricompense (importo minimo, posti rimasti) e la ricompensa a importo libero «FAI TU»; pulsante «Sostieni il progetto»; modulo di donazione con casella «donatore anonimo».
- Pagine per chi vuole lanciare una campagna: «Come funziona» (testo continuo con 7 immagini: contatti, formazione, campaign manager, costi, raccolta, dopo la campagna), FAQ (25 domande in un'unica lista), registrazione all'area progettisti (5 campi: username, password, email e due conferme; consenso obbligatorio, newsletter facoltativa, reCAPTCHA).
- Da smartphone le quattro pagine del percorso del donatore (Partnership, Progetti, Mind the Climate, modulo di donazione) non superano i Core Web Vitals: LCP 3,4 s contro la soglia di 2,5 s.
</contesto_sito>

<riferimenti_teorici_dagli_appunti>
Usa questa terminologia, coerente con gli appunti del corso:
- Persona: archetipo che rappresenta le caratteristiche essenziali comuni a un tipo di utente, il suo comportamento e il suo modo di pensare mentre usa il servizio; serve al team per ipotizzare soluzioni concrete. Sezioni: informazioni del profilo (dati anagrafici), motto (frase che rappresenta l'attitudine), comportamenti (abitudini e difficoltà nell'uso del servizio), frequenza d'uso del servizio, familiarità con gli strumenti digitali, strumenti di riferimento.
- Journey map: rappresenta l'esperienza di una persona lungo un percorso verso un obiettivo specifico, collegando fasi, azioni, pensieri, emozioni, touchpoint, canali e difficoltà. Per ogni difficoltà ipotizzata occorre cercare una soluzione.
- Touchpoint: momento in cui la persona interagisce con il servizio (es. iscrizione, scelta della ricompensa). Canale: mezzo attraverso cui avviene il touchpoint (sito da desktop, sito da smartphone, email, telefono, social). Un canale può ospitare più touchpoint. Tra touchpoint va garantita continuità (non chiedere di nuovo dati già inseriti, non perdere lo stato).
- Concetti utilizzabili quando pertinenti, senza forzarli: ciclo dell'azione di Norman e golfi dell'esecuzione e della valutazione; modello mentale contrapposto al modello concettuale; carico sulla memoria e riconoscimento anziché ricordo; tipi di attenzione (automatica, sostenuta, selettiva, divisa); principi della Gestalt; banner blindness; gerarchia visiva e piega della pagina; ricerca conosciuta, esplorativa ed esaustiva; modello del berrypicking; regole di Shneiderman; framework HEART; accessibilità.
- Distingui con cura: usabilità e UX; efficacia ed efficienza; affordance e signifier; touchpoint e canale.
</riferimenti_teorici_dagli_appunti>

<catalogo_problemi>
Problemi rilevati nella presentazione «Funds TOgether: analisi di usabilità» (Gruppo A, 82 slide). ID = numero di slide del PDF. Criterio: H1–H10 = euristiche di Nielsen; LG1–LG10 = NN/g Top 10 Homepage Guidelines. Gravità: G1 superficiale, G2 minore, G3 importante, G4 grave.

AREA A · Pagina partner UniTo (Partnership e Progetti)
- S09 · H1 · G3 · Stato dell'iniziativa non chiaro: testi al futuro («verranno selezionati»), nessuna data di candidatura o di campagna, blog con articoli del 2021–2022. Soluzione: dire se le call 2026 sono aperte o chiuse; aggiornare o nascondere il blog.
- S10 · H1 · G3 · I progetti in corso oltre il 100% (MILK-ACT 181%, RePatch 109%) non hanno un badge «obiettivo raggiunto»: lo stato è affidato al colore; il donatore non capisce se la sua donazione serve ancora. Soluzione: badge «Obiettivo raggiunto · raccolta ancora aperta» con testo e icona.
- S11 · H2 · G2 · I giorni rimanenti sono scritti come numero negativo («-36 giorni»): le campagne sembrano scadute. Soluzione: «36 giorni rimasti».
- S12 · H2 · G2 · Gergo e inglese non spiegati («Overfunding», «369% OVERFUNDING», «100% SUCCESSO», «Partnership», «by»); traduzione del sito incompleta, didascalie IT con sotto EN. Soluzione: tooltip, internazionalizzazione completa.
- S13 · H2 · G2 · Dagli autori («by Departments & Dragons», «by Team GaIA») non si capisce che sono gruppi di ricerca UniTo. Soluzione: convenzione «NomeGruppo – UniTo».
- S14 · H3 · G3 · «Scopri tutti i progetti!» apre una nuova scheda (il tasto Indietro non riporta alla descrizione); «Scopri la guida dell'iniziativa» porta su unito.it senza icona di link esterno. Soluzione: link interni nella stessa scheda, icona per i link esterni.
- S15 · H3 · G4 · Tornando indietro da un progetto si perdono la posizione di scorrimento e i progetti caricati con «ALTRI». Soluzione: conservare lo stato o usare una paginazione.
- S16 · H4 · G2 · Barre di avanzamento poco chiare; il contatore «18 progetti» non distingue attivi e conclusi; il chip «Obiettivo raggiunto» compare solo sui conclusi. Soluzione: un solo colore pieno su sfondo neutro e un chip testuale.
- S17 · H4 · G4 · Al passaggio del mouse le card non sembrano cliccabili e non hanno aria-label: chi usa uno screen reader non riesce ad andare avanti. Soluzione: hover evidente, pulsante «Scopri il progetto», aria-label.
- S18 · H6 · G2 · La card non indica il tema o la categoria del progetto. Soluzione: categoria sotto il titolo.
- S19 · H6 · G1 · Piccola icona «casetta» senza etichetta prima del logo, che duplica il link alla home. Soluzione: rimuoverla.
- S20 · H7 · G3 · Manca un pulsante «Torna su» nelle pagine lunghe. Soluzione: pulsante fisso con icona ed etichetta.
- S21 · H7 · G3 · Nessun filtro né ordinamento dei progetti UniTo (categoria, SDG, edizione, scadenza). Soluzione: filtri e paginazione.
- S22 · H7 · G3 · «ALTRI» carica al massimo 4 progetti per volta e non dice quanti ne restano (13 conclusi, 3 clic). Soluzione: paginazione.
- S23 · H8 · G4 · Contrasto insufficiente: titoli arancioni circa 2,5:1, pulsanti verdi con testo bianco, footer circa 2:1 con titoli molto piccoli, chip con testo piccolo. Soluzione: scurire gli sfondi e ingrandire i titoli (soglia WCAG AA corretta per il testo normale: 4,5:1).
- S24 · H9 · G2 · A fine elenco «ALTRI» scompare senza dire che i progetti sono finiti. Soluzione: «Hai visto tutti i progetti conclusi».
- S25 · H10 · G2 · La pagina non dice chi può candidarsi, entro quando e con quale modulo, e non riporta un contatto UniTo. Soluzione: email di contatto e sezione sulla selezione.

AREA B · Pagine progetto e donazione
- S28 · H1 · G3 · «Contatta il progettista» mostra i contatti dopo diversi secondi senza indicatore di caricamento: sembra non aver preso il clic. Soluzione: feedback immediato o contatti già presenti.
- S29 · H1 · G3 · Sui progetti conclusi (BRIGHT, Fai Brillare la Ricerca!, MatematIcA) il box «SOSTIENI» con le ricompense e i prezzi resta visibile, il campo «FAI TU» è ancora scrivibile, mancano i pulsanti e lo stato è un pallino rosso senza legenda. Soluzione: nascondere il box o pulsante grigio con tooltip «campagna conclusa».
- S30 · H2 · G2 · In BRIGHT gli aggiornamenti («Nuovo obiettivo», «Secondo obiettivo») precedono la presentazione del progetto. Soluzione: link alle news e poi la descrizione.
- S31 · H3 · G3 · Le 10 ricompense di BRIGHT sono un lungo elenco verticale con immagini, testo bilingue e contatori, non comprimibile né confrontabile. Soluzione: elenco compatto espandibile, tabella di confronto.
- S32 · H4 · G4 · In inglese cambia solo la panoramica del progetto (rimanda alla sezione News); il resto resta in italiano con testi sovrapposti; mancano SDG e formula «tutto o niente». Soluzione: versione inglese completa, selezionabile o automatica.
- S33 · H4/H10 · G1 · I tooltip («O tutto o niente!», obiettivi di sostenibilità) sembrano link e il browser li tratta come tali. Soluzione: icona «?».
- S34 · H4 · G1 · Le ricompense più alte non mostrano il contatore dei sostenitori; ordine delle ricompense e delle sezioni diverso tra progetti. Soluzione: contatore sempre visibile, ordine crescente.
- S35 · H4 · G3 · La pagina di MatematIcA senza barriere non è accessibile: immagini descrittive senza alt, titoli vuoti e h4 usati per formattare. Soluzione: testi alternativi e HTML semantico.
- S36 · H4 · G2 · Nel box «SOSTIENI» ogni progetto dispone italiano e inglese in modo diverso. Soluzione: un unico modello.
- S37 · H6 · G3 · Il raddoppio di UniTo non è rappresentato nell'interfaccia vicino al punto in cui si dona. Soluzione: barre che mostrano il raddoppio.
- S38 · H7 · G4 · La pagina progetto è molto lunga, senza indice, ancore né «Torna su» (Mind the Climate, MILK-ACT). Soluzione: indice laterale e pulsante «Torna su».
- S39 · H7 · G1 · Il clic sulla barra dell'obiettivo ricarica la stessa pagina. Soluzione: barra non cliccabile.
- S40 · H8 · G2 · Ogni ricompensa ripete il testo in italiano e in inglese; in MatematIcA ogni fascia compare due volte. Soluzione: selettore IT/EN, una lingua alla volta.
- S41 · H9 · G4 · Gli errori del modulo di donazione (es. importo sotto il minimo) compaiono solo dopo l'invio e solo in italiano; la regola «tutto o niente» non è richiamata nel modulo. Soluzione: validazione in linea nella lingua dell'utente e richiamo della regola.
- S42 · H5 · G2 · Il nome del donatore diventa pubblico se non si spunta «donatore anonimo», che non è selezionata. Soluzione: due pulsanti radio obbligatori senza scelta preimpostata.

AREA C · Percorso di chi vuole lanciare una campagna
- S45 · H1 · G2 · Nel modulo di registrazione i consensi (obbligatorio e newsletter) sembrano caselle di spunta ma sono pulsanti senza ruolo né stato: problemi con gli screen reader. Soluzione: vere checkbox o role="checkbox" con aria-checked.
- S46 · H2 · G2 · «Come funziona» usa «campaign manager», «call di consulenza», «fee di accesso» senza spiegarli. Soluzione: termini italiani, tooltip o glossario.
- S47 · H3 · G2 · Le pagine nominano il passo successivo senza portarci: la FAQ dice di andare su «Lancia una campagna» senza link; il link «commissioni» apre le Condizioni d'uso. Soluzione: collegare i testi alle pagine giuste.
- S48 · H4 · G1 · La stessa modalità di raccolta si chiama «Prende ciò che raccoglie» in «Come funziona» e «keep it all» nelle FAQ. Soluzione: una sola formula.
- S49 · H5 · G4 · La quota di 350 € + IVA per pubblicare è nascosta alla fine di un paragrafo, senza grassetto e in corpo piccolo: chi legge in fretta la scopre durante l'iscrizione. Soluzione: sezione costi con titolo e testo evidente.
- S50 · H5 · G2 · Il modulo di registrazione non usa i controlli del browser: campi non obbligatori, email come testo semplice, autocompletamento disattivato (su mobile niente tastiera email). Soluzione: required, type corretti, autocompletamento.
- S51 · H6 · G3 · Nel modulo di registrazione le etichette sono solo segnaposto: spariscono appena si scrive e per lo screen reader il campo resta senza nome. Soluzione: etichette visibili e attributi ARIA su requisiti ed errori.
- S52 · H7 · G3 · «Come funziona» è un testo continuo: 7 sezioni senza titoli, separate da immagini con testo alternativo uguale al nome del file, senza indice. Soluzione: titoli di sezione e indice iniziale.
- S53 · H7 · G3 · Le 25 FAQ sono un'unica sequenza senza gruppi, indice né ricerca; domande per progettisti e donatori mescolate. Soluzione: due gruppi, Donatori e Progettisti.
- S54 · H8 · G4 · In «Come funziona» i testi sono troppo piccoli e di dimensione disomogenea, comprese le informazioni sui costi. Soluzione: corpo più grande e uniforme.
- S55 · H9 · G2 · Il messaggio di errore della registrazione resta visibile anche dopo aver corretto il campo, fino al nuovo invio. Soluzione: rimuoverlo appena il campo è valido, vicino all'input.

AREA D · Homepage di Ginger (NN/g Top 10 Homepage Guidelines)
- S59 · LG1 · G4 · La homepage non dice in una frase che cos'è Ginger (la descrizione è solo nella meta description). Soluzione: tagline visibile in alto.
- S60 · LG2 · G1 · Il titolo della finestra è lungo 83 caratteri (troncato su Google) e il marchio cambia nome («GINGER», «Idea Ginger»). Soluzione: titolo sotto i 70 caratteri, un solo nome.
- S61 · LG3 · G3 · «Chi siamo» è solo nel footer; i contatori non dicono chi gestisce la piattaforma, a scapito della credibilità. Soluzione: «Chi siamo» nella barra di servizio in alto.
- S62 · LG4 · G2 · Prima dei progetti da sostenere la homepage mostra quattro blocchi per progettisti (Academy, podcast, campaign manager, blog). Soluzione: progetti da sostenere nella prima schermata.
- S63 · LG5 · G1 · Nessun campo di ricerca in pagina: «Cerca tra tutti i progetti» è solo testo e «CERCA PROGETTI» apre un elenco di categorie. Soluzione: campo di ricerca sempre visibile.
- S64 · LG6 · G3 · Titoli delle card troncati («RePatch | il cerotto per il cuore …»); la sezione «Per ispirarti» non dice che i progetti sono conclusi. Soluzione: titoli su più righe, etichetta «Concluso».
- S65 · LG7 · G2 · Il link «Vai alla pagina» è ripetuto 25 volte nella sezione partner: con uno screen reader l'elenco dei link ha 25 voci uguali. Soluzione: link descrittivi.
- S66 · LG8 · G1 · Il blog in homepage è solo un invito, senza articoli né date. Soluzione: ultimi articoli con titolo e data.
- S67 · LG9 · G2 · Menu e tendine contano oltre 70 voci, ripetute nel footer; da tastiera le tendine non si chiudono con Esc e la X non si raggiunge. Soluzione: menu ridotto e pagina di esplorazione con filtri.
- S68 · LG10 · G1 · Il testo alternativo delle icone di categoria ripete l'etichetta accanto: lo screen reader legge due volte la stessa parola. Soluzione: alt vuoto sulle icone decorative.

AREA E · Mobile e prestazioni
- S71 · Mobile · G3 · Su smartphone i caroselli di contatori e progetti scorrono di lato senza frecce né pallini; si vedono 2 contatori su 5; «ALTRI» aggiunge una nuova fila con un altro «ALTRI». Soluzione: indicatori di posizione, ultima card tagliata a metà.
- S74 · Prestazioni (slide 74–78, nessuna gravità assegnata) · Da smartphone nessuna delle quattro pagine del percorso del donatore supera i Core Web Vitals (LCP 3,4 s, FCP 2,3 s, TTFB 1,6 s); punteggio Lighthouse Prestazioni su smartphone: Partnership 68, Progetti 50, Mind the Climate 41, modulo di donazione 39 (il più basso, proprio nel passaggio finale). Accessibilità Lighthouse tra 64 e 77 su tutte le pagine.
</catalogo_problemi>

<aspetti_positivi>
Da usare per dare realismo e momenti positivi alla curva emotiva. Citali come [S27 · positivo].
- S08 · Pagina partner: sezioni «in corso» e «conclusi» chiare; ogni card riassume percentuale, importo su obiettivo e donatori; linguaggio chiaro («raccolto», «donatori»); card uniformi; menu hamburger su mobile; FAQ, «Come funziona» e contatti sopra la navbar.
- S27 · Pagine progetto: box di stato completo con scadenza esplicita; breadcrumb cliccabile e schede sticky; ricompense con struttura uniforme e posti rimasti; pulsanti con attributi ARIA; «Copia link» e condivisione su vari canali; parole chiave in grassetto e infografiche; nella donazione libera un errore chiaro segnala l'importo sotto il minimo; la descrizione anticipa le domande (uso dei fondi, team, dati).
- S44 · «Come funziona» e FAQ: tono diretto, FAQ scritte come domande, mail, telefono e orari ripetuti all'inizio e alla fine, tre modi per iniziare (mail, telefono, profilo), nel modulo l'errore porta il focus sul campo sbagliato.
- S58 · Homepage: 29 progetti reali, «LANCIA UNA CAMPAGNA» ben visibile nel menu, sezione «SOSTIENILI ORA», loghi dei partner e icone SDG.
- S70 · Mobile: pagine progetto in una colonna senza scorrimento orizzontale, riepilogo della campagna prima del video, «Sostieni il progetto» ben visibile, barra delle sezioni sticky.
</aspetti_positivi>

<fatti_integrativi>
Fatti emersi dalle analisi preliminari del gruppo (ottobre 2026), NON presenti nella presentazione. Usali solo se il prompt singolo li assegna e citali come [X0n · analisi preliminare, da verificare].
- X01 · Metodi di pagamento incoerenti: le FAQ citano PayPal, PayWay (carte) e bonifico; «Come funziona» aggiunge Satispay. «PayWay» è un nome tecnico poco familiare.
- X02 · Le commissioni del metodo di pagamento sono a carico del donatore (PayPal 1,8% + 0,35 €, PayWay 1,8–2%, bonifico senza trattenute); se l'obiettivo non viene raggiunto il donatore è rimborsato ma le commissioni restano a suo carico. L'informazione è nelle FAQ.
- X03 · Anche con l'anonimato il progettista riceve nome, email, importo e ricompensa del donatore (FAQ).
- X04 · Né le FAQ né le schede progetto chiariscono se la donazione è fiscalmente detraibile e che ricevuta si ottiene (si parla di «attestato»).
- X05 · La ricompensa «FAI TU» (importo libero) ha un minimo diverso tra progetti: 10 € in MILK-ACT, 5 € in Mind the Climate; il nome non dice che si tratta di un importo a scelta.
- X06 · Nella pagina Partnership i numeri non coincidono: il testo parla di 13 progetti, oltre 312.000 € e 2.400 sostenitori; i contatori di 18 progetti, oltre 343.000 € e più di 2.900 donatori.
- X07 · «Lancia una campagna» porta alla registrazione generica di Ginger, mentre un ricercatore UniTo deve passare dalla selezione d'Ateneo; la pagina unito.it raggiunta da «Scopri la guida dell'iniziativa» non contiene un bando né una guida vera e propria.
- X08 · I progetti oltre il 100% mostrano un «nuovo obiettivo» («10.000 € in più») senza dire rispetto a quale cifra; in Mind the Climate convivono soglia minima 7.000 €, obiettivo totale 14.000 € e 18.750 € «incluso il cofinanziamento».
</fatti_integrativi>

<template_del_corso>
I documenti vanno prodotti OBBLIGATORIAMENTE secondo i due template ufficiali del corso (Cristina Gena · Human-Computer Interaction):
- «Scheda persona» (file template.pdf) per ogni persona Pxx;
- «Scheda user journey» (file user_journey.pdf) per ogni journey Jxx.
Se i PDF sono allegati alla conversazione, sono il riferimento vincolante per campi, etichette e ordine: rispettali alla lettera. I contenuti già scritti negli esempi dei PDF (la persona «Ginevra» e il percorso su un'app di incontri) sono solo esempi di compilazione: non copiarli e non prenderli come modello di contenuto. Se i PDF non sono allegati, usa la struttura dei template riprodotta fedelmente in <formato_persona> e <formato_journey>.
Non aggiungere sezioni che non esistono nei template. Le richieste dei prompt singoli che nominano sezioni diverse vanno collocate nei campi del template secondo <corrispondenze>.
Valori fissi dell'intestazione: Gruppo: «Gruppo A»; Servizio o progetto: «IdeaGinger · Funds TOgether (Università di Torino)»; Data/versione: «27/10/2026 · v1».
</template_del_corso>

<corrispondenze>
Come collocare nei template le richieste dei prompt singoli e le sezioni degli appunti:
- Informazioni del profilo (appunti) → «Nome convenzionale e descrizione del profilo».
- Motto (appunti) → «Frase rappresentativa e provenienza», con provenienza «sintesi costruita dal gruppo» (non è una frase realmente raccolta).
- Comportamenti, abitudini (appunti) → «Attività e comportamenti»; difficoltà con il servizio → «Difficoltà e frustrazioni».
- Frequenza d'uso del servizio (appunti) → «Contesto e vincoli di utilizzo».
- Familiarità con gli strumenti digitali e strumenti di riferimento (appunti) → «Competenze e strumenti digitali».
- Problemi del sito che riguardano la persona → «Difficoltà e frustrazioni», ciascuno con la sua citazione; l'elenco degli ID va anche in «Fonti ed evidenze disponibili».
- «Note per il team», fonti, ipotesi, [IPOTESI], domande di validazione → persona: «Fonti ed evidenze disponibili» e «Ipotesi da verificare e informazioni mancanti»; journey: «Fonti e ipotesi».
- Riga «Emozioni» e «curva emotiva» → riga «Emozioni e loro base»: ogni cella contiene emozione, punteggio da −2 a +2 e base (dichiarata, interpretata o ipotizzata).
- Righe «Difficoltà» e «Opportunità» → righe «Criticità e barriere» e «Opportunità di miglioramento».
- «Momenti critici», indicatori HEART e «Continuità tra touchpoint» → in «Fonti e ipotesi», sotto le voci omonime.
- «Aspettative iniziali» del journey → riga «Pensieri e aspettative» della prima fase (e, se serve, in «Scenario e obiettivo» dell'intestazione).
</corrispondenze>

<regole>
1. Fai emergere tutti i problemi elencati nel prompt singolo, ciascuno citato almeno una volta nel formato [Sxx · criterio · Gx] (es. [S17 · H4 · G4], [S59 · LG1 · G4], [S74 · prestazioni]) o [X0n · analisi preliminare, da verificare]. Non citare problemi del catalogo che il prompt singolo non assegna, salvo al massimo due in più se sono davvero coerenti con la persona: in quel caso spiegalo nel campo delle fonti e ipotesi.
2. Non inventare problemi del sito. Se ipotizzi un comportamento del sito non presente nel catalogo (per esempio l'area riservata dei progettisti, che la presentazione non ha analizzato), marcalo con [IPOTESI].
3. Non inventare numeri, date, URL, citazioni o nomi di persone reali. I progetti reali (MILK-ACT, Mind the Climate, ecc.) si possono nominare come oggetti della visita, mai attribuendo loro persone reali. I nomi delle personas sono fittizi.
4. Il problema deve sembrare vissuto dalla persona: descrivi che cosa fa, che cosa pensa e che cosa prova, poi collega il problema all'euristica o al concetto teorico pertinente. Evita di trasformare la persona in un elenco di difetti del sito: una persona ha anche obiettivi, momenti positivi e strategie di aggiramento.
5. Le esigenze di accessibilità vanno descritte con rispetto e precisione (strumenti usati, strategie), senza pietismo e senza stereotipi.
6. Coerenza: età, dispositivo, familiarità digitale, frequenza d'uso e accessibilità devono essere quelli indicati nella scheda del prompt singolo. Puoi aggiungere dettagli plausibili (famiglia, hobby, abitudini) purché non li contraddicano e siano pertinenti al servizio: il template chiede un profilo utile al progetto, non una biografia (evita dati sensibili non pertinenti come orientamento sessuale, religione o idee politiche).
7. Queste sono personas ipotetiche derivate da una valutazione euristica, non da ricerca con utenti: nella scheda persona spunta «Proto-persona»; nella scheda journey spunta «As-is (attuale)» e «Base: Mista» (evidenze sul sito dalla valutazione euristica, comportamenti della persona ipotizzati) e spiegalo in «Fonti e ipotesi».
8. Lingua italiana; termini tecnici inglesi quando sono quelli usati nella letteratura HCI.
9. Rispondi solo con il documento in Markdown che riproduce il template, senza frasi introduttive né commenti finali. Non racchiudere l'intero documento in un blocco di codice. Il front matter iniziale è un metadato per il gruppo e non va riportato nel PDF.
</regole>

<formato_persona>
Riproduci la «Scheda persona» del template, con questi campi, queste etichette e quest'ordine (nel PDF i riquadri sono su due colonne: l'ordine sotto è quello di lettura, da sinistra a destra e dall'alto in basso). Nei riquadri usa elenchi puntati brevi, come nel template.

---
id: Pxx
tipo: persona
nome: Nome Cognome
eta: numero
ruolo: donatore | promotore | visitatore
dispositivo_principale: dispositivo
familiarita_digitale: 1–5
accessibilita: esigenza oppure "nessuna esigenza specifica"
frequenza_uso: descrizione breve
problemi_citati: [elenco degli ID citati, es. S17, S23, X02]
---

# Scheda persona
Cristina Gena · Human-Computer Interaction

Gruppo: Gruppo A · Data/versione: 27/10/2026 · v1
Servizio o progetto: IdeaGinger · Funds TOgether (Università di Torino)
Tipo: ☒ Proto-persona ☐ Persona basata sulla ricerca

### Nome convenzionale e descrizione del profilo
Nome, età, occupazione, città, situazione familiare, rapporto con UniTo e con Ginger, archetipo tra virgolette (2–4 righe).

### Scenario e obiettivo principale
2–3 righe: in quale situazione arriva al servizio e che cosa vuole ottenere.

### Attività e comportamenti
4–6 punti: abitudini, come si informa, decide, dona o lavora.

### Bisogni e aspettative
3–5 punti, formulati come bisogni dell'utente (non come soluzioni tecniche).

### Obiettivi e motivazioni
3–5 punti: perché usa il servizio e che cosa considera un successo.

### Difficoltà e frustrazioni
5–10 punti: difficoltà personali e difficoltà con il sito; ogni difficoltà legata al sito cita il problema del catalogo e dice in mezza riga come la vive la persona.

### Contesto e vincoli di utilizzo
Dove, quando e con quale dispositivo usa il servizio; frequenza d'uso (quanto spesso, durata delle visite); vincoli di tempo, rete, attenzione.

### Competenze e strumenti digitali
Familiarità digitale da 1 a 5 con motivazione; che cosa sa fare e dove si blocca; dispositivi, sistema operativo, browser, app, tecnologie assistive, altri servizi di donazione o crowdfunding conosciuti.

### Esigenze di accessibilità
Esigenze permanenti, temporanee o situazionali e strategie usate; «Nessuna esigenza specifica» se non ce ne sono.

### Frase rappresentativa e provenienza
> «Una frase in prima persona, al massimo 15 parole.»
Provenienza: sintesi costruita dal gruppo (non è una frase realmente raccolta).

### Fonti ed evidenze disponibili
- Presentazione «Funds TOgether: analisi di usabilità», Gruppo A: elenco degli ID delle slide citate.
- Eventuali fatti integrativi X0n (analisi preliminare, da verificare).
- Nessuna ricerca diretta con utenti.

### Ipotesi da verificare e informazioni mancanti
- Dettagli inventati per dare realismo e affermazioni marcate [IPOTESI].
- 1–2 domande da porre in un'intervista o in un test con utenti simili.
</formato_persona>

<formato_journey>
Riproduci la «Scheda user journey» del template, con questi campi, queste etichette e quest'ordine. Le fasi sono le colonne: usa i nomi e il numero di fasi indicati dal prompt singolo (il template permette di aggiungere o eliminare colonne).

---
id: Jxx
tipo: journey_map
persona: Pxx
fasi: [nomi delle fasi in ordine]
canali: [canali usati]
problemi_citati: [elenco degli ID citati]
fase_emozione_min: nome della fase
fase_emozione_max: nome della fase
---

# Scheda user journey
Cristina Gena · Human-Computer Interaction

Gruppo: Gruppo A · Data/versione: 27/10/2026 · v1 · Servizio: IdeaGinger · Funds TOgether (Università di Torino)
Persona: Pxx · Nome Cognome · Scenario e obiettivo: una frase con situazione e obiettivo
Inizio del percorso: evento o luogo da cui parte · Fine del percorso: esito con cui si chiude
Mappa: ☒ As-is (attuale) ☐ To-be (proposta) · Base: ☐ Ricerca ☐ Ipotesi ☒ Mista

| Dimensione | Fase 1 · nome | Fase 2 · nome | … |
|---|---|---|---|
| **Azioni e attività** | | | |
| **Touchpoint e canali** | | | |
| **Pensieri e aspettative** | | | |
| **Emozioni e loro base** | | | |
| **Criticità e barriere** | | | |
| **Opportunità di miglioramento** | | | |

Regole per le celle:
- Al massimo 30 parole per cella; usa <br> per andare a capo dentro una cella.
- Touchpoint e canali: «touchpoint · canale» (es. «Scelta della ricompensa · sito da smartphone»); non confondere i due concetti.
- Pensieri e aspettative: in prima persona, tra virgolette.
- Emozioni e loro base: emozione, punteggio da −2 a +2 e base, es. «Frustrazione (−2) · ipotizzata: l'errore compare dopo l'invio». Qui le emozioni sono sempre ipotizzate o interpretate, mai dichiarate.
- Criticità e barriere: con la citazione del problema; «—» se in quella fase non ce ne sono.
- Opportunità di miglioramento: per ogni criticità, la soluzione coerente con quella proposta nella presentazione.

### Fonti e ipotesi
- Fonti: ID delle slide e dei fatti integrativi citati; nessuna ricerca diretta con utenti; motivo della base «Mista».
- Ipotesi: passaggi non verificati nella presentazione, marcati [IPOTESI]; informazioni mancanti.
- Momenti critici: 2–4 punti con fase, rischio (abbandono o perdita di fiducia), indicatore HEART pertinente (Happiness, Engagement, Adoption, Retention, Task success) e una metrica osservabile, senza inventare valori.
- Continuità tra touchpoint: dove il percorso si interrompe o costringe a ripetere azioni.
</formato_journey>

<attesa>
Se questo messaggio non contiene ancora un prompt Pxx o Jxx, rispondi soltanto con: «Contesto C00 acquisito. Incolla il prompt della persona (Pxx) o del journey (Jxx).»
Se invece lo contiene, genera direttamente il documento richiesto.
</attesa>

</prompt>
````
<!-- END PROMPT id="C00" -->
