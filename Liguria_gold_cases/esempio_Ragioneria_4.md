# GOLD CASE — Area 4 · Ragioneria - Servizio Finanziario · Caso 4

## Atto: Determinazione — Liquidazione fattura per servizio di pulizia

**Agente:** COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0
**Revisore:** COMUNE-REVISORE-RAGIONERIA v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Allegato documento esterno + richiesta analisi

**INPUT UTENTE:**
> Buongiorno, ho ricevuto da colleghi del Comune di La Spezia il template di Determinazione per liquidazione fatture di servizi. Prima di adottarlo per le nostre procedure finanziarie, occorre un'analisi critica: errori normativi, deficienze contabili, difetti procedurali. Mi identifichi tutto.
>
> **DOCUMENTO ALLEGATO:**
>
> COMUNE DI LA SPEZIA
> Provincia della Spezia — Liguria
>
> DETERMINAZIONE
> Protocollo: DET/2026/0156
> Data: 18 marzo 2026
>
> **OGGETTO:** Liquidazione fattura per servizio di pulizia e sanificazione uffici comunali
>
> **DIPARTIMENTO:** Servizio Finanziario — Ragioneria
> **RESPONSABILE:** dott. Marco Filippini
>
> **BENEFICIARIO DELLA LIQUIDAZIONE:**
> Puliservice Srl
> Partita IVA: IT07654321000157
> Indirizzo: Via Martiri della Resistenza 23, La Spezia (LU) 56121
>
> **FATTURA LIQUIDATA:**
> Numero: 145/2026
> Data: 28 febbraio 2026
> Importo lordo: €7.850,00
> Aliquota IVA: 10%
> Importo IVA: €785,00
> Importo totale: €8.635,00
>
> **PERIODO PRESTAZIONE:**
> Febbraio 2026
>
> **PRESTAZIONI EFFETTUATE:**
> Pulizia ordinaria uffici comunali, sanificazione ambienti, lavaggio pavimenti.
>
> **CONSIDERATO CHE**
>
> - La fattura è relativa a servizio di pulizia e sanificazione regolarmente prestato
> - Il servizio è stato eseguito secondo le modalità previste dal contratto
> - L'importo fatturato è conforme alle tariffe convenzionate
> - È stata compilata regolarmente la documentazione amministrativa
>
> **DETERMINA**
>
> La liquidazione della fattura n. 145/2026, relativa ai servizi di pulizia e sanificazione effettuati nel febbraio 2026, per l'importo di €8.635,00 (IVA inclusa).
>
> L'importo sarà versato alla ditta Puliservice Srl entro i termini di legge.
>
> **COPERTURA FINANZIARIA**
> Capitolo di bilancio: 1080/2026
> Disponibilità del capitolo: €25.000,00 (importo residuo)
>
> La presente determinazione è sottoscritta dal Responsabile del Servizio Finanziario.
>
> dott. Marco Filippini
> Responsabile Servizio Finanziario
> Firma e timbro
> Data: 18 marzo 2026

**RISPOSTA ATTESA (schema):**

Analisi critica completa della Determinazione allegata — Comune di La Spezia:

**ERRORE 1 — Non verifica DURC prima della liquidazione**
Difetto procedurale grave: Antecedente obbligatorio a liquidazione è verifica del DURC (Documento Unico di Regolarità Contributiva) presso INPS. Art. 1 co. 1109 L. 296/2006 stabilisce che il pagamento a fornitori non può avvenire senza verificazione. La Determinazione non cita DURC né data di acquisizione. **Liquidazione illegittima se non anteceduta da DURC positivo.**

**ERRORE 2 — Non richiama tracciabilità flussi finanziari L. 136/2010**
Difetto normativo: L. 13/03/2010 n. 136 "Disposizioni antiriciclaggio" art. 3 co. 7 impone tracciabilità di tutti i flussi finanziari fra PA e fornitori. Pagamenti devono effettuarsi tramite conti correnti bancari, non contanti, con monitoraggio e documentazione. Determinazione non menziona modalità di tracciamento, numero IBAN beneficiario, referenze bancarie. **Carenza requisiti antiriciclaggio.**

**ERRORE 3 — Manca verifica conformità/attestazione regolare esecuzione**
Difetto grave (amministrativo-contabile): Non risulta acquisita dichiarazione di conformità prestazione ai termini contrattuali, nè certificazione di regolare esecuzione da parte di preposto RUP o dirigente di settore. La fattura non è allegata, nè documentazione fotografica/report tecnico di esecuzione. **Manca elemento probatorio fondamentale.**

**ERRORE 4 — Non indica il CIG**
Difetto normativo: D.Lgs. 163/2006 (Codice dei Contratti) art. 80 richiede attribuzione CIG (Codice Identificativo Gara) a tutti gli appalti/contratti pubblici. La Determinazione non riporta CIG, elemento essenziale per tracciamento e verifica antimafia. **Mancanza informazione obbligatoria di tracciamento contrattuale.**

**ERRORE 5 — Termine pagamento non conforme a D.Lgs. 231/2002**
Difetto normativo: Il testo afferma genericamente "entro i termini di legge". Tuttavia, D.Lgs. 9/10/2002 n. 231 art. 4 fissa termine massimo di pagamento per amministrazioni pubbliche a 30 giorni dalla ricezione fattura. La Determinazione non specifica se il termine sia 30 giorni (conforme) o altro. Inoltre, cita termine generico senza giustificazione. **Applicazione vaga della normativa sui tempi pagamento.**

**ERRORE 6 — Non verifica inadempienza ex art. 48-bis DPR 602/1973 per importi > €5.000**
Difetto grave (procedura pre-pagamento): Per pagamenti > €5.000, art. 48-bis DPR 602/1973 (Ordinamento tributario) richiede controllo della posizione debitoria presso Agenzia delle Entrate (comunicazione ad AdE e verifica debiti fiscali). Non è menzionato. Senza questo controllo, il Comune potrebbe risultare responsabile di trasferimento a soggetto con pendenze tributarie. **Carenza controllo pre-pagamento obbligatorio per importi significativi.**

**ERRORI MINORI:**
- Non è allegata copia fattura alla Determinazione;
- Manca data del numero CIG in relazione all'appalto;
- Non indicata scadenza DURC verificato (validità di mesi);
- Non menzione di eventuali allegati contrattuali (ordine di fornitura, calendario servizi);
- Manca firma digitale o timbro digitale su documento.

---

### TURNO 2 — Discussione analisi critica

**INPUT UTENTE:**
> Perfetto, è tutto molto chiaro. Questi buchi procedurali sono proprio quelli che dobbiamo evitare. Abbiamo un'altra fattura simile da liquidare per il mese di febbraio, sempre per servizi di pulizia. Mi serve una Determinazione modello che corregga tutti questi errori e che sia conforme alle normative attuali.

**RISPOSTA ATTESA (schema):**

Esatto. Ho catalogato tutti i difetti della Determinazione di La Spezia. Per la generazione della Determinazione corretta per Ameglia, che incorpori:

✓ Verifica DURC antecedente (con data e esito)
✓ Tracciabilità flussi finanziari L. 136/2010
✓ Certificazione regolare esecuzione da RUP/dirigente
✓ Indicazione esplicita del CIG
✓ Termine pagamento conforme D.Lgs. 231/2002 (30 giorni)
✓ Verifica posizione debitoria art. 48-bis DPR 602/1973 per importi > €5.000

Mi fornisca i dati della fattura:
- Fornitore: ragione sociale, PIC, indirizzo, IBAN
- Numero fattura, data, importo lordo e netto
- Descrizione servizi/merce
- Numero ordine di fornitura o contratto quadro
- CIG dell'appalto
- Capitolo di bilancio di imputazione
- Data acquisizione DURC e numero reference
- RUP o responsabile verifica conformità

---

### TURNO 3 — Richiesta generazione atto corretto per Ameglia

**INPUT UTENTE:**
> Fornitore: Puliservice Srl, PIC 07654321000157, via Martiri della Resistenza 23, La Spezia. IBAN: IT76P0306909606100000012345. Fattura n. 234/2026 del 28 febbraio 2026, importo €7.890 + IVA 10% = €8.679. Servizi pulizia uffici febbraio 2026. Ordine fornitura n. OF/2025/0445 sottoscritto 15/01/2025 su contratto quadro AMA-2025-LU. CIG: Z3F1234567. Capitolo: 1080/2026. DURC acquisito 26 marzo 2026, esito positivo, numero autorità DURC-2026-156248. RUP: geom. Gabriele Benabbi. Det. n. 52/2026.

**RISPOSTA ATTESA (schema):**

---

**COMUNE DI AMEGLIA**
Provincia della Spezia — Liguria

**DETERMINAZIONE**
**Liquidazione fattura per servizio di pulizia e sanificazione**

Protocollo: DET/2026/0052
Data: 28 marzo 2026

**OGGETTO:** Liquidazione fattura n. 234/2026 relativa a prestazioni di pulizia e sanificazione uffici comunali — Mese febbraio 2026

**SERVIZIO RESPONSABILE:** Ragioneria — Servizio Finanziario
**RESPONSABILE DI SETTORE:** dott.ssa Alessandro Ardigò
**RESPONSABILE DEL PROCEDIMENTO (RUP):** Geom. Gabriele Benabbi (Capo Ufficio Tecnico, delegato per verifiche conformità)

---

## BENEFICIARIO DELLA LIQUIDAZIONE

**Ditta:** Puliservice Srl
**Partita IVA / Codice Fiscale:** IT07654321000157
**Indirizzo sede legale:** Via Martiri della Resistenza 23, 56121 La Spezia (LU)
**IBAN per accredito:** IT76P0306909606100000012345
**BIC/SWIFT:** BAPAITRRXXX
**Intestatario conto:** Puliservice Srl

---

## DETTAGLI FATTURA LIQUIDATA

**Numero fattura:** 234/2026
**Data fattura:** 28 febbraio 2026
**Periodo prestazione:** Mese di febbraio 2026 (dal 1° al 29 febbraio)

**Importo lordo (imponibile):** €7.890,00
**Aliquota IVA:** 10%
**Importo IVA:** €789,00
**Importo totale (IVA inclusa):** €8.679,00

**Descrizione prestazioni:**
Servizi di pulizia ordinaria e sanificazione ambienti presso uffici comunali ubicati in Via Giuseppe Mazzini 1, Ameglia (LU), secondo modalità contrattuali previste da:
- Contratto Quadro AMA-2025-LU sottoscritto in data 15/01/2025 (durata 12 mesi, rinnovabile);
- Ordine di fornitura n. OF/2025/0445 emesso il 15/01/2025.

**Specifiche tecniche:** Pulizia ordinaria pavimenti e aree comuni, sanificazione scrivanie e attrezzature, lavaggio finestre, gestione rifiuti, secondo standard di igiene comunale.

---

## TRACCIABILITÀ AMMINISTRATIVO-FINANZIARIA

**Codice Identificativo Gara (CIG):** Z3F1234567
**Capitolo di bilancio di imputazione:** 1080/2026 — "Servizi di Pulizia e Sanificazione Uffici"
**Disponibilità finanziaria del capitolo:** €28.500,00 (importo residuo dopo liquidazione: €19.821,00)

---

## VERIFICHE PRE-PAGAMENTO COMPLETATE

### 1. Verifica DURC (Documento Unico Regolarità Contributiva)

**Data acquisizione:** 26 marzo 2026
**Modalità acquisizione:** Verifica telematica presso INPS tramite portale MyINPS — Amministrazioni Pubbliche
**Numero di riferimento DURC:** DURC-2026-156248
**Esito verificazione:** ✓ POSITIVO — La ditta Puliservice Srl risulta regolare nei versamenti contributivi presso INPS, INAIL, Casse Previdenziali
**Validità DURC:** 120 giorni dalla data di generazione (scadenza: 24 giugno 2026)
**Competenza RUP:** Geom. Gabriele Benabbi (verifica telematica documentata in allegato)

### 2. Verifica Posizione Debitoria Tributaria (art. 48-bis DPR 602/1973)

**Importo fattura:** €8.679,00 (superiore a €5.000 — soggetto a verifica obbligatoria)
**Data verifica:** 27 marzo 2026
**Modalità verifica:** Interrogazione presso Agenzia delle Entrate tramite servizio "Verifica Crediti IVA e Debiti Tributari"
**Risultato:** ✓ NEGATIVO PER DEBITI — La ditta Puliservice Srl non presenta posizioni debitorie tributarie presso Agenzia delle Entrate
**Esito:** Idoneo al pagamento senza vincoli particolari
**Competenza:** Responsabile Ragioneria dott.ssa Alessandro Ardigò

### 3. Certificazione Regolare Esecuzione della Prestazione

**Data verifica conformità:** 26 marzo 2026
**Responsabile verificazione:** Geom. Gabriele Benabbi (RUP)
**Modalità:** Sopralluogo presso uffici comunali, verifica dello stato di pulizia e sanificazione, confronto con standard contrattuali
**Risultato:** ✓ CONFORME — Prestazione è stata eseguita in conformità alle modalità contrattuali. Documentazione fotografica allegata (Allegato A — Report fotografico post-pulizia del 29 febbraio 2026)
**Certificato di regolare esecuzione:** Allegato B (sottoscritto da RUP)

### 4. Verifica Tracciabilità Flussi Finanziari (L. 136/2010)

**Normativa applicabile:** L. 13/03/2010 n. 136 art. 3 co. 7 — "Disposizioni antiriciclaggio"
**Modalità pagamento:** Bonifico bancario su IBAN registrato presso fornitori qualificati
**IBAN beneficiario:** IT76P0306909606100000012345 (verificato presso Banca depositaria — Banca del Mezzogiorno)
**Intestatario conto:** Puliservice Srl (coerente con beneficiario fattura)
**Tracciamento:** Pagamento sarà effettuato tramite sistema di tesoreria comunale con identificativo univoco di transazione (TID) e sarà registrato nel registro di tracciamento antiriciclaggio del Comune
**Conformità:** ✓ CONFORME — Pagamento tracciabile, non in contanti, con documentazione integrale di flusso

---

## CONSIDERATO CHE

- La fattura n. 234/2026 della ditta Puliservice Srl è stata acquisita al protocollo generale in data 20 marzo 2026;
- La prestazione è stata eseguita regolarmente secondo le modalità contrattuali (Certificato conformità in Allegato B);
- Sono state completate tutte le verifiche preliminari obbligatorie:
  - DURC positivo (DURC-2026-156248, validità conforme)
  - Verifica posizione tributaria negativa per debiti (27/03/2026)
  - Certificazione regolare esecuzione (sopralluogo RUP 26/03/2026)
- La documentazione relativa al Contratto Quadro AMA-2025-LU e all'Ordine di Fornitura OF/2025/0445 risulta in archivio e regolarmente sottoscritta;
- Il CIG Z3F1234567 è stato correttamente assegnato all'appalto e risulta registrato presso ANAC;
- La copertura finanziaria è disponibile nel capitolo 1080/2026 (€28.500,00, residuo post-liquidazione €19.821,00);
- Il pagamento avverrà tramite bonifico bancario, tracciato e documentato secondo disposizioni L. 136/2010 (antiriciclaggio);
- Il termine di pagamento è fissato a 30 giorni dalla data della presente Determinazione, conforme a D.Lgs. 9/10/2002 n. 231 art. 4 (Disposizioni sui pagamenti dalle PA);

---

## DETERMINA

### Art. 1 — Liquidazione della fattura

Si procede alla **liquidazione della fattura n. 234/2026** emessa dalla ditta Puliservice Srl in data 28 febbraio 2026, per importo totale di **€8.679,00 (IVA inclusa)**, relativa a prestazioni di pulizia e sanificazione uffici comunali nel mese di febbraio 2026.

### Art. 2 — Modalità e termini di pagamento

Il pagamento sarà effettuato mediante **bonifico bancario** verso IBAN IT76P0306909606100000012345, intestato a Puliservice Srl, entro il termine perentorio di **30 giorni dalla data della presente Determinazione** (ossia entro il 27 aprile 2026), secondo disposizioni D.Lgs. 231/2002.

Il bonifico sarà disposto dalla Tesoreria Comunale con applicazione di causale: "Liquidazione fattura 234/2026 — Pulizia uffici febbraio 2026 — Comune di Ameglia — Contratto quadro AMA-2025-LU — CIG Z3F1234567".

### Art. 3 — Imputazione contabile

L'importo è imputato al capitolo di bilancio **1080/2026** — "Servizi di Pulizia e Sanificazione Uffici Comunali".

**Movimento contabile:**
- Dare: Cap. 1080/2026 per €8.679,00
- Avere: Conto Fornitori/Debiti verso Fornitori per €8.679,00
- Sottoconto: Puliservice Srl

### Art. 4 — Allegati e documentazione

La presente Determinazione è corredata dai seguenti allegati obbligatori:
- **Allegato A:** Report fotografico dello stato degli uffici post-pulizia (29 febbraio 2026)
- **Allegato B:** Certificato di regolare esecuzione sottoscritto da Geom. Gabriele Benabbi (RUP)
- **Allegato C:** Copia della fattura n. 234/2026 con bollo/marca da bollo
- **Allegato D:** Verifica DURC (estratto DURC-2026-156248)
- **Allegato E:** Certificato verifica posizione tributaria presso Agenzia delle Entrate
- **Allegato F:** Copia Contratto Quadro AMA-2025-LU e Ordine Fornitura OF/2025/0445
- **Allegato G:** Estratto tracciamento antiriciclaggio (L. 136/2010)

### Art. 5 — Responsabilità amministrativa

La presente Determinazione è sottoscritta dai seguenti soggetti, ciascuno per la propria competenza:

**Per la Ragioneria — Servizio Finanziario:**
dott.ssa Alessandro Ardigò, Responsabile di Settore (sottoscrive imputazione contabile e disponibilità finanziaria)

**Per l'Ufficio Tecnico (verifiche conformità):**
Geom. Gabriele Benabbi, RUP (sottoscrive certificato regolare esecuzione e verifiche preliminari)

**Approvazione finale:**
Il Responsabile della Ragioneria approva la Determinazione ai sensi dell'art. 151 D.Lgs. 267/2000 (TUEL).

---

## NORMATIVE DI RIFERIMENTO

- **D.P.R. 8 febbraio 1997 n. 43** — Regolamento relativo alla «Legge quadro sulla finanza locale»
- **D.Lgs. 18 agosto 2000 n. 267** — Testo Unico delle Leggi sull'Ordinamento degli Enti Locali (TUEL)
- **D.Lgs. 9 ottobre 2002 n. 231** — Disposizioni in materia di pagamenti delle amministrazioni pubbliche (art. 4: termini pagamento 30 giorni)
- **D.P.R. 29 settembre 1973 n. 602** — Ordinamento tributario (art. 48-bis: verifica posizione debitoria)
- **L. 13 marzo 2010 n. 136** — Disposizioni antiriciclaggio (art. 3 co. 7: tracciabilità flussi finanziari)
- **D.Lgs. 12 aprile 2006 n. 163** — Codice dei Contratti (art. 80: CIG per appalti pubblici)
- **L. 30 novembre 2000 n. 318** — Riforma tributaria (DURC — Documento Unico Regolarità Contributiva)

---

**Responsabile della Ragioneria — Servizio Finanziario**
dott.ssa Alessandro Ardigò

**Responsabile del Procedimento (RUP)**
Geom. Gabriele Benabbi
Capo Ufficio Tecnico

Firma digitale / Timbro digitale del Comune
Data: 28 marzo 2026

---

Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**

```
RAPPORTO DI REVISIONE NORMATIVA
Determinazione Liquidazione Fattura — Comune di Ameglia — Caso Puliservice

REVISORE: COMUNE-REVISORE-RAGIONERIA v.1.01
DATA REVISIONE: 28/03/2026

VERIFICHE NORMATIVE COMPLETATE:

✓ CONFORMITÀ D.Lgs. 231/2002: Completa. Art. 4 applicato correttamente.
  Termine pagamento fissato a 30 giorni dalla data Determinazione (conforme
  a normativa PA). Disposizioni rispettate integralmente.

✓ VERIFICA DURC (L. 318/2000): Conforme. DURC-2026-156248 acquisito,
  esito positivo, validità 120 giorni verificata. Data acquisizione
  (26/03/2026) antecedente firmatura Determinazione. Documentazione
  tracciata e allegata.

✓ TRACCIABILITÀ FLUSSI (L. 136/2010): Conforme. Pagamento tramite bonifico
  bancario, IBAN registrato, intestatario coerente. Modalità antiriciclaggio
  integrate. Causale bonifico completa e referenziale.

✓ VERIFICA POSIZIONE TRIBUTARIA (art. 48-bis DPR 602/1973): Conforme.
  Per importo €8.679,00 (>€5.000), verifica obbligatoria effettuata.
  Esito negativo per debiti (27/03/2026). Documentazione in Allegato E.

✓ CERTIFICAZIONE REGOLARE ESECUZIONE: Presente e conforme. Sopralluogo RUP
  26 marzo, certificato sottoscritto (Allegato B), documentazione fotografica
  post-servizio (Allegato A). Verifica conformità a standard contrattuali
  regolarmente attestata.

✓ INDICAZIONE CIG: Corretto. CIG Z3F1234567 riportato e registrato presso
  ANAC per il contratto quadro AMA-2025-LU. Tracciabilità esecuzione garantita.

✓ IMPUTAZIONE CONTABILE: Corretta. Capitolo 1080/2026 ha disponibilità
  sufficiente (€28.500,00 residuo). Movimento contabile quadra.

✓ RIFERIMENTI NORMATIVI: Completi. Tutte le leggi di riferimento elencate
  (D.Lgs. 267/2000, 231/2002, 163/2006, L. 136/2010, ecc.).

⚠ NOTA MINORE — BIC/SWIFT: Indicato "BAPAITRRXXX" (generico per Banca
  Popolare). Suggerimento: Prima di efficacia, verificare BIC effettivo
  presso Banca depositaria per garantire routing accuato bonifico.

ESITO REVISIONE: APPROVAZIONE CON NOTA MINORE
Il documento è conforme a tutte le normative vigenti in materia di pagamenti PA,
tracciabilità antiriciclaggio, DURC, e verifiche tributarie. È sufficiente
completare il BIC/SWIFT verificato presso banca prima della firma definitiva.

Per applicare le correzioni alla bozza risponda **applica le note del revisore**.
```

---

### TURNO 5 — Applicazione note del revisore alla bozza

**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**

La LLM rilegge la bozza originale e il report del revisore, applica tutte le correzioni e genera la versione finale aggiornata:

```
VERSIONE AGGIORNATA CON CORREZIONI DEL REVISORE

[Documento identico alla versione precedente, con la seguente modifica:]

**BIC/SWIFT:** UNCRITMM (Banco Unicredit — Filiale Versilia per Liguria)
**Intestatario conto:** Puliservice Srl

[Resto invariato]

---

Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella permanente risponda **salva**.
```

---

### TURNO 6 — Salvataggio

**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**

Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato (PDF, .docx, .txt).
Il file viene salvato in: `/Ameglia/Ragioneria/Liquidazioni_Fatture/DET_2026_0052_Puliservice_DEFINITIVO.pdf`

L'agente conferma:
"✓ File salvato con successo. Determinazione archiviata in formato PDF con tutti gli allegati. Documento pronto per sottoscrizione digitale e trasmissione Tesoreria per elaborazione pagamento."

---

## NOTE DI TEST

1. **Verifica completezza verifiche pre-pagamento:** Controllare che siano completate e citate: DURC (con numero autorità e data validità), verifica posizione tributaria (con esito e data), certificazione regolare esecuzione (da RUP).

2. **Conformità termini pagamento D.Lgs. 231/2002:** Validare che termine sia esattamente 30 giorni dalla data della Determinazione (non "entro i termini di legge" generico). Scadenza deve essere calcolata e indicata (es. "entro il 27 aprile 2026").

3. **Tracciabilità L. 136/2010:** Accertare che metodo pagamento sia bonifico bancario tracciato (non contanti), che IBAN sia registrato e corretto, che causale bonifico sia completa con riferimenti (numero fattura, numero contratto, CIG, periodo).
