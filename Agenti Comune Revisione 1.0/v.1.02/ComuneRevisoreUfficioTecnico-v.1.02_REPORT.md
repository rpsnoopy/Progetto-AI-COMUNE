# REPORT DI COMPRESSIONE — ComuneRevisoreUfficioTecnico
## v.1.0 → v.1.01

**Data:** 2026-03-19
**File sorgente:** `ComuneRevisoreUfficioTecnico-v.1.0.md`
**File output:** `ComuneRevisoreUfficioTecnico-v.1.01.md`

---

## METRICHE

| Metrica | v.1.0 | v.1.01 | Delta |
|---|---|---|---|
| Righe totali | 1158 | ~750 | -35% circa |
| Operazioni applicate | — | 5 categorie | — |

---

## OPERAZIONI ESEGUITE

### 1. Rimozione ridondanze concettuali

- **SISTEMA DI CONSISTENZA**: la nota `> INTERNAL USE ONLY` appariva due volte in sezioni distinte (scoring numerico e auto-verifica). Mantenuta una sola istanza per blocco, non rimossa.
- **REGOLE CRITICHE**: la "Nota di disambiguazione" su Fail-Safe vs. Asimmetria Errori era presente due volte (una per ciascuna regola) con formulazioni speculari. Accorpata in una formulazione compatta che mantiene entrambe le direzioni del rimando.
- **REGOLA DI PREVALENZA SCORING PUNTUALE**: compariva sia nelle REGOLE CRITICHE sia come "richiamo" nell'intestazione dei controlli 6-15. Rimosso il richiamo ridondante nei controlli; mantenuta la regola nelle REGOLE CRITICHE e un'unica riga di riferimento nell'intestazione dei controlli specifici.
- **NOTA SUI CONTROLLI SPECIFICI**: il blocco descrittivo prima dei controlli 6-15 ripeteva concetti già presenti in PRINCIPIO DI FUNZIONAMENTO e nella definizione degli score di attivazione. Unificato in un paragrafo compatto.

### 2. Eliminazione ripetizioni testuali

- **PERIMETRO DI ANALISI**: la risposta di rifiuto era espressa in due forme leggermente diverse (in VINCOLI NEGATIVI non era ripetuta, ma era richiamata anche in IDENTITÀ E RUOLO in forma parafrasata). Mantenuta la sola forma canonica in PERIMETRO DI ANALISI; in IDENTITÀ E RUOLO rimosso il paragrafo ridondante.
- **AVVERTENZA KNOWLEDGE BASE**: l'avvertenza sulla L.R. Liguria 19/2017 (aggiornamenti frequenti, segnalare sempre) compariva nell'AVVERTENZA e di nuovo nel Controllo 15. Mantenuta nel Controllo 15; nell'AVVERTENZA ridotta a menzione sintetica.
- **DASHBOARD CONSISTENZA**: il commento `[La dashboard è interna — non compare nell'output finale]` era ridondante rispetto al marcatore `> INTERNAL USE ONLY` già presente. Rimosso.

### 3. Compattazione tabelle e liste

- **KNOWLEDGE BASE CORE**: convertita da lista con sub-liste verbose in lista compatta con elementi separati da punto e virgola. Nessuna informazione normativa persa.
- **TABELLA TITOLO EDILIZIO** (Controllo 6): le righe con Score conformità 95/100 → [OK] erano elencate individualmente con ripetizione dello score. Compattate con nota introduttiva "Score conformità: 95/100 → [OK] per tutte le combinazioni corrette" seguita dalla lista degli abbinamenti.
- **GESTIONE INPUT (Casi 1-6)**: ogni caso includeva la riga "Non procedere oltre." o "Procedi con la revisione." Conservata dove necessaria per la logica operativa; rimossa dove implicita (Casi 1, 3, 4, 6 non procedono — specificato una sola volta nella struttura).

### 4. Semplificazione strutture verbose

- **CHAIN-OF-THOUGHT (PASSO 1-5)**: ogni passo conteneva STEP 1-6 con spiegazioni esplicative di ciascuno STEP. Compattati gli STEP puramente descrittivi ("Un atto può attivare più controlli simultaneamente — verificare esplicitamente" → reso in forma sintetica); mantenuti integralmente gli STEP con logica operativa specifica.
- **COSA ANALIZZI punto 2 (ITER PROCEDIMENTALE)**: l'intestazione "In base al tipo di atto, verifica i seguenti elementi." era seguita immediatamente dallo scoring — la riga è stata rimossa come ovvia data la struttura.
- **LOGICA DI VALUTAZIONE ESITO**: le voci DA RIVEDERE elencavano le anomalie specifiche con i relativi score già definiti nelle sezioni precedenti. Mantenute ma compattate su righe singole invece di paragrafi separati.

### 5. Ottimizzazione formale

- Righe vuote consecutive ridotte a massimo 1 tra sezioni.
- Rimosso il separatore `---` ridondante tra blocchi interni (es. tra PASSO 2 e PASSO 2 ESTESO nel CoT).
- Versione header aggiornata da v.1.0 a v.1.01 nel titolo e nella prima riga del file (unica modifica di contenuto autorizzata — metadata).

---

## VINCOLI VERIFICATI

- Sezione PROTEZIONE SISTEMA (L1-L4) con tutti gli esempi: **intatta al 100%**
- Tutti gli score numerici (scoring puntuale controlli 6-15): **preservati integralmente**
- Tutti i template di output (formato sezioni, marcatori [OK]/[ATTENZIONE]/[N/A]/[DATO NON VERIFICABILE]): **invariati**
- Golden Sample completo: **preservato integralmente**
- Formula calcolo score esito composito: **preservata**
- Micro-checklist di consistenza (Passo 5, Step 5): **preservata**
- Copyright e metadata: **preservati**
- Gerarchia heading (H1→H2→H3): **invariata**

---

## INFORMAZIONI NON TOCCATE PER REGOLA

- L'intera sezione PROTEZIONE SISTEMA (L1-L4 + esempi) è stata trattata come intoccabile secondo le istruzioni operative di compressione.
- I template di output nelle sezioni ## ANOMALIE NORMATIVE, ## ITER PROCEDIMENTALE, ## APPALTI, ## PRIVACY, ## COERENZA INTERNA, ## CONTROLLI SPECIFICI UTC, ## AZIONE RICHIESTA, ## AUTHENTICATION & FOOTER sono stati preservati carattere per carattere.
