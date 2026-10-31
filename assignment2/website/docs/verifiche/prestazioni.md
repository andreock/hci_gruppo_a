# Prestazioni (Lighthouse mobile)

Generato da `tools/prestazioni.js` il 31/10/2026, 15:25:46 con Lighthouse 12.8.2 e Google Chrome, impostazioni mobile predefinite (Moto G Power emulato, rete 4G lenta e CPU rallentata simulate), server statico locale.

| Pagina | Prestazioni | Accessibilità | Best practice | SEO | FCP | LCP | TBT | CLS | Speed Index | Peso trasferito |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | **100** | 100 | 100 | 100 | 1,1 s | **1,7 s** | 0 ms | **0,000** | 1,1 s | 100 KB |
| Elenco dei progetti | **100** | 100 | 100 | 100 | 1,1 s | **1,9 s** | 0 ms | **0,000** | 1,1 s | 149 KB |
| Pagina progetto | **100** | 100 | 100 | 100 | 1,1 s | **1,7 s** | 0 ms | **0,000** | 1,1 s | 97 KB |
| Donazione | **100** | 100 | 100 | 100 | 0,9 s | **1,6 s** | 0 ms | **0,000** | 0,9 s | 134 KB |

## Confronto con IdeaGinger (assignment1, report del 15/10/2026, smartphone)

| Pagina ideaBlume | Pagina IdeaGinger | Prestazioni | Accessibilità | LCP | CLS | TBT |
|---|---|---|---|---|---|---|
| Elenco dei progetti | Progetti (scheda partner) | 50 → **100** | 71 → **100** | 16,6 s → **1,9 s** | 0,003 → **0,000** | 60 ms → **0 ms** |
| Pagina progetto | Mind the Climate | 41 → **100** | 73 → **100** | 34,1 s → **1,7 s** | 0,165 → **0,000** | 440 ms → **0 ms** |
| Donazione | Donazione (di fatto la home) | 39 → **100** | 74 → **100** | 72,1 s → **1,6 s** | 0,478 → **0,000** | 170 ms → **0 ms** |

Obiettivi (R-122): LCP ≤ 2,5 s, CLS ≤ 0,1, INP ≤ 200 ms. Lighthouse in laboratorio non misura l'INP: si usa il TBT come indicatore (≤ 200 ms). Il server locale non comprime i file (su GitHub Pages i file sono serviti con compressione gzip), quindi i valori pubblicati possono solo migliorare.
