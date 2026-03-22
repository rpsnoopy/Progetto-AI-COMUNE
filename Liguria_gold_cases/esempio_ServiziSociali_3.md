# GOLD CASE — Area 2 · Servizi Sociali · Caso 3

## Atto: Determinazione — Approvazione Piano Assistenziale Individualizzato (PAI)

**Agente:** COMUNE-SERVIZI-SOCIALI v.2.0
**Revisore:** COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Cos'è il Piano Assistenziale Individualizzato (PAI) e chi lo redige?
> Deve essere approvato con determinazione?

**RISPOSTA ATTESA (schema):**
L'agente spiega che il PAI è lo strumento di programmazione degli interventi
per persone con bisogni complessi (anziani non autosufficienti, disabili).
È redatto dall'équipe multidisciplinare (assistente sociale, medico, operatori).
Richiama L. 328/2000, DPCM 12/01/2017 per i LEA, e la prassi amministrativa
di approvarlo con determinazione del Responsabile del Servizio.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di approvazione del PAI per la sig.ra Teresa
> Fontana, nata il 03/09/1938, CF FNTTRС38P43A261W, residente in Via
> Oberdan 22, Ameglia. Diagnosi: demenza senile moderata, parziale
> non autosufficienza. PAI predisposto dall'équipe UVM il 19/03/2026.
> Interventi previsti: SAD 10 ore/settimana, trasporto al centro diurno
> 3 giorni/settimana, telesoccorso. ISEE € 9.100,00. Det. n. 90/2026
> del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con diagnosi UVM e ISEE,
richiamo DPCM 12/01/2017 e L. 328/2000, determina di approvare il PAI
allegato, di autorizzare gli interventi indicati (SAD, trasporto, telesoccorso),
di stabilire la revisione del PAI entro 6 mesi, di comunicare alla sig.ra
Fontana e ai soggetti erogatori.
Schema: [Det. n. 90/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> La sig.ra Fontana non è in grado di intendere e volere: il tutore legale
> è il figlio sig. Marco Fontana. Inserisci questa informazione nelle premesse
> e adegua la comunicazione.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna le premesse specificando che la sig.ra Fontana è soggetta
a tutela legale affidata al sig. Marco Fontana (nominato con decreto del
Tribunale della Spezia del [data]). Adegua la comunicazione: "da notificarsi
al tutore legale sig. Marco Fontana, in luogo dell'interessata."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 90/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-SOCIALI v.2.0
Revisionato da: COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01
---
[Output del revisore: verifica conformità DPCM 12/01/2017 LEA;
controllo che il PAI contenga obiettivi, interventi, operatori,
durata e revisione; verifica tutela legale e rapporto con Tribunale;
nota su consenso informato del tutore ex art. 408 c.c.;
controllo privacy minima necessaria GDPR.]
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

- Verificare che la bozza gestisca correttamente la presenza del tutore legale.
- Verificare che il revisore segnali le implicazioni giuridiche della tutela
  (art. 408 c.c.) e la necessità del consenso informato.
