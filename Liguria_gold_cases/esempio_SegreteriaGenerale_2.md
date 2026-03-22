# GOLD CASE — Area 1 · Segreteria Generale · Caso 2

## Atto: Determinazione Dirigenziale — Affidamento diretto servizio

**Agente:** COMUNE-SEGRETERIA-GENERALE v.2.0
**Revisore:** COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quando posso procedere con affidamento diretto senza gara per un servizio?
> Quali sono i limiti di importo attuali?

**RISPOSTA ATTESA (schema):**
L'agente illustra la disciplina degli affidamenti diretti: soglia € 140.000 per
servizi (D.Lgs. 36/2023, art. 50), obbligo di motivazione rafforzata, principio
di rotazione, invito ad almeno un operatore economico. Distingue affidamento
diretto sotto € 5.000 (semplificato) e tra € 5.000 e € 140.000.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera una determinazione dirigenziale per l'affidamento diretto del servizio
> di trascrizione verbali del Consiglio Comunale per l'anno 2026 alla ditta
> Verbatim Srl, P.IVA 01234567890, sede in Via Mazzini 10, La Spezia, per un importo
> di € 4.800,00 IVA inclusa. CIG: Z3A1234567. Responsabile del procedimento:
> dott.ssa Maria Bianchi. Comune di Ameglia, det. n. 215 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con richiamo al D.Lgs. 36/2023
art. 50 co. 1 lett. a), verifica DURC e antimafia, determina di affidare il
servizio, impegnare la spesa sul cap. di bilancio indicato, trasmettere
all'operatore. Schema: [Det. n. 215/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Il capitolo di bilancio è il 1040/2026, stanziamento € 10.000,00.
> Aggiungilo nel dispositivo.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo inserendo: "di impegnare la spesa di € 4.800,00
IVA inclusa sul capitolo 1040 del bilancio 2026, recante lo stanziamento di
€ 10.000,00, sufficiente alla copertura."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 215/2026 · 25/03/2026
Prodotto da: COMUNE-SEGRETERIA-GENERALE v.2.0
Revisionato da: COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01
---
[Output del revisore: verifica soglia affidamento diretto art. 50 D.Lgs. 36/2023;
controllo CIG, DURC, tracciabilità flussi finanziari L. 136/2010;
verifica principio di rotazione; note su eventuali elementi mancanti.]
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

- Verificare che la bozza contenga CIG, riferimento normativo D.Lgs. 36/2023,
  tracciabilità flussi finanziari, impegno di spesa con capitolo.
- Verificare che la revisione evidenzi eventuale mancanza di elementi obbligatori
  (es. verifica antimafia, DURC, principio di rotazione).
