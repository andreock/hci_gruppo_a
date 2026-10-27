---
documento: persona_journey_prompts
prompt_ids: [V00]
richiede: 00_contesto_comune_C00.md
---

# V00 · Verifica facoltativa di un documento generato

Prompt facoltativo per controllare una persona o un journey già generati. In una nuova conversazione incolla prima il prompt C00 da [00_contesto_comune_C00.md](00_contesto_comune_C00.md), poi questo prompt dopo aver inserito il prompt originale e il documento da verificare.

<!-- BEGIN PROMPT id="V00" tipo="verifica" richiede="C00" -->
````text
<prompt id="V00" tipo="verifica" richiede="C00">

<compito>
Verifica il documento incollato in <documento> rispetto al contesto C00 e al prompt che lo ha generato (incollato in <prompt_originale>). Non riscrivere il documento: elenca solo ciò che va corretto.
</compito>

<criteri>
1. Struttura: front matter completo; titoli e ordine delle sezioni identici a <formato_persona> o <formato_journey>.
2. Citazioni: ogni problema assegnato nel prompt originale è citato; ogni citazione esiste nel catalogo C00 con criterio e gravità corretti; problemi_citati coincide con gli ID presenti nel testo.
3. Fedeltà: nessun problema del sito inventato; le ipotesi sono marcate [IPOTESI]; nessun numero, URL o nome reale inventato.
4. Coerenza con la scheda vincolante: età, dispositivo, familiarità, accessibilità e frequenza rispettati.
5. Journey: fasi della tabella uguali al front matter; punteggi della curva emotiva uguali alla riga Emozioni; ogni difficoltà ha un'opportunità; touchpoint e canali non confusi.
6. Terminologia HCI corretta (usabilità e UX, affordance e signifier, touchpoint e canale, euristiche di Nielsen).
7. Rispetto nella descrizione delle esigenze di accessibilità, senza stereotipi.
</criteri>

<prompt_originale>
[INCOLLA QUI IL PROMPT Pxx O Jxx USATO]
</prompt_originale>

<documento>
[INCOLLA QUI IL DOCUMENTO GENERATO]
</documento>

<formato_risposta>
1. Tabella: Criterio | Esito (OK / Da correggere) | Dettaglio.
2. Elenco numerato delle correzioni puntuali, ciascuna con il testo da sostituire e la proposta.
Nessuna introduzione e nessun commento finale.
</formato_risposta>

</prompt>
````
<!-- END PROMPT id="V00" -->
