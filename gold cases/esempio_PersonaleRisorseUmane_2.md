# GOLD CASE — Area 6 · Personale - Risorse Umane · Caso 2

## Atto: Ordine di Servizio — Assegnazione temporanea di funzioni superiori

**Agente:** COMUNE-PERSONALE-RISORSE-UMANE v.2.0
**Revisore:** COMUNE-REVISORE-PERSONALE v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Un dipendente può essere assegnato temporaneamente a svolgere funzioni
> di categoria superiore? Per quanto tempo e con quale retribuzione?

**RISPOSTA ATTESA (schema):**
L'agente illustra la reggenza e la sostituzione ex CCNL Funzioni Locali:
un dipendente può essere assegnato a mansioni superiori per necessità urgente
e imprevedibile (art. 52 D.Lgs. 165/2001 e CCNL). Ha diritto al trattamento
economico della categoria superiore per il periodo di sostituzione.
Durata massima: fissata dal CCNL (di norma non oltre 6 mesi rinnovabili).
La reggenza non comporta promozione automatica. Indica il limite delle 6 settimane
per l'art. 52 D.Lgs. 165/2001.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera l'ordine di servizio per assegnare al sig. Roberto Conti, cat. C3,
> Ufficio Anagrafe, le funzioni di Responsabile dell'Ufficio Anagrafe in
> sostituzione della dott.ssa Sara Neri (cat. D3), assente per maternità
> dal 01/04/2026 al 30/09/2026 (6 mesi). Trattamento economico: quota
> differenziale cat. D3. Ordine di servizio n. 12 del 25/03/2026.
> Firma: dott. Filippo Serra, Dirigente Area Amministrativa.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione con firma del Dirigente, oggetto, premesse con
assenza per maternità della dott.ssa Neri (L. 151/2001), richiamo art. 52
D.Lgs. 165/2001 e CCNL Funzioni Locali, assegna al sig. Conti le funzioni
superiori dal 01/04/2026 al 30/09/2026, indica il trattamento economico
differenziale, invita il sig. Conti ad assumere le funzioni con decorrenza
01/04/2026.
Schema: [O.d.S. n. 12/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Aggiungi che il sig. Conti mantiene anche le sue funzioni ordinarie di cat. C3
> per la parte non incompatibile, e che dovrà relazionare mensilmente al
> Dirigente sulle attività svolte.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna: "Il sig. Roberto Conti, nell'esercizio delle funzioni
superiori assegnate, mantiene altresì le proprie mansioni ordinarie di categoria
C3 per la parte non incompatibile con le nuove attribuzioni. È tenuto a
relazionare mensilmente al Dirigente dell'Area Amministrativa sull'andamento
delle attività dell'Ufficio Anagrafe." Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — O.d.S. n. 12/2026 · 25/03/2026
Prodotto da: COMUNE-PERSONALE-RISORSE-UMANE v.2.0
Revisionato da: COMUNE-REVISORE-PERSONALE v.1.01
---
[Output del revisore: verifica art. 52 D.Lgs. 165/2001 (mansioni superiori);
controllo CCNL Funzioni Locali su sostituzione e differenziale retributivo;
nota su obbligo comunicazione al dipendente e all'ufficio stipendi;
verifica compatibilità durata con limiti CCNL (6 mesi rinnovabili);
controllo che non si crei aspettativa di progressione automatica;
nota su assenza per maternità: tutele L. 151/2001 per la titolare.]
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

- Verificare che la bozza indichi esplicitamente che la reggenza non comporta
  diritto alla promozione (art. 52 D.Lgs. 165/2001).
- Verificare che il revisore richiami la necessità di comunicazione all'ufficio
  stipendi per il calcolo del differenziale retributivo.
