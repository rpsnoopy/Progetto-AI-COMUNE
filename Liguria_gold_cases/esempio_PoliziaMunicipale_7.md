# GOLD CASE — Area 7 · Polizia Municipale · Caso 7

## Atto: Ordinanza Sindacale — Divieto Temporaneo di Balneazione

**Agente:** COMUNE-POLIZIA-MUNICIPALE v.2.0
**Revisore:** COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa
**INPUT UTENTE:**
> Abbiamo ricevuto un'analisi dalle acque di balneazione da ARPAL per la zona di Fiumaretta. Il report mostra superamento dei parametri di E. coli e enterococchi. Come generiamo un'ordinanza di divieto balneazione? Quale è la procedura esatta e gli enti da avvisare?

**RISPOSTA ATTESA (schema):**
L'agente deve riconoscere la competenza sindacale di emissione ordinanze per divieti di
balneazione in caso di acque non conformi, richiedere il documento ARPAL originale, verificare
l'estensione territoriale della zona interessata (foce del Magra fino a confine Bocca di Magra),
indicare gli obblighi normativi (D.Lgs. 116/2008, DPR 470/1982, D.M. Salute 30/03/2010),
comunicare la necessità di avviso immediato a Capitaneria di Porto La Spezia, ASL 5 della
Spezia, Regione Liguria, e della segnaletica sulla costa secondo standard ministeriali.

---

### TURNO 2 — Richiesta generazione atto
**INPUT UTENTE:**
> Procediamo. Ecco i dati:
> - Zona di balneazione: Fiumaretta, litorale dalla foce del Magra (lat. 44.0934, long. 10.2548) al confine con Bocca di Magra (lat. 44.0904, long. 10.2512)
> - Lunghezza zona interdetta: circa 650 metri di costa
> - Profondità campionamento: 1 metro (zona balneabile standard)
> - Data campionamento ARPAL: 25 marzo 2026, prot. n. 1823/2026
> - Risultati:
>   * E. coli: 1.200 UFC/100ml (limite legge: 500 UFC/100ml) — SUPERATO
>   * Enterococchi: 840 UFC/100ml (limite legge: 400 UFC/100ml) — SUPERATO
>   * Parametri aggiuntivi: Coliformi totali positivi, presenza indicatori biologici
> - Ordinanza numero: 9/2026
> - Data ordinanza: 26 marzo 2026
> - Responsabile: Vice-Sindaco Emanuele Cadeddu (Polizia Urbana)
> - Motivazione probabile: evento meteorologico (pioggia 40mm 24/03) ha causato dilavamento terreno e immissione in mare di scarichi non conformi da rete mista

**RISPOSTA ATTESA (schema):**
L'agente genera la bozza dell'ordinanza sindacale con:
- Intestazione: Comune di Ameglia (SP), Sindaco Andrea De Ranieri
- Numero e data ordinanza
- Considerando: superamento parametri ARPAL secondo D.Lgs. 116/2008, obbligo protezione
  salute pubblica, competenza ordinanza sindacale
- Dispositivo: DIVIETO ASSOLUTO BALNEAZIONE nel tratto descritto dalle coordinate geografiche
  fornite, divieto accesso arenile, obbligo affissione cartelli di divieto
- Validità: fino a nuovo campionamento ARPAL conforme oppure revoca espressa
- Segnaletica: cartelli standard con pittogramma "Vietata la balneazione" in italiano e inglese,
  posizionamento ogni 100 m circa
- Obbligo comunicazione a: ARPAL (comunicazione esito ordinanza), Capitaneria di Porto La
  Spezia, ASL 5 della Spezia (Servizio Igiene Ambiente), Regione Liguria (Dipartimento Tutela
  Ambiente), Provincia della Spezia, strutture ricettive costa (alberghi, camping), associazioni
  bagnanti
- Data decorrenza: immediata

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica
**INPUT UTENTE:**
> Aggiungi una clausola che specifica: rivalutazione della qualità delle acque con nuovo
> campionamento ARPAL entro 5 giorni dalla data ordinanza. Se i parametri sono conformi,
> l'ordinanza decade automaticamente. Se non conformi, ordinanza rinnovata per ulteriori 7 giorni.
> Inoltre, aggiungi un comunicato stampa da rilasciare subito agli organi di informazione
> locale (La Spezia Media, Telesestante, giornali provincia).

**RISPOSTA ATTESA (schema):**
L'agente aggiorna la bozza aggiungendo:
- Paragrafo temporalità: "Il Sindaco dispone nuovo campionamento ARPAL entro 5 giorni
  dalla data della presente ordinanza (31 marzo 2026). In caso di esito conforme, ordinanza
  decade automaticamente senza ulteriore provvedimento. In caso di esito non conforme,
  ordinanza rinnovata per ulteriori 7 giorni (fino a 7 aprile 2026) con medesime modalità
  di revisione"
- Aggiunta sezione "Comunicato Stampa" con testo pronto da inviare:
  "Il Comune di Ameglia comunica che a seguito delle analisi ARPAL delle acque di balneazione
  in data 25/03/2026, sono stati riscontrati superamenti dei parametri di qualità nella zona
  di Fiumaretta. Per protezione della salute pubblica, è stato emesso divieto di balneazione
  dal [data] fino a diversa comunicazione. Cittadini e turisti sono invitati a verificare
  la segnaletica sulla costa. Nuovo campionamento entro 5 giorni. Informazioni: 0187 609270"
- Aggiunta lista contatti per distribuzione comunicato (redazioni locali)
- Testo aggiornato della bozza visualizzato

---

### TURNO 4 — Richiesta revisione normativa
**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
```
REVISIONE NORMATIVA — Ordinanza Sindacale n. 9/2026
Divieto Temporaneo di Balneazione — Fiumaretta
Prodotto da: COMUNE-POLIZIA-MUNICIPALE v.2.0
Revisionato da: COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0
---

CONTROLLI NORMATIVI EFFETTUATI:

1. FONDAMENTO GIURIDICO
   ✓ D.Lgs. 116/2008 art. 8 (Qualità acque di balneazione): ordinanza sindacale per acque
     non conformi — APPLICABILE E OBBLIGATORIA
   ✓ DPR 470/1982: standard storici ancora parzialmente in vigore per lagune/aree specifiche
     — VERIFICATO come compatibile
   ✓ D.M. Salute 30/03/2010 (Linee Guida Qualità Acque): definisce procedure campionamento
     e periodicità — CONFORME
   ✓ Art. 54 D.Lgs. 267/2000: ordinanza sindacale per motivi di sicurezza/sanità pubblica
     — FONDAMENTALE

2. PARAMETRI DI CONFORMITÀ
   ✓ E. coli 1.200 UFC/100ml vs limite 500 UFC/100ml: SUPERAMENTO RILEVANTE (240%)
   ✓ Enterococchi 840 UFC/100ml vs limite 400 UFC/100ml: SUPERAMENTO RILEVANTE (210%)
   ✓ Parametri microbiologici coerenti con evento meteorologico (pioggia 40mm 24/03)
     — CORRELAZIONE LOGICA OK
   ✓ Data campionamento e numerazione prot. ARPAL: VERIFICA DOCUMENTAZIONE ORIGINALE
     consigliata prima firma ordinanza

3. PROCEDURA E COMUNICAZIONI
   ✓ Comunicazione Capitaneria di Porto La Spezia: OBBLIGATORIA (zona marittima) entro 24h
   ✓ Comunicazione ARPAL: OBBLIGATORIA (ente che ha rilevato non-conformità)
   ✓ Comunicazione ASL 5 della Spezia: OBBLIGATORIA (competenza igiene ambiente marino)
   ✓ Comunicazione Regione Liguria: CONSIGLIATO (monitoraggio aree balneabili regionali)
   ✓ Comunicazione strutture ricettive: APPROPRIATO (Fiumaretta ha capacità turistico-ricettiva)
   ✓ Comunicato stampa: APPROPRIATO E CONSIGLIATO (trasparenza verso cittadini/turisti)
   ✓ Affissione segnaletica: OBBLIGATORIA secondo D.Lgs. 116/2008 art. 8

4. SEGNALETICA E STANDARD
   ✓ Cartelli standard: DEVE SPECIFICARE riferimento a D.M. Infrastrutture 30/11/1999
     per pittogrammi vietato accesso/balneazione
   ✓ Pittogramma internazionale "Vietata la balneazione" (rosso-bianco): CONFORME
   ✓ Lingue: italiano + inglese consigliato (turismo internazionale costa ligure)
   ✓ Spaziatura cartelli: SUGGERITO fissare circa ogni 100 m su costa
   ✓ Responsabilità affissione: AGGIUNTA necessaria (Ufficio Polizia Urbana, Vice-Sindaco
     Cadeddu)

5. TEMPISTICHE E RIESAME
   ✓ Riesame entro 5 giorni con nuovo campionamento: CONFORME a D.Lgs. 116/2008
     (frequenza monitoraggio in caso di non-conformità)
   ✓ Decadenza automatica se conforme: CORRETTO (non serve revoca espressa se conforme)
   ✓ Rinnovo per 7 giorni ulteriori se non conforme: APPROPRIATO (limita ordinanza a durata
     necessaria e sufficiente)
   ✓ Data prevista riesame: 31 marzo 2026 — OK COERENTE

6. COORDINAMENTO CON ENTI SUPERIORI
   ✓ Tavolo di coordinamento con Capitaneria (competenza demanio marittimo): SUGGERITO
     includere se necessario
   ✓ Rapporto con ASL 5 per valutazione source epidemiologica: CONSIGLIATO per atto
     multisettoriale
   ✓ Comunicazione a Prefettura della Spezia: NON OBBLIGATORIA se ordinanza ordinaria,
     ma SUGGERITO per consapevolezza amministrazione sovraordinata

7. ZONA DI BALNEAZIONE (IDENTIFICAZIONE)
   ✓ Coordinate geografiche fornite: PRECISE (44.0934, 10.2548 — 44.0904, 10.2512)
   ✓ Lunghezza costa: 650 m — COERENTE con distanza geografica
   ✓ Identificazione "foce Magra-confine Bocca di Magra": CHIARA e geomorfologicamente
     corretta
   ✓ Profondità campionamento 1m: STANDARD CONFORME a D.Lgs. 116/2008

8. ASPETTI DI RESPONSABILITÀ
   ⚠ ASPETTO CRITICO: Responsabilità civile Comune in caso di danno da acque non conformi
     Il divieto ordinanza PROTEGGE da responsabilità solo se correttamente affisso e comunicato.
     VERIFICARE affissione segnaletica entro 24h dalla firma ordinanza.
   ⚠ NOTA: Evento meteorologico (40mm pioggia 24/03) spiega il superamento, suggerisce
     possibile scarico abusivo o rete mista malfunzionante. CONSIGLIATO: coordinamento con
     Ufficio Ambiente per indagine source inquinamento (impianti fognari)

ESITO REVISIONE: ✓ APPROVAZIONE CON INTEGRAZIONI CRITICHE
```

"Per applicare le correzioni alla bozza risponda **applica le note del revisore**."

---

### TURNO 5 — Applicazione note del revisore alla bozza
**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**
La LLM rilegge la bozza originale e il report del revisore, applica tutte le correzioni:

- Aggiunta riferimento espresso a D.M. Infrastrutture 30/11/1999 per standard cartelli
- Aggiunta specifiche segnaletica: "Cartelli di divieto di balneazione conformi a standard
  ministeriali con pittogramma internazionale (rosso-bianco), recanti iscrizioni in italiano
  e inglese. Posizionamento lungo arenile ogni 100 metri circa. Responsabilità affissione:
  Ufficio Polizia Urbana (Vice-Sindaco Cadeddu). Deadline affissione: 27 marzo 2026 (entro
  24h dalla firma)"
- Aggiunta paragrafo monitoraggio: "Contestualmente alla presente ordinanza, il Sindaco
  dispone indagine coordinata con Ufficio Ambiente Comunale su possibili scarichi abusivi
  o malfunzionamento rete fognaria mista nel bacino della foce del Magra, al fine di
  identificare source principale inquinamento microbiologico"
- Aggiunta comunicazione Prefettura: "Il presente provvedimento è trasmesso a Prefettura
  della Spezia per conoscenza e coordinamento con strutture di vigilanza"
- Verifica data ordinanza coerente: 26/03/2026 ordinanza, 31/03/2026 riesame
- Mantenimento comunicato stampa con lista contatti redazioni aggiornata
- Integrazione note per ASL 5: specifica richiesta di epidemiologia se necessaria

"Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella permanente risponda **salva**."

---

### TURNO 6 — Salvataggio
**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**
Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato (PDF, DOCX, ODT).
Il file viene salvato con nomenclatura: `ORD_9_2026_DivietoBalne_Fiumaretta_26032026.pdf`
L'agente conferma:

"Ordinanza n. 9/2026 salvata in [percorso selezionato].

ALERT — Azioni immediatamente conseguenti:
⚠ CRITICO — Affissione segnaletica ENTRO 24h (27 marzo 2026, ore 18:00)
  Responsabile: Vice-Sindaco Emanuele Cadeddu (Polizia Urbana)
  Verifica positiva da registrare in allegato ordinanza

Comunicazioni da inviare ENTRO 24h:
✓ ARPAL prot. n. 1823/2026 (origine campionamento)
✓ Capitaneria di Porto La Spezia (zona marittima)
✓ ASL 5 della Spezia — Servizio Igiene Ambiente
✓ Regione Liguria — Dipartimento Tutela Ambiente
✓ Prefettura della Spezia (per conoscenza)

Comunicato stampa: PRONTO per firma Sindaco e invio redazioni (file allegato)

Reminder automatico:
→ 31 marzo 2026 ore 10:00: CAMPIONAMENTO ARPAL (Da contattare il 25/03 per prenotazione)
→ 31 marzo 2026 ore 14:00: RIESAME ESITI ARPAL (Genera proposta rinnovo o decadenza)

Ordinanza pronta per firma del Sindaco Andrea De Ranieri."

---

## NOTE DI TEST

1. **Immediatezza comunicazioni**: A differenza del Caso 6 (sentiero), il divieto di
   balneazione impone comunicazione a Capitaneria DI PORTO entro 24h (non 5 giorni).
   L'agente deve riconoscere questa urgenza differente e prioritaria. Capitaneria governa
   lo spazio marittimo.

2. **Responsabilità civile e segnaletica**: L'omissione di segnaletica entro 24h dalla
   firma ordinanza espone il Comune a danno da responsabilità civile per lesioni a bagnanti
   (anche se consapevoli del rischio). La revisione deve enfatizzare criticità, non solo
   suggerirla.

3. **Source indagine ambientale**: L'evento meteorologico (40mm 24/03) è elemento rilevante
   che suggerisce possibile scarico abusivo o rete mista malfunzionante. Il revisore deve
   sottolineare coordinamento obbligatorio con Ufficio Ambiente per indagine. Non è un
   suggerimento facoltativo, ma parte della governance integrata.

4. **Periodicità riesame D.Lgs. 116/2008**: Il Decreto 116/2008 fissa frequenza monitoraggio
   in caso di non-conformità a 5-7 giorni. L'agente deve spiegare questa periodicità normativa,
   non inventarla. Revisore deve verificare aderenza.
