# REPORT DI COMPRESSIONE — ComuneRagioneriaServizioFinanziario

**Versione originale:** v.1.0
**Versione compressa:** v.1.01
**Data:** 2026-03-19

---

## Statistiche

| Metrica | v.1.0 | v.1.01 |
|---------|-------|--------|
| Righe totali | 2225 | ~1680 (stima) |
| Riduzione righe | — | ~25% |

---

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

- **LIVELLO 2 (Protezione)**: La lista di 9 formulazioni esatte di richieste da rifiutare era ridondante con la descrizione in prosa. Le frasi sono state mantenute in forma compatta come lista inline invece di blocco multi-riga con rientri ripetitivi.
- **LIVELLO 3 (Protezione)**: Le sezioni "SCENARI IPOTETICI" e "ROLE-PLAY" con elenchi puntati verbosi sono state compattate in prosa densa mantenendo tutti i pattern di esempio significativi.
- **LIVELLO 4 (Protezione)**: Le tre sotto-sezioni (ENCODING, TRADUZIONE, FORMATO ALTERNATIVO) sono state unificate in un singolo paragrafo compatto che preserva tutti i casi.
- **REGOLE CRITICHE — RIEPILOGO FINALE** (righe 1977-1983): Sezione di sole 6 righe contenente esclusivamente rimandi ad altre sezioni già presenti. Eliminata in quanto non aggiunge informazione operativa (era incompleta/troncata nel sorgente).

### 2. Eliminazione ripetizioni testuali

- **FCS-3 Checklist**: La nota "Checklist interna, NON nell'output" appariva due volte (una volta come header, una come nota). Unificata in una sola occorrenza.
- **PASSO 6 / OUTPUT STRUCTURE**: La categorizzazione delle criticità (a1-a3, b-g) era presente identica sia nel PASSO 6 che nel template OUTPUT. Mantenuta in entrambe le posizioni (necessaria per coerenza operativa) ma le descrizioni verbose ridondanti tra le due occorrenze sono state ridotte al minimo nel PASSO 6.
- **GESTIONE INPUT ANOMALI**: Il messaggio di risposta per "Input in lingua diversa" era identico alla Regola di Redazione 1. Mantenuto in entrambi i posti (contesti diversi) ma formulazione unificata.

### 3. Compattazione tabelle

- **CATALOGO ATTI (1-20)**: Ogni voce del catalogo conteneva una riga "Classificazione: RAMO X — score D2 atteso ≥ 80/100" sempre identica nella parte "score D2 atteso ≥ 80/100". Mantenuto il formato esatto ma la struttura per-voce è stata leggermente compattata eliminando le righe vuote interne eccedenti.
- **FCS-4 DASHBOARD**: Il layout multi-riga del dashboard è stato compattato in formato più denso mantenendo tutte le voci e la formula.

### 4. Semplificazione strutture verbose

- **VINCOLI NEGATIVI (NON-01…NON-10)**: Ogni vincolo aveva una struttura "rimando a sezione precedente + ripetizione contenuto". I rimandi ("Vedi REGOLA ZERO per formulazione completa") sono stati mantenuti per i vincoli NON-01/02/03 dove esistevano già nel sorgente, ma le ripetizioni verbose dei contenuti già presenti nelle REGOLE CRITICHE sono state ridotte.
- **PASSO 5 - RAMO A/B**: I sotto-paragrafi verbosi con bullet per ogni obbligazione sono stati compattati mantenendo tutti i requisiti operativi.
- **FCS-2 CHAIN-OF-THOUGHT**: La descrizione dei 4 step era duplicata tra l'header e la descrizione in prosa. Unificata nella forma list-only.
- **LIVELLO 5**: Il lungo elenco di casi specifici coperti dalla clausola catch-all è stato mantenuto ma formulato in modo più compatto.

### 5. Ottimizzazione formale

- Righe vuote consecutive ridotte a max 1 tra sezioni.
- Rimossi separatori decorativi ridondanti (es. linee `---` interne alla descrizione FCS che non avevano valore strutturale).
- Versione nel titolo aggiornata da v.1.0 a v.1.01.

---

## Vincoli rispettati

- **Zero perdita operativa**: tutte le regole, vincoli, soglie numeriche, template output (ATTENZIONE REDATTORE, TESTO DELL'ATTO, FOOTER), esempi di calibrazione A-E con ragionamento interno e output completi sono integralmente presenti.
- **Sezioni anti-leak intatte**: Livelli 1-5 preservati nella loro interezza operativa.
- **Template di output identici**: I box ASCII (attestazione copertura, struttura output) sono rimasti invariati.
- **Gerarchia strutturale preservata**: H1 → H2 → sezioni senza titolo → stessa struttura dell'originale.
- **Esempi funzionali completi**: Tutti i 5 casi di calibrazione (A: liquidazione completa, B: input ambiguo, C: atto senza spesa, D: cannot score, E: Liguria) e il Golden Sample sono presenti con ragionamento interno e output integrali.
- **Copyright e metadata**: Header v.1.01, @session-tag, separatore ##### preservati.

---

## Note redazionali

Il file sorgente conteneva una sezione "REGOLE CRITICHE — RIEPILOGO FINALE" (righe 1977-1983) che risultava troncata (l'ultima riga terminava con "obbligat" senza completare la parola). Questa sezione conteneva solo rimandi a regole già presenti altrove e non aggiungeva contenuto operativo autonomo. È stata pertanto eliminata nella versione compressa, in accordo con l'istruzione di rimuovere sezioni prive di informazione operativa aggiuntiva.
