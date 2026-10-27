---
documento: personas_journey_prompts
progetto: HCI_Assignment · Gruppo A · Funds TOgether su IdeaGinger
versione: 1.0
data: 2026-10-27
modello_consigliato: Claude Opus 5.5 (claude-opus-5-5)
lingua: it
prompt_totali: 26
file: [00_contesto_comune_C00.md, P01_giuseppe_ferrero.md, P02_sara_colombo.md, P03_davide_rinaldi.md, P04_tomas_garcia.md, P05_luca_moretti.md, P06_elena_conti.md, P07_giulia_esposito.md, P08_roberta_galli.md, P09_chiara_marino.md, P10_franco_gallo.md, P11_amir_haddad.md, P12_maria_lombardi.md, 99_verifica_V00.md]
---

# 12 personas e 12 journey map per un sito di crowdfunding: prompt per Opus 5.5

Questa cartella contiene i prompt per generare, con Claude Opus 5.5, **12 personas** e **12 journey map** del sito di crowdfunding **IdeaGinger** (ideaginger.it), nel contesto dell'iniziativa **Funds TOgether** dell'Università di Torino. Ogni persona e ogni journey ha un prompt autonomo, così più persone del gruppo possono generarli in parallelo, ciascuna nella propria conversazione, ottenendo documenti con la stessa struttura.

Le personas e i journey sono costruiti per far emergere i **problemi di usabilità rilevati nella presentazione «Funds TOgether: analisi di usabilità» (Gruppo A, assignment1_gruppoA.pdf, 82 slide)**. Ogni problema è citato con il numero della slide del PDF, nel formato `[S17 · H4 · G4]` (slide 17, euristica H4 di Nielsen, gravità 4).

## Come usarlo

I prompt sono divisi in file:

- [00_contesto_comune_C00.md](00_contesto_comune_C00.md): il **contesto comune C00**, da incollare all'inizio di ogni conversazione.
- 12 file `Pxx_nome.md`, uno per persona, ciascuno con il prompt della persona (`Pxx`) e quello del suo journey (`Jxx`). Sono elencati nell'indice qui sotto.
- [99_verifica_V00.md](99_verifica_V00.md): prompt facoltativo per verificare un documento generato.

Procedura:

1. Apri una **nuova conversazione** con Opus 5.5 per ogni documento da generare (una persona oppure un journey).
2. Incolla il prompt **C00**. Il modello risponde solo con una conferma.
3. Incolla il prompt singolo (`Pxx` per la persona, `Jxx` per il journey) dal file della persona. In alternativa puoi incollare C00 e il prompt singolo **nello stesso messaggio**.
4. Per un journey, se la persona corrispondente è già stata generata (anche da un'altra persona del gruppo), incolla il suo output dentro il tag `<persona_generata>` del prompt `Jxx`. Se non c'è ancora, lascia il tag com'è: il prompt contiene una scheda sintetica sufficiente, quindi persona e journey si possono generare **in qualsiasi ordine e in parallelo**.
5. Salva l'output come `Pxx_nome_output.md` o `Jxx_nome_output.md`. Facoltativo: in una nuova conversazione incolla C00 e il prompt **V00** con l'output per verificare formato e citazioni.

In ogni file, ogni prompt è racchiuso tra due commenti HTML, utili per estrarli in automatico: uno di apertura `BEGIN PROMPT` con gli attributi `id`, `tipo`, `persona` (se c'è) e `richiede`, e uno di chiusura `END PROMPT` con lo stesso `id`. Tra i due c'è un blocco di codice: il testo da copiare è sempre quello **dentro il blocco** (tra le righe con le quattro virgolette inverse). All'interno, ogni prompt usa tag XML (`<scheda_vincolante>`, `<problemi_assegnati>`, `<fasi>`…), che Opus interpreta come sezioni distinte.

## Indice e assegnazione

| ID persona | Prompt journey | File | Persona | Ruolo | Dispositivo principale | Familiarità digitale | Esigenza di accessibilità o contesto | Assegnato a |
|---|---|---|---|---|---|---|---|---|
| P01 | J01 | [P01_giuseppe_ferrero.md](P01_giuseppe_ferrero.md) | Giuseppe Ferrero, 71 | Donatore alla prima esperienza | Tablet Android | Medio-bassa | Presbiopia, tocchi imprecisi | |
| P02 | J02 | [P02_sara_colombo.md](P02_sara_colombo.md) | Sara Colombo, 34 | Donatrice occasionale | Smartphone Android di fascia media, 4G | Media | Attenzione divisa, una mano, pause brevi | |
| P03 | J03 | [P03_davide_rinaldi.md](P03_davide_rinaldi.md) | Davide Rinaldi, 39 | Donatore | PC con screen reader NVDA, iPhone con VoiceOver | Alta (tecnologie assistive) | Non vedente | |
| P04 | J04 | [P04_tomas_garcia.md](P04_tomas_garcia.md) | Tomás García, 31 | Donatore dall'estero | Laptop, smartphone | Alta | Italiano livello A2 | |
| P05 | J05 | [P05_luca_moretti.md](P05_luca_moretti.md) | Luca Moretti, 52 | Donatore abituale e metodico | PC desktop | Media | Daltonismo (deuteranopia) | |
| P06 | J06 | [P06_elena_conti.md](P06_elena_conti.md) | Elena Conti, 58 | Donatrice attenta a fiducia e privacy | PC desktop | Alta | Nessuna specifica; forte bisogno di trasparenza | |
| P07 | J07 | [P07_giulia_esposito.md](P07_giulia_esposito.md) | Giulia Esposito, 20 | Studentessa donatrice, piccolo importo | iPhone | Alta sui social, bassa sui testi lunghi | Dislessia (DSA) | |
| P08 | J08 | [P08_roberta_galli.md](P08_roberta_galli.md) | Roberta Galli, 47 | Visitatrice: giornalista scientifica | Laptop | Alta | Ricerca esaustiva, molte schede aperte | |
| P09 | J09 | [P09_chiara_marino.md](P09_chiara_marino.md) | Chiara Marino, 32 | Promotrice: ricercatrice UniTo che si candida | Laptop macOS | Alta | Tempo frammentato | |
| P10 | J10 | [P10_franco_gallo.md](P10_franco_gallo.md) | Franco Gallo, 63 | Promotore: responsabile di una campagna in corso | PC con monitor grande | Medio-bassa | Presbiopia lieve, poco tempo | |
| P11 | J11 | [P11_amir_haddad.md](P11_amir_haddad.md) | Amir Haddad, 27 | Promotore: comunicazione della campagna | Laptop Linux, smartphone Android | Molto alta | Italiano B2, usa molto la tastiera | |
| P12 | J12 | [P12_maria_lombardi.md](P12_maria_lombardi.md) | Maria Lombardi, 49 | Promotrice esterna a UniTo (associazione) | Smartphone, vecchio PC | Medio-bassa | Tremore lieve alle mani | |

La matrice copre: 8 donatori o visitatori e 4 promotori; 6 donne e 6 uomini; età da 20 a 71 anni; tablet, smartphone di fascia media, desktop, laptop e screen reader; familiarità digitale da medio-bassa a molto alta; frequenza d'uso dalla visita unica all'uso quotidiano; esigenze di accessibilità visive, cognitive, motorie, linguistiche e situazionali.

### Copertura dei problemi principali della presentazione

| Area della presentazione | Problemi più gravi (G3–G4) | Personas che li fanno emergere |
|---|---|---|
| Stato delle campagne e dell'iniziativa | S09, S10, S29, S37 | P01, P03, P05, P06, P08, P09, P10 |
| Accessibilità (contrasto, alt, aria, etichette, testi piccoli) | S17, S23, S35, S51, S54 | P01, P03, P05, P09, P12 |
| Internazionalizzazione | S32, S36, S40 | P04, P11 |
| Modulo di donazione (errori tardivi, anonimato) | S41, S42 | P01, P02, P03, P04, P06, P07, P11 |
| Navigazione e orientamento | S14, S15, S20, S21, S22, S38, S52, S53 | tutte tranne P10 |
| Percorso del promotore (costi, registrazione) | S49, S51, S52, S53, S54 | P09, P12 |
| Homepage (NN/g) | S59, S61, S64 | P01, P06, P07, P10, P12 |
| Mobile e prestazioni | S71, S74 | P02, P03, P07, P11 |

## Note di revisione sulla presentazione (per il gruppo)

Durante la lettura delle 82 slide sono emerse alcune incoerenze da sistemare prima della consegna. Non cambiano i contenuti dei prompt.

- **Conteggio dei problemi.** Il grafico di slide 80 riporta 57 problemi (17 + 15 + 12 + 11 + 2), ma le slide con un problema sono 54: la homepage ne ha 10 (S59–S68), non 12, e la versione mobile ha una sola slide di problema (S71). Anche la distribuzione per gravità del grafico (10/20/18/9) non coincide con le gravità scritte nelle slide (circa 9/19/17/9). Di conseguenza va ricontrollato anche «27 problemi su 57 di gravità 3 o 4» di slide 81.
- **Slide 24.** L'intestazione indica «2 · Minore», il testo «Gravità 1». In questo file è usato il valore dell'intestazione.
- **Slide 23 (contrasto).** La soluzione propone «un contrasto di almeno 3:1». Secondo le WCAG 2.2 (criterio 1.4.3, livello AA) il testo normale richiede almeno **4,5:1**; 3:1 vale solo per testo grande (≥ 18 pt, o ≥ 14 pt in grassetto) e per i componenti grafici dell'interfaccia (criterio 1.4.11). Anche il chip «Obiettivo raggiunto!» a 3,5:1 con testo piccolo non è quindi «sufficiente». Fonte: W3C, *Web Content Accessibility Guidelines 2.2*, https://www.w3.org/TR/WCAG22/#contrast-minimum
- **Piè di pagina delle slide 32–34.** L'indicazione «Pagine… Task…» sembra riferita alla slide adiacente (per esempio slide 33 parla di tooltip in Mind the Climate, MILK-ACT e VIBE, ma il piè di pagina che li nomina è sulla slide 32). Per questo il catalogo qui sotto non riporta i task per singolo problema.

## Nota di metodo

Secondo gli appunti, le personas «raccontano le evidenze della ricerca». Queste 12 personas, invece, non derivano da interviste o osservazioni con utenti reali: sono **personas ipotetiche (proto-personas)** costruite a partire da una valutazione euristica. Vanno dichiarate come tali nella consegna e, idealmente, validate con almeno qualche intervista o test di usabilità. I prompt chiedono al modello di indicarlo nella sezione «Note per il team».
