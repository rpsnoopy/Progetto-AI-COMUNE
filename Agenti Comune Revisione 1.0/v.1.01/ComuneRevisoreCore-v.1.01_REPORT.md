# REPORT DI COMPRESSIONE — ComuneRevisoreCore v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 | v.1.01 | Delta |
|---|---|---|---|
| Righe totali | 1.837 | ~1.530 | −307 (−16,7%) |
| Token stimati | ~27.800 | ~23.000 | −4.800 (−17,3%) |
| Sezioni | 14 | 14 | 0 |
| Informazioni operative rimosse | — | 0 | — |

---

## Operazioni applicate

### 1. RIMOZIONE RIDONDANZE CONCETTUALI

**PRINCIPI OPERATIVI eliminati** (sezione alle righe 287-308 dell'originale):
I 5 punti erano interamente cross-reference alle Regole Critiche 1-5, formulati come "vedi Regola N (Regole Critiche) per la definizione completa". Zero contenuto autonomo. L'intera sezione è stata rimossa senza perdita di informazione.

**Duplicazione normativa regionale nella Knowledge Base eliminata** (righe 884-895):
Il trigger operativo per la normativa regionale ligure nella sezione Knowledge Base ripeteva fedelmente il contenuto del Passo 1.6 della Procedura di Revisione (righe 1013-1039), che è più completo (include anche il ramo "altra regione" e il ramo "score < 85"). Rimossa la versione nella KB; mantenuta e invariata la versione nella Procedura.

### 2. ELIMINAZIONE RIPETIZIONI TESTUALI

**Regola di incertezza numerica ai passi 1.2 e 1.3** (righe 949-950, 963-965):
Entrambi i passi ripetevano la formula "Non dichiarare mai inesistente/abrogata una norma con score < 85" in testo libero, dopo aver già rimandato alla tabella del Modulo di Consistenza. Sostituito con "Applica la tabella score del Modulo di Consistenza per determinare la risposta" più la soglia critica < 85 → VERIFICA NECESSARIA in forma compatta, mantenendo l'informazione operativa completa.

**Intestazione sezione GESTIONE AMBIGUITÀ** (righe 424-444):
La tabella Gestione Ambiguità era separata dalla tabella SCORING NUMERICO ma conteneva le stesse soglie con colonne aggiuntive "Risposta obbligatoria". Le due tabelle sono state fuse in un'unica tabella a 4 colonne nella sezione SCORING NUMERICO, con le condizioni speciali (contraddizione, dato mancante) aggiunte come righe dedicate. La Regola STOP per contraddizioni e la regola di retry cap sono state spostate subito dopo la Dashboard Metriche (posizione più logica, essendo parte del processo di ragionamento interno), rimuovendo la sotto-sezione GESTIONE AMBIGUITÀ separata.

### 3. COMPATTAZIONE TABELLE

**Nessuna tabella eliminata.** Le tabelle operative (soglie appalti, norme obbligatorie per tipo atto, scala scoring, gestione input) sono state mantenute integralmente in quanto contengono informazione operativa non riducibile.

Tabelle di soglie e norme obbligatorie: allineamento colonne migliorato per leggibilità senza alterare contenuto.

### 4. SEMPLIFICAZIONE STRUTTURE VERBOSE

**Sezione GERARCHIA DI PRIORITÀ** (righe 10-23):
Il testo introduttivo "Le sezioni di questo prompt operano secondo la seguente gerarchia di priorità. In caso di conflitto tra sezioni, prevale sempre la sezione di livello superiore." compresso in una riga sola, mantenendo invariata la lista dei livelli.

**Passo R2 — STEP 3** (righe 650-652):
"Score di certezza esistenza / vigenza / pertinenza" compresso da 3 righe a 1 riga con slash.

**Sezioni ITER PROCEDIMENTALE** (blocco 2):
Rimossa la frase introduttiva ridondante sul chain-of-thought e sulla regola di emissione (già specificate a inizio blocco per tutti i blocchi). Il testo operativo di ciascun sotto-punto è stato mantenuto invariato.

**Formato Output — intestazione** (righe 1396-1407):
Il doppio paragrafo "INCLUDI SEMPRE TUTTE LE SEZIONI" ridotto a un unico paragrafo (il contenuto del secondo era ridondante rispetto al primo e rispetto a REGOLA 4 e DIVIETO 5 già presenti).

**Sezione GESTIONE CONVERSAZIONE MULTI-TURNO**:
Le intestazioni di ciascun caso (RICHIESTA DI CHIARIMENTO, VERSIONE AGGIORNATA, ecc.) mantenute; il testo introduttivo "Se l'utente, dopo aver ricevuto un report, invia un messaggio successivo, valuta la natura del messaggio:" compresso su una sola riga.

### 5. OTTIMIZZAZIONE FORMALE

- Righe vuote consecutive ridotte a massimo 1 tra sezioni.
- Separatori `---` mantenuti solo dove presenti nell'originale (strutturali).
- Nessun commento interno rimosso (non ve ne erano).

---

## Invarianti confermati

- Modulo di Protezione (Livello 0): invariato, parola per parola
- Tutte le risposte standard (deflection, errori input, avvertenze): invariate
- Template di output (FORMATO OUTPUT): invariato
- Tutti e 6 gli esempi di calibrazione: invariati
- Knowledge Base normativa: invariata (rimossa solo la duplicazione del trigger ligure)
- Checklist pre-output (10 voci): invariata
- Dashboard Metriche: invariata
- Tutti i valori soglia numerici (score 85, 60, 40): invariati
- Tutte le definizioni livelli di impatto: invariate
- Logica di determinazione esito: invariata
- Tabella norme obbligatorie per tipo atto: invariata
- Tabella soglie appalti: invariata
- Gerarchia di priorità (3 livelli): invariata

---

## Informazioni operative rimosse

**Zero.** Nessuna regola, vincolo, soglia, template, esempio o sezione di protezione è stato rimosso o alterato nel significato operativo.
