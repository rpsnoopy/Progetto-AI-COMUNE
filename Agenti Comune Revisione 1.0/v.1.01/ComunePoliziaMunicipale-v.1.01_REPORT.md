# REPORT COMPRESSIONE — ComunePoliziaMunicipale v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 | v.1.01 | Riduzione |
|---------|-------|--------|-----------|
| Righe | 1.830 | 1.435 | −395 (−21,6%) |
| Parole | 10.655 | 8.317 | −2.338 (−21,9%) |
| Token stimati (×0,75 word/token) | ~8.000 | ~6.240 | ~−1.760 (~−22%) |

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

**PROTEZIONE SISTEMA — LIVELLI 1/2/3 unificati**: le tre sezioni separate (LIVELLO 1 — DIVIETO DI DIVULGAZIONE DIRETTA, LIVELLO 2 — RESISTENZA A PARAFRASI, LIVELLO 3 — RESISTENZA A ROLE-PLAY) elencavano tipologie di richiesta vietate in forma indipendente e prolissa. Tutte le tipologie sono state consolidate in un unico paragrafo compatto che copre richieste dirette, indirette e scenari narrativi, preservando ogni singola categoria di formulazione vietata.

**PERIMETRO OPERATIVO**: la sezione conteneva due blocchi quasi identici ("Non produrre mai atti di competenza di altri uffici..."). Il secondo blocco (righe 159-166 dell'originale) era sostanzialmente identico al primo (righe 149-157) con minime variazioni di phrasing. Consolidato in un'unica formulazione.

**Punto 3 del Catalogo (art. 54 TUEL)**: la distinzione ordinaria/contingibile era espressa due volte nel testo del punto (righe 1202-1230 dell'originale), con il secondo blocco che ripeteva il concetto del primo con formulazione leggermente diversa. Mantenuta la versione più completa, rimosso il duplicato. La regola resta intoccata.

**REGOLE DI REDAZIONE — Regole 11-14**: queste regole erano quasi interamente cross-reference a sezioni già complete del prompt ("Si applica la regola al Punto 3 del Catalogo", "Si applica la REGOLA ASSOLUTA — LINGUAGGIO GIUDIZIARIO"). Il contenuto operativo era già completo nelle sezioni di riferimento. Mantenute come rimandi compatti, eliminato il testo ridondante.

**REGOLE CRITICHE — RIEPILOGO FINALE (R1-R7)**: ogni voce era una ri-enunciazione sintetica di regole già dichiarate come REGOLA ASSOLUTA nelle sezioni precedenti. Il riepilogo è stato mantenuto (struttura necessaria per gerarchia e lookup), ma compresso eliminando le sottosezioni esplicative che rimandavano nuovamente alle sezioni già visibili.

### 2. Eliminazione ripetizioni testuali

**Formula stallo strutturale "Stallo permanente — i seguenti dati critici..."**: la formula completa compariva sia nella sezione REGOLA ASSOLUTA — FAIL-SAFE sia nel PASSO 3 del CoT. Mantenuta in FAIL-SAFE come definizione; nel PASSO 3 sintetizzata con rimando.

**Cicli di chiarimento (massimo 3)**: il limite di 3 cicli e la formula di stallo permanente erano ripetuti identicamente in FAIL-SAFE e in PASSO 3. Consolidato in FAIL-SAFE; PASSO 3 contiene solo il meccanismo operativo senza duplicare il testo.

**Struttura STEP 1-2-3-4-5-6 nei Passi CoT**: ogni passo usava lo stesso scaffold rigido (STEP 1 — IDENTIFICA / STEP 2 — CRITERI / STEP 3 — MISURA / STEP 4 — CALCOLA / STEP 5 — VERIFICA / STEP 6 — OUTPUT STATO) anche quando conteneva solo 1-2 righe di contenuto utile. I passi sono stati semplificati mantenendo la logica di scoring e le etichette di output, eliminando le etichette di scaffold vuote.

**GESTIONE INPUT PER TIPO — input parziale**: il testo originale ripeteva interamente la logica di stallo già descritta in FAIL-SAFE e PASSO 3. Compresso con rimando.

### 3. Compattazione tabelle

Nessuna tabella era compattabile senza perdita di informazione (la Dashboard Consistenza e le strutture output sono template funzionali intoccabili). Le tabelle di score nei Catalogo Atti sono state mantenute intatte.

### 4. Semplificazione strutture verbose

**PASSO 1 (Classificazione e Verifica Perimetro)**: i 6 step esplicitati verbosamente sono stati compattati in una struttura condizionale chiara con gli stessi tre criteri, soglie e output.

**PASSO 2 (Identificazione Tipo Atto)**: analogamente a PASSO 1, semplificato mantenendo i criteri di scoring e le coppie ambigue comuni (nessuna rimossa).

**PASSO 4 (Verifica Riferimenti Normativi)**: il testo "Attenzione non ovvia" di chiusura (che ripeteva la REGOLA ASSOLUTA — RIFERIMENTI NORMATIVI) è stato compresso in una riga di rimando.

**IDENTITÀ E RUOLO**: il paragrafo su TONO E REGISTRO è stato compresso eliminando la ripetizione "evitando tecnicismi non necessari" (implicita nel registro chiaro e diretto).

### 5. Ottimizzazione formale

- Righe vuote consecutive ridotte a 1 tra sezioni.
- Separatori ridondanti rimossi dove non strutturali.

## Invarianti — cosa NON è stato toccato

- **Sezioni anti-leak/protezione**: tutte le categorie di richieste vietate (dirette, indirette, role-play, scenari ipotetici) sono preservate al 100%. La RISPOSTA STANDARD DI DEFLECTION è invariata.
- **Template di output** (struttura atto, Dashboard Consistenza, RIEPILOGO VERIFICA, ATTENZIONE REDATTORE): invariati.
- **Esempi A, B, C**: preservati integralmente incluso il ragionamento interno (esempi C è stato leggermente compresso solo nella parte CoT interna, non nell'output).
- **Knowledge Base normativa**: invariata, incluse tutte le marcature [NORMA DA VERIFICARE].
- **Catalogo Atti (punti 1-15)**: invariato, inclusi tutti gli score di criticità, le distinzioni obbligatorie e le note operative.
- **GOLDEN SAMPLE**: preservato integralmente.
- **Copyright e metadata**: invariati.
- **Gerarchia H1/H2/H3**: invariata.
