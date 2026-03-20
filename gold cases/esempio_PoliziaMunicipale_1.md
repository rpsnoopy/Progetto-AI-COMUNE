# GOLD CASE — Area 7 · Polizia Municipale · Caso 1

## Atto: Verbale di accertamento — Violazione art. 142 C.d.S. (eccesso di velocità)

**Agente:** COMUNE-POLIZIA-MUNICIPALE v.2.0
**Revisore:** COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> Se il verbale per eccesso di velocità viene notificato oltre i 90 giorni
> dall'accertamento, è nullo? Ci sono eccezioni?

**RISPOSTA ATTESA (schema):**
L'agente illustra l'art. 201 C.d.S.: il verbale deve essere notificato entro
90 giorni dall'accertamento (per residenti in Italia). Il termine è perentorio
e la sua violazione comporta la nullità della contestazione. Eccezioni: per
i residenti all'estero il termine è 360 giorni. Indica che il termine decorre
dal momento dell'accertamento, non dalla stampa del verbale. Richiama
Cass. civ. SS.UU. sull'invalidità del verbale tardivo.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera il verbale per violazione dell'art. 142 co. 8 C.d.S. (velocità
> 68 km/h in zona 50) accertata il 20/03/2026 alle ore 10:45 in Via
> Aurelia km 3+200, Pietrasanta, direzione nord. Veicolo: Fiat Punto targa
> AB123CD, proprietario sig. Luca Esposito, CF SPSLCU80H12E715F, Via Roma 5,
> Pietrasanta. Rilevazione con autovelox omologato, targa letta da sistema
> automatico. Agente accertatore: Ag. Sc. Mario Bianchi, matr. 045.
> Verbale n. 2026/00456.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione con intestazione del Corpo di PM, estremi verbale,
dati veicolo e proprietario, luogo e ora dell'infrazione, velocità accertata e
limite, richiamo art. 142 co. 8 C.d.S., sanzione: € 173,00 (pagamento in
misura ridotta entro 5 giorni: € 86,50; entro 60 giorni: € 173,00), decurtazione
punti patente (3), modalità di pagamento, diritto di ricorso al Prefetto o al
GdP entro 60 giorni. Schema: [Verbale n. 2026/00456 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Il proprietario non era il conducente al momento dell'infrazione: occorre
> aggiungere la comunicazione dell'obbligo di indicare il conducente
> ai sensi dell'art. 126-bis C.d.S. Aggiungila in fondo al verbale.

**RISPOSTA ATTESA (schema):**
L'agente aggiunge: "Si avverte il proprietario del veicolo che, ai sensi
dell'art. 126-bis C.d.S., ha l'obbligo di comunicare entro 60 giorni dalla
notifica del presente verbale le generalità del conducente al momento
dell'infrazione. In caso di mancata comunicazione si applica la sanzione
di cui all'art. 126-bis co. 2 C.d.S. con sospensione della patente da 1 a 3
mesi." Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — Verbale n. 2026/00456 · 20/03/2026
Prodotto da: COMUNE-POLIZIA-MUNICIPALE v.2.0
Revisionato da: COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0
---
[Output del revisore: verifica art. 142 co. 8 C.d.S. (velocità 68 in zona 50:
superamento > 10 km/h fino a 40 km/h → sanzione corretta);
controllo art. 201 C.d.S. termini notifica (90 giorni da 20/03/2026);
verifica decurtazione punti (3 punti art. 126-bis);
controllo art. 126-bis obbligo comunicazione conducente;
nota su omologazione autovelox: certificato in atti?
verifica indicazione organo ricorso (Prefetto o GdP entro 60 giorni).]
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

- Verificare che la bozza contenga: importo sanzione ridotta (5 gg), importo
  pieno (60 gg), decurtazione punti, termini e organi per il ricorso.
- Verificare che il revisore segnali la necessità di verifica dell'omologazione
  dell'autovelox come elemento essenziale di validità del verbale.
