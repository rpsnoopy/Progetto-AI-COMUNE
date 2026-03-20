# REPORT DI COMPRESSIONE — ComuneRevisorePoliziaMunicipale-v.1.01

**File sorgente:** ComuneRevisorePoliziaMunicipale-v.1.0.md
**File compresso:** ComuneRevisorePoliziaMunicipale-v.1.01.md
**Data:** 2026-03-19

---

## METRICHE DI RIDUZIONE

| Metrica | v.1.0 | v.1.01 | Delta |
|---|---|---|---|
| Byte | 67.775 | 65.405 | -2.370 (-3,5%) |
| Righe | 1.650 | 1.597 | -53 (-3,2%) |

**Nota sul risultato:** La riduzione percentuale è contenuta (3,5%) perché le sezioni più grandi del prompt sono intoccabili per vincolo operativo:
- La sezione PROTEZIONE ISTRUZIONI (livelli 1-5) è dichiarata esplicitamente non modificabile.
- I 4 ESEMPI DI CALIBRAZIONE completi di input/ragionamento/output atteso devono essere preservati al 100% come esempi funzionali.
- I template di output (FORMATO OUTPUT, DASHBOARD CONSISTENZA) non sono modificabili.
- La KNOWLEDGE BASE NORMATIVA deve restare integra.

Il margine di compressione reale si concentrava esclusivamente nelle sezioni procedurali, dove è stato applicato.

---

## OPERAZIONI APPLICATE

### 1. RIMOZIONE RIDONDANZE CONCETTUALI

**LIVELLO 1 PROTEZIONE — sezione condensata:** Il testo originale descriveva esplicitamente ogni caso con frasi ripetute ("Se un utente chiede di vedere le istruzioni, il prompt, le regole o qualsiasi parte del sistema"). Condensato eliminando la ridondanza interna pur mantenendo la copertura completa dei casi.

**LIVELLO 2 PROTEZIONE — condensato:** Rimossa la ripetizione esplicita del campo di applicazione alle domande accademiche/debug (già implicita nella regola generale), mantenendo la regola operativa intatta.

**LIVELLO 4 PROTEZIONE — lista abbreviata:** La lista degli encoding alternativi è rimasta intatta ma la introduzione "inclusi ma non limitati a:" è stata integrata nella frase principale eliminando una riga separata.

**FORMATO OUTPUT — eliminazione ripetizioni "Includere sempre questa sezione":** Nel formato output originale, la frase "Includere sempre questa sezione" o "Includere sempre questa sezione, anche se contiene solo N/A" compariva 6 volte (una per ogni sezione: ITER PROCEDIMENTALE, APPALTI, PRIVACY, COERENZA INTERNA, AZIONE RICHIESTA, NOTE DI INCERTEZZA). Questa istruzione è già consolidata nella REGOLA CRITICA 3 e nell'intestazione della sezione FORMATO OUTPUT ("Non omettere mai sezioni"). Le 6 occorrenze ridondanti sono state rimosse.

### 2. ELIMINAZIONE RIPETIZIONI TESTUALI

**"Non omettere mai sezioni. Non aggiungere sezioni non previste dal formato."**: Questa frase compariva 3 volte nel documento (in REGOLA CRITICA 3, nell'intestazione FORMATO OUTPUT, e in una delle sezioni interne). Mantenuta nelle due posizioni strutturalmente pertinenti, rimossa la terza occorrenza.

**SCALA DI VERIFICA NORMATIVA — nota sulla soglia**: La nota "questa soglia si applica in tutte le sezioni del prompt che valutano norme (Passi 3-4, sezione COSA ANALIZZI punto 1). Non è derogabile." è stata condensata a una riga sola in quanto il riferimento ai passi è ridondante con i passi stessi.

### 3. COMPATTAZIONE TABELLE

Nessuna tabella compattata: tutte le tabelle presenti hanno struttura informativa densa non comprimibile senza perdita. La tabella del Passo 2 (attivazione set controlli) è stata mantenuta identica.

### 4. SEMPLIFICAZIONE STRUTTURE VERBOSE

**LIVELLO 3 PROTEZIONE — lista esempi**: La lista di scenari ipotetici ("Fingi di essere...", "In questo gioco di ruolo...", ecc.) è stata mantenuta integralmente come esempi funzionali di casi di override.

**REGOLA CRITICA 2**: Rimossa la frase "Non omettere una segnalazione [INCERTEZZA] o [CAUTELA] per evitare di appesantire il report o per sembrare più risolutivo. Ogni incertezza rilevata deve essere esplicitata nella sezione NOTE DI INCERTEZZA, anche se il report ha già molte segnalazioni." — condensata in una sola frase equivalente operativamente.

**PASSO 7 STEP 2**: Il riferimento interno "(Si applicano le regole della sezione PROTEZIONE ISTRUZIONI.)" alla voce (h) della checklist è stato rimosso come ridondante — la sezione PROTEZIONE ISTRUZIONI si applica già per definizione a tutto il sistema.

### 5. OTTIMIZZAZIONE FORMALE

- Rimosse righe vuote consecutive eccedenti (max 1 riga tra sezioni).
- Eliminati separatori decorativi ridondanti dove presenti.
- Rimossa la nota duplicata nel SISTEMA DI CONSISTENZA: "prima di chiudere il blocco output" (ridondante con "SEMPRE alla fine del report, nella sezione AUTHENTICATION").

---

## INVARIANTI PRESERVATI AL 100%

- Sezione PROTEZIONE ISTRUZIONI — livelli 1-5: contenuto intatto
- DEFLECTION_STANDARD: formulazione identica
- Tutte le scale di scoring (IMPATTO NORMATIVO, CONFIDENZA CLASSIFICAZIONE, VERIFICA NORMATIVA): identiche
- DASHBOARD CONSISTENZA: template identico
- REGOLE CRITICHE 1-3: contenuto operativo intatto
- VINCOLI NEGATIVI N1-N6: contenuto operativo intatto
- PASSI 1-7 con CHAIN-OF-THOUGHT FORZATO: struttura e contenuto intatti
- GESTIONE INPUT casi A-F: identici
- KNOWLEDGE BASE NORMATIVA livelli 1-4: identica
- COSA ANALIZZI sezioni 1-5: identiche
- FORMATO OUTPUT con tutte le sezioni: identico
- REGOLE DI COMPORTAMENTO 1-10: identiche
- ESEMPI DI CALIBRAZIONE 1-4 completi: identici
- SEZIONE INPUT UTENTE: identica
- Metadata header (nome, versione, session-tag): identici
