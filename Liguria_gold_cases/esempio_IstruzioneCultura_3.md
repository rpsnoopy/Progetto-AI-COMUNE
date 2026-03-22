# GOLD CASE — Area 8 · Istruzione - Cultura · Caso 3

## Atto: Convenzione — Istituzione scolastica per progetto di educazione ambientale

**Agente:** COMUNE-ISTRUZIONE-CULTURA v.2.0
**Revisore:** COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Il Comune può stipulare una convenzione con una scuola statale?
> La scuola ha capacità di stipulare contratti o deve agire tramite il MIUR?

**RISPOSTA ATTESA (schema):**
L'agente spiega che le istituzioni scolastiche statali hanno personalità giuridica
e autonomia negoziale (D.Lgs. 165/2001, DPR 275/1999 art. 1). Il Dirigente
Scolastico rappresenta l'istituto ed è autorizzato a stipulare convenzioni con
gli enti locali, in particolare per attività complementari al POF/PTOF.
Non serve autorizzazione del MIUR per convenzioni con Comuni. Il Comune delibera
o determina, la scuola approva con delibera del Consiglio di Istituto.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la convenzione tra il Comune di Ameglia e l'I.C. "G. Pascoli"
> (CF 80012345678, Dirigente Scolastico prof.ssa Carla Beni) per il progetto
> di educazione ambientale "Mare Pulito" rivolto alle classi III e IV della
> scuola primaria (n. 120 alunni), a.s. 2025/2026. Il Comune mette a
> disposizione: personale esperto (3 incontri da 2 ore ciascuno), materiali
> didattici (budget € 800,00), trasporto per un'uscita al mare.
> La scuola coordina le attività e rendiconta. Durata: aprile-maggio 2026.
> Det. di approvazione n. 72 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera la convenzione con: premesse (autonomia scolastica DPR 275/1999,
delibera Consiglio Istituto), oggetto (progetto "Mare Pulito"), obbligazioni
del Comune (personale esperto, materiali € 800,00, trasporto), obbligazioni
della scuola (coordinamento, rendiconto entro 30/06/2026), durata (aprile-maggio
2026), responsabili per le parti, clausola di riservatezza dati minori (GDPR),
foro competente, firma delle parti.
Schema: [Convenzione "Mare Pulito" — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Aggiungi una clausola che prevede la possibilità di estendere il progetto
> all'a.s. 2026/2027 con semplice scambio di lettere tra le parti, senza
> necessità di nuova convenzione, se le risorse sono disponibili.

**RISPOSTA ATTESA (schema):**
L'agente aggiunge all'articolo sulla durata: "Art. X — Proroga: Le parti
potranno concordare la prosecuzione del progetto per l'anno scolastico
2026/2027 mediante semplice scambio di comunicazioni scritte (anche a mezzo
PEC), senza necessità di stipulare una nuova convenzione, a condizione che:
a) le risorse finanziarie necessarie siano regolarmente stanziate nel bilancio
comunale; b) entrambe le parti manifestino formalmente il proprio consenso
entro il 28/02/2027."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Convenzione "Mare Pulito" · 25/03/2026
Prodotto da: COMUNE-ISTRUZIONE-CULTURA v.2.0
Revisionato da: COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01
---
[Output del revisore: verifica DPR 275/1999 art. 1 (autonomia negoziale
istituti scolastici); controllo D.Lgs. 165/2001 art. 15 (accordi tra
pubbliche amministrazioni); verifica clausola GDPR per dati minori
(titolarità e responsabilità del trattamento, consenso genitori);
nota su copertura finanziaria (€ 800,00 materiali + trasporto: impegno
di spesa preventivo necessario); controllo che il Consiglio di Istituto
abbia deliberato l'approvazione della convenzione;
verifica foro competente (TAR Liguria per eventuali controversie).]
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

- Verificare che la convenzione contenga una clausola GDPR esplicita per
  il trattamento dei dati degli alunni minori.
- Verificare che il revisore segnali la necessità di delibera preventiva
  del Consiglio di Istituto e dell'impegno di spesa comunale.
