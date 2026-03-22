# GOLD CASE — Area 1 · Segreteria Generale · Caso 3

## Atto: Ordinanza Sindacale — Igiene pubblica

**Agente:** COMUNE-SEGRETERIA-GENERALE v.2.0
**Revisore:** COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Il Sindaco può emanare un'ordinanza contingibile e urgente in materia di igiene
> pubblica? Quali poteri ha e quali limiti?

**RISPOSTA ATTESA (schema):**
L'agente illustra il potere del Sindaco ex art. 50 co. 5 D.Lgs. 267/2000 per
ordinanze contingibili e urgenti in materia di igiene, sanità, sicurezza pubblica.
Indica i requisiti: presupposto urgente e contingibile, motivazione adeguata,
proporzionalità, durata limitata, comunicazione al Prefetto.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera un'ordinanza sindacale urgente per imporre la chiusura temporanea e la
> bonifica di un'area privata in Via dei Platani 12 a Ameglia, a causa della
> presenza di rifiuti speciali abbandonati che costituiscono rischio sanitario.
> Proprietario: Rossi Costruzioni Srl. Termine per la bonifica: 15 giorni dalla
> notifica. Ordinanza n. 18 del 25/03/2026. Responsabile istruttoria: geom.
> Carlo Verdi, Ufficio Ambiente.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione con poteri del Sindaco, richiamo art. 50 co. 5
D.Lgs. 267/2000 e D.Lgs. 152/2006 (Codice Ambiente), visto il sopralluogo
dell'Ufficio Ambiente, ordina la chiusura immediata dell'area e la bonifica entro
15 giorni, prevede diffida e sanzioni in caso di inadempimento, dispone la
notifica al proprietario e comunicazione al Prefetto.
Schema: [Ordinanza n. 18/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Aggiungi che in caso di inadempimento entro il termine, il Comune procederà
> d'ufficio con rivalsa delle spese sul proprietario.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il dispositivo con la clausola: "Avvertendo che, in caso di
mancata esecuzione entro il termine indicato, il Comune di Ameglia procederà
d'ufficio ai sensi dell'art. 41 D.Lgs. 152/2006, con rivalsa delle spese
sostenute nei confronti del soggetto obbligato."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Ordinanza Sindacale n. 18/2026 · 25/03/2026
Prodotto da: COMUNE-SEGRETERIA-GENERALE v.2.0
Revisionato da: COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01
---
[Output del revisore: verifica presupposti art. 50 co. 5 D.Lgs. 267/2000;
controllo riferimenti D.Lgs. 152/2006; verifica motivazione urgenza;
controllo obbligo di comunicazione al Prefetto; nota su eventuale
coinvolgimento ARPAT per sopralluogo tecnico; proporzionalità del termine.]
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

- Verificare che la bozza contenga la comunicazione al Prefetto (obbligatoria
  per ordinanze contingibili e urgenti).
- Verificare che il revisore segnali l'eventuale necessità di coinvolgere ARPAT
  o ASL per la certificazione del rischio sanitario.
