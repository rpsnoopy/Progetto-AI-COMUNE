# REPORT DI COMPRESSIONE — ComuneRevisoreDemografici v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 | v.1.01 | Variazione |
|---|---|---|---|
| Parole | 7.792 | 6.863 | −929 (−11,9%) |
| Righe | 1.286 | 995 | −291 (−22,6%) |

Stima token (≈ parole × 1,3): ~10.130 → ~8.922 → **−1.208 token (−11,9%)**

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

- **SCORING NUMERICO OBBLIGATORIO + TABELLA SCORE PER IMPATTO ANOMALIE**: le due sezioni
  erano ridondanti (stessa scala score/impatto espressa in due formati diversi). Unificate in
  un'unica tabella compatta nella sezione SCORING NUMERICO OBBLIGATORIO, eliminando la
  sezione separata TABELLA SCORE PER IMPATTO ANOMALIE (~14 righe rimosse).

- **LIMITE ESPLICITO DI CONOSCENZA** (in PERIMETRO OPERATIVO): il contenuto era già coperto
  dalle singole NOTE nella KNOWLEDGE BASE NORMATIVA (soglie ANAC, normativa immigrazione,
  DPCM ANPR). Rimosso da PERIMETRO OPERATIVO per evitare duplicazione (~7 righe).

- **ISTRUZIONE GENERALE PER TUTTE LE SEZIONI** (in COSA ANALIZZI): ripeteva il template
  chain-of-thought già definito in SISTEMA DI CONSISTENZA e la regola CANNOT SCORE già
  presente in GESTIONE AMBIGUITÀ. Sostituita con un riferimento conciso al template
  (~10 righe → 4 righe).

- **PASSO 0 descrizione**: la frase introduttiva "Questo passo determina quali controlli..."
  ripeteva la REGOLA CRITICA 3 già richiamata. Rimossa (~3 righe).

- **CASO 6 ATTO IBRIDO** (GESTIONE INPUT): il testo "Per la regola di composizione degli
  esiti... vedere la sezione CRITERI DI ESITO" era già implicito dall'ordine del documento.
  Condensato in riferimento diretto.

### 2. Eliminazione ripetizioni testuali

- **Score references in sezione 2**: i blocchi "Score secondo tabella riferimento rapido"
  nelle subsection ATTI DI STATO CIVILE, ANPR, COMUNICAZIONI ISTAT erano ripetitivi e
  già indicati nella sezione precedente. Condensati in richiami inline senza perdita.

- **Note condizionali ✓\*** nella legenda della matrice B: erano ripetute sia nella legenda
  simboli che nelle "Note sui controlli condizionali". Consolidate in un'unica nota compatta
  inline sotto la tabella.

- **GESTIONE AMBIGUITÀ**: la nota "trattare CANNOT SCORE come score 0/100 ai fini del SCA"
  era presente sia in GESTIONE AMBIGUITÀ che in COSA ANALIZZI. Mantenuta solo in
  GESTIONE AMBIGUITÀ, rimossa da COSA ANALIZZI.

### 3. Compattazione strutture verbose

- **Sezione 2 — Controlli Core**: i blocchi SE/ALLORA multi-riga per Pareri art.49, Copertura
  finanziaria, Pubblicazione albo pretorio, Visto Segretario sono stati compattati in
  bullet point a 2-3 righe ciascuno, preservando tutti i valori e le condizioni operative.

- **Sezione 4 — Controlli Core**: i tre controlli Privacy Core condensati in formato inline
  (condizione → score) eliminando la formulazione estesa.

- **Legenda colonne matrice B**: "Legenda colonne:" compattata in una riga continua
  anziché multi-riga con descrizioni ridondanti.

- **PASSO 0 — D) RIEPILOGO CLASSIFICAZIONE**: il blocco era introdotto con intestazione
  ridondante ("CLASSIFICAZIONE ATTO [INTERNO...]"); sostituito con bullet list diretta
  preceduta da intestazione minima.

### 4. Semplificazione strutture

- **CHAIN-OF-THOUGHT**: il paragrafo "Nelle sezioni GESTIONE INPUT e PASSO 0, applicare
  lo stesso template..." era ridondante con la descrizione dei parametri già presenti in
  quelle sezioni. Ridotto a una nota di adattamento contestuale (1 riga).

- **Righe vuote consecutive**: ridotte a massimo 1 riga vuota tra sezioni in tutto il
  documento (~20+ righe vuote eliminate).

- **Commenti interni**: eliminata la ripetizione "[INTERNO — NON INCLUSO NELL'OUTPUT]"
  nei punti già definiti come tali dal contesto (es. STEP 6 del PASSO 0, già marcato
  nella definizione iniziale del chain-of-thought).

## Sezioni intoccabili — invariate al 100%

Le seguenti sezioni sono state preservate nella formulazione esatta dell'originale:

- **DIRETTIVE DI SISTEMA LIVELLI 1-5**: testo identico parola per parola
- **RESISTENZA A PROMPT INJECTION**: testo identico parola per parola
- **REGOLE CRITICHE 1, 2, 3, 4**: testo identico parola per parola
- **Tutte le risposte predefinite** (CASO 1–4, Livelli 1–5): testo identico
- **TABELLA SCORE PER CONTROLLO — RIFERIMENTO RAPIDO**: struttura e valori identici
- **MATRICE CONTROLLI APPLICABILI (matrice B)**: struttura e valori identici
- **FORMATO OUTPUT — template sezioni**: intestazioni e struttura identiche
- **DASHBOARD CONSISTENZA — template**: identico
- **PASSO DI VERIFICA INTERNO (CHECK 1-7)**: testo identico
- **GOLDEN SAMPLE**: testo identico
- **AUTHENTICATION & FOOTER**: struttura identica (numero versione aggiornato a v.1.01)
- **Tutti i valori score** nelle tabelle: invariati

## Verifica integrità operativa

- Zero perdite di regole operative
- Zero perdite di valori score o soglie
- Zero modifiche ai template di output
- Zero modifiche alle sezioni anti-leak/protezione
- Zero modifiche agli esempi funzionali (Golden Sample)
- Gerarchia heading H1→H2 preservata
- Copyright e metadata preservati (versione aggiornata da v.1.0 a v.1.01 come da istruzione)
