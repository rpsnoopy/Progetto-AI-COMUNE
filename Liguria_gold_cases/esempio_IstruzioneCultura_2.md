# GOLD CASE — Area 8 · Istruzione - Cultura · Caso 2

## Atto: Determinazione — Contributo ad associazione culturale

**Agente:** COMUNE-ISTRUZIONE-CULTURA v.2.0
**Revisore:** COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Il Comune può erogare un contributo a un'associazione culturale senza bando?
> Quando è obbligatorio il bando pubblico e quando si può procedere
> con affidamento diretto?

**RISPOSTA ATTESA (schema):**
L'agente illustra la disciplina ex D.Lgs. 117/2017 (Codice Terzo Settore) e
L. 241/1990 art. 12: i contributi a enti del Terzo Settore iscritti al RUNTS
seguono procedure specifiche (co-progettazione, co-programmazione, convenzioni).
Per contributi a soggetti non iscritti al RUNTS si applica l'art. 12 L. 241/1990:
il regolamento comunale fissa criteri e modalità. Il bando è necessario quando
i contributi sono rivolti a più soggetti in concorrenza; per contributi nominativi
(indicati nel bilancio) si può procedere con atto diretto. Indica soglie tipiche.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la determinazione di concessione di un contributo di € 2.500,00
> all'Associazione Culturale "Pietra Viva" (CF 90087654321), iscritta al RUNTS
> sez. APS, per la realizzazione del progetto "Ameglia Racconta"
> (rassegna letteraria, maggio-luglio 2026). Il contributo è previsto nel
> bilancio 2026, cap. 3500, stanziamento € 20.000,00. Rendicontazione dovuta
> entro il 31/10/2026. Det. n. 68 del 25/03/2026. Resp.: dott.ssa Serena Ferti.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione, oggetto, premesse con domanda dell'associazione,
iscrizione RUNTS, valutazione del progetto, richiamo D.Lgs. 117/2017 e
regolamento comunale, previsione bilancio, determina di concedere il contributo
di € 2.500,00, di impegnare la spesa sul cap. 3500/2026, di subordinare
l'erogazione alla presentazione del rendiconto entro 31/10/2026, di prevedere
recupero in caso di mancata rendicontazione.
Schema: [Det. n. 68/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> L'erogazione avverrà in due tranche: il 50% all'avvio del progetto
> (entro aprile 2026) e il 50% a rendicontazione approvata. Aggiorna
> il dispositivo con questo piano di erogazione.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna: "L'erogazione del contributo avverrà in due tranche:
• Prima tranche: € 1.250,00 (50%) entro il 30/04/2026, previa verifica
  dell'avvio delle attività progettuali;
• Seconda tranche: € 1.250,00 (50%) entro 30 giorni dall'approvazione
  del rendiconto finale da presentarsi entro il 31/10/2026.
In caso di mancata o parziale rendicontazione, la seconda tranche non sarà
erogata e si procederà al recupero delle somme eventualmente erogate in eccesso."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Determinazione n. 68/2026 · 25/03/2026
Prodotto da: COMUNE-ISTRUZIONE-CULTURA v.2.0
Revisionato da: COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01
---
[Output del revisore: verifica art. 12 L. 241/1990 (criteri e modalità);
controllo D.Lgs. 117/2017 per APS iscritta RUNTS (convenzione preferibile
a contributo diretto?); nota su obbligo pubblicazione contributo su Albo
Pretorio e sito trasparenza (D.Lgs. 33/2013 art. 26);
verifica clausola di rendicontazione e recupero;
controllo che il progetto non implichi attività economica prevalente
(diversamente cambierebbe la disciplina applicabile);
verifica visto di regolarità contabile.]
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

- Verificare che la bozza contenga clausola di rendicontazione con termine
  e previsione di recupero in caso di inadempimento.
- Verificare che il revisore segnali l'obbligo di pubblicazione ex D.Lgs.
  33/2013 art. 26 (trasparenza contributi ad enti privati).
