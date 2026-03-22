# GOLD CASE — Area 6 · Personale - Risorse Umane · Caso 1

## Atto: Determinazione — Autorizzazione lavoro straordinario

**Agente:** COMUNE-PERSONALE-RISORSE-UMANE v.2.0
**Revisore:** COMUNE-REVISORE-PERSONALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Quali sono i limiti annuali di ore di straordinario per il personale
> comunale? Serve sempre un'autorizzazione preventiva?

**RISPOSTA ATTESA (schema):**
L'agente illustra i limiti del CCNL Funzioni Locali 2019-2021: max 180 ore
annue pro-capite di lavoro straordinario (elevabili a 240 con accordo decentrato).
L'autorizzazione preventiva da parte del dirigente è obbligatoria. Le ore devono
essere recuperate o retribuite con le tariffe previste dal CCNL (maggiorazione
15% feriale, 30% festivo, 50% notturno). Richiama D.Lgs. 165/2001 e CCNL.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di autorizzazione al lavoro straordinario per il
> personale del Servizio Demografico in occasione delle elezioni comunali del
> 15-16 aprile 2026. N. 8 dipendenti, max 12 ore ciascuno nei giorni 13-16
> aprile 2026. Costo stimato: € 3.200,00 oneri inclusi. Cap. 1010/2026 —
> Straordinari elezioni, disponibilità € 8.000,00. Det. n. 201 del 25/03/2026.
> Dirigente: dott. Filippo Serra.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con motivazione (elezioni
comunali), richiamo CCNL Funzioni Locali e D.Lgs. 165/2001, elenco dipendenti
autorizzati (o rinvio ad allegato A), monte ore max pro-capite 12 ore, costo
stimato, copertura finanziaria, autorizza il Dirigente a disporre le ore
straordinarie nei giorni indicati.
Schema: [Det. n. 201/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Due dei dipendenti sono part-time al 50%. Per loro il tetto massimo di
> straordinario è proporzionalmente ridotto. Aggiungi una nota a riguardo.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna con una nota: "Per i dipendenti in regime di part-time al 50%,
il limite di ore di lavoro straordinario è proporzionalmente ridotto in conformità
all'art. [X] del CCNL Funzioni Locali e alle disposizioni ministeriali in materia;
le ore autorizzate per detti dipendenti non potranno comunque superare le 6 ore
nel periodo di riferimento." Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 201/2026 · 25/03/2026
Prodotto da: COMUNE-PERSONALE-RISORSE-UMANE v.2.0
Revisionato da: COMUNE-REVISORE-PERSONALE v.1.01
---
[Output del revisore: verifica CCNL Funzioni Locali 2019-2021 artt. sullo
straordinario; controllo limiti pro-capite (180/240 ore annue);
verifica copertura finanziaria cap. 1010/2026; nota su obbligo
comunicazione ai dipendenti interessati; controllo proporzionalità
per part-time; verifica che non siano superate le 48 ore settimanali
ex D.Lgs. 66/2003.]
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

- Verificare che la bozza contenga copertura finanziaria, riferimento CCNL
  e D.Lgs. 165/2001, elenco o rinvio ad allegato per i nominativi.
- Verificare che il revisore richiami il limite delle 48 ore settimanali
  ex D.Lgs. 66/2003 (recepimento direttiva europea orario di lavoro).
