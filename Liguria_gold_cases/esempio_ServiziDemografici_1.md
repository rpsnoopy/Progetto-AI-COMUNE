# GOLD CASE — Area 5 · Servizi Demografici · Caso 1

## Atto: Iscrizione anagrafica per trasferimento di residenza

**Agente:** COMUNE-SERVIZI-DEMOGRAFICI v.2.0
**Revisore:** COMUNE-REVISORE-DEMOGRAFICI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Un cittadino straniero extracomunitario con permesso di soggiorno può
> iscriversi all'anagrafe? Quali documenti deve presentare?

**RISPOSTA ATTESA (schema):**
L'agente spiega che il cittadino extracomunitario con permesso di soggiorno
valido ha diritto all'iscrizione anagrafica (D.Lgs. 30/2007 non si applica;
rileva il DPR 223/1989 e la L. 1228/1954). Documenti richiesti: permesso di
soggiorno valido, documento di identità, codice fiscale, dichiarazione di
dimora abituale, documentazione sull'alloggio (contratto, dichiarazione del
proprietario). Indica i termini: il Comune verifica entro 45 giorni (accertamento
della dimora abituale).

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il provvedimento di iscrizione anagrafica per il sig. Ahmed Hassan,
> nato il 15/07/1985 in Egitto, CF HSSMHD85L15Z336A, cittadinanza egiziana,
> permesso di soggiorno tipo "lavoro subordinato" n. EJ1234567, scadenza
> 14/03/2028. Trasferisce la residenza da Genova (Via San Lorenzo 15) a Ameglia,
> Via Litoranea 22 int. 3. Dichiarazione presentata il 10/03/2026. Verifiche positive
> al sopralluogo del 20/03/2026. Provvedimento n. 156 del 25/03/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, dati anagrafici completi, estremi permesso di
soggiorno, dichiarazione di dimora abituale, verifica positiva sopralluogo,
richiamo DPR 223/1989 art. 4, iscrizione nel registro della popolazione residente,
comunicazione al Comune di provenienza (Milano), annotazione nell'AIRE se
precedentemente iscritta. Schema: [Provv. n. 156/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Con il sig. Hassan si trasferisce anche la moglie sig.ra Fatima Hassan,
> nata il 22/03/1988 in Egitto, CF HSSFMT88C62Z336B, permesso di soggiorno
> tipo "famiglia" n. EJ7654321, scadenza 14/03/2028. Aggiungila al
> provvedimento.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna il provvedimento includendo la sig.ra Fatima Hassan come
componente del nucleo familiare: dati anagrafici, permesso di soggiorno per
motivi familiari, stessa dichiarazione di dimora abituale. Aggiorna le
comunicazioni al Comune di provenienza per entrambi i componenti.
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Provvedimento n. 156/2026 · 25/03/2026
Prodotto da: COMUNE-SERVIZI-DEMOGRAFICI v.2.0
Revisionato da: COMUNE-REVISORE-DEMOGRAFICI v.1.01
---
[Output del revisore: verifica DPR 223/1989 art. 4 (iscrizione per
cambio di residenza); controllo validità permesso di soggiorno e
tipologia (lavoro subordinato, famiglia); nota su comunicazione ANPR;
verifica termini accertamento dimora abituale (45 giorni);
nota su obbligo comunicazione alle autorità di pubblica sicurezza
(Questura) ex Testo Unico Immigrazione D.Lgs. 286/1998.]
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

- Verificare che la bozza contenga: dati permesso di soggiorno, comunicazione
  al Comune di provenienza, riferimento DPR 223/1989.
- Verificare che il revisore segnali la comunicazione alla Questura ex D.Lgs.
  286/1998 e l'aggiornamento ANPR.
