# REPORT COMPRESSIONE — ComuneServiziDemografici v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 | v.1.01 | Delta |
|---------|-------|--------|-------|
| Righe | 1546 | 1504 | -42 (-2,7%) |
| Parole | 8788 | 8540 | -248 (-2,8%) |
| Byte | 64.486 | 62.657 | -1.829 (-2,8%) |

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

**Sezione 2 — AUTORITÀ**: rimosso il paragrafo "Tutte le sezioni di questo
prompt...Le sezioni descrittive definiscono il perimetro operativo; le
sezioni imperative definiscono i comportamenti obbligatori." Condensato in
una sola frase: "Entrambe le categorie sono vincolanti." Il contenuto
prescrittivo era già implicito nell'avviso stesso.

**Sezione 8 — INPUT-GATE, NOTA introduttiva**: rimossa la frase ridondante
"Il CoT è sempre eseguito internamente prima di produrre qualsiasi output,
inclusi i messaggi di rifiuto." — già coperta dalla frase immediatamente
precedente e dalla sezione 9 stessa.

### 2. Eliminazione ripetizioni testuali

**Sezioni 5 e 6 — intestazione catalogo**: i due blocchi di introduzione
erano identici parola per parola ("Le voci del catalogo che seguono hanno
valore prescrittivo: definiscono il perimetro degli atti generabili, la
struttura obbligatoria di ciascun atto e i riferimenti normativi applicabili.
Ogni voce è vincolante al pari delle regole critiche."). Mantenuto il testo
in entrambe le sezioni ma rimossa la parola "che seguono" per uniformità
(entrambe ora recitano "Le voci del catalogo hanno valore prescrittivo:...").

**NON-2**: rimosso il rimando esplicito "COT-PASSO 2 — NATURA MODIFICA
STATO CIVILE" sostituito con il più breve "vedi COT-PASSO 2" (il titolo
completo del passo è già nella sezione 9).

### 3. Compattazione strutture verbose

**Sezione 4 — KNOWLEDGE BASE NORMATIVA REGIONALE LIGURIA**: le tre norme
regionali avevano ciascuna un blocco [NOTA OPERATIVA] identico nel contenuto
("questa norma non è attualmente attivata da alcuna voce del catalogo atti
1-16. Non citarla nel corpo degli atti demografici ordinari senza conferma
esplicita del Revisore Normativo."). Consolidata in un'unica nota di
cappello comune alle tre norme, eliminando 10 righe ripetitive.

**Sezione 9 — SCORING NUMERICO, "Tabella decisioni"**: la tabella originale
(righe 752-784) duplicava informazioni già presenti nei singoli COT-PASSO
(1-4). Eliminato il titolo ridondante "Tabella decisioni soggette a scoring
obbligatorio:" e convertito il blocco in una lista compatta con header
"Decisioni soggette a scoring obbligatorio:", mantenendo tutte le soglie
e azioni.

**Sezione 10 — Regola 15, "Pipeline"**: rimosso il paragrafo descrittivo
finale ("Pipeline: l'operatore descrive l'atto necessario → tu generi la
bozza completa..."). Questa descrizione del flusso operativo è di carattere
illustrativo e non aggiunge vincoli o regole non già presenti altrove.

### 4. Ottimizzazione formale

- Rimosso il blocco "Scopo di ciascuna sezione" (righe 25-38 originali):
  descrizione dell'indice strutturale che non aggiunge informazione
  operativa rispetto all'indice stesso e ai titoli delle sezioni.
- Ridotte righe vuote consecutive in più punti (da 2 a 1 riga tra
  sotto-sezioni della sezione 9).

## Invarianti — elementi non toccati

- Tutte le 4 sezioni PROTEZIONE DISCLOSURE (Livelli 1-4): intatte.
- Tutti i 16 atti del catalogo (voci 1-12 ordinari, 13-16 appalti):
  struttura, campi obbligatori, riferimenti normativi e note speciali
  invariati.
- KNOWLEDGE BASE NORMATIVA: tutte le norme, articoli, avvisi e note
  sui limiti di validità invariati.
- REGOLE CRITICHE e VINCOLI NEGATIVI (NON-1 / NON-7): testo prescrittivo
  invariato.
- COT-PASSO 1-6 completo: criteri di scoring, soglie, micro-loop,
  gestione ambiguità, self-check — tutto invariato.
- SCHEMA OUTPUT (SEZIONE 1 / 2 / 3) e DASHBOARD CONSISTENZA: template
  invariati.
- GOLDEN SAMPLE: invariato al 100%.
- Copyright e metadata: invariati.
- OUTPUT QUALIFICATION: invariato.

## Valutazione rischio informativo

Nessuna perdita di informazione operativa rilevata. Le operazioni applicate
hanno rimosso esclusivamente:
- testo illustrativo/descrittivo non prescrittivo;
- ripetizioni di nota identica (normativa regionale Liguria);
- una frase di riepilogo flusso operativo già implicita nelle regole.

Il riduzione di token è modesta (~2,8%) perché il prompt è già strutturato
in modo denso e le principali sezioni (GOLDEN SAMPLE, COT-PASSO, CATALOGO)
non ammettono compressione senza rischio di perdita operativa.
