# GOLD CASE — Area 3 · Ufficio Tecnico · Caso 2

## Atto: Permesso di Costruire — Ampliamento abitazione unifamiliare

**Agente:** COMUNE-UFFICIO-TECNICO v.2.0
**Revisore:** COMUNE-REVISORE-UFFICIO-TECNICO v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Per l'ampliamento di un'abitazione unifamiliare di 30 mq serve il permesso
> di costruire o basta la SCIA? E se il fabbricato è in zona B di PRG?

**RISPOSTA ATTESA (schema):**
L'agente illustra che un ampliamento comportante aumento di volumetria richiede
il permesso di costruire (DPR 380/2001, art. 10). La SCIA alternativa al PDC
è possibile solo per interventi di ristrutturazione senza aumento di volumetria.
In zona B di PRG occorre verificare gli indici urbanistici (IF, RC, altezza max).
Suggerisce di consultare il PRG vigente e le NTA per la zona B specifica.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il permesso di costruire per l'ampliamento di 28 mq al piano terra
> dell'abitazione di proprietà di Giulia Ferri, CF FRRGLI75E68A261B,
> in Via Aurelia 45, Ameglia, fg. 12 mapp. 334. Progettista: arch.
> Luca Belli, iscritto Ordine della Spezia n. 1502. Conforme al PRG zona B,
> IF rispettato. Contributo di costruzione: € 3.200,00 già versato prot. 4521.
> PDC n. 18/2026 del 25/03/2026. Responsabile SUAP: geom. Sara Neri.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, dati catastali, dati progettista, verifica
conformità urbanistica (PRG zona B, NTA, IF, RC, altezza), verifica documentazione
completa, verifica versamento contributo di costruzione, rilascia il permesso con
condizioni (inizio lavori entro 12 mesi, fine lavori entro 3 anni, comunicazione
inizio lavori), indicazione dell'ufficio per sopralluogo finale.
Schema: [PDC n. 18/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> L'immobile è soggetto a vincolo paesaggistico (D.Lgs. 42/2004). Il nulla
> osta paesaggistico è stato rilasciato dalla Soprintendenza con prot. 12345
> del 10/03/2026. Aggiungilo nelle premesse.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna le premesse: "Visto il nulla osta paesaggistico rilasciato
dalla Soprintendenza Archeologia, Belle Arti e Paesaggio per le Province di
La Spezia con prot. n. 12345 del 10/03/2026, ai sensi dell'art. 146
D.Lgs. 42/2004 (Codice dei Beni Culturali e del Paesaggio)."
Aggiunge nel dispositivo la condizione di rispetto delle prescrizioni della
Soprintendenza. Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — PDC n. 18/2026 · 25/03/2026
Prodotto da: COMUNE-UFFICIO-TECNICO v.2.0
Revisionato da: COMUNE-REVISORE-UFFICIO-TECNICO v.1.01
---
[Output del revisore: verifica conformità DPR 380/2001 artt. 10, 20;
controllo termini decadenza (inizio 12 mesi, fine 3 anni art. 15);
verifica nulla osta paesaggistico art. 146 D.Lgs. 42/2004;
controllo contributo di costruzione (art. 16 DPR 380/2001);
nota su obbligo CIL all'inizio lavori; verifica indicazione
dell'autorità per ricorso (TAR Liguria).]
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

- Verificare che la bozza contenga: termini di inizio e fine lavori, dati
  catastali, nulla osta paesaggistico, contributo di costruzione.
- Verificare che il revisore richiami l'art. 146 D.Lgs. 42/2004 e i termini
  di decadenza del permesso ex art. 15 DPR 380/2001.
