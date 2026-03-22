# GOLD CASE — Area 3 · Ufficio Tecnico · Caso 1

## Atto: Determinazione — Aggiudicazione lavori manutenzione ordinaria strade

**Agente:** COMUNE-UFFICIO-TECNICO v.2.0
**Revisore:** COMUNE-REVISORE-UFFICIO-TECNICO v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Per lavori di manutenzione stradale sotto soglia comunitaria, posso usare
> la procedura negoziata senza bando? Quante ditte devo invitare?

**RISPOSTA ATTESA (schema):**
L'agente illustra la procedura negoziata ex art. 50 D.Lgs. 36/2023: per lavori
tra € 150.000 e € 1.000.000 occorre invitare almeno 5 operatori; sotto € 150.000
almeno 3; sotto € 40.000 affidamento diretto. Richiama l'obbligo di rotazione
e il principio di concorrenza. Indica l'obbligo di CIG e tracciabilità.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di aggiudicazione per i lavori di manutenzione
> ordinaria delle strade comunali — lotto 1, anno 2026. Importo contrattuale:
> € 87.500,00 IVA esclusa. Aggiudicataria: Impresa Edile Rossi Srl,
> P.IVA 09876543210, ribasso del 6,5% sull'elenco prezzi. CIG: AB1234567C.
> RUP: ing. Paolo Mancini. 5 ditte invitate, 3 offerte pervenute.
> Det. n. 312 del 25/03/2026, Comune di Pietrasanta.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con iter procedura negoziata,
verbale di gara, verifica DURC e antimafia, determina di aggiudicare i lavori
all'Impresa Edile Rossi Srl per € 87.500,00 IVA esclusa, di impegnare la spesa,
di stipulare il contratto, di comunicare agli altri concorrenti, di trasmettere
all'ANAC. Schema: [Det. n. 312/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> La spesa è finanziata per € 50.000,00 dal cap. 2100/2026 e per € 37.500,00
> dal cap. 2101/2026. Aggiorna il dispositivo con la copertura finanziaria.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna: "di impegnare la spesa complessiva di € 106.750,00 (IVA
inclusa al 22%) così ripartita: € 61.000,00 sul cap. 2100/2026 e € 45.750,00
sul cap. 2101/2026, entrambi recanti sufficiente disponibilità."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 312/2026 · 25/03/2026
Prodotto da: COMUNE-UFFICIO-TECNICO v.2.0
Revisionato da: COMUNE-REVISORE-UFFICIO-TECNICO v.1.01
---
[Output del revisore: verifica procedura negoziata art. 50 D.Lgs. 36/2023;
controllo CIG, DURC, antimafia; verifica efficacia aggiudicazione (35 giorni
stand-still se applicabile); controllo tracciabilità L. 136/2010;
nota su comunicazione ai concorrenti non aggiudicatari; verifica
pubblicazione ANAC portale trasparenza.]
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

- Verificare che la bozza contenga: CIG, ribasso percentuale, numero ditte
  invitate e offerte, RUP, copertura finanziaria dettagliata.
- Verificare che il revisore richiami lo stand-still period e la pubblicazione ANAC.
