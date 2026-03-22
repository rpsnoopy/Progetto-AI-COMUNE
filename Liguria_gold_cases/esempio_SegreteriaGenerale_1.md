# GOLD CASE — Area 1 · Segreteria Generale · Caso 1

## Atto: Delibera di Giunta Municipale — Approvazione Regolamento

**Agente:** COMUNE-SEGRETERIA-GENERALE v.2.0
**Revisore:** COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quali sono i requisiti formali per l'approvazione di un regolamento comunale da parte della Giunta?

**RISPOSTA ATTESA (schema):**
L'agente illustra brevemente il procedimento: proposta del dirigente competente,
pareri obbligatori (regolarità tecnica e contabile), deliberazione di Giunta,
pubblicazione all'albo pretorio, esecutività. Indica il riferimento normativo
principale (D.Lgs. 267/2000, art. 48 e 134).

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la delibera di Giunta per l'approvazione del Regolamento comunale per
> la gestione del patrimonio immobiliare. Il regolamento è composto da 18 articoli
> ed è stato predisposto dall'Ufficio Patrimonio. La delibera è del Comune di
> Ameglia, seduta del 25 marzo 2026, n. 42.

**RISPOSTA ATTESA (schema):**
L'agente genera la bozza completa: intestazione, oggetto, premesse con richiamo
al D.Lgs. 267/2000, visto il parere di regolarità tecnica e contabile, delibera
di approvare il Regolamento allegato (all. A), di dichiarare il presente atto
immediatamente eseguibile, di disporne la pubblicazione all'albo pretorio.
Schema: [Delibera n. 42/2026 — Comune di Ameglia — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Aggiungi nelle premesse il riferimento alla deliberazione del Consiglio Comunale
> n. 18/2025 che ha indirizzato la Giunta alla redazione del regolamento.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna la bozza inserendo nelle premesse: "Visto l'indirizzo espresso
dal Consiglio Comunale con deliberazione n. 18 del [data] 2025 con cui si
demandava alla Giunta la predisposizione del presente regolamento;"
Ripresenta la bozza aggiornata con la stessa offerta salva/revisione.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Delibera di Giunta · 25/03/2026
Prodotto da: COMUNE-SEGRETERIA-GENERALE v.2.0
Revisionato da: COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01
---
[Output del revisore: verifica conformità D.Lgs. 267/2000, art. 48;
controllo pareri obbligatori; verifica dichiarazione di immediata
eseguibilità ex art. 134 co. 4; eventuali note su formule mancanti
o riferimenti normativi da aggiornare.]
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
Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato
(es. .docx). Il file viene salvato. L'agente conferma il salvataggio.

---

## NOTE DI TEST

- Verificare che la bozza al TURNO 2 contenga: intestazione, oggetto, premesse,
  pareri, dispositivo, dichiarazione di eseguibilità.
- Verificare che al TURNO 4 il testo mostrato sia l'output del REVISORE (non
  una rielaborazione dell'agente).
- Verificare che al TURNO 5 si apra il dialog di salvataggio.
