# Assignment 2 - contributo Alex

Questa cartella contiene tre proto-personas e i relativi user journey, prodotti in modo originale a partire dai prompt P01-P03 e dai template ufficiali del corso.

## Contenuti

- `personas/`: schede sorgente in Markdown per Giuseppe Ferrero, Sara Colombo e Davide Rinaldi.
- `journeys/`: user journey sorgente in Markdown, uno per ogni persona.
- `documentazione_uso_ai.md`: sintesi di prompt, criticità delle prime bozze e revisioni effettuate.
- `output/pdf/`: versioni PDF pronte per la revisione del gruppo.
- `scripts/genera_pdf.py`: generatore riproducibile dei PDF a partire dai file Markdown.

## Rigenerazione dei PDF

Eseguire dalla cartella `alex`:

```bash
/home/mega/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3 scripts/genera_pdf.py
```

I documenti descrivono proto-personas ipotetiche. Non derivano da interviste o osservazioni con utenti reali; le ipotesi da validare sono indicate esplicitamente nelle schede.
