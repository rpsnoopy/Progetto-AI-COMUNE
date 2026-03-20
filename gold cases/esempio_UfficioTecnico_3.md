# GOLD CASE — Area 3 · Ufficio Tecnico · Caso 3

## Atto: Certificato di Agibilità — Nuova costruzione residenziale

**Agente:** COMUNE-UFFICIO-TECNICO v.2.0
**Revisore:** COMUNE-REVISORE-UFFICIO-TECNICO v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Qual è la procedura per il rilascio del certificato di agibilità?
> Chi deve fare il sopralluogo e in quanto tempo deve rispondere il Comune?

**RISPOSTA ATTESA (schema):**
L'agente illustra la procedura ex art. 24 DPR 380/2001 (come modificato dal
D.Lgs. 222/2016): la SCIA di agibilità sostituisce il certificato nella maggior
parte dei casi. Il Comune effettua il controllo entro 30 giorni (prorogabili a
60). Indica la documentazione necessaria: certificato di collaudo statico,
dichiarazione conformità impianti (D.M. 37/2008), attestato APE, frazionamento
catastale aggiornato.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il certificato di agibilità per la nuova costruzione residenziale
> bifamiliare in Via Rossini 7, Pietrasanta, fg. 8 mapp. 901 sub. 1 e 2.
> Proprietari: coniugi Alberto e Sara Conti, CF CNTLRT70A01E715X e
> CNTSRA73B42E715Y. Costruita su PDC n. 5/2023. Sopralluogo eseguito il
> 20/03/2026 dal geom. Mario Poli. Tutta la documentazione tecnica è
> presente. Certificato n. 12/2026 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, dati catastali e proprietari, richiamo al PDC
originario, elenco documenti verificati (collaudo statico, conformità impianti,
APE, accatastamento), verifica sopralluogo positivo, attestazione sussistenza
condizioni di sicurezza, igiene, salubrità e risparmio energetico, rilascio
del certificato con eventuali condizioni.
Schema: [Cert. Agibilità n. 12/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> L'APE riporta classe energetica A2. Inseriscila esplicitamente nel
> certificato e indica il tecnico certificatore: ing. Fabio Lucchi,
> prot. APE 2026-LU-00234.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna inserendo: "Visto l'Attestato di Prestazione Energetica
(APE) prot. 2026-LU-00234, redatto dall'ing. Fabio Lucchi, che attesta la
classe energetica A2 dell'immobile, ai sensi del D.Lgs. 192/2005 e s.m.i."
Aggiunge la classe energetica nel dispositivo. Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Certificato Agibilità n. 12/2026 · 25/03/2026
Prodotto da: COMUNE-UFFICIO-TECNICO v.2.0
Revisionato da: COMUNE-REVISORE-UFFICIO-TECNICO v.1.01
---
[Output del revisore: verifica art. 24 DPR 380/2001 e D.Lgs. 222/2016;
controllo completezza documentazione (collaudo, impianti D.M. 37/2008, APE,
accatastamento); verifica dichiarazione tecnico asseverante; nota su
deposito telematico al SUAP; controllo indicazione termini per ricorso;
nota su validità APE D.Lgs. 192/2005.]
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

- Verificare che la bozza elenca tutti i documenti verificati e include APE
  con classe energetica esplicita.
- Verificare che il revisore controlli la conformità all'art. 24 DPR 380/2001
  nella versione post D.Lgs. 222/2016.
