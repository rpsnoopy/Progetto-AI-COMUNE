# GOLD CASE — Area 6 · Personale - Risorse Umane · Caso 3

## Atto: Determinazione — Approvazione Piano Ferie

**Agente:** COMUNE-PERSONALE-RISORSE-UMANE v.2.0
**Revisore:** COMUNE-REVISORE-PERSONALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Il Comune è obbligato ad approvare un piano ferie formale? Entro quando
> deve comunicarlo ai dipendenti? Il dipendente può rifiutare le ferie
> assegnate d'ufficio?

**RISPOSTA ATTESA (schema):**
L'agente illustra che il CCNL Funzioni Locali prevede l'approvazione del piano
ferie entro il 30 aprile di ogni anno. Le ferie sono un diritto irrinunciabile
(art. 36 Cost., D.Lgs. 66/2003 art. 10) ma il datore di lavoro fissa il periodo
di godimento tenendo conto delle esigenze di servizio e dei desiderata del
dipendente. Il dipendente non può rifiutare le ferie assegnate per esigenze
organizzative, ma il piano deve garantire un periodo minimo di 2 settimane
consecutive. Le ferie non godute vanno monetizzate solo alla cessazione.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di approvazione del piano ferie 2026 per il
> personale dell'Area Amministrativa (15 dipendenti). Il piano è stato
> redatto dal Responsabile dott.ssa Alessia Giannarelli con richiesta di preferenze
> ai dipendenti entro il 31/03/2026. Sono garantiti: almeno 15 giorni
> consecutivi estivi (luglio-agosto), presenza minima di 6 unità in servizio
> per tutto il periodo. Il piano è allegato alla determinazione (all. A).
> Det. n. 210 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con raccolta preferenze,
richiamo CCNL Funzioni Locali e D.Lgs. 66/2003, verifica copertura del servizio
(min. 6 unità), determina di approvare il piano ferie 2026 dell'Area Amministrativa
come da allegato A, di comunicarlo a tutti i dipendenti interessati, di garantire
il minimo di 15 giorni consecutivi, di disporre che le eventuali modifiche siano
autorizzate dal Dirigente per comprovate esigenze.
Schema: [Det. n. 210/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Aggiungi che i dipendenti che rinunciano volontariamente al periodo estivo
> per esigenze di servizio straordinarie avranno priorità nella scelta del
> periodo autunnale o invernale.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna: "I dipendenti che, su base volontaria e per comprovate
esigenze di servizio straordinarie debitamente attestate dal Dirigente, rinunceranno
al periodo feriale estivo programmato, avranno diritto di priorità assoluta
nella scelta del periodo di ferie autunnale (settembre-ottobre) o invernale
(dicembre-gennaio), compatibilmente con le esigenze di servizio."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 210/2026 · 25/03/2026
Prodotto da: COMUNE-PERSONALE-RISORSE-UMANE v.2.0
Revisionato da: COMUNE-REVISORE-PERSONALE v.1.01
---
[Output del revisore: verifica art. 10 D.Lgs. 66/2003 (ferie minime
4 settimane, di cui 2 consecutive da godere nell'anno);
controllo CCNL Funzioni Locali su ferie (28 giorni lavorativi annui);
nota su divieto di monetizzazione in costanza di rapporto ex art. 5
co. 8 D.L. 95/2012 (conv. L. 135/2012);
verifica che il piano garantisca il godimento entro il 30/06 dell'anno
successivo; controllo comunicazione ai dipendenti (art. 7 Statuto Lavoratori).]
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

- Verificare che la bozza garantisca le 2 settimane consecutive (D.Lgs. 66/2003).
- Verificare che il revisore richiami il divieto di monetizzazione delle ferie
  in costanza di rapporto (D.L. 95/2012 art. 5 co. 8).
