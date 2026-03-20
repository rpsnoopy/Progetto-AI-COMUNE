# GOLD CASE — Area 2 · Servizi Sociali · Caso 1

## Atto: Determinazione — Concessione contributo economico straordinario

**Agente:** COMUNE-SERVIZI-SOCIALI v.2.0
**Revisore:** COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quali sono i presupposti per concedere un contributo economico straordinario
> a una famiglia in difficoltà? Serve una graduatoria o si può procedere
> per bisogno urgente?

**RISPOSTA ATTESA (schema):**
L'agente illustra la distinzione tra contributi ordinari (con graduatoria ISEE)
e straordinari (per situazione di bisogno urgente e documentata, senza
necessità di graduatoria). Richiama il Regolamento comunale per i servizi
sociali e la L. 328/2000. Indica la documentazione necessaria: relazione
dell'assistente sociale, ISEE o dichiarazione sostitutiva, motivazione urgenza.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione per la concessione di un contributo economico
> straordinario di € 600,00 alla famiglia Marino (sig.ra Anna Marino, CF
> MRNNNA80A41E715Z, 3 figli minori), residente in Via Cavour 5 a Pietrasanta,
> in situazione di grave difficoltà economica documentata da relazione
> dell'assistente sociale dott.ssa Lucia Neri del 20/03/2026. ISEE € 4.200,00.
> Det. n. 88 del 25/03/2026. Capitolo di spesa 3210/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con relazione assistente sociale,
ISEE, richiamo L. 328/2000 e Regolamento comunale, visto parere di regolarità
tecnica, determina di concedere il contributo di € 600,00 alla sig.ra Marino,
di impegnare la spesa sul cap. 3210/2026, di procedere al pagamento tramite
bonifico sul conto indicato, di garantire la riservatezza dei dati ex GDPR.
Schema: [Det. n. 88/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Il pagamento avverrà tramite bonifico su IBAN IT60X0542811101000000123456
> intestato alla sig.ra Marino. Aggiungilo nel dispositivo.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo con i dati del bonifico: "di disporre il
pagamento mediante bonifico bancario sul conto corrente IBAN
IT60X0542811101000000123456, intestato alla sig.ra Anna Marino, entro 30 giorni
dalla presente determinazione."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 88/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-SOCIALI v.2.0
Revisionato da: COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01
---
[Output del revisore: verifica conformità L. 328/2000; controllo clausola
privacy GDPR (Reg. UE 2016/679); verifica motivazione straordinarietà;
controllo che il provvedimento sia adeguatamente anonimizzabile per
pubblicazione; nota su eventuale obbligo di comunicazione all'INPS.]
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

- Verificare che la bozza contenga clausola di riservatezza (GDPR).
- Verificare che il revisore segnali l'eventuale obbligo di pubblicazione
  in forma anonima sull'albo pretorio.
- Verificare che i dati personali (CF, IBAN) siano presenti nel documento
  ma il revisore ne suggerisca la gestione conforme alla normativa privacy.
