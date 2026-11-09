# Registro delle correzioni

| Data | Fix | File modificati | Pagine coinvolte | Commit |
|---|---|---|---|---|
| 2026-11-09 | F01 Indicatore di focus del link «Salta al contenuto» (WCAG 2.4.7, AA) | css/ideablume.css, tools/contrasto.py, docs/verifiche/contrasti.md | tutte le 50 pagine (25 IT + 25 EN) | 78cbbec |
| 2026-11-09 | F02 Marchio `idea<b>Blume</b>`: `<b>` usato solo per lo stile → `<span class="brand__accent">` (WCAG 1.4.4, AA) | tools/build.py, css/ideablume.css, docs/verifiche/anteprima-design-system.html | tutte le 50 pagine (25 IT + 25 EN) | 1541ed1 |
| 2026-11-09 | F03 `role="status"` spostato dall'`<h2>` dei risultati di ricerca a un `<div>` contenitore (WCAG 1.3.1 / 4.1.2, A) | tools/build.py | cerca.html, en/cerca.html | 6e864be |
| 2026-11-09 | Chiusura: limiti noti della dichiarazione di accessibilità aggiornati (messaggi di stato non ancora verificati con screen reader) | data/sito.json | accessibilita.html, en/accessibilita.html | e8a3ae1 |
