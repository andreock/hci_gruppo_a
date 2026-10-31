# 01 · Inventario delle fonti

Data dell'inventario: 31/10/2026 · Repository: `hci_gruppo_a`, branch `assignment1-valutazione-euristica` (commit `c67c067`).

Questo documento elenca **tutti i file del repository** fuori da `assignment2/website/`, con il loro ruolo nel progetto del sito. La colonna «Letto» dice come è stato usato il file: **sì** (letto per intero), **estratto** (testo estratto con uno strumento e letto), **parziale** (lette le parti rilevanti), **immagine** (guardata), **no** (non necessario, con il motivo nelle note).

## 1. Strumenti disponibili nell'ambiente

| Strumento | Presente | Uso previsto |
|---|---|---|
| `python3` 3.15.1 | sì | script di build (solo libreria standard), verifiche di dati, link e contrasti |
| `node` v24.21.0, `npx`, `npm` 11.19 | sì | Playwright e axe-core nella Fase 4 (da installare in `tools/`, solo se servono) |
| `pdftotext`, `pdfinfo` (poppler) | sì | lettura dei PDF di assignment1 |
| Browser Playwright in cache (`chromium-1234`, `chromium_headless_shell-1234`, `firefox-1538`, `webkit-2336`) | sì | screenshot, test da tastiera, axe-core |
| Pacchetto `playwright` per Python | **no** | si userà il pacchetto npm |
| Google Chrome.app, Safari.app | sì | verifica manuale |
| `lighthouse`, `pa11y` | **no** | Lighthouse si potrà provare con `npx lighthouse` nella Fase 4; se non funziona, la verifica sarà descritta a mano |
| PIL (Pillow) 13.0 | sì | ritaglio delle immagini dei report |
| `sips` (macOS) | sì | dimensioni e ritagli delle immagini |

## 2. Radice e consegna

| Percorso | Tipo | Che cosa contiene | Letto | Note |
|---|---|---|---|---|
| `README.md` | md, 14 B | Solo il titolo «#HCI gruppo A» | sì | Nessuna informazione utile |
| `.gitignore` | testo, 9 B | Esclude `.DS_Store` | sì | — |
| `.DS_Store`, `assignment1/.DS_Store`, `assignment2/.DS_Store`, `assignment2/personas/.DS_Store` | binari macOS | Metadati del Finder | no | Irrilevanti, ignorati da Git ma presenti nella cartella |
| `assignment2/Istruzioni.md` | md, 11 KB | Consegna della docente per l'assignment 2: personas, journey, prototipo HTML/CSS, documentazione dell'AI, criteri di valutazione | sì | **Vincoli che prevalgono sul prompt** (vedi `decisioni.md` D-01, D-02): il prototipo deve funzionare **senza server**, aprendo i file nel browser; è richiesta la **versione desktop**; per un gruppo di 4 servono **almeno 10 pagine distinte** e almeno 5 personas |
| `assignment2/README.md` | md, 9 KB | Indice dei 26 prompt (C00, P01–P12/J01–J12, V00), matrice delle 12 personas, tabella di copertura area → chiavi Sxx → personas, note di revisione sulla presentazione | sì | Spiega che le chiavi `Sxx` sono i **numeri di slide** di `assignment1_gruppoA.pdf`. Segnala incoerenze nel conteggio dei problemi (slide 80: 57 problemi, ma le slide-problema sono 54) e un errore WCAG a slide 23 (3:1 invece di 4,5:1) |
| `assignment1/README.md` | md, 4 KB | Struttura di assignment1, stato delle parti, convenzioni (ID, separatore `;` dei CSV, severità 0–4) | sì | La tabella «Stato delle parti» indica le parti 2–4 come «da fare», ma le parti di andre, lorenzo e alex esistono: il README non è aggiornato |

## 3. Assignment 1 · Valutazione euristica (fonte principale dei problemi)

| Percorso | Tipo | Che cosa contiene | Letto | Note |
|---|---|---|---|---|
| `assignment1/assignment1_gruppoA.pdf` | PDF, 82 pagine, 11 MB | Presentazione finale del gruppo «Funds TOgether: analisi di usabilità»: metodo, task T1–T8, 54 slide-problema (Nielsen, NN/g homepage, mobile), Core Web Vitals, conclusioni | estratto (`pdftotext -layout`, tutte le 82 slide) | **Fonte consolidata di riferimento**: le chiavi `Sxx` del catalogo C00 sono i suoi numeri di slide. Slide 80 è un grafico senza testo estraibile. Slide 24: intestazione «2 · Minore», testo «Gravità 1» |
| `assignment1/parti/antofallea/problemi_antofallea.csv` | CSV `;`, UTF-8 con BOM, 22 righe + intestazione | Registro di 22 problemi (pagina partner, BRIGHT, Fai Brillare la Ricerca!, MILK-ACT, checkout, 404, ricerca). Colonne: ID, Autore, Pagine, Task, Problema, Descrizione e conseguenze, Euristica, Motivazione euristica, Severita, Frequenza, Impatto, Persistenza, Giustificazione severita, Proposta, Figure | sì (tutte le righe) | Il problema `Pnn` sta alla riga `nn+1` del file. Molti problemi confluiscono nella presentazione di gruppo, altri no (checkout, 404, ricerca vuota, CTA lontana) |
| `assignment1/parti/antofallea/valutazione_antofallea.pdf` | PDF, 36 pagine | Stampa della presentazione della parte 1: stessi 22 problemi del CSV, confronto desktop/mobile, tre proposte di riprogettazione | estratto | Coincide con il CSV (stessi ID P01–P22). Pag. 32 riporta: «Se una campagna raggiunge l'obiettivo, l'Ateneo raddoppia i fondi fino a 10.000 €» e le 4 fasi del programma (Formazione, Selezione, Accompagnamento, Raccolta e raddoppio) |
| `assignment1/parti/antofallea/src/presentazione.html` | HTML, 65 KB | Sorgente della presentazione della parte 1 | parziale | Il testo è inserito da script: l'estrazione statica dà un risultato vuoto. Si è usato il PDF, che ne è la stampa |
| `assignment1/parti/antofallea/src/img/*.jpg` (36 file) | JPG, 20–235 KB | Screenshot dei problemi della parte 1 (checkout, 404, liste, BRIGHT, MILK-ACT, partner, mobile) | no | Le descrizioni del CSV sono sufficienti; da consultare solo per dubbi puntuali |
| `assignment1/parti/antofallea2/problemi_antofallea2.csv` | CSV `;`, UTF-8 con BOM, 16 righe + intestazione | 16 problemi su menu «Partner», «Servizi», «Collaborazioni», «Come funziona» | sì | Stessa struttura del primo CSV |
| `assignment1/parti/antofallea2/valutazione_antofallea2.pdf` | PDF, 30 pagine | Stampa della seconda parte: stessi 16 problemi, tre proposte di riprogettazione | estratto | Coincide con il CSV |
| `assignment1/parti/antofallea2/src/presentazione.html` | HTML, 58 KB | Sorgente della seconda parte | parziale | Come sopra: testo generato da script |
| `assignment1/parti/antofallea2/src/img/*.jpg` (25 file) | JPG | Screenshot di menu, Servizi, Come funziona | no | Come sopra |
| `assignment1/parti/andre/Pagina_Progetti.md` | md, 14 KB | Analisi euristica della scheda «Progetti» UniTo (12/10/2026) | sì | Le sezioni 1–2 sono commentate (`<!-- -->`). Usa gravità «5», fuori dalla scala 0–4: riportata così com'è con una nota. Le immagini citate (`![[Screenshot …]]`, sintassi Obsidian) **non sono nel repository** |
| `assignment1/parti/andre/Pagina_MindTheClimate.md` | md, 12 KB | Analisi euristica della pagina progetto «Mind the Climate» | sì | Come sopra; nella parte commentata (riga 32) segnala l'obiettivo di 7.000 € nel riquadro e 14.000 € nel testo. Screenshot citati assenti |
| `assignment1/lorenzo/Pagina_ComeFunziona.md` | md, 15 KB | Analisi euristica di «Come funziona» (14/10/2026) | sì | Si trova in `assignment1/lorenzo/`, non in `assignment1/parti/lorenzo/` come le altre parti |
| `assignment1/lorenzo/Pagina_FAQ.md` | md, 16 KB | Analisi euristica della pagina FAQ | sì | Come sopra |
| `assignment1/lorenzo/screen_faq/cmf_e9_404.png`, `faq_e6_404.png` | PNG, 698 KB ciascuno | Pagina 404 di IdeaGinger in inglese («Opps! page not found», «adress») | immagine | I due file hanno la stessa dimensione: probabilmente sono la stessa immagine. **Precisazione rispetto al prompt**: la 404 è stata ottenuta digitando un indirizzo errato (`/faqs.html`, `Pagina_FAQ.md:130`), non seguendo un link rotto di FAQ o «Come funziona» |
| `assignment1/lorenzo/screen_faq/faq_e1_title.png`, `cmf_e9_img.png` | PNG | Titolo della scheda FAQ uguale alla home; immagine di «Come funziona» | no | Descritte nel testo |
| `assignment1/alex/README.md` | md, 36 KB | Valutazione di MatematIcA, VIBE, registrazione progettisti, checkout MILK-ACT (13–15/10/2026): 15 problemi nuovi (A-P01–A-P15) e 3 ricorrenze (R-P02, R-P04, R-P07), verifica di accessibilità e colori, proposte testuali | sì | Scala di severità con 3 = «grave» e 4 = «critico» (diversa dalla presentazione di gruppo, dove 3 = «importante», 4 = «grave»). I nomi dei componenti sono segnaposto `[NOME DA INSERIRE]` |
| `assignment1/alex/img/fig01…fig08*.png` | PNG, 0,1–1,5 MB | Figure 1–8 del README di alex (stato mobile, ricompense bilingui, signup, checkout) | no | Le didascalie nel README descrivono il contenuto |
| `assignment1/web_core_vitals/*.png` (8 file) | PNG ~3420 × 15000 px | Report PageSpeed Insights del 15/10/2026 per Partnership, Progetti, Mind the Climate, Donazione, su smartphone e computer | immagine (ritagli delle metriche) | `partner_wcv.png` è la versione smartphone; `parner_wcv_computer.png` ha un refuso nel nome. I report «donazione» mostrano nel filmstrip la **homepage con il banner dei cookie**: il checkout aperto direttamente reindirizza alla home (coerente con A-P11 di alex), quindi le misure del «modulo di donazione» riguardano in realtà la homepage |

### 3.1 Valori Core Web Vitals annotati dai report

Dati reali (Chrome UX Report, 28 giorni, da slide 75 di `assignment1_gruppoA.pdf` e verificati sul report `donazione_wcv_mobile.png`): uguali per le quattro pagine perché il dato è aggregato a livello di origine.

| Dispositivo | LCP | INP | CLS | FCP | TTFB | Esito |
|---|---|---|---|---|---|---|
| Smartphone | 3,4 s | 131–132 ms | 0,01 | 2,3 s | 1,6 s | non superata |
| Computer | 1,7 s | 51 ms | 0,04 | 1,5 s | 1,1–1,2 s | superata |

Test di laboratorio (Lighthouse 13.5.0, letti dai ritagli dei report):

| Pagina | Dispositivo | Prestazioni | Accessibilità | FCP | LCP | TBT | CLS | Speed Index |
|---|---|---|---|---|---|---|---|---|
| Partnership | Smartphone | 68 | 77 | 5,6 s | 15,5 s | 0 ms | 0,001 | 6,3 s |
| Partnership | Computer | 84 | 71 | 1,2 s | 2,4 s | 10 ms | 0,003 | 1,2 s |
| Progetti | Smartphone | 50 | 71 | 5,5 s | 16,6 s | 60 ms | 0,003 | 6,0 s |
| Progetti | Computer | 67 | 65 | 0,4 s | 3,1 s | 0 ms | 0,313 | 1,1 s |
| Mind the Climate | Smartphone | 41 | 73 | 4,2 s | 34,1 s | 440 ms | 0,165 | 7,5 s |
| Mind the Climate | Computer | 68 | 65 | 0,9 s | 2,9 s | 390 ms | 0,01 | 2,4 s |
| Donazione (di fatto: homepage) | Smartphone | 39 | 74 | 4,5 s | 72,1 s | 170 ms | 0,478 | 5,8 s |
| Donazione (di fatto: homepage) | Computer | 64 | 64 | 0,9 s | 5,0 s | 60 ms | 0,228 | 1,3 s |

Punteggi Prestazioni e Accessibilità da slide 77; metriche dai ritagli. Dal report `donazione_wcv_mobile.png` emergono anche le cause principali: richieste che bloccano il rendering (risparmio stimato 3.170 ms), font (700 ms), cache inefficiente (204 KiB), immagini non ottimizzate.

## 4. Assignment 2 · Utenti del nuovo sito

| Percorso | Tipo | Che cosa contiene | Letto | Note |
|---|---|---|---|---|
| `assignment2/00_contesto_comune_C00.md` | md, 25 KB | Prompt di contesto C00: catalogo dei problemi con chiavi `S09…S74` (= slide del PDF di gruppo) e `X01…X08` («analisi preliminare»), aspetti positivi (`S08`, `S27`, `S44`, `S58`, `S70`), terminologia del corso, formati di persona e journey | sì | Ponte tra assignment1 e personas. **Le chiavi `X01–X08` non hanno una slide**: per ognuna è stata cercata la fonte nei file di assignment1 (vedi `02_problemi_consolidati.md`); per **X03** non è stata trovata |
| `assignment2/99_verifica_V00.md` | md, 2 KB | Prompt di verifica: criteri di qualità (struttura, citazioni, fedeltà, coerenza, terminologia HCI, rispetto) | sì | I criteri 3, 6 e 7 si applicano anche ai testi del sito |
| `assignment2/personas/P01_…P12_*.md` (12 file) | md, ~7,7 KB | **Prompt** (non output) di ogni persona e journey: scheda vincolante, frustrazioni con chiavi `Sxx`, fasi del journey con le chiavi assegnate | sì (scheda e fasi di tutti) | Fonte della mappa fase del journey → chiavi `Sxx`, usata nella tracciabilità |
| `assignment2/personas/da_rivedere_P10-P12.md` | md, 12 KB | Note di revisione di Lorenzo su P10–P12 (v2): personas scollegate da IdeaGinger, journey «To-be», P12 ridefinita come partner esterna, decisioni aperte del gruppo | sì | **P10–P12 sono in versione 2 ma con decisioni ancora aperte** (§2: template vs Istruzioni, approvazione di P12, varietà P10/P11). Contiene un elenco «Opportunità → elementi del prototipo» per P10–P12, usato nei requisiti |
| `assignment2/personas/personas/*.html` (12 file) | HTML | **Schede persona P01–P12** (output) | estratto | **Versione di riferimento** (vedi §5). P04–P06 e P10–P12 pesano ~475 KB per immagini incorporate nel template |
| `assignment2/personas/journey/*.html` (12 file) | HTML | **Journey J01–J12** (output) | estratto | Versione di riferimento |
| `assignment2/personas/personas_template.html`, `user_journey_template.html` | HTML ~470 KB | Template HTML vuoti del corso | no | Modelli, senza contenuti |
| `assignment2/personas/scheda_persona.pdf`, `scheda_user_journey.pdf` | PDF | Template ufficiali del corso | no | Il C00 li cita come `template/…`, ma sono in `assignment2/personas/`: percorso diverso da quello indicato |
| `assignment2/alex/README.md` | md, 1 KB | Contributo di Alex: P01–P03 e J01–J03 in md e HTML | sì | — |
| `assignment2/alex/personas/P01–P03.md`, `alex/journeys/J01–J03.md` | md, ~4,5 KB | Sorgenti Markdown di P01–P03 e J01–J03 | sì (P01; gli altri confrontati tramite gli HTML) | Contenuto identico agli HTML generati |
| `assignment2/alex/output/html/*.html` (6 file) | HTML | P01–P03 e J01–J03 generati | confrontati | **Byte per byte identici** alle copie in `assignment2/personas/personas/` e `assignment2/personas/journey/` (verificato con `cmp`) |
| `assignment2/alex/scripts/genera_html.py` | Python, 10 KB | Generatore degli HTML di Alex | no | Non serve al sito |
| `assignment2/alex/documentazione_uso_ai.md` | md, 5,5 KB | Documentazione dell'uso dell'AI per P01–P03 | no | Pertinente al PDF della consegna, non al sito |

## 5. Personas e journey: versione di riferimento

| Persona | Versione di riferimento | Versione/stato | Note |
|---|---|---|---|
| P01–P03 | `assignment2/personas/personas/P0x_*.html` (= `alex/output/html/`, = `alex/personas/*.md`) | v3, servizio generico, journey As-is | Copie identiche: nessun conflitto |
| P04–P06 | `assignment2/personas/personas/P0x_*_scheda_persona.html` | v3, servizio generico, As-is | Unica copia |
| P07–P09 | `assignment2/personas/personas/P0x_*_persona.html` | **v1**: nominano IdeaGinger, Funds TOgether, UniTo e citano le chiavi `[Sxx · Hx · Gx]` | In contrasto con la regola 1 del C00 (genericità). Utili per la tracciabilità perché citano le chiavi; restano bozze da allineare |
| P10–P12 | `assignment2/personas/personas/P1x_*_persona.html` | v2, «nuovo sito UniTo», journey **To-be** | Bozze con decisioni aperte (`da_rivedere_P10-P12.md`). P12 è ridefinita come **partner esterna** (associazione) che segue il percorso «contatto», non la registrazione; P10 è professore ordinario di area veterinaria, campagna inventata «AlveareSano» al 130% |

Motivazione: le cartelle `personas/personas/` e `personas/journey/` sono le uniche che contengono tutte e 12 le schede, sono state create dopo le copie di Alex (commit `c67c067` «Move alex's personas» del 30/10/2026) e i file di Alex sono identici. Le versioni hanno però **tre livelli di maturità** diversi (v1, v2, v3): il sito tiene conto di tutti i punti di dolore, ma per P07–P12 le scelte che dipendono solo da quelle bozze sono segnate in `decisioni.md`.

Incoerenze tra le fonti di assignment2 da segnalare al gruppo:
- P07: il README la descrive con familiarità «alta sui social, bassa sui testi lunghi»; la scheda dà 4/5 sui social e 2/5 con moduli e testi lunghi. Non c'è contraddizione sostanziale.
- P10: il README dice «Presbiopia lieve, poco tempo» e familiarità «medio-bassa»; la scheda dà 2/5. Coerente.
- P12: il README la indica come «Promotrice esterna a UniTo (associazione)» che lancia la campagna; la v2 la trasforma in partner che chiede un contatto. Il README non è stato aggiornato (lo segnala lo stesso `da_rivedere_P10-P12.md`, §2.2).
- C00 cita i template in `template/`, che non esiste.

## 6. Stato iniziale di `assignment2/website/`

La cartella esisteva ed era **vuota** (verificato con `ls -la` il 31/10/2026). Nessun file da preservare.
