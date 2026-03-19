# DEPLOY SCORING REPORT — Suite Comunale v.1.0

**Data**: 2026-03-19 (valutazione definitiva)
**Valutatore**: Claude Opus 4.6
**Metodo**: lettura integrale di ciascun deploy di produzione
**Revisione**: quarta e ultima valutazione — tutti i golden sample inseriti, header max 7 righe

---

## Legenda dimensioni

| Sigla | Dimensione | Cosa misura |
|:-----:|------------|-------------|
| H | Header | Conformita TTR-SUITE (riga 1-7, dichiarazione max 7 righe) |
| D | Dominio | KB normativa, catalogo atti, regole, perimetro |
| A | Anti-leak | Protezione multi-livello contro estrazione prompt |
| C | CoT/Scoring | Chain-of-thought, scoring numerico, soglie, self-check |
| K | Calibrazione | Golden sample, esempi con CoT in azione |
| O | Output | Template fisso, dashboard, footer, OUTPUT QUALIFICATION |
| R | Robustezza | Edge case, input anomali, cap loop, vincoli assoluti |
| E | Efficienza | Token economy, rapporto segnale/rumore |

**Scala**: 1-3 insufficiente, 4-5 sufficiente, 6-7 buono, 8-9 ottimo, 10 perfetto

---

## Classifica generale

| # | Prompt | H | D | A | C | K | O | R | E | Media | Tipo |
|--:|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-----:|------|
| 1 | REVISORE-CORE | 9 | 9 | 10 | 10 | 10 | 10 | 10 | 6 | **9.3** | Revisore |
| 2 | RAGIONERIA-SERV-FIN | 9 | 10 | 9 | 10 | 9 | 10 | 9 | 6 | **9.0** | Area |
| 3 | SERVIZI-DEMOGRAFICI | 9 | 9 | 9 | 10 | 10 | 9 | 9 | 7 | **9.0** | Area |
| 4 | REVISORE-POLIZIA-MUN | 9 | 9 | 10 | 9 | 9 | 9 | 9 | 7 | **8.9** | Revisore |
| 5 | POLIZIA-MUNICIPALE | 9 | 9 | 8 | 9 | 10 | 9 | 9 | 7 | **8.8** | Area |
| 6 | SEGRETERIA-GENERALE | 9 | 9 | 9 | 9 | 9 | 9 | 9 | 7 | **8.8** | Area |
| 7 | SERVIZI-SOCIALI | 9 | 9 | 10 | 9 | 8 | 9 | 9 | 7 | **8.8** | Area |
| 8 | REVISORE-DEMOGRAFICI | 9 | 10 | 8 | 9 | 9 | 10 | 9 | 6 | **8.8** | Revisore |
| 9 | UFFICIO-TECNICO | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 7 | **8.6** | Area |
| 10 | REVISORE-PERSONALE | 9 | 9 | 9 | 9 | 8 | 9 | 9 | 7 | **8.6** | Revisore |
| 11 | REVISORE-UFFICIO-TEC | 9 | 9 | 9 | 9 | 8 | 8 | 9 | 7 | **8.5** | Revisore |
| 12 | PERSONALE-RISORSE-UMANE | 9 | 9 | 9 | 8 | 8 | 9 | 9 | 7 | **8.5** | Area |
| 13 | ISTRUZIONE-CULTURA | 9 | 9 | 7 | 9 | 9 | 9 | 8 | 7 | **8.4** | Area |
| 14 | REVISORE-SERVIZI-SOC | 9 | 9 | 8 | 9 | 8 | 9 | 9 | 6 | **8.4** | Revisore |
| 15 | REVISORE-ISTR-CULTURA | 9 | 8 | 7 | 8 | 9 | 8 | 8 | 7 | **8.0** | Revisore |
| 16 | REVISORE-RAGIONERIA | 9 | 9 | 8 | 7 | 9 | 8 | 8 | 7 | **8.1** | Revisore |
| 17 | REVISORE-SEG-GEN | 9 | 9 | 8 | 8 | 7 | 9 | 9 | 6 | **8.1** | Revisore |

**Media suite: 8.6/10**
**Mediana: 8.6/10**
**Range: 8.0 — 9.3**

---

## Giudizi individuali

### 1. REVISORE-CORE — 9.3/10

Il prompt con la piu alta qualita ingegneristica. Modulo di Protezione a Livello 0 con gerarchia esplicita (L0 > L1 > L2), pattern di estrazione tassonomicamente classificati, catch-all basato su effetto potenziale della risposta. CoT a 6 step forzato con scoring 0-100 su 4 categorie, checklist pre-output a 10 voci, retry cap 3 tentativi, dashboard metriche. Golden sample eccezionale: 4 esempi completi (APPROVATO, DA RIVEDERE con report, CON RISERVE, privacy) con ragionamento R1-R6. Gestione input a 7 casi (A-G). Procedura revisione a 5 blocchi con tabella soglie-procedura. Unico punto debole: lunghezza (~28K token).

### 2. RAGIONERIA-SERVIZIO-FINANZIARIO — 9.0/10

Il sistema di scoring piu sofisticato della suite. Layer FCS con 6 decisioni classificatorie D1-D6, formula confidenza esplicita, dashboard con soglia 70% per produzione atto, mappatura confidenza-affidabilita ALTO/MEDIO. Catalogo 20 voci con distinzione RAMO A/B e codifica bilancio D.Lgs. 118/2011. Attestazione copertura a 7 elementi obbligatori. Cinque esempi calibrazione (liquidazione, ambiguo, ingiunzione RAMO B, CANNOT SCORE, trigger Liguria). Anti-leak a 5 livelli con principio "in dubio pro protezione". Footer autenticazione con livello affidabilita.

### 3. SERVIZI-DEMOGRAFICI — 9.0/10

Il prompt piu strutturato del lotto. Indice esplicito a 12 sezioni con scopo dichiarato per ciascuna. CoT a 6 passi con fail-safe dedicato per stato civile (soglia < 70 blocco). Micro-loop SCORING-STEP 1-6. INPUT-GATE 1-5 e 4-BIS. Golden sample eccezionale con input realistico, output completo con ATTENZIONE REDATTORE, e report revisione punto per punto. Graceful degradation con sezioni interrotte e motivate. KB normativa specifica (DPR 223/1989, DPR 396/2000, ANPR, AIRE, immigrazione).

### 4. REVISORE-POLIZIA-MUNICIPALE — 8.9/10

Anti-leak a 5 livelli espliciti con DEFLECTION_STANDARD, catch-all e encoding resistance — la migliore implementazione tra i revisori. Dominio eccezionale: ordinanze viabilita (4 elementi), art. 54 TUEL (ordinaria/contingibile), verbali CdS, ingiunzioni, atti misti. CoT forzato a 6 step con 3 scale scoring indipendenti. Due golden sample con ragionamento esplicito, decisioni non ovvie documentate. Lunghezza elevata (~75KB).

### 5. POLIZIA-MUNICIPALE — 8.8/10

Catalogo 15 voci (viabilita, sicurezza urbana, verbali CdS, comunicazioni giudiziarie, polizia commerciale). CoT a 6 passi con scoring su perimetro, univocita, criticita campi, certezza norme. Tre golden sample completi: ambiguita competenza, dati parziali appalto, comunicazione notizia di reato con draft integrale e linguaggio fattuale verificato. Robustezza con coppie ambigue, cap 3 cicli, gestione confine perimetro.

### 6. SEGRETERIA-GENERALE — 8.8/10

Catalogo 18 atti (il piu ampio delle aree). KB normativa completa (TUEL, L.241/90, D.Lgs. 36/2023, normativa Liguria). CoT a 6 passi con scoring e dashboard. Golden sample completo con output agente e output revisore normativo — dimostra il ciclo completo. Scenari A/B/C di certezza normativa forniscono calibrazione operativa eccellente. 10 vincoli negativi VN-01/VN-10.

### 7. SERVIZI-SOCIALI — 8.8/10

Protezione PROT-1/PROT-5 centralizzata — la migliore architettura anti-leak tra le aree. MCU con scala invertita per rischio privacy, auto-verifica MCU-3 a 7 check PASS/FAIL. Schema output tripartito A/B/C (Pubblico/Riservato) gold standard per atti con dati sensibili. Golden sample con output documento pubblico, allegato riservato e report revisore. Dominio forte: ETS/RUNTS, co-progettazione, segnalazioni giudiziarie, housing, 0-6.

### 8. REVISORE-DEMOGRAFICI — 8.8/10

Dominio eccezionalmente dettagliato: DPR 223/1989 con articoli specifici, DPR 396/2000 stato civile con principio fidefacenza, ANPR, AIRE, immigrazione. Tabella score per controllo con criteri deterministici. Matrice selezione controlli per tipo atto. Golden sample completo (iscrizione anagrafica straniero) con tutti gli score e motivazioni. CoT con SCA (Score Complessivo Atto) e criteri esito numerici.

### 9. UFFICIO-TECNICO — 8.6/10

18 voci catalogo (edilizia + urbanistica + appalti). CoT a 7 passi con Passo 5 dedicato a vincoli paesaggistici/idrogeologici/sismici. Scoring con formula matematica (Score x 0.95/0.90 per fascia). Protezione sistema consolidata. Golden sample adeguato ma potrebbe mostrare piu esplicitamente il CoT con score. Output a 5 sezioni con Sez. 0 Verifica Pre-Output.

### 10. REVISORE-PERSONALE — 8.6/10

Anti-leak PROTEZIONE-1 a PROTEZIONE-5 con deflection standard. Sistema SCU con 5 componenti e regola anti-upgrade numerica. Dominio eccellente: incarichi art. 7 co.6 TUPI (test 4 criteri), disciplinari con 3 termini perentori, concorsi GU/InPA, PO, progressioni. Un golden sample completo (incarico avvocato APPROVATO CON RISERVE) — manca copertura degli altri esiti.

### 11. REVISORE-UFFICIO-TECNICO — 8.5/10

KB normativa UTC ricca (DPR 380, D.Lgs. 36/2023, NTC, VAS/VIA, L.R. Liguria). 15 controlli specifici con scoring numerico, tiebreak ancorato, Regola Asimmetria Errori. Anti-leak L1-L4 completo. Golden sample con report revisione reale. Qualche ridondanza nelle sezioni di scoring.

### 12. PERSONALE-RISORSE-UMANE — 8.5/10

16 voci catalogo con normativa TUPI/CCNL/DPR 487 dettagliata. Anti-leak a 4 livelli con gerarchia priorita. CoT a 7 passi con classificazione campi input C/B/A e gestione ambiguita a 3 cicli. Due esempi calibrazione (ambiguo + parziale) ma mancano edge case piu complessi. Output a 5 sezioni con Dashboard Consistenza.

### 13. ISTRUZIONE-CULTURA — 8.4/10

Dominio solido con catalogo 17 atti, soglia educativa EUR 750.000 vs ordinaria. Scoring su 3 domini con CoT a 6 step. Golden sample completo (489 righe) con 5 esempi incluso ragionamento e output. Anti-leak su 2 livelli: adeguato ma meno stratificato dei migliori (manca encoding/catch-all esplicito).

### 14. REVISORE-SERVIZI-SOCIALI — 8.4/10

Framework SC piu avanzato e modulare: SC-1 a SC-5, SCORE-REF centralizzata con 40+ codici. Anti-leak distribuito in 3 punti con nota architetturale. KB forte: L. 328/2000, D.Lgs. 117/2017, RUNTS, co-progettazione. Golden sample completo (determina contributo EUR 600) ma calibration example 1 e 2 sono placeholder. 7 vincoli negativi. Privacy differenziata con/senza beneficiario.

### 15. REVISORE-RAGIONERIA — 8.1/10

KB specifica per bilancio armonizzato, FPV, variazioni bilancio con routing assenza/errore. Tre golden sample eccellenti (RISERVE, DA RIVEDERE, APPROVATO) con output completi. Anti-leak solida ma non stratificata. CoT meno formalizzato: assente framework SC/SCU codificato. Scoring basato su IMPATTO senza valori numerici espliciti nelle sezioni operative.

### 16. REVISORE-SEGRETERIA-GENERALE — 8.1/10

Perimetro piu ampio dei revisori: 14 controlli. Quorum, competenza organo, accesso atti 3 tipologie, decreti Sindaco, anticorruzione, responsabile procedimento. CoT SC con scala invertita (score alto = anomalia grave) — rischio confusione cross-agente. Un golden sample dettagliato ma manca copertura esiti negativi.

### 17. REVISORE-ISTRUZIONE-CULTURA — 8.0/10

9 sotto-tipi (refezione, tariffe, graduatorie, nido, biblioteche, sport). Soglie educativi EUR 750k calibrate. Tre golden sample che coprono tutti e 3 gli esiti (APPROVATO, DA RIVEDERE, RISERVE) con output e dashboard. CoT a 6 step con scoring ternario semplificato (0/50/100) — perde granularita rispetto alla scala 0-100. Anti-leak essenziale, meno stratificato.

---

## Analisi per dimensione

| Dimensione | Media | Min | Max | Note |
|------------|:-----:|:---:|:---:|------|
| Header | 9.0 | 9 | 9 | Conforme ovunque con soglia 7 righe |
| Dominio | 9.1 | 8 | 10 | KB normative solide, top: Ragioneria e Demografici |
| Anti-leak | 8.6 | 7 | 10 | Top: Revisore Core (10), Revisore PM (10), Servizi Sociali (10) |
| CoT/Scoring | 8.9 | 7 | 10 | Top: Revisore Core, Ragioneria, Servizi Demografici (10) |
| Calibrazione | 8.7 | 7 | 10 | Migliorata significativamente con inserimento golden sample |
| Output | 9.0 | 8 | 10 | Template strutturati ovunque |
| Robustezza | 8.9 | 8 | 10 | Gestione edge case generalmente buona |
| Efficienza | 6.7 | 6 | 7 | Punto debole sistemico: prompt 45-84KB |

---

## Distribuzione qualita

| Fascia | Prompt | Conteggio |
|--------|--------|:---------:|
| Eccellente (9.0+) | Revisore Core, Ragioneria, Servizi Demografici | 3 |
| Ottimo (8.5-8.9) | Revisore PM, Polizia Mun, Segreteria Gen, Servizi Sociali, Rev Demografici, Ufficio Tec, Rev Personale, Rev UT, Personale RU | 9 |
| Buono (8.0-8.4) | Istruzione Cultura, Rev Servizi Soc, Rev Istr Cultura, Rev Ragioneria, Rev Seg Gen | 5 |

Tutti i 17 prompt sono sopra 8.0 — **nessuno sotto la soglia di produzione**.

---

## Raccomandazioni

1. **Efficienza** (media 6.7): unico punto debole sistemico. Un passo di compressione post-pipeline (rimozione ridondanze, compattazione tabelle) potrebbe ridurre i token del 15-25% senza perdita funzionale.

2. **Anti-leak** (A:7 su 2 prompt): ISTRUZIONE-CULTURA e REVISORE-ISTR-CULTURA beneficerebbero di una riesecuzione ALK con il nuovo template a 5 livelli strutturati.

3. **CoT/Scoring** (C:7 su 2 prompt): REVISORE-RAGIONERIA e REVISORE-SEG-GEN hanno CoT meno formalizzato o scala invertita. Margine di miglioramento con standardizzazione framework SC.
