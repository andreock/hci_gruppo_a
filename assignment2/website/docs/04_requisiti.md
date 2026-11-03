# 04 · Requisiti del nuovo sito

Requisiti derivati da `02_problemi_consolidati.md` (P-xxx), da `03_bisogni_personas.md` (Bxx-n, Jxx-Fn) e dai vincoli di consegna (`assignment2/Istruzioni.md`). Ogni requisito ha almeno un'origine: nessuno è arbitrario.

**Priorità MoSCoW**: **M** = Must (senza, il prototipo non risolve un problema grave o non rispetta la consegna), **S** = Should, **C** = Could, **W** = Won't (escluso, con motivo).

**Metodi di verifica** (Fase 4 e 5): `SCRIPT` script in `tools/`; `AXE` axe-core con Playwright; `TAST` percorso da tastiera con screenshot del focus; `AT` ispezione dell'albero di accessibilità (nome, ruolo, stato); `VIS` controllo visivo/screenshot a 320, 375, 768, 1280 px; `LH` Lighthouse mobile; `PERS` ripercorrere il journey della persona; `REV` revisione del testo.

Le informazioni istituzionali non documentate nelle fonti sono scritte nel sito come **[DA VERIFICARE con l'Ateneo]** (vedi `decisioni.md`).

---

## 1. Navigazione e homepage

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-001 | La homepage dice in una frase che cos'è il servizio e chi lo gestisce, nella prima schermata | P-001, P-003; B01-1, B06-1, B07-1, B12-1; J01-F2, J06-F1, J07-F2, J12-F1 | M | A 1280 × 720 e a 375 × 667 il titolo `h1` e la frase «… dell'Università di Torino …» sono visibili senza scorrere | VIS |
| R-002 | Nella homepage i progetti da sostenere vengono prima dei contenuti per i promotori | P-004; J07-F2 | M | Nel DOM e a schermo il blocco «Progetti in corso» precede il blocco «Hai un progetto di ricerca?» | VIS, SCRIPT |
| R-003 | Campo di ricerca vero e visibile, con etichetta, che cerca in titolo, sottotitolo, descrizione, dipartimento e categoria | P-005; B07-2; J07-F3 | M | Il campo è un `input type="search"` con `label`, largo almeno 27 caratteri su desktop, presente in intestazione o in homepage e nella pagina dei progetti; cercando il nome di un dipartimento si trovano i suoi progetti | VIS, SCRIPT |
| R-004 | La pagina dei risultati dice quanti risultati ci sono e gestisce il caso «nessun risultato» con alternative | P-006 | M | Con una parola inesistente compare «Nessun progetto per “…”», suggerimenti (controllare l'ortografia, categorie, tutti i progetti, FAQ); il conteggio è annunciato con `aria-live` | VIS, AT |
| R-005 | Menu principale breve (al massimo 8 voci più lingua, D-44), con etichette chiare; il programma con l'Ateneo è una voce con il suo nome | P-007, P-008, P-088 (principio); B12-2; J12-F2 | M | Il menu ha ≤ 8 voci di navigazione; «Programma dell'Ateneo» (o nome equivalente) è una voce di primo livello | VIS |
| R-006 | Il menu mobile (e ogni sottomenu) si apre e chiude con Invio e Spazio, si chiude con Esc, comunica lo stato con `aria-expanded`; a menu chiuso le sue voci non ricevono il focus | P-008, P-085; B03-4, B11-3; J03-F4, J11-F5 | M | Con Tab, a menu chiuso, il focus non entra nelle voci nascoste; Esc chiude e riporta il focus al pulsante; `aria-expanded` passa da `false` a `true` | TAST, AT |
| R-007 | La voce di menu della sezione corrente è evidenziata e marcata con `aria-current="page"` | P-009 | S | In ogni pagina la voce corrispondente ha `aria-current` e uno stile distinto non solo di colore (sottolineatura) | AT, VIS |
| R-008 | Nell'intestazione la home si raggiunge dal logo e dalla voce «Home» del menu (D-44); nessuna icona duplicata senza etichetta | P-010 | M | Due link alla home in `header`, il logo e la voce «Home», entrambi con un nome accessibile | AT |
| R-009 | I link interni si aprono nella stessa scheda; i link esterni sono dichiarati nel testo e con un'icona che ha un nome accessibile | P-014; J01-F4, J04-F3, J08-F1, J09-F2 | M | Nessun link interno ha `target="_blank"`; ogni link esterno contiene «(sito esterno)» o un'icona con testo nascosto equivalente | SCRIPT |
| R-010 | Nessun link con testo generico ripetuto («Scopri di più», «qui») senza contesto, nessun link vuoto | P-011, P-086 | M | Lo script non trova link con testo vuoto né testi uguali che puntano a destinazioni diverse nella stessa pagina | SCRIPT, AXE |
| R-011 | Briciole di pane su tutte le pagine interne | P-016 | M | Ogni pagina tranne la home ha un `nav` «Percorso» con l'ultima voce `aria-current="page"` | SCRIPT |
| R-012 | Pulsante «Torna su» nelle pagine lunghe | P-015; J07-F4, J08-F2, J11-F5 | S | Nelle pagine più alte di 2 schermate c'è un link «Torna su» che porta il focus all'inizio del contenuto | TAST, VIS |
| R-013 | Titoli di pagina brevi e univoci, nel formato «Pagina – Marchio», con un solo nome del marchio | P-002; J01-F1 | M | Tutti i `<title>` sono diversi tra loro e lunghi ≤ 60 caratteri; il marchio è scritto sempre allo stesso modo | SCRIPT |
| R-014 | Pagina 404 personalizzata nel modello del sito, nella lingua della pagina, con spiegazione, ricerca e link a home, progetti e FAQ | P-019, P-020 | M | `404.html` (e la versione inglese) hanno intestazione, piè di pagina, viewport, campo di ricerca e i tre link | VIS, SCRIPT |
| R-015 | Nessun link interno rotto e nessuna ancora inesistente | P-069; checklist di `Istruzioni.md` | M | Lo script dei link non trova errori su tutte le pagine IT ed EN | SCRIPT |
| R-016 | «Chi siamo» e i contatti sono raggiungibili dall'alto di ogni pagina | P-003, P-080; J06-F1, J12-F2 | S | «Chi siamo» è nel menu principale o nella barra di servizio, sopra la piega | VIS |
| R-017 | La homepage mostra gli ultimi aggiornamenti dei progetti con la data | P-013; B08-1 | C | Blocco «Ultimi aggiornamenti» con 3 voci datate, generate dai dati | VIS, SCRIPT |

## 2. Elenco dei progetti

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-020 | Ogni card mostra titolo completo, gruppo e dipartimento UniTo, categoria, raccolto, obiettivo, percentuale, sostenitori e stato | P-038, P-026, P-030, P-028; B05-2, B10-1; J05-F2, J10-F1 | M | Nessun titolo troncato con «…» a 320 px; ogni card ha tutti i campi elencati | VIS, SCRIPT |
| R-021 | Lo stato è sempre in testo, oltre a colore e icona, con quattro formule fisse e mai giorni negativi: «In corso · mancano N giorni (scade il gg/mm/aaaa)», «Obiettivo raggiunto · puoi ancora sostenerlo per N giorni», «Conclusa · obiettivo raggiunto», «Conclusa · obiettivo non raggiunto» | P-022, P-024, P-028, P-040; B01-4, B05-1, B10-2; J01-F4, J05-F3, J10-F2 | M | Lo script, simulando date diverse, non produce mai numeri negativi né stati diversi dalle quattro formule; ultimo giorno = «ultimo giorno» | SCRIPT, VIS |
| R-022 | Lo stato è calcolato da un'unica funzione a partire dai dati: nessuna combinazione impossibile | P-023 | M | Lo script di coerenza verifica che «Obiettivo raggiunto» compaia solo con raccolto ≥ obiettivo e che i giorni rimanenti siano calcolati dalla data corrente | SCRIPT |
| R-023 | Card interamente cliccabile con un unico link dal nome significativo (il titolo), con un cambiamento visibile al passaggio del mouse e al focus | P-029; J03-F4 | M | Ogni card contiene un solo `a` (sul titolo) con l'area estesa a tutta la card; hover e focus cambiano bordo e ombra (contrasto ≥ 3:1) | AT, TAST, VIS |
| R-024 | Filtri (stato, categoria, dipartimento, edizione) e ordinamento (scadenza, percentuale, più recenti) riflessi nella URL; con Indietro filtri e posizione restano invariati | P-031, P-027; B05-2, B05-3, B08-2; J05-F2, J08-F2 | M | Applicando un filtro la URL cambia (`?stato=…&ordina=…`); aprendo un progetto e tornando indietro filtri, risultati e posizione di scorrimento sono quelli di prima | TAST, SCRIPT |
| R-025 | L'elenco indica quanti progetti sono mostrati e il totale; se c'è una paginazione o «Mostra altri», dice quanti restano e quando sono finiti | P-032, P-033; J05-F2, J08-F2 | M | Testo «Mostrati 12 di 14 progetti» aggiornato e annunciato; alla fine «Hai visto tutti i progetti» | VIS, AT |
| R-026 | I contatori complessivi sono calcolati dai dati e distinguono campagne attive e concluse | P-036, P-028; B06-2, B08-1; J06-F2, J08-F5 | M | Lo script di coerenza confronta i contatori mostrati con quelli calcolati da `data/progetti.json` | SCRIPT |
| R-027 | La barra di avanzamento usa un solo colore su sfondo neutro, non è un link e ha un'alternativa testuale | P-028, P-050; J05-F1 | M | La barra è un elemento non interattivo con `role="img"` o testo equivalente («38% dell'obiettivo»); il colore pieno ha contrasto ≥ 3:1 con lo sfondo | AT, SCRIPT |
| R-028 | Nessun carosello che nasconde contenuti; se presente, ha frecce, posizione «2 di 5» e non scorre da solo | P-037; J02-F6, J07-F3, J11-F3 | M | Le liste di progetti sono griglie che vanno a capo; nessun elemento scorre in orizzontale | VIS |
| R-029 | L'elenco si apre con una frase che spiega raddoppio dell'Ateneo e regola «tutto o niente», con link alle regole | P-048 | S | Paragrafo introduttivo sopra i filtri con i due link | VIS |

## 3. Pagina del progetto

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-030 | Riquadro di stato in alto con raccolto, obiettivo, percentuale, sostenitori, scadenza in data, stato in testo e cifra che manca all'obiettivo | P-022, P-023, P-024; B01-4, B05-4; J01-F4, J05-F3 | M | Il riquadro è nella prima schermata a 1280 px e subito sotto il titolo a 375 px; contiene «Mancano € …» quando la campagna è sotto l'obiettivo | VIS |
| R-031 | La barra di avanzamento non è un link e ha un'alternativa testuale | P-050 | M | Vedi R-027 | AT |
| R-032 | Ordine fisso delle sezioni in tutti i progetti: presentazione, uso dei fondi, team, ricompense, aggiornamenti, commenti, sostenitori | P-041, P-045; B08-3; J08-F3 | M | Lo script verifica che tutte le pagine progetto abbiano le sezioni con gli stessi `id` nello stesso ordine | SCRIPT |
| R-033 | Indice con ancore all'inizio della pagina | P-049; B02-2, B07-3; J02-F3, J07-F4 | M | `nav` «In questa pagina» con un link per sezione; tutte le ancore esistono | SCRIPT, TAST |
| R-034 | Soglie spiegate in un solo riquadro, vicino al pulsante per sostenere: obiettivo minimo, eventuale secondo obiettivo con cifra e scopo, effetto del cofinanziamento con un esempio numerico | P-048, P-053; B05-5, B10-2, B10-3; J05-F4, J10-F2, J10-F3 | M | Il riquadro «Come funzionano obiettivo e raddoppio» contiene un esempio calcolato dai dati del progetto (es. «Se si raggiungono € 7.000, l'Ateneo aggiunge € 7.000») | VIS, SCRIPT |
| R-035 | La regola «tutto o niente» è spiegata in una frase dove si sceglie l'importo e nel modulo di donazione | P-044, P-054; J04-F3, J06-F5 | M | La frase compare nelle ricompense e nel passo «Importo» e nel riepilogo | VIS |
| R-036 | Ricompense in un formato compatto e confrontabile: importo minimo, che cosa si riceve, posti rimasti, quante persone l'hanno scelta (anche 0), ordinate dalla più bassa alla più alta | P-042, P-045; B02-3; J02-F4, J04-F4 | M | Le ricompense sono una lista di righe uniformi con gli stessi quattro dati, in ordine crescente in tutti i progetti | VIS, SCRIPT |
| R-037 | La donazione a importo libero si chiama «Donazione libera» ed ha lo stesso minimo in tutti i progetti, scritto accanto al campo | P-065; B01-5, B02-3, B07-4; J01-F5, J02-F4, J07-F5 | M | Minimo uguale in tutti i progetti (vedi `decisioni.md`), visibile nell'etichetta o nella descrizione del campo | SCRIPT, VIS |
| R-038 | Campagne concluse: ricompense in sola lettura, nessun campo importo né pulsante attivo, spiegazione in testo con data ed esito e link alle campagne attive e ai risultati | P-040; B03-3, B10-5; J03-F3, J05-F3, J10-F5 | M | Nelle pagine concluse non esistono `input` di importo né link «Sostieni»; c'è il riquadro «Raccolta conclusa il …» | SCRIPT, AT |
| R-039 | «Scrivi al gruppo» con indicatore di caricamento e conferma immediata che dice i tempi di risposta; email del gruppo visibile subito; modulo simulato | P-039; B10-4; J02-F3, J08-F4, J10-F4 | M | Dopo l'invio compare entro 100 ms un indicatore «Invio in corso…», poi un messaggio annunciato con `role="status"` | TAST, AT |
| R-040 | Immagini con testo alternativo significativo o vuoto se decorative; un solo `h1`; titoli in ordine; nessun titolo vuoto | P-046, P-012; J03-F2 | M | AXE senza violazioni `image-alt`, `heading-order`, `empty-heading`; script: un `h1` per pagina | AXE, SCRIPT |
| R-041 | Le spiegazioni a comparsa sono pulsanti (non link), si aprono da tastiera e con il clic, si chiudono con Esc e restano visibili finché servono | P-044; J03-F2, J11-F5 | M | Elemento `button` con `aria-expanded` e contenuto collegato; Esc chiude; nessun link `href="#"` | TAST, AT |
| R-042 | Il pulsante per sostenere è nella prima schermata e resta raggiungibile, senza coprire il focus | P-052 | S | A 1280 px il pulsante è sopra la piega; su mobile c'è un link «Sostieni» nel riquadro di stato | VIS, TAST |
| R-043 | Il promotore è indicato con nome del gruppo, dipartimento e «Università di Torino», con responsabile scientifico e ruolo | P-026; B06-2, B10-1; J06-F2, J08-F3 | M | Formula unica «Gruppo · Dipartimento di …, Università di Torino» in card e pagina | SCRIPT |
| R-044 | «Copia link» con conferma annunciata | S27 (positivo da conservare); B04-6, B07-5 | S | Il clic copia la URL e mostra «Link copiato» con `role="status"` | AT |
| R-045 | Le campagne concluse mostrano il resoconto finale negli aggiornamenti | B10-6; J10-F6 | C | Almeno un progetto concluso ha un aggiornamento «Resoconto finale» datato | VIS |

## 4. Donazione (checkout simulato)

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-050 | Percorso in passi con indicatore di avanzamento: importo o ricompensa, dati personali, privacy e visibilità, pagamento, riepilogo, conferma | P-057; J01-F5, J02-F5 | M | L'indicatore mostra «Passo 2 di 5» e marca il passo corrente con `aria-current="step"` | VIS, AT |
| R-051 | In ogni passo si può tornare indietro, cambiare importo o ricompensa e tornare al progetto; i dati già inseriti restano (WCAG 3.3.7) | P-058; B02-4; J02-F5, J02-F6 | M | Tornando dal passo 4 al passo 2 i campi sono ancora compilati (anche dopo ricaricare la pagina, nella stessa sessione) | TAST |
| R-052 | Validazione in linea quando si lascia il campo e all'invio: messaggio vicino al campo, nella lingua della pagina, che dice come correggere e sparisce appena il valore è corretto; riepilogo degli errori in testa con link ai campi; focus sul riepilogo | P-054, P-077; B01-6, B03-5, B04-1, B07-4, B11-2; J01-F5, J03-F5, J04-F5, J07-F5, J11-F4 | M | Con 3 € nel campo «Donazione libera» compare all'uscita dal campo «L'importo minimo è 5 €. Scrivi 5 o più.»; il campo ha `aria-invalid` e `aria-describedby`; correggendo, il messaggio sparisce | TAST, AT |
| R-053 | Etichette sempre visibili; `type`, `autocomplete`, `inputmode` corretti; obbligatorietà dichiarata; radio raggruppati con `fieldset` e `legend` | P-059, P-060, P-072; B09-6 | M | AXE senza violazioni `label`; email `type="email" autocomplete="email"`, nome `given-name`, cognome `family-name`, importo `inputmode="decimal"` | AXE, SCRIPT |
| R-054 | La visibilità del nome è una scelta esplicita senza valore preselezionato, che spiega che cosa vedono il pubblico e il team del progetto | P-055, P-056; B06-4; J06-F5 | M | Due radio «Mostra il mio nome» / «Dona in forma anonima», nessuno `checked`; testo su cosa riceve il team marcato [DA VERIFICARE] | AT, VIS |
| R-055 | Metodi di pagamento presi da un'unica fonte dati, uguali in modulo, FAQ e «Come funziona», con nomi comprensibili | P-062; B04-4; J04-F5 | M | Lo script verifica che l'elenco dei metodi nelle tre pagine coincida con i dati | SCRIPT |
| R-056 | Commissioni e loro destino in caso di rimborso mostrati nel riepilogo, con il totale, prima della conferma | P-063; B04-3, B06-3; J04-F5, J06-F3 | M | Il riepilogo mostra importo, commissione stimata, totale e la frase su che cosa succede se l'obiettivo non viene raggiunto | VIS |
| R-057 | Ricevuta e detraibilità spiegate nel modulo e nella conferma; dove le fonti non lo dicono, segnaposto «[DA VERIFICARE]» | P-064; B06-5; J06-F6 | M | Riquadro «Ricevuta e detraibilità» nel passo dei dati e nella conferma | VIS |
| R-058 | Nessun campo per numeri di carta o credenziali: il pagamento è simulato da un pulsante «Simula il pagamento» e la pagina lo dichiara | Obiettivo (prototipo didattico) | M | Nessun `input` con `autocomplete="cc-*"`; avviso «Pagamento simulato» visibile | SCRIPT |
| R-059 | L'indirizzo della donazione contiene progetto ed eventuale ricompensa; se manca il contesto o la campagna è conclusa, la pagina lo spiega e offre i link giusti invece di reindirizzare | P-061, P-040 | M | `donazione.html?progetto=x&ricompensa=y` funziona aperto direttamente; senza parametri mostra «Scegli un progetto per continuare» | TAST |
| R-060 | Il riepilogo (progetto, ricompensa, importo, con «Modifica») è visibile in alto in ogni passo, anche su smartphone prima del pulsante | P-057; J02-F5 | M | A 375 px il riepilogo precede i campi del passo | VIS |
| R-061 | La conferma mostra un codice di riferimento simulato, il riepilogo stampabile e i contatti con orari | J01-F6; B01-6; P-080 | S | Pagina di conferma con codice, pulsante «Stampa» e contatti | VIS |
| R-062 | Aiuto se il pagamento non va a buon fine: che cosa fare dopo | P-066 | S | FAQ «Il pagamento non è andato a buon fine: che cosa faccio?» con i passi e il contatto, collegata dal passo del pagamento | VIS |

## 5. Programma con l'Ateneo e percorso di chi propone un progetto

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-070 | Pagina del programma con lo stato attuale (bando aperto, chiuso, prossima edizione), le date esplicite e la fase corrente evidenziata | P-021; B06-2, B08-1, B09-1; J06-F2, J08-F1, J08-F6, J09-F1 | M | In apertura: «Edizione 2026 · campagne in corso fino al …; candidature 2027 [DA VERIFICARE]»; le quattro fasi con quella corrente marcata anche in testo | VIS |
| R-071 | Chi può candidarsi, requisiti, come, entro quando, chi contattare | P-035; B09-2, B12-3; J06-F2, J08-F4, J09-F2, J12-F3 | M | Sezioni con titoli «Chi può candidarsi», «Requisiti», «Come e quando», «A chi scrivere»; contatto fittizio ma credibile (`programma@ideablume.it`, D-22) | VIS |
| R-072 | Cofinanziamento spiegato con un esempio numerico, compreso il tetto e il caso delle donazioni oltre l'obiettivo | P-048, P-053; B10-3; J10-F3 | M | Esempio «Obiettivo 6.000 € raggiunto → l'Ateneo aggiunge 6.000 €»; tetto di 10.000 € indicato come da verificare | VIS |
| R-073 | Numeri delle edizioni passate calcolati dai dati | P-036; J08-F5 | M | I contatori per edizione coincidono con lo script di coerenza | SCRIPT |
| R-074 | Il pulsante per candidarsi porta al percorso del programma, distinto dal contatto generico | P-078; B09-2; J09-F2, J09-F4 | M | «Candidati al programma» porta alla pagina di candidatura del programma; nessun link generico «Registrati» lo sostituisce | VIS |
| R-075 | I costi per il promotore sono scritti subito, in evidenza, con lo stesso testo in pagina del programma, «Come funziona» e FAQ | P-071, P-076; B09-3, B12-3; J09-F3, J12-F3 | M | Riquadro «Quanto costa» entro la prima schermata della sezione promotori; testo identico (stessa chiave di traduzione) nelle tre pagine | VIS, SCRIPT |
| R-076 | Sezione per gli enti esterni e modulo «Proponi una collaborazione» (simulato), con la nota «inviare non vi impegna» e i tempi di risposta | B12-3, B12-4; J12-F3, J12-F4, J12-F5 (P12) | M | La pagina «Proponi un progetto» ha la sezione «Sei un ente esterno?» e il modulo con conferma | VIS, TAST |
| R-077 | Moduli di candidatura e di collaborazione accessibili: caselle di consenso native, etichette visibili, controlli nativi, autocompletamento attivo, errori in linea che spariscono | P-067, P-072, P-073, P-077; B09-6, B12-4; J09-F5, J12-F4 | M | AXE senza violazioni; consenso = `input type="checkbox"` con `label`; nessun segnaposto usato come etichetta | AXE, AT |
| R-078 | Informazioni per pianificare: fasi, tempi, formazione e accompagnamento, che cosa si può modificare dopo la pubblicazione | P-079 | S | Sezione «Tempi e fasi» con segnaposto [DA VERIFICARE] dove mancano le fonti | VIS |
| R-079 | Indicazioni per i team: come preparare i contenuti nelle due lingue e come segnalare un problema | B11-5; J11-F1, J11-F6 (P11) | C | Sezione «Per i gruppi con una campagna in corso» in `proponi.html#gruppi` con le indicazioni e un link al modulo contatti | VIS |
| R-080w | Area riservata dei promotori con account e login | `Istruzioni.md` §4 («non sono richiesti account reali»); `da_rivedere_P10-P12.md` §2.3 | W | Escluso: i contenuti dei team passano dall'ufficio [IPOTESI], come nei journey To-be J10–J12 | — |

## 6. Aiuto, contenuti e contatti

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-081 | «Come funziona» diviso per sostenitori e promotori, con titoli, indice e passi numerati; ogni passo che nomina un'azione ha il link a quell'azione | P-074, P-069, P-075; B01-3, B09-4, B09-5; J01-F3, J09-F3, J09-F4 | M | Due sezioni con `h2`, indice iniziale, `ol` di passi; ogni passo con verbo d'azione contiene un link interno valido | VIS, SCRIPT |
| R-082 | FAQ divise per destinatario (sostenitori, promotori, generali) e argomento, con ricerca interna, accordion accessibili e un'ancora condivisibile per ogni risposta | P-075; B06-3, B09-4, B12-3; J06-F3, J09-F3, J12-F3 | M | `details`/`summary` (funzionano senza JS); campo «Cerca nelle domande» che filtra e annuncia il numero di risultati; aprendo `faq.html#id` la risposta si apre | TAST, AT |
| R-083 | Spiegazione dei termini del crowdfunding nelle FAQ, sezione «Le parole di ideaBlume» (D-45), con rimandi alle FAQ dove servono | P-025, P-068; B01-3, B04-3; J01-F3, J04-F2, J09-F3 | M | `faq.html#parole` e le risposte delle FAQ spiegano almeno: tutto o niente, obiettivo, secondo obiettivo, cofinanziamento, ricompensa, donazione libera, commissione, sostenitore, promotore, edizione | VIS |
| R-084 | Terminologia unica in tutto il sito: lo stesso concetto ha sempre lo stesso nome | P-070, P-048; B06-3, B09-3 | M | Lessico controllato nei file di traduzione; lo script non trova i termini esclusi («keep it all», «overfunding», «FAI TU», «campaign manager», «fee», «progettista») | SCRIPT |
| R-085 | Contatti e aiuto nella stessa posizione in tutte le pagine (WCAG 3.2.6), con orari e tempi di risposta da un'unica fonte e telefono cliccabile | P-080, P-081; B01-6, B06-6; J01-F6, J11-F6, J12-F5 | M | Il piè di pagina di ogni pagina ha lo stesso blocco «Aiuto» con link `tel:` e `mailto:`; gli orari vengono da un unico dato | SCRIPT |
| R-086 | Testi brevi: risposte che iniziano con la risposta in una frase, paragrafi corti, nessun tono promozionale, nessun dato senza fonte | P-082, P-084; B07-3 | S | Revisione: risposte FAQ ≤ 80 parole; nessuna cifra senza fonte o segnaposto | REV |
| R-087 | Testi senza refusi | P-083 | S | Controllo ortografico dei file di traduzione | REV |
| R-088 | Pagina «Chi siamo» che dice chi gestisce il servizio, nella sezione «Le persone dell'Ufficio» (D-48) | P-003; B06-1, B12-1 | M | Pagina con gestore (ufficio fittizio dell'Ateneo, [DA VERIFICARE]) e contatti | VIS |
| R-089 | Data di ultimo aggiornamento su FAQ e pagina del programma | P-013 | C | Riga «Ultimo aggiornamento: …» | VIS |

## 7. Accessibilità trasversale (obiettivo WCAG 2.2 AA)

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-090 | Link «Salta al contenuto», landmark `header`, `nav`, `main`, `footer`, un solo `h1`, titoli in ordine | P-017, P-046; B03-1 | M | Il primo Tab mostra «Salta al contenuto»; AXE senza violazioni `region`, `landmark-*`, `heading-order` | TAST, AXE |
| R-091 | Tutto utilizzabile da tastiera, senza trappole, con focus sempre visibile e non coperto da elementi fissi (2.4.7, 2.4.11) | P-085; B03-4, B11-3; J03-F4, J11-F5 | M | Percorso ricerca → progetto → donazione completato solo con la tastiera; contorno di focus ≥ 2 px con contrasto ≥ 3:1 | TAST |
| R-092 | Contrasto ≥ 4,5:1 per il testo normale, ≥ 3:1 per testo grande, componenti e indicatori di focus | P-034; B01-2; J01-F2, J05-F1 | M | Lo script dei contrasti verifica tutte le coppie del design system | SCRIPT, AXE |
| R-093 | Nessuna informazione affidata al solo colore; badge e barre leggibili con deuteranopia | P-022, P-028, P-040; B05-1; J05-F1, J05-F3 | M | Ogni stato ha testo e icona; screenshot con simulazione di deuteranopia | VIS |
| R-094 | Testo ridimensionabile al 200% e nessuno scorrimento orizzontale a 320 px (1.4.4, 1.4.10) | P-019; B01-2 | M | Screenshot a 320 px senza barra orizzontale; zoom 200% senza perdita di contenuto | VIS, SCRIPT |
| R-095 | Aree cliccabili di almeno 24 × 24 px (2.5.8) e di 44 × 44 px per i comandi principali | B01-2, B12-2 (P01, P12) | M | Lo script misura le dimensioni dei controlli nel browser | SCRIPT |
| R-096 | Messaggi di stato annunciati agli screen reader (4.1.3) | P-039, P-054, P-006 | M | Risultati di ricerca, filtri, errori, invii e «Link copiato» in regioni `role="status"` o `aria-live` | AT |
| R-097 | `prefers-reduced-motion` rispettato; nessun contenuto che si muove da solo | P-037 | M | Con riduzione del movimento attiva nessuna transizione; nessun carosello automatico | VIS |
| R-098 | Tutti i controlli hanno un nome accessibile; consensi con caselle native; icone decorative con `alt=""` o `aria-hidden` | P-086, P-012, P-067, P-060 | M | AXE senza violazioni `button-name`, `link-name`, `label` | AXE |
| R-099 | Leggibilità: corpo di base ≥ 16 px (18 px sul corpo del testo), interlinea ≥ 1,5, paragrafi corti, parole chiave in grassetto, frasi semplici | P-076, P-082; B01-2, B07-3 (P01, P07, P04) | S | Valori nel design system; revisione dei testi | VIS, REV |
| R-100 | Dichiarazione di accessibilità con un canale per segnalare problemi | J03-F6, J11-F6 | S | Pagina o sezione «Accessibilità» con lo stato di conformità verificato e un contatto | VIS |

## 8. Multilingua

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-110 | Italiano come lingua principale e inglese completo: interfaccia, errori, FAQ, regole, ricompense, aggiornamenti | P-043, P-054; B04-1, B11-1; J04-F2, J04-F5, J11-F2, J11-F4 | M | Ogni pagina IT ha la corrispondente EN; lo script verifica che non manchino chiavi di traduzione | SCRIPT |
| R-111 | Una sola lingua visibile per volta: mai i due testi uno sotto l'altro | P-051, P-047; B04-2; J04-F4 | M | Nessuna pagina contiene i testi delle due lingue (script sulle chiavi) | SCRIPT |
| R-112 | Selettore di lingua visibile in intestazione che porta alla stessa pagina nell'altra lingua, conservando filtri e ancore | J04-F6, J11-F2; B04-6 | M | Dalla pagina elenco filtrata, il passaggio a EN mantiene la query; il link ha `hreflang` e `lang` | TAST |
| R-113 | Attributo `lang` corretto sulla pagina e sulle parti in un'altra lingua; formati di data e valuta coerenti con la lingua | P-051 (frasi inglesi senza `lang`) | M | `<html lang="it">` / `"en"`; date «17/11/2026» e «17 Nov 2026», importi «€ 7.000» e «€7,000» | SCRIPT |

## 9. Mobile e prestazioni

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-120 | Progettazione mobile first, con versione desktop curata; provata a 320, 375, 768 e 1280 px | `Istruzioni.md` §4 (versione desktop richiesta); checkpoint 1 (responsive su mobile e desktop); P-087, P-037 | M | Screenshot delle pagine principali ai quattro tagli senza difetti | VIS |
| R-121 | Su smartphone il contenuto principale viene prima della navigazione secondaria | P-018 | M | A 375 px il titolo della pagina è nella prima metà della schermata | VIS |
| R-122 | Core Web Vitals sulle pagine critiche (progetto e donazione): LCP ≤ 2,5 s, CLS ≤ 0,1, INP ≤ 200 ms (TBT come indicatore in laboratorio) | P-087; B02-1, B11-4; J02-F2, J11-F3 | M | Lighthouse mobile su home, elenco, progetto, donazione; confronto con `01_inventario_fonti.md` §3.1 | LH |
| R-123 | Immagini leggere (SVG) con dimensioni dichiarate, `loading="lazy"` sotto la piega; CSS e JS leggeri; nessun font o script esterno | P-087 | M | Peso totale della pagina progetto < 200 KB; nessuna richiesta a domini esterni | SCRIPT, LH |

## 10. Vincoli di consegna, dati e onestà del prototipo

| ID | Requisito | Origine | P | Criterio di accettazione | Verifica |
|---|---|---|---|---|---|
| R-130 | Il prototipo funziona aprendo `index.html` direttamente nel browser, senza server, ed è pubblicabile così com'è su GitHub Pages | `Istruzioni.md` §7 B («non devono essere richiesti server»); checkpoint 1 (D-21) | M | Tutte le pagine e le funzioni (filtri, ricerca, donazione) funzionano da `file://` in Chrome, Firefox e Safari e da un server statico in una sottocartella (simulazione di GitHub Pages), compresa la 404 a qualunque profondità | TAST |
| R-131 | I dati dei progetti stanno in un'unica fonte da cui derivano tutte le pagine; numeri coerenti tra elenco, pagina, contatori | P-036, P-023 | M | Script di coerenza: budget = obiettivo, percentuali, stati e contatori corretti | SCRIPT |
| R-132 | Ogni pagina mostra nel piè di pagina «Prototipo didattico realizzato per il corso di HCI: nessun pagamento reale»; le informazioni istituzionali non documentate sono segnaposto «[DA VERIFICARE con l'Ateneo]» | Regole generali del prompt; regola 4 di C00 (non inventare dati presentati come reali) | M | Script: la nota è in ogni pagina IT ed EN; elenco dei segnaposto nel README | SCRIPT |
| R-133 | Almeno 12 pagine distinte per contenuti o funzioni (richiesta del gruppo al checkpoint 1; la consegna ne chiede 10 per un gruppo di 4) | `Istruzioni.md` §4; checkpoint 1 (D-23) | M | Elenco delle pagine in `06_architettura.md` con la funzione di ognuna: almeno 12 tipi diversi | REV |
| R-134 | Nessun pagamento reale, nessun dato inviato a un server, nessun servizio esterno | Obiettivo del prompt; `Istruzioni.md` §4 | M | Nessuna richiesta di rete esterna durante il percorso di donazione | SCRIPT |
| R-135 | Le funzioni essenziali (leggere un progetto, le sue sezioni, le FAQ) funzionano anche senza JavaScript | Vincolo di stack del prompt | M | Con JS disattivato pagine progetto, FAQ (accordion `details`) e «Come funziona» sono complete | TAST |
| R-136 | Nessun marchio, logo, grafica o testo di IdeaGinger; nessun logo ufficiale UniTo; nome di piattaforma proprio | Regola 4 del prompt | M | Revisione; nessun file grafico esterno | REV |

---

## Sintesi

| Area | Must | Should | Could | Won't | Totale |
|---|---|---|---|---|---|
| 1 Navigazione e homepage | 13 | 3 | 1 | 0 | 17 |
| 2 Elenco dei progetti | 9 | 1 | 0 | 0 | 10 |
| 3 Pagina del progetto | 13 | 2 | 1 | 0 | 16 |
| 4 Donazione | 11 | 2 | 0 | 0 | 13 |
| 5 Programma e promotore | 8 | 1 | 1 | 1 | 11 |
| 6 Aiuto e contenuti | 6 | 2 | 1 | 0 | 9 |
| 7 Accessibilità | 9 | 2 | 0 | 0 | 11 |
| 8 Multilingua | 4 | 0 | 0 | 0 | 4 |
| 9 Mobile e prestazioni | 4 | 0 | 0 | 0 | 4 |
| 10 Vincoli e dati | 7 | 0 | 0 | 0 | 7 |
| **Totale** | **84** | **13** | **4** | **1** | **102** |
