# GOLD CASE — Area 8 · Istruzione - Cultura · Caso 1

## Atto: Determinazione — Concessione patrocinio per evento culturale

**Agente:** COMUNE-ISTRUZIONE-CULTURA v.2.0
**Revisore:** COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Il patrocinio comunale è gratuito oppure implica un contributo economico?
> Quali eventi possono ottenerlo e chi decide?

**RISPOSTA ATTESA (schema):**
L'agente spiega che il patrocinio è di norma gratuito (solo concessione del
nome/logo del Comune) e non implica automaticamente contributo economico.
Il contributo è eventuale e separato. La concessione è decisa dal Sindaco o
dal Dirigente delegato, su istruttoria dell'ufficio cultura, con delibera o
determinazione. I requisiti tipici: rilevanza pubblica, assenza scopo di lucro
esclusivo, coerenza con le finalità istituzionali. Richiama il Regolamento
comunale per la concessione di patrocini (se adottato).

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di concessione del patrocinio comunale per la
> "Sagra del Pesce" organizzata dall'Associazione Pescatori di Ameglia
> (CF 90012345678), edizione 2026, che si terrà il 25-26 aprile 2026 in
> Piazza della Libertà. L'evento ha rilevanza turistica e promuove le tradizioni locali.
> Il patrocinio è solo nominale (logo Comune), nessun contributo economico.
> Det. n. 55 del 25/03/2026. Responsabile: dott.ssa Serena Ferti,
> Settore Istruzione e Cultura.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con domanda dell'associazione,
richiamo al Regolamento patrocini o alle disposizioni generali, valutazione
della rilevanza pubblica dell'evento, determina di concedere il patrocinio
nominale del Comune di Ameglia all'evento "Sagra del Pesce" 25-26/04/2026,
autorizza l'utilizzo del logo comunale con le modalità indicate dall'ufficio,
precisa che il patrocinio non comporta oneri finanziari per l'Ente.
Schema: [Det. n. 55/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> L'associazione chiede anche di poter usare il logo nella pubblicità online
> e sui social. Aggiungi questa autorizzazione con il vincolo che i materiali
> devono essere approvati preventivamente dall'ufficio comunicazione.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo: "Il patrocinio autorizza l'utilizzo del logo
del Comune di Ameglia nei materiali promozionali dell'evento, incluse le
piattaforme digitali e i canali social, a condizione che ogni materiale
contenente il logo sia preventivamente trasmesso all'Ufficio Comunicazione del
Comune per approvazione formale, con preavviso di almeno 5 giorni lavorativi."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 55/2026 · 25/03/2026
Prodotto da: COMUNE-ISTRUZIONE-CULTURA v.2.0
Revisionato da: COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01
---
[Output del revisore: verifica che il patrocinio sia solo nominale (nessun
impegno di spesa → nessun visto di regolarità contabile necessario);
controllo che l'utilizzo del logo rispetti le linee guida identità visiva
del Comune; nota su responsabilità dell'organizzatore per sicurezza
dell'evento (TULPS, SIAE, autorizzazioni di pubblica sicurezza);
verifica che la determinazione escluda responsabilità del Comune per
l'organizzazione e per eventuali danni; controllo privacy su utilizzo logo
online (GDPR se il logo compare con immagini di persone).]
```

"Per applicare le correzioni alla bozza risponda **applica le note del revisore**."

---


---

### TURNO 5 — Applicazione note del revisore alla bozza

**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**
La LLM rilegge la bozza originale e il report del revisore, applica tutte le
correzioni e le integrazioni indicate e genera la versione finale dell'atto,
che presenta all'utente integralmente.
Al termine aggiunge:

"Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella
permanente risponda **salva**."

### TURNO 6 — Salvataggio

**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**
Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato.
Il file viene salvato. L'agente conferma.

---

## NOTE DI TEST

- Verificare che la bozza escluda esplicitamente impegni finanziari del Comune.
- Verificare che il revisore segnali la necessità di una clausola di manleva
  sulla responsabilità organizzativa dell'evento.
