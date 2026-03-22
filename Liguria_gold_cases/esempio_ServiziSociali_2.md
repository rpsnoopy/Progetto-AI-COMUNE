# GOLD CASE — Area 2 · Servizi Sociali · Caso 2

## Atto: Provvedimento — Ammissione al servizio di assistenza domiciliare (SAD)

**Agente:** COMUNE-SERVIZI-SOCIALI v.2.0
**Revisore:** COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Cos'è il SAD e chi può accedervi? Il Comune può erogarlo direttamente
> o deve affidarsi a cooperative?

**RISPOSTA ATTESA (schema):**
L'agente descrive il Servizio di Assistenza Domiciliare (SAD): prestazioni
socio-assistenziali a domicilio per anziani, disabili, persone non autosufficienti.
Spiega che il Comune può erogarlo direttamente o tramite cooperative accreditate.
Richiama L. 328/2000, Piano di Zona, ISEE come criterio di accesso e compartecipazione.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il provvedimento di ammissione al SAD per il sig. Giovanni Esposito,
> nato il 12/04/1942, CF SPOGNN42D12A261K, residente in Via Mazzini 8,
> Ameglia. Valutazione UVM del 18/03/2026: non autosufficienza parziale,
> ISEE € 7.500,00. Ore assegnate: 8 ore settimanali. Operatore assegnato:
> Cooperativa Insieme Srl. Compartecipazione utente: € 1,20/ora.
> Det. n. 89 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con valutazione UVM, ISEE,
richiamo L. 328/2000 e Regolamento SAD, determina di ammettere il sig. Esposito
al servizio con 8 ore settimanali, di affidare l'erogazione alla Cooperativa
Insieme Srl, di stabilire la compartecipazione a € 1,20/ora, di comunicare
il provvedimento all'interessato e alla cooperativa.
Schema: [Det. n. 89/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Il servizio decorre dal 1° aprile 2026 e ha durata di 6 mesi, rinnovabile
> previa rivalutazione UVM. Aggiungi queste informazioni.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo specificando: "che il servizio ha decorrenza
dal 01/04/2026 e durata di 6 (sei) mesi, con scadenza al 30/09/2026, rinnovabile
previa nuova valutazione dell'Unità di Valutazione Multidisciplinare (UVM)."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 89/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-SOCIALI v.2.0
Revisionato da: COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01
---
[Output del revisore: verifica conformità L. 328/2000; controllo
riferimento al Piano di Zona; verifica clausola di rivalutazione periodica;
controllo comunicazione all'interessato con indicazione del responsabile
del procedimento; nota su diritto di ricorso (L. 241/1990 art. 3).]
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

- Verificare che la bozza indichi decorrenza, durata e compartecipazione.
- Verificare che il revisore segnali l'obbligo di indicare il responsabile
  del procedimento e i termini per eventuale ricorso.
