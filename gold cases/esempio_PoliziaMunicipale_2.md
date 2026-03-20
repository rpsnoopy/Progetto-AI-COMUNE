# GOLD CASE — Area 7 · Polizia Municipale · Caso 2

## Atto: Ordinanza — Rimozione e deposito veicolo abbandonato

**Agente:** COMUNE-POLIZIA-MUNICIPALE v.2.0
**Revisore:** COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Come si gestisce un veicolo abbandonato su suolo pubblico?
> Qual è la procedura e chi paga le spese di rimozione?

**RISPOSTA ATTESA (schema):**
L'agente illustra l'art. 159 C.d.S.: la Polizia Municipale accerta
l'abbandono (assenza targhe o targa non abbinata, stato di degrado), appone
un avviso di 10 giorni per il ritiro del proprietario. Decorso il termine
inutilmente, il Sindaco emette ordinanza di rimozione e deposito. Il veicolo
è custodito per 60 giorni; trascorsi i quali se non ritirato è confiscato e
demolito. Le spese di rimozione e custodia gravano sul proprietario.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera l'ordinanza di rimozione per un veicolo abbandonato: Renault Clio
> targa YY999ZZ, priva di assicurazione e con pneumatici sgonfi, in stato
> di abbandono accertato dall'Ag. Sc. Paolo Neri (matr. 032) il 10/03/2026
> in Via dei Pini 4, Pietrasanta. Avviso affisso il 10/03/2026, non ritirato
> dal proprietario. Proprietario risultante dal PRA: sig.ra Giovanna Landi,
> Via Cavour 18, Livorno (irreperibile). Ordinanza n. 45 del 25/03/2026.
> Deposito: rimessa comunale Via Industriale 2, Pietrasanta.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione con poteri del Sindaco, richiamo art. 159 e 214
C.d.S., verbale di accertamento abbandono, avviso affisso e decorso del termine,
infruttuosa notifica al proprietario, ordina la rimozione del veicolo e il
deposito presso la rimessa comunale, pone le spese a carico della sig.ra Landi,
indica i 60 giorni per il ritiro con pagamento spese, avverte delle conseguenze
di mancato ritiro (confisca e demolizione ex art. 159 co. 7).
Schema: [Ordinanza n. 45/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Il veicolo ha anche la revisione scaduta dal 2023 e non è assicurato.
> Aggiungi le relative sanzioni amministrative accessorie nelle premesse.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna le premesse: "Accertato altresì che il veicolo risulta privo
di copertura assicurativa obbligatoria (art. 193 C.d.S., sanzione € 866,00
ridotta a € 433,00 se pagata entro 5 giorni) e con revisione scaduta dal 2023
(art. 80 co. 14 C.d.S., sanzione € 173,00); i relativi verbali di accertamento
sono stati redatti separatamente."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Ordinanza n. 45/2026 · 25/03/2026
Prodotto da: COMUNE-POLIZIA-MUNICIPALE v.2.0
Revisionato da: COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0
---
[Output del revisore: verifica art. 159 C.d.S. (procedura abbandono veicoli);
controllo rispetto termine 10 giorni avviso prima dell'ordinanza;
verifica indicazione dei 60 giorni per ritiro e avvertimento demolizione;
nota su notifica dell'ordinanza al proprietario (obbligatoria anche se
irreperibile: notifica per pubblici proclami o deposito atti);
controllo sanzioni accessorie mancata assicurazione art. 193 C.d.S.;
verifica che le spese siano liquidate e il titolo esecutivo sia indicato.]
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

- Verificare che la bozza rispetti la sequenza procedurale: accertamento →
  avviso 10 gg → ordinanza → 60 gg deposito → confisca.
- Verificare che il revisore segnali il problema della notifica al proprietario
  irreperibile (notifica per pubblici proclami).
