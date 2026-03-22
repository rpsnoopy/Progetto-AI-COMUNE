# GOLD CASE — Area 4 · Ragioneria - Servizio Finanziario · Caso 3

## Atto: Variazione al Piano Esecutivo di Gestione (PEG)

**Agente:** COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0
**Revisore:** COMUNE-REVISORE-RAGIONERIA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Chi può approvare una variazione al PEG in corso d'anno?
> Ci sono limiti a quante variazioni si possono fare?

**RISPOSTA ATTESA (schema):**
L'agente spiega che le variazioni al PEG sono approvate dalla Giunta Municipale
(art. 175 D.Lgs. 267/2000), salvo variazioni di sola competenza dirigenziale
(storni tra capitoli dello stesso servizio entro il 30 novembre). Non ci sono
limiti numerici, ma le variazioni che incidono sull'equilibrio di bilancio
richiedono parere del revisore dei conti. Indica il divieto di variazioni nel
mese di dicembre (salvo eccezioni art. 175 co. 3).

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di variazione al PEG per stornare € 8.000,00
> dal cap. 1600/2026 "Spese per formazione personale" (disponibilità residua
> € 12.000,00) al cap. 1620/2026 "Spese per acquisto libri e riviste"
> (dotazione attuale € 1.500,00). Entrambi i capitoli appartengono al
> servizio Biblioteca — centro di costo 14. Motivazione: incremento delle
> acquisizioni bibliografiche per il nuovo polo culturale.
> Det. n. 67 del 25/03/2026. RUP: dott.ssa Carla Rossi.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con disponibilità capitoli,
motivazione della variazione, verifica che la variazione avviene tra capitoli
dello stesso centro di costo (storno dirigenziale), richiamo art. 175 D.Lgs.
267/2000, determina di variare il PEG diminuendo cap. 1600 di € 8.000 e
incrementando cap. 1620 di € 8.000, di aggiornare le scritture contabili.
Schema: [Det. n. 67/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> La variazione è urgente perché entro il 31/03/2026 scade un'offerta
> per l'acquisto di una raccolta di volumi. Inserisci la motivazione
> di urgenza nelle premesse.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna le premesse: "Considerata l'urgenza di procedere entro il
31/03/2026, termine di scadenza dell'offerta commerciale per l'acquisto di una
raccolta di testi specializzati a condizioni economiche particolarmente vantaggiose
per l'Ente, che non potrebbe essere rinviata senza pregiudizio per gli interessi
dell'Amministrazione." Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 67/2026 · 25/03/2026
Prodotto da: COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0
Revisionato da: COMUNE-REVISORE-RAGIONERIA v.1.01
---
[Output del revisore: verifica art. 175 D.Lgs. 267/2000 variazioni PEG;
conferma che storno tra capitoli stesso servizio è di competenza dirigenziale;
controllo che la variazione non alteri equilibri di bilancio;
verifica divieto variazioni dicembre (non applicabile — marzo);
nota su eventuale necessità parere revisore dei conti se variazione
incide su equilibri fondamentali ex art. 175 co. 4.]
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

- Verificare che la bozza indichi disponibilità pre e post variazione per
  entrambi i capitoli e il centro di costo.
- Verificare che il revisore distingua tra variazione dirigenziale e di Giunta
  e indichi correttamente la competenza.
