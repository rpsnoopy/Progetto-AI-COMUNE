# GOLD CASE — Area 5 · Servizi Demografici · Caso 2

## Atto: Rettifica di atto di nascita

**Agente:** COMUNE-SERVIZI-DEMOGRAFICI v.2.0
**Revisore:** COMUNE-REVISORE-DEMOGRAFICI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quando si può procedere alla rettifica di un atto di stato civile d'ufficio
> e quando invece occorre il decreto del Tribunale?

**RISPOSTA ATTESA (schema):**
L'agente distingue: la rettifica d'ufficio (art. 98 DPR 396/2000) è possibile
per errori materiali evidenti (refusi, errori di trascrizione) che non incidono
sullo stato della persona. Quando la rettifica implica una modifica sostanziale
(data di nascita, paternità, nazionalità) occorre il decreto del Tribunale
ex art. 95 DPR 396/2000. Indica il ruolo del Procuratore della Repubblica
nel procedimento di rettifica giudiziale.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il provvedimento di rettifica d'ufficio dell'atto di nascita n. 87/1992
> serie A, del Comune di Ameglia, relativo a Marco Bianchi nato il
> 14/05/1992. Errore: il nome del padre è trascritto come "Giusepe" invece
> di "Giuseppe" (refuso). La rettifica è autorizzata dalla sig.ra Ufficiale
> di Stato Civile dott.ssa Anna Ferretti. Provvedimento n. 23 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, estremi dell'atto originale, descrizione dell'errore
materiale riscontrato, richiamo art. 98 DPR 396/2000, attestazione che si tratta
di errore materiale non incidente sullo stato della persona, determina la rettifica
sostituendo "Giusepe" con "Giuseppe", dispone l'annotazione a margine dell'atto
originale, comunicazione all'interessato.
Schema: [Provv. rettifica n. 23/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> L'errore è presente anche nella trascrizione nel registro informatico ANPR.
> Specifica che la rettifica viene eseguita sia sull'atto cartaceo sia
> nell'ANPR.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo: "di procedere alla rettifica sia sull'atto
di nascita cartaceo n. 87/1992, con annotazione a margine, sia nell'Anagrafe
Nazionale della Popolazione Residente (ANPR) attraverso l'aggiornamento della
relativa posizione informatica, ai sensi del D.Lgs. 82/2005 (Codice del
Consumo Digitale) e delle disposizioni ministeriali sull'ANPR."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Provvedimento rettifica n. 23/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-DEMOGRAFICI v.2.0
Revisionato da: COMUNE-REVISORE-DEMOGRAFICI v.1.01
---
[Output del revisore: verifica art. 98 DPR 396/2000 (rettifica d'ufficio
per errore materiale); conferma che il refuso "Giusepe/Giuseppe" rientra
nella rettifica amministrativa senza ricorso al Tribunale;
controllo obbligo annotazione a margine dell'atto originale;
nota su comunicazione all'interessato con indicazione termini ricorso;
verifica aggiornamento ANPR e coerenza con altri registri.]
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

- Verificare che la bozza contenga: estremi esatti dell'atto originale,
  descrizione precisa dell'errore, richiamo art. 98 DPR 396/2000.
- Verificare che il revisore distingua chiaramente tra rettifica d'ufficio
  e rettifica giudiziale (art. 95 DPR 396/2000).
