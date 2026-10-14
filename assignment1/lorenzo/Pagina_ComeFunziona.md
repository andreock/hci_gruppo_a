# Stato della UX della pagina "Come funziona" di Ideaginger: analisi di massima secondo le 10 euristiche di Nielsen

**Pagina analizzata**: <https://www.ideaginger.it/ginger_come-funziona.html> (pagina "Come funziona" del sito Ideaginger / GINGER)
**Data**: 14/10/2026
**Come è stata svolta**: lettura del contenuto e della struttura della pagina (testi, titoli, link, testi alternativi, metadati), senza browser interattivo. Resa grafica, colori, comportamento JavaScript, tastiera, zoom e mobile **non sono stati osservati**: dove servono sono indicati con un placeholder. Dove l'osservazione riprende quanto già verificato sulla pagina FAQ dello stesso sito (stesso template) è indicato.
**Riferimento metodologico**: `checklist_analisi_euristica.md` (sezione 5 per gli elementi da osservare, sezione 3 per la scala di gravità 0–4).

> **Come leggere i placeholder**
> - `[VERIFICA: …]` è un controllo da fare a mano sul sito, che può confermare, modificare o annullare l'osservazione.
> - `[SCREENSHOT: …]` è l'immagine da inserire nel report, con il problema evidenziato.
> - `[GRAVITÀ: x?]` è un valore provvisorio da confermare dopo la verifica (scala Nielsen 0–4). Dove la gravità non ha il punto interrogativo, l'osservazione si basa su ciò che è scritto nella pagina e non dipende dalla resa grafica.
> - Annotare per ogni verifica **browser, dispositivo, risoluzione e data** (checklist, sez. 8).

---

## 1. Che cos'è la pagina e a cosa serve

È la pagina che spiega a chi vuole lanciare una campagna come funziona il crowdfunding di Ginger: come iniziare, formazione, supporto del campaign manager, caratteristiche della piattaforma, costi, durata e modalità di raccolta, cosa fare dopo la campagna. Si rivolge quasi solo a **chi vuole lanciare un progetto** (progettisti); i donatori sono citati solo in un punto dell'elenco dei vantaggi. Struttura rilevata, dall'alto:

1. barra di servizio (Faq, Contatti, Come funziona, Login progettista) e menu principale (icona, logo, Home, Cerca progetti, Lancia una campagna, Partner, Servizi);
2. blocco di navigazione che nel testo estratto precede il contenuto: Progetti (Sostienili ora, Per ispirarti, Tutti), 26 Categorie, 17 SDGs ONU, 25 Partner;
3. elenco di link di servizio (Come funziona, Condizioni d'uso, Privacy, Cookies, Formazione, Chi Siamo, Contatti, Collaborazioni, FAQ);
4. titolo **Come funziona** seguito da un testo continuo, **senza sottotitoli**, scandito da 7 immagini: benvenuto e a chi è aperta la piattaforma, come iniziare (contatti e orari), formazione, campaign manager, funzionalità della piattaforma e fee di accesso, modalità di raccolta (30–60 giorni, "O tutto o niente"), cosa fare dopo la campagna, invito a consultare FAQ o a contattare Ginger;
5. footer (Home, Chi siamo, Collaborazioni, Contatti, Login partner, Condizioni d'uso, Privacy, Cookies, Preferenze cookie, FAQ, social, blog "Il Gingerino", © 2013 - 2026).

## 2. Giudizio complessivo provvisorio

La pagina **svolge il suo compito principale**: spiega in modo accogliente e concreto cosa offre Ginger, quali sono i contatti e come si sviluppa il percorso di una campagna. I problemi principali sono di **organizzazione** (promette "pochi passi" ma non li mostra, e non ha sottotitoli), di **informazioni importanti poco visibili o assenti** (la fee di 350 euro + IVA è dentro un paragrafo, non è chiaro se il corso di formazione sia obbligatorio né quanto costi) e di **coerenza con il resto del sito** (modalità di raccolta, metodi di pagamento e costi descritti in modo diverso rispetto alla pagina FAQ). Ci sono anche aspetti di accessibilità da controllare (testi alternativi delle immagini, link "qui", numero di telefono non cliccabile, zoom bloccato su mobile). Molti aspetti dipendono dalla resa a schermo e vanno verificati prima di assegnare le gravità definitive.

---

## 3. Analisi per euristica

### E1. Visibilità dello stato del sistema

**Positivo**
- Il titolo della scheda del browser è specifico ("Come funziona") e coincide con il titolo in testa al contenuto, quindi la pagina è riconoscibile tra le schede aperte e tra i preferiti (a differenza della pagina FAQ, che ha il titolo della home). 
- Il titolo "Come funziona" e il link nella barra di servizio e nell'elenco rendono chiaro dove ci si trova.

**Criticità**
- **Nessun indicatore di posizione nella pagina**: la pagina è lunga e senza indice. `[GRAVITÀ: 2?]`

### E2. Corrispondenza tra sistema e mondo reale

**Positivo**
- Tono diretto e inclusivo ("Benvenuto o benvenuta", "Scrivici una mail, chiamaci al telefono"), con la seconda persona e domande che anticipano i dubbi dell'utente.
- Le parole chiave importanti sono in grassetto (privati, terzo settore, imprese, ricompense, campaign manager), quindi l'utente le riconosce a colpo d'occhio.

**Criticità**
- **Mix di italiano e inglese**: "Campaign Manager", "call di consulenza", "fee di accesso", "profit e non profit", "Pixel Meta", "database" compaiono senza spiegazione. Il nome corretto del prodotto di Meta è "Meta Pixel". `[GRAVITÀ: 2]`
- **"Territoriale" non spiegato**: la pagina si presenta come "piattaforma di crowdfunding territoriale di Ginger", ma non dice cosa significhi, e la parola non ha un legame evidente con il resto del testo. `[GRAVITÀ: 1]`
- **Il titolo "Come funziona" non dice a chi si rivolge**: chi arriva per capire come donare, o come funziona un progetto già online, trova solo il percorso di chi lancia una campagna. Il donatore compare in una sola riga ("Nessuna registrazione richiesta ai donatori"). `[GRAVITÀ: 2]`
- **"Tasso di successo superiore al 90%, il più alto in Italia"**: dato citato senza spiegare come è calcolato (percentuale di campagne che raggiungono l'obiettivo?) né con una fonte o un periodo. `[GRAVITÀ: 1]`

### E3. Controllo e libertà dell'utente

**Positivo**
- Per iniziare ci sono tre strade alternative (mail, telefono, apertura del profilo): l'utente sceglie quella che preferisce.
- In fondo c'è un rimando a FAQ, mail e telefono per chi ha ancora dubbi.

**Criticità**
- **Il link "commissioni" porta alle Condizioni d'uso**: chi clicca per capire quali commissioni applicano i sistemi di pagamento arriva a un documento legale lungo invece che alla risposta delle FAQ. `[GRAVITÀ: 2?]`
- **Nessun pulsante finale per lanciare la campagna**: il testo termina con "Ancora qualche dubbio?" e non con un'azione principale evidente. `[GRAVITÀ: 2?]`
- **Breadcrumb assente**: dato che la pagina non è profonda, il problema è contenuto. `[GRAVITÀ: 1]`

### E4. Consistenza e standard

**Positivo**
- Il nome *Ideaginger.it* è scritto sempre allo stesso modo in corsivo nel testo, e il tono è coerente dall'inizio alla fine. 

**Criticità**
- **Modalità di raccolta con nomi diversi tra le pagine**: qui compaiono "Tutto o Niente!" e "O tutto o niente", e per l'altra modalità "Prende ciò che raccoglie". Nella pagina FAQ la stessa modalità si chiama "keep it all". Anche la maiuscola e la punteggiatura variano tra i due punti di questa pagina. `[GRAVITÀ: 2]`
- **Metodi di pagamento non allineati con la pagina FAQ**: qui sono "carte di credito, PayPal, Satispay e bonifico bancario"; nelle FAQ si parla di PayPal, PayWay e bonifico, senza Satispay. `[GRAVITÀ: 2]`
- **Costi non allineati con la pagina FAQ**: questa pagina indica una fee di accesso di 350 euro + IVA per pubblicare un progetto. Nelle FAQ le domande "GINGER trattiene una percentuale…?" e "Chi può presentare un progetto?" non menzionano nessuna fee, e una risposta dice che chiunque può pubblicare il proprio progetto. Un lettore che consulta solo le FAQ può credere che la pubblicazione sia gratuita. `[GRAVITÀ: 3]`
- **Percorso di candidatura descritto in due modi**: qui si parte da un confronto con un campaign manager e da un corso di formazione; nelle FAQ ("Come faccio a sottoporvi il mio progetto?") si costruisce il Profilo, si va su "Lancia una campagna" e si invia il progetto allo staff. Le due pagine non si richiamano né spiegano come si combinano. `[GRAVITÀ: 2]`
- **Terminologia variabile per lo stesso ruolo**: chi dona è "donatore" in un punto ("Nessuna registrazione richiesta ai donatori") e "sostenitore" in tutti gli altri; chi lancia il progetto è "progettista", "tu" o chi "vuole raccogliere fondi". `[GRAVITÀ: 1]`
- **Immagini caricate con indirizzo http**: le sette immagini del testo puntano a `http://www.ideaginger.it/upload/…` invece che a https. `[GRAVITÀ: 1?]`
- **Account Twitter errato nei metadati**: il tag `twitter:site` indica `@nytimes`, mentre `twitter:creator` indica `@IdeaGinger`. Condividendo la pagina su Twitter l'anteprima potrebbe attribuirla a un altro account. Osservazione tecnica collaterale, da segnalare a parte. `[GRAVITÀ: 1]`

### E5. Prevenzione dell'errore

- **Fee di 350 euro + IVA nascosta in un paragrafo**: compare in fondo alla frase che spiega chi può lanciare una campagna, senza grassetto e dopo l'elenco dei vantaggi "Nessuna trattenuta Ginger" e "Nessuna registrazione richiesta". Chi legge velocemente può non vederla e scoprire il costo solo dopo aver contattato Ginger o aperto il profilo. `[GRAVITÀ: 3]`
- **Non è chiaro se il corso di formazione sia obbligatorio, quanto costi e quanto duri**: la pagina dice che l'aver partecipato a un corso "accomuna chiunque abbia lanciato una campagna" ed è alla base del tasso di successo, ma non dice se sia richiesto, e rimanda al sito dei corsi per date e iscrizione. Un progettista può pianificare male tempi e budget. `[GRAVITÀ: 3]`
- **La fee è rimborsata se la campagna non raggiunge l'obiettivo?** La pagina non lo dice, e spiega solo che i fondi raccolti tornano ai sostenitori. `[GRAVITÀ: 2]`
- **Il perché del "Tutto o Niente" è rimandato a un contatto**: la pagina afferma che è la modalità più efficace ma chiude con "contattaci e ti spiegheremo il perché!". Un progettista non può valutare la scelta da solo prima di contattare Ginger. `[GRAVITÀ: 2]`
- **Collaborazione con i partner poco verificabile**: "Il tuo territorio o settore è di pertinenza di uno dei nostri partner?" rimanda a una telefonata, e il link porta al sito dei corsi invece che all'elenco dei partner di Ideaginger, presente solo nel menu. `[GRAVITÀ: 2]`

### E6. Riconoscimento più che ricordo

Positivo:
- Le informazioni di contatto (mail, telefono, orari) sono riportate in modo ben visibile e ripetute alla fine, quindi l'utente non deve ricordarle.
- Le parole chiave in grassetto aiutano a riconoscere i temi senza dover rileggere tutto.

Criticità:
- **Nessun sottotitolo**: la pagina è un testo continuo, e le sezioni si riconoscono solo dalle immagini. Chi torna sulla pagina per ritrovare un'informazione (ad esempio la durata della campagna) deve rileggere tutto. `[GRAVITÀ: 3]`
- **Testi alternativi delle immagini non descrittivi**: le sette immagini hanno come testo alternativo un nome di file troncato ("900-pixel-hai-u", "900-pixel-conta", "900-pixel-forma", "900-pixel-campa", "900-pixel-lanci", "900-pixel-racco", "900-pixel-obiet"). Per uno screen reader sono senza significato; dato che sono il titolo delle varie sezioni, dovrebbero avere come testo alternativo una descrizione testuale. `[SCREENSHOT: una delle immagini con il testo alternativo mostrato in DevTools]` `[GRAVITÀ: 2]`

### E7. Flessibilità ed efficienza d'uso

Positivo:
- Tre modi per iniziare (mail, telefono, profilo), con orari di contatto chiari.

Criticità:
- **Numero di telefono non cliccabile**: nel testo "051 19501024" non è un collegamento (a differenza della mail). Da smartphone l'utente deve copiarlo a mano. `[GRAVITÀ: 2?]`
- **Nessun indice né ancore**: per rileggere una sezione bisogna scorrere. `[GRAVITÀ: 2]`
- **Navigazione da tastiera**: sulla pagina FAQ è stato verificato che il Tab attraversa prima la navigazione e l'elenco delle 26 categorie e solo dopo arriva al contenuto, senza un collegamento "vai al contenuto". `[GRAVITÀ: 3?]`

### E8. Estetica e design minimalista

Positivo:
- Paragrafi brevi, grassetti per le parole chiave ed elenchi puntati rendono la lettura scorrevole nella maggior parte del testo.
- Le immagini separano visivamente le sezioni e danno un ritmo alla pagina.

Criticità:
- **Pagina lunga senza gerarchia visiva**: senza sottotitoli le sezioni si distinguono solo per le immagini. `[GRAVITÀ: 2?]`

### E9. Aiutare a riconoscere, diagnosticare e uscire dagli errori

Positivo:
- Gli orari di contatto sono indicati (lunedì–venerdì, 9:30–16:30), quindi chi chiama sa quando può aspettarsi una risposta.

Criticità:
- **Nessuna alternativa per chi scrive o chiama fuori orario**: la pagina non dice in quanto tempo risponde la mail né se esista un modulo di contatto. `[GRAVITÀ: 1]`
- **Costo e rimborso non chiariti**: la mancanza di indicazioni sulla fee in caso di campagna non riuscita può portare a decisioni sbagliate e a richieste di assistenza evitabili (vedi E5). `[GRAVITÀ: 2]`
- **Link vuoto prima di "FAQ"**: se il link non porta in modo chiaro alla pagina giusta o non viene letto correttamente, l'utente non capisce dove arriva (c'è un tag a con href compilato ma testo vuoto prima del link FAQ al fondo pagina). `[GRAVITÀ: 1]`
- **Pagina 404 in inglese**: digitando un indirizzo errato (es. /faqs.html) compare una pagina “Not Found” in inglese, mentre il resto del sito è in italiano. L’utente italiano che sbaglia indirizzo o segue un link rotto trova un messaggio d’errore in una lingua diversa da quella del sito. `[SCREENSHOT: pagina 404]` `[GRAVITÀ: 1–2?]`

### E10. Aiuto e documentazione

Positivo:
- La pagina è già di per sé documentazione di aiuto, ed è raggiungibile da barra di servizio e footer.
- Mail, telefono, orari e link alle FAQ sono riportati all'inizio e alla fine.
- Spiega con chiarezza durata (30–60 giorni), modalità di raccolta, metodi di pagamento e assenza di trattenute Ginger.

Criticità:
- **"Scopri i servizi aggiuntivi!" senza link**: il testo invita a scoprire i servizi per un supporto più intenso, ma nel contenuto non c'è un collegamento (il link "Servizi" esiste solo nel menu). `[GRAVITÀ: 2?]`
- **Informazioni mancanti per pianificare**: la pagina non dice quanto tempo passa dal primo contatto alla pubblicazione, quanto dura la consulenza né quali sono i servizi aggiuntivi e i loro costi. `[GRAVITÀ: 2]`
- **Rimandi a più siti**: corsi e iniziative dei partner sono su `gingeracademy.it`, le commissioni nelle Condizioni d'uso, le risposte più dettagliate nelle FAQ. L'utente deve ricomporre da solo il quadro dei costi e dei passi. `[GRAVITÀ: 2]`
- **Pagina FAQ e questa pagina non si richiamano**: la FAQ non rimanda a "Come funziona" e questa pagina rimanda alle FAQ solo in fondo, con un link generico. `[GRAVITÀ: 1]`

---