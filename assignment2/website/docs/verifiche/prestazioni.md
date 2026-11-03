# Prestazioni (Lighthouse mobile)

Generato da `tools/prestazioni.js` il 03/11/2026, 10:20:42 con Lighthouse 12.8.2 e Google Chrome, impostazioni mobile predefinite (Moto G Power emulato, rete 4G lenta e CPU rallentata simulate), server statico locale.

| Pagina | Prestazioni | Accessibilità | Best practice | SEO | FCP | LCP | TBT | CLS | Speed Index | Peso trasferito |
|---|---|---|---|---|---|---|---|---|---|---|
| Home | **98** | 100 | 100 | 100 | 1,7 s | **2,3 s** | 0 ms | **0,000** | 1,7 s | 226 KB |
| Elenco dei progetti | **95** | 100 | 100 | 100 | 2,0 s | **2,6 s** | 0 ms | **0,000** | 2,0 s | 271 KB |
| Pagina progetto | **98** | 100 | 100 | 100 | 1,2 s | **2,3 s** | 0 ms | **0,000** | 1,2 s | 219 KB |
| Donazione | **97** | 100 | 100 | 100 | 1,8 s | **2,4 s** | 0 ms | **0,000** | 1,8 s | 256 KB |

## Confronto con IdeaGinger (assignment1, report del 15/10/2026, smartphone)

| Pagina ideaBlume | Pagina IdeaGinger | Prestazioni | Accessibilità | LCP | CLS | TBT |
|---|---|---|---|---|---|---|
| Elenco dei progetti | Progetti (scheda partner) | 50 → **95** | 71 → **100** | 16,6 s → **2,6 s** | 0,003 → **0,000** | 60 ms → **0 ms** |
| Pagina progetto | Mind the Climate | 41 → **98** | 73 → **100** | 34,1 s → **2,3 s** | 0,165 → **0,000** | 440 ms → **0 ms** |
| Donazione | Donazione (di fatto la home) | 39 → **97** | 74 → **100** | 72,1 s → **2,4 s** | 0,478 → **0,000** | 170 ms → **0 ms** |

Obiettivi (R-122): LCP ≤ 2,5 s, CLS ≤ 0,1, INP ≤ 200 ms. Lighthouse in laboratorio non misura l'INP: si usa il TBT come indicatore (≤ 200 ms). Il server locale non comprime i file (su GitHub Pages i file sono serviti con compressione gzip), quindi i valori pubblicati possono solo migliorare.
