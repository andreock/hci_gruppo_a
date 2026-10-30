# Assignment 2 - contributo Alex

Questa cartella contiene tre proto-personas e i relativi user journey, prodotti in modo originale a partire dai prompt P01-P03 e dai template ufficiali del corso.

## Contenuti

- `personas/`: schede sorgente in Markdown per Giuseppe Ferrero, Sara Colombo e Davide Rinaldi.
- `journeys/`: user journey sorgente in Markdown, uno per ogni persona.
- `documentazione_uso_ai.md`: sintesi di prompt, criticità delle prime bozze e revisioni effettuate.
- `output/html/`: schede HTML compilate secondo i due template ufficiali.
- `scripts/genera_html.py`: generatore riproducibile degli HTML a partire dai file Markdown.

## Apertura e rigenerazione

I file in `output/html/` sono autonomi e si aprono direttamente in un browser, senza server. Per rigenerarli, eseguire dalla cartella `alex`:

```bash
python3 scripts/genera_html.py
```

I documenti descrivono proto-personas ipotetiche. Non derivano da interviste o osservazioni con utenti reali; le ipotesi da validare sono indicate esplicitamente nelle schede.
