# GOLD CASE — Area 5 · Servizi Demografici · Caso 3

## Atto: Atto di notorietà — Dichiarazione sostitutiva per successione

**Agente:** COMUNE-SERVIZI-DEMOGRAFICI v.2.0
**Revisore:** COMUNE-REVISORE-DEMOGRAFICI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> L'ufficio anagrafe può autenticare una dichiarazione sostitutiva di atto
> di notorietà? Serve il notaio o basta l'Ufficiale di Stato Civile?

**RISPOSTA ATTESA (schema):**
L'agente spiega che la dichiarazione sostitutiva di atto di notorietà (DSAN)
può essere resa davanti all'Ufficiale di Stato Civile del Comune (art. 21 DPR
445/2000) senza necessità del notaio, salvo casi specifici (atti da produrre
all'estero o per atti pubblici soggetti a trascrizione). L'autenticazione della
firma è gratuita ex art. 40 L. 183/2011.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera l'atto di notorietà per la sig.ra Lucia Mori, CF MROLCU65A42A261Z,
> nata il 02/01/1965 a Ameglia, residente in Via Verdi 11, che dichiara
> di essere l'unica erede del defunto sig. Carlo Mori, deceduto il 10/01/2026
> a Ameglia, CF MROCLR45C12A261X, senza testamento, essendo l'unica figlia.
> Dichiarazione resa davanti all'Ufficiale di Stato Civile dott.ssa Anna Ferretti.
> Atto n. 34 del 25/03/2026. Due testimoni: sig. Renato Bacci e sig.ra Irene Naldi.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione con autorità ricevente, dati dichiarante (Lucia
Mori), oggetto della dichiarazione (unica erede del sig. Carlo Mori), attestazione
assenza testamento, indicazione dei testimoni con dati identificativi, formula
di notorietà, autenticazione della firma, richiamo art. 21 DPR 445/2000 e
avvertimento penale ex art. 76 DPR 445/2000.
Schema: [Atto notorietà n. 34/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> La dichiarazione serve per la banca ai fini dello svincolo del conto corrente
> del defunto. Aggiungi questa finalità nell'intestazione dell'atto.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna l'intestazione: "La presente dichiarazione sostitutiva di
atto di notorietà è resa ai sensi dell'art. 21 DPR 445/2000 per l'utilizzo
presso istituto bancario ai fini dello svincolo del conto corrente intestato
al defunto sig. Carlo Mori, ai sensi dell'art. 1 co. 4-ter D.Lgs. 209/2005."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Atto di notorietà n. 34/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-DEMOGRAFICI v.2.0
Revisionato da: COMUNE-REVISORE-DEMOGRAFICI v.1.01
---
[Output del revisore: verifica art. 21 DPR 445/2000 (autenticazione firma);
controllo formula di avvertimento penale art. 76 DPR 445/2000 (obbligatoria);
verifica dati testimoni (devono essere maggiorenni, non parenti, presenti);
nota su utilizzo bancario: banche non possono rifiutare la DSAN ex
art. 1 co. 4-ter D.Lgs. 209/2005; controllo che l'atto non richieda
trascrizione (in tal caso serve notaio).]
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

- Verificare che la bozza contenga l'avvertimento penale ex art. 76 DPR 445/2000
  (elemento essenziale, la sua mancanza invalida l'atto).
- Verificare che il revisore indichi correttamente i requisiti dei testimoni
  (maggiorenni, non parenti, presenti fisicamente).
