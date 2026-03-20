# COMPRESSION REPORT — ComuneSegreteriaGenerale v.1.0 → v.1.01

## Metriche di riduzione

| Metrica | v.1.0 | v.1.01 | Riduzione |
|---------|-------|--------|-----------|
| Righe | 1412 | 1322 | −90 righe (−6,4%) |
| Byte | 63.441 | 59.043 | −4.398 byte (−6,9%) |

Nota: il file originale è prevalentemente non ridondante e ben strutturato. La riduzione è conservativa per rispettare il vincolo di zero perdita di informazione operativa. Il Golden Sample (circa 215 righe) è intoccabile e non comprimibile in quanto esempio funzionale.

---

## Operazioni applicate

### 1. RIMOZIONE RIDONDANZE CONCETTUALI

**Soglie scoring duplicate (SISTEMA DI CONSISTENZA + CoT intro)**
- Il SISTEMA DI CONSISTENZA definisce le soglie HIGH/MEDIUM/LOW con la nota "I singoli Passi possono definire sotto-fasce; in caso di dubbio le soglie generali prevalgono."
- Nella sezione CoT il testo ripeteva: "I singoli Passi del CoT (1-5) possono definire sotto-fasce specifiche all'interno di queste categorie (es. MEDIUM con indicazione 'procedi con placeholder' vs. 'chiedi chiarimento'). In caso di dubbio, le soglie generali qui definite prevalgono." — rimosso dalla sezione di introduzione al CoT, mantenuto solo nel SISTEMA DI CONSISTENZA.

**Nota globale "includi TUTTE le sezioni" nel catalogo atti**
- Ogni voce del catalogo (tipi 1, 2, 3, 5, 7, 17, 18) ripeteva esplicitamente "(includi TUTTE le sezioni, anche se una sezione contiene solo N/A o placeholder)".
- Consolidato in un'unica nota globale all'apertura del CATALOGO ATTI ORDINARI, con rimando a VN-06. Rimosso da ogni singola voce.

**Regola di Redazione 11 ridondante con VN-06**
- Regola 11 ripeteva esattamente il concetto di VN-06 (non omettere sezioni). Mantenuta in posizione ma resa concisa; il testo duplicato è stato eliminato.

**Identità e Ruolo — definizione "bozza pronta per revisione"**
- Originale: due paragrafi separati. Compattato in un unico blocco mantenendo tutti gli elementi.

### 2. ELIMINAZIONE RIPETIZIONI TESTUALI

**Avvertenza RC4 in Regola Critica 4 vs. avvertenza ATTENZIONE REDATTORE**
- La nota standard di RC4 ("Verificare che i riferimenti normativi citati...") era scritta per esteso sia in RC4 che nella sezione OUTPUT (sezione 2a). Mantenuta in entrambi i punti (obbligatorio per funzionamento), ma il testo introduttivo in RC4 è stato ridotto eliminando la ripetizione del concetto già espresso nel SISTEMA DI CONSISTENZA.

**GESTIONE CONVERSAZIONE MULTI-TURN**
- Tre casi (modifica atto, secondo atto, dati aggiuntivi) erano espressi con paragrafi prolissi. Compattati mantenendo tutte le regole operative. Eliminata la lista di esempi di modifiche nel testo principale (es. "cambia l'importo", "aggiungi un visto", "togli la clausola") che fungevano da illustrazione non operativa.

**RC2 — Formula di rifiuto**
- La formula era scritta due volte nella sezione RC2 (una volta come definizione, una volta come "formula da usare"). Unificata in un'unica occorrenza.

**VN-03 — Rinforzo "non considerare urgenza implicita"**
- Identico concetto già espresso in RC1/VN-03 e ripetuto anche nella scheda Tipo 2 del catalogo. La scheda Tipo 2 mantiene la nota operativa (necessaria per la generazione), il rinforzo ridondante in VN-03 è stato rimosso.

### 3. COMPATTAZIONE TABELLE

Nessuna tabella compattabile identificata: tutte le tabelle presenti sono nel Golden Sample (intoccabile) o hanno colonne con valori distinti.

### 4. SEMPLIFICAZIONE STRUTTURE VERBOSE

**GESTIONE INPUT ANOMALI**
- Il punto relativo a "input in lingua diversa" conteneva un paragrafo introduttivo ("Input in lingua diversa dall'italiano") con formula di risposta estesa. Reso più conciso mantenendo la formula di risposta invariata.
- Il punto "input fuori dominio" aveva due frasi ridondanti ("applica RC2" + richiamo esplicito al catalogo). Ridotto a "applica RC2."

**RC2 — Esempi di applicazione**
- Scenario B (ambiguo al confine) aveva una spiegazione a due passi ridondante ("verifica → sì → score sale → procede. Se il dubbio persiste, applica RC3"). Mantenuta la logica, eliminato il passaggio intermedio verboso.

**CoT — Passo 3 — lista campi critici**
- La nota sui pareri art. 49 aveva un doppio riferimento a "Regola di Redazione 10 per biforcazione spesa/non-spesa". Mantenuto uno solo.

**Sezione GESTIONE AMBIGUITÀ SCORING**
- Il testo originale aveva "Se informazione mancante per calcolare uno score" e poi "Se due score si contraddicono" espressi in forma di paragrafo. Compattati in forma di lista già strutturata (invariata funzionalmente).

### 5. OTTIMIZZAZIONE FORMALE

- Eliminate tutte le righe vuote consecutive superiori a 1 (numerose occorrenze tra sezioni).
- Rimosso il separatore decorativo ridondante tra Golden Sample input e intestazione del testo atto (era presente una riga `---` non strutturale aggiuntiva).
- La versione nel titolo e metadata è aggiornata da v.1.0 a v.1.01 come richiesto.

---

## Vincoli verificati

- **Zero perdita di informazione operativa**: tutte le regole, vincoli, soglie, placeholder, formule di risposta, strutture di output e logiche di biforcazione sono presenti e invariate.
- **Sezioni anti-leak/protezione (L1-L4)**: intoccate, testo identico all'originale.
- **Template di output (SEZIONE 1 e SEZIONE 2)**: identici all'originale, incluse le box con bordi ASCII.
- **Golden Sample**: intoccato, testo identico all'originale.
- **Gerarchia heading**: invariata (H1 → H2 → H3 → testo).
- **Esempi funzionali**: tutti mantenuti (disambiguazione Tipo 4, Tipo 7, RC2 scenari A/B/C, VN-02, VN-03, Tipo 16 soglie preventivi, Tipo 18 stand-still, contraddizione affidamento diretto).
- **Copyright e metadata**: invariati ("(c)2026 Aviolab AI").
