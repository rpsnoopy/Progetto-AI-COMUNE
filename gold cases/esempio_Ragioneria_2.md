# GOLD CASE — Area 4 · Ragioneria - Servizio Finanziario · Caso 2

## Atto: Determinazione — Liquidazione fattura fornitura servizi

**Agente:** COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0
**Revisore:** COMUNE-REVISORE-RAGIONERIA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quali sono i termini di pagamento delle fatture per la PA?
> Cosa succede se il Comune paga in ritardo?

**RISPOSTA ATTESA (schema):**
L'agente illustra il D.Lgs. 231/2002 come modificato dal D.Lgs. 192/2012:
termine ordinario 30 giorni dalla ricezione fattura (60 giorni per enti sanitari).
In caso di ritardo si applicano interessi moratori al tasso BCE + 8 punti.
Indica la piattaforma PCC (Piattaforma Crediti Commerciali) per la gestione
e il monitoraggio dei tempi di pagamento. Richiama l'obbligo di fattura
elettronica ex D.Lgs. 148/2018.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di liquidazione della fattura n. 2026/00145 del
> 05/03/2026 emessa da Pulizie Italia Srl, P.IVA 11223344556, per il servizio
> di pulizie degli uffici comunali — marzo 2026. Importo: € 2.340,00 IVA inclusa
> (imponibile € 1.918,03 + IVA 22% € 421,97). Impegno n. 312/2026 cap. 1180.
> Split payment applicato. Det. n. 178 del 25/03/2026, RUP: sig. Pietro Galli.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con estremi fattura, verifica
regolarità DURC, attestazione di regolare esecuzione del servizio, richiamo
all'impegno originario, determina di liquidare € 2.340,00 a favore di Pulizie
Italia Srl sul cap. 1180/2026 imputando IVA allo Stato (split payment ex
art. 17-ter DPR 633/72), di trasmettere all'ufficio ragioneria per il mandato.
Schema: [Det. n. 178/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> La fattura è stata ricevuta tramite SDI il 06/03/2026, codice univoco
> dell'ufficio AABBCC. Aggiorna le premesse con questi dati.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna le premesse: "Vista la fattura elettronica n. 2026/00145
del 05/03/2026, ricevuta tramite Sistema di Interscambio (SDI) in data 06/03/2026,
codice destinatario ufficio AABBCC, per un importo complessivo di € 2.340,00
IVA inclusa con applicazione dello split payment ex art. 17-ter DPR 633/72."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 178/2026 · 25/03/2026
Prodotto da: COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0
Revisionato da: COMUNE-REVISORE-RAGIONERIA v.1.01
---
[Output del revisore: verifica D.Lgs. 231/2002 termini pagamento;
controllo split payment art. 17-ter DPR 633/72;
verifica DURC regolare e sua validità (120 giorni);
controllo attestazione regolare esecuzione (RUP/DEC);
nota su registrazione PCC entro 30 giorni dalla ricezione;
controllo che l'impegno originario copra la spesa liquidata.]
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

- Verificare che la bozza contenga: data ricezione SDI, estremi impegno,
  split payment, attestazione regolare esecuzione, DURC.
- Verificare che il revisore richiami la PCC e i termini D.Lgs. 231/2002.
