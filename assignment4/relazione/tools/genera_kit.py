#!/usr/bin/env python3
"""Genera il kit da stampare per le sessioni (kit/kit_test.html e kit/kit_test.pdf).
Uso (da assignment4):  python3 relazione/tools/genera_kit.py"""
import html, os, subprocess, sys
QUI = os.path.dirname(os.path.abspath(__file__)); A4 = os.path.dirname(os.path.dirname(QUI))
sys.path.insert(0, QUI)
from task import TASK, SUS, DEFINIZIONI, URL_TEST, DATI_FINTI  # noqa: E402

import csv
LIMITI = {r["task"]: int(r["tempo_limite_s"]) // 60 for r in csv.DictReader(open(os.path.join(A4, "dati", "task.csv"), encoding="utf-8"))}
e = html.escape
def campo(etichetta): return f'<div class="campo"><span class="l">{e(etichetta)}</span><span class="r"></span></div>'
def scelte(*voci): return " &nbsp; ".join(f'<span class="quad"></span>{e(v)}' for v in voci)

def copione():
    return f"""
<section><h2 id="k1">1 · Prima di ogni sessione</h2>
<ul>
<li>Due persone del gruppo: un <strong>facilitatore</strong> (parla con l'utente) e un <strong>osservatore</strong> (cronometra e compila la scheda, senza intervenire).</li>
<li>Browser in finestra normale, zoom 100%, cronologia e dati del sito cancellati (o finestra anonima), pagina aperta: <code>{e(URL_TEST)}</code>. È la versione consegnata con l'Assignment 3: <strong>non va modificata finché le 8 sessioni non sono finite</strong>.</li>
<li>Registrazione dello schermo e della voce avviata solo dopo il consenso firmato (per esempio OBS Studio, QuickTime o la registrazione di Meet/Zoom se da remoto).</li>
<li>Cartoncini dei task stampati e ritagliati, un task per cartoncino, da consegnare uno alla volta. Scheda dell'osservatore, questionari e penna pronti.</li>
<li>Durata prevista: 30–35 minuti. Ordine dei task uguale per tutti: T1, T2, T3, T4.</li>
</ul>
<h3>Che cosa può dire il facilitatore durante i task</h3>
<div class="due">
<div class="box box--ok"><span class="box__tit">Sì</span><p>«Che cosa stai pensando?» · «Che cosa stai guardando?» · «Che cosa ti aspetti che succeda?» · «Tu che cosa faresti se fossi a casa?» · «Va bene, continua pure.»</p></div>
<div class="box box--problema"><span class="box__tit">No</span><p>Indicare menu, pulsanti o pagine. Usare le parole dell'interfaccia. Dire «giusto» o «sbagliato». Spiegare il sito. Rispondere alle domande sul sito prima della fine («Te lo dico alla fine, promesso»).</p></div>
</div>
<p>Se l'utente è bloccato da più di un minuto e chiede aiuto per la seconda volta, il facilitatore può dare <strong>un solo suggerimento generico</strong> («Prova a guardare se nella pagina c'è altro»): l'osservatore lo segna e l'esito diventa al massimo A. Al tempo limite si chiude il task con «Va benissimo così, passiamo al prossimo».</p>
</section>

<section><h2 id="k2">2 · Copione del facilitatore</h2>
<p class="piccolo">Adattato dal copione di Steve Krug (<em>Rocket Surgery Made Easy</em>). Le parti con la barra arancione vanno lette così come sono.</p>
<h3>Accoglienza (3 minuti)</h3>
<div class="dire"><p>Ciao, grazie di essere qui. Io sono ___ e ti accompagno in questa prova; ___ prende appunti.</p>
<p>Stiamo lavorando a un sito per un esame universitario e vogliamo capire se è facile da usare. Ti chiederò di provare a fare alcune cose sul sito. La sessione dura circa mezz'ora.</p>
<p>La cosa più importante: <strong>stiamo provando il sito, non te</strong>. Qui non puoi sbagliare niente. Se qualcosa non funziona o non si capisce, è proprio quello che ci serve sapere.</p>
<p>Mentre usi il sito ti chiedo di <strong>pensare ad alta voce</strong>: dimmi che cosa guardi, che cosa cerchi, che cosa ti aspetti, che cosa ti sorprende. Non preoccuparti di offenderci: il sito non l'ho fatto io da solo e ci servono opinioni sincere.</p>
<p>Se hai domande falle pure. Ad alcune non potrò rispondere subito, perché ci interessa vedere che cosa fanno le persone quando non hanno nessuno accanto. Ti rispondo alla fine.</p>
<p>Il sito è un prototipo: i progetti sono inventati e non si paga niente davvero. Userai dati di fantasia che ti do io.</p>
<p>Con il tuo permesso registriamo lo schermo e la voce. La registrazione serve solo a noi quattro per riguardare la sessione, e la cancelliamo dopo l'esame. Nella relazione comparirai solo come «Utente» con un numero. Puoi fermarti quando vuoi, senza dare spiegazioni.</p></div>
<p>→ Far firmare il <strong>consenso</strong> (modulo 3), poi avviare la registrazione. → Far compilare il <strong>questionario iniziale</strong> (modulo 4).</p>
<h3>Prova del pensare ad alta voce (1 minuto)</h3>
<div class="dire"><p>Per scaldarci: guarda questa prima pagina senza cliccare niente. Secondo te di chi è questo sito? Che cosa ci si può fare? Che cosa ti colpisce?</p></div>
<p class="piccolo">Non si misura. Serve ad abituare l'utente a parlare e a raccogliere la prima impressione (da annotare nella scheda).</p>
<h3>I quattro task (20 minuti)</h3>
<div class="dire"><p>Adesso ti do un cartoncino alla volta. Leggilo ad alta voce, poi prova a farlo come faresti a casa. Quando pensi di aver finito, dimmelo. Si riparte ogni volta dalla prima pagina del sito.</p></div>
<p>Per ogni task: consegnare il cartoncino → l'utente legge → l'osservatore fa partire il cronometro → alla fine: «Da 1 a 7, quanto è stato facile?» → tornare alla home.</p>
<h3>Chiusura (8 minuti)</h3>
<p>→ Far compilare il <strong>questionario SUS</strong> (modulo 7) senza commentare le risposte. → <strong>Intervista</strong> (modulo 8). → Rispondere alle domande rimaste in sospeso.</p>
<div class="dire"><p>Abbiamo finito. Ci sei stato/a davvero utile, grazie.</p></div>
<p>→ Fermare la registrazione. Entro la giornata: facilitatore e osservatore riguardano insieme la scheda (10 minuti) e copiano i dati nei file <code>dati/*.csv</code>.</p>
</section>"""

def consenso():
    return f"""
<section><h2 id="k3">3 · Consenso informato</h2>
<p>Partecipo volontariamente a una prova di usabilità del prototipo «ideaBlume», svolta dal Gruppo A per il corso di Human-Computer Interaction dell'Università di Torino.</p>
<ul>
<li>La prova riguarda il sito e non le mie capacità. Posso interromperla in qualunque momento senza dare spiegazioni.</li>
<li>Durante la prova non inserisco miei dati personali reali nel sito.</li>
<li>Le mie risposte e le osservazioni sono riportate nella relazione in forma anonima («Utente 1», «Utente 2», …).</li>
</ul>
<p>{scelte("Acconsento")} alla registrazione dello schermo e della voce. La registrazione è vista solo dai quattro componenti del gruppo e viene cancellata dopo l'esame.</p>
<p>{scelte("Non acconsento")} alla registrazione: gli osservatori prendono soltanto appunti scritti.</p>
<p>&nbsp;</p>{campo("Data")}{campo("Firma")}
<p class="piccolo">Questo foglio resta al gruppo e non viene consegnato con la relazione. Codice assegnato (lo scrive il gruppo): Utente ___</p>
</section>"""

def iniziale():
    return f"""
<section><h2 id="k4">4 · Questionario iniziale</h2>
<p class="piccolo">Utente ___ · lo compila l'utente oppure il facilitatore a voce. Nessun nome.</p>
<p><strong>Età</strong><br>{scelte("18–24", "25–34", "35–44", "45–54", "55–64", "65 o più")}</p>
<p><strong>Genere</strong><br>{scelte("Donna", "Uomo", "Altro", "Preferisco non dirlo")}</p>
{campo("Occupazione (per esempio studentessa, impiegato, pensionata)")}
<p><strong>Titolo di studio</strong><br>{scelte("Licenza media", "Diploma", "Laurea", "Oltre la laurea")}</p>
<p><strong>Quanto ti senti a tuo agio con computer e siti web?</strong><br>{scelte("1 per niente", "2", "3", "4", "5 moltissimo")}</p>
<p><strong>Ogni quanto compri o paghi qualcosa online?</strong><br>{scelte("Mai", "Qualche volta l'anno", "Ogni mese", "Ogni settimana")}</p>
<p><strong>Conosci il crowdfunding (raccolte fondi online come GoFundMe, Kickstarter, Produzioni dal Basso)?</strong><br>{scelte("Mai sentito", "Ne ho sentito parlare", "Ho visitato un sito", "Ho donato almeno una volta")}</p>
<p><strong>Hai mai fatto una donazione online (anche non crowdfunding)?</strong><br>{scelte("Sì", "No")}</p>
<p><strong>Hai un legame con l'università o con la ricerca?</strong><br>{scelte("No", "Studio o ho studiato all'università", "Ci lavoro")}</p>
</section>"""

def cartoncini():
    out = ['<section><h2 id="k5">5 · Cartoncini dei task</h2><p class="piccolo">Da ritagliare. Si consegna un cartoncino alla volta; il numero serve solo al gruppo.</p>']
    for t in TASK:
        extra = f'<p class="piccolo"><strong>Dati da usare:</strong> {e(DATI_FINTI)}</p>' if t["id"] in ("T3", "T4") else ""
        out.append(f'<div class="cartoncino"><h3>Attività {t["id"][1]}</h3><p>{e(t["scenario"])}</p>{extra}</div>')
    out.append("</section>")
    return "\n".join(out)

def scheda():
    out = [f"""<section><h2 id="k6">6 · Scheda dell'osservatore</h2>
<p>Utente ___ · Data ______ · Ora ______ · Facilitatore __________ · Osservatore __________</p>
<p>{scelte("In presenza", "Da remoto")} &nbsp; Dispositivo e browser: ______________________</p>
<div class="tabella"><table><caption><b>Come si contano le misure</b> (uguale per tutti gli osservatori)</caption><tbody>
{"".join(f'<tr><th scope="row">{e(n)}</th><td>{e(d)}</td></tr>' for n, d in DEFINIZIONI)}
</tbody></table></div>
<p><strong>Prima impressione</strong> (prova del pensare ad alta voce):</p><div class="riga"></div><div class="riga"></div>
</section>"""]
    for t in TASK:
        out.append(f"""<section><h2 id="k6-{t['id']}">Scheda · {t['id']} {e(t['titolo'])}</h2>
<p class="piccolo">Utente ___ · tempo limite: {LIMITI.get(t['id'], '—')} minuti</p>
<div class="box box--info"><span class="box__tit">Completato se</span><p>{e(t['successo'])}</p></div>
<div class="tabella"><table><thead><tr><th>Tempo (min:s)</th><th>Esito</th><th>Errori (una tacca ciascuno)</th><th>Richieste di aiuto</th><th>Blocchi</th><th>Facilità 1–7</th></tr></thead>
<tbody><tr><td class="alta"></td><td class="alta">{scelte("S", "A", "F")}</td><td class="alta"></td><td class="alta"></td><td class="alta"></td><td class="alta"></td></tr></tbody></table></div>
<p><strong>Da osservare</strong> (ipotesi da verificare, non risposte attese):</p>
<ul>{"".join(f"<li>{e(o)}</li>" for o in t['osservare'])}</ul>
<p><strong>Errori tipici da contare:</strong> {e(t['errori'])}</p>
<p><strong>Percorso seguito</strong> (pagine nell'ordine):</p><div class="riga"></div><div class="riga"></div>
<p><strong>Che cosa fa e dove esita:</strong></p>{'<div class="riga"></div>' * 5}
<p><strong>Frasi dette, tra virgolette:</strong></p>{'<div class="riga"></div>' * 4}
<p><strong>Segni di confusione o frustrazione</strong> (sospiri, risate, «boh», torna indietro più volte…):</p>{'<div class="riga"></div>' * 2}
</section>""")
    return "\n".join(out)

def sus():
    righe = "".join(f'<tr><th scope="row">{i}. {e(q)}</th>' + '<td class="scala"><span class="q"></span></td>' * 5 + "</tr>" for i, q in enumerate(SUS, 1))
    return f"""
<section><h2 id="k7">7 · Questionario finale (SUS)</h2>
<p class="piccolo">Utente ___ · Per ogni frase segna quanto sei d'accordo, pensando al sito che hai appena usato. Rispondi d'istinto.</p>
<div class="tabella"><table><thead><tr><th></th><th class="scala">1<br>Per niente d'accordo</th><th class="scala">2</th><th class="scala">3</th><th class="scala">4</th><th class="scala">5<br>Del tutto d'accordo</th></tr></thead><tbody>{righe}</tbody></table></div>
</section>
<section><h2 id="k8">8 · Intervista finale</h2>
<p class="piccolo">Utente ___ · Domande aperte, 5 minuti. L'osservatore scrive le risposte con le parole dell'utente.</p>
{"".join(f'<p><strong>{e(d)}</strong></p>' + '<div class="riga"></div>' * 3 for d in [
    "1. Che cosa ti è piaciuto di più del sito?",
    "2. Qual è stata la cosa più difficile o fastidiosa?",
    "3. Se potessi cambiare una sola cosa, quale cambieresti?",
    "4. Ti fideresti a donare davvero su un sito così? Che cosa ti farebbe fidare di più?",
    "5. C'è qualcosa che ti aspettavi di trovare e non hai trovato?"])}
</section>"""

def main():
    testo = f"""<!doctype html>
<html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kit del test di usabilità · ideaBlume · Gruppo A</title>
<link rel="stylesheet" href="../relazione/relazione.css">
<style>@page {{ @bottom-left {{ content: "Gruppo A · Kit del test di usabilità"; }} }} @page :first {{ margin: 18mm 18mm 19mm 18mm; }}
.kit h1 {{ font-size: 24pt; margin: 0 0 6pt; }} .kit section:first-of-type h2 {{ break-before: auto; }}</style></head>
<body class="kit"><main>
<h1>Kit del test di usabilità di ideaBlume</h1>
<p>Human-Computer Interaction · Assignment 4 · Gruppo A. Stampare una copia dei moduli 3, 4, 6, 7 e 8 per ogni utente (8 copie), una sola copia dei moduli 1, 2 e 5.</p>
{copione()}{consenso()}{iniziale()}{cartoncini()}{scheda()}{sus()}
</main></body></html>"""
    dest = os.path.join(A4, "kit", "kit_test.html")
    open(dest, "w", encoding="utf-8").write(testo)
    subprocess.run(["node", os.path.join(QUI, "genera_pdf.js"), dest, dest[:-5] + ".pdf"], check=True)

if __name__ == "__main__":
    main()
