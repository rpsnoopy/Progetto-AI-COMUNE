# Suite Agenti IA — Comune italiano < 5.000 abitanti

**Secondo esperimento — 13 marzo 2026**

Suite completa di system prompt per agenti IA destinati alla redazione assistita di atti amministrativi comunali e alla loro revisione normativa automatica.

Comune di riferimento per i golden sample: **Pieve Ligure (GE)**.

## Architettura

```
Utente (operatore comunale)
  │
  ▼
Agente di Area  ──genera bozza atto──►  Revisore Normativo  ──report──►  Operatore firma
  (8 agenti)                              (Core + 8 specifici)
```

L'operatore fornisce tipo atto, oggetto e dati disponibili. L'agente di area produce una bozza formale con placeholder `[DATO MANCANTE]` per i campi non forniti. Il revisore normativo analizza autonomamente l'atto e produce un report strutturato (APPROVATO / APPROVATO CON RISERVE / DA RIVEDERE). L'operatore completa i placeholder, applica eventuali correzioni e firma.

## Contenuto della directory (25 file)

### Prompt Agenti di Area (8)

| File | Area | Atti coperti |
|------|------|-------------|
| `AREA 1 — SEGRETERIA GENERALE.md` | Segreteria, Affari Generali | Delibere CC/GC, decreti Sindaco, determine, regolamenti, accesso atti, convocazioni |
| `AREA 2 — SERVIZI SOCIALI.md` | Servizi Sociali, Terzo Settore | Contributi assistenziali, rette RSA, segnalazioni TM, co-progettazione ETS, SAD |
| `AREA 3 — UFFICIO TECNICO.md` | Lavori Pubblici, Urbanistica, Edilizia | Permessi di costruire, SCIA, determine lavori, ordinanze sicurezza, collaudi |
| `AREA 4 — RAGIONERIA - SERVIZIO FINANZIARIO.md` | Bilancio, Tributi, Contabilita | Liquidazioni, variazioni bilancio, equilibri, rendiconto, pareri contabili |
| `AREA 5 — SERVIZI DEMOGRAFICI.md` | Anagrafe, Stato Civile, Elettorale | Iscrizioni/cancellazioni anagrafiche, matrimoni, cittadinanza, liste elettorali |
| `AREA 6 — PERSONALE - RISORSE UMANE.md` | Personale, Organizzazione | Assunzioni, progressioni, incarichi, mobilita, fondo risorse decentrate |
| `AREA 7 — POLIZIA MUNICIPALE.md` | Viabilita, Sicurezza urbana | Ordinanze viabilita, verbali CdS, autorizzazioni OSP, ingiunzioni, notizie di reato |
| `AREA 8 — ISTRUZIONE - CULTURA.md` | Scuola, Cultura, Sport | Nidi, mense, trasporto scolastico, biblioteche, concessioni spazi, manifestazioni |

### Revisori Normativi (9)

| File | Ruolo |
|------|-------|
| `REVISORE CORE.md` | Revisore trasversale — controlli comuni a tutti gli atti (TUEL, L. 241/90, D.Lgs. 33/2013, D.Lgs. 36/2023) |
| `REVISORE SEGRETERIA GENERALE.md` | Controlli specifici Segreteria + golden sample revisore |
| `REVISORE SERVIZI SOCIALI.md` | Controlli specifici Servizi Sociali (privacy, ETS, RUNTS) + golden sample |
| `REVISORE UFFICIO TECNICO.md` | Controlli specifici UTC (DPR 380, SCIA, collaudi) + golden sample |
| `REVISORE RAGIONERIA.md` | Controlli specifici Ragioneria (bilancio armonizzato, pareri contabili) + golden sample |
| `REVISORE DEMOGRAFICI.md` | Controlli specifici Demografici (DPR 223, stato civile) + golden sample |
| `REVISORE PERSONALE.md` | Controlli specifici Personale (CCNL, D.Lgs. 165/2001) + golden sample |
| `REVISORE POLIZIA MUNICIPALE.md` | Controlli specifici PM (CdS, TULPS, art. 54 TUEL) + golden sample |
| `REVISORE ISTRUZIONE - CULTURA.md` | Controlli specifici Istruzione (D.Lgs. 65/2017, soglia 750K) + golden sample |

### Golden Sample (8)

Ogni file contiene un esempio completo della pipeline: input utente, output agente (bozza atto), output revisore (report di revisione).

| File | Scenario | Esito revisore |
|------|----------|---------------|
| `GOLDEN SAMPLE — AREA 1 — SEGRETERIA GENERALE.md` | Delibera GC procedura negoziata refezione scolastica, 120.000 EUR | APPROVATO |
| `GOLDEN SAMPLE — AREA 2 — SERVIZI SOCIALI.md` | Determina affidamento diretto SAD, 25.000 EUR + allegato riservato | APPROVATO |
| `GOLDEN SAMPLE — AREA 3 — UFFICIO TECNICO.md` | Determina affidamento diretto manutenzione strade, 80.000 EUR | APPROVATO CON RISERVE |
| `GOLDEN SAMPLE — AREA 4 — RAGIONERIA - SERVIZIO FINANZIARIO.md` | Determina liquidazione fattura verde pubblico, 8.500 EUR | APPROVATO CON RISERVE |
| `GOLDEN SAMPLE — AREA 5 — SERVIZI DEMOGRAFICI.md` | Iscrizione anagrafica cittadino straniero | APPROVATO |
| `GOLDEN SAMPLE — AREA 6 — PERSONALE - RISORSE UMANE.md` | Determina incarico avvocato esterno, 4.500 EUR | APPROVATO CON RISERVE |
| `GOLDEN SAMPLE — AREA 7 — POLIZIA MUNICIPALE.md` | Ordinanza viabilita temporanea per lavori stradali | APPROVATO |
| `GOLDEN SAMPLE — AREA 8 — ISTRUZIONE - CULTURA.md` | Delibera GC affidamento diretto refezione, 180.000 EUR (soglia 750K) | APPROVATO |

## Struttura dei golden sample

```
## INPUT
Descrizione dello scenario in linguaggio naturale.

## OUTPUT AGENTE — Testo Atto
Blocco ATTENZIONE REDATTORE + bozza atto completa con [DATO MANCANTE].

## OUTPUT REVISORE NORMATIVO
Report strutturato: anomalie normative, iter, appalti, privacy, coerenza, azione richiesta.
```

## Normativa di riferimento principale

- **TUEL**: D.Lgs. 18 agosto 2000, n. 267
- **Procedimento amministrativo**: L. 7 agosto 1990, n. 241
- **Trasparenza**: D.Lgs. 14 marzo 2013, n. 33
- **Codice Contratti Pubblici**: D.Lgs. 31 marzo 2023, n. 36
- **GDPR**: Reg. UE 2016/679
- **Codice Terzo Settore**: D.Lgs. 3 luglio 2017, n. 117
- **Normativa regionale**: L.R. Liguria 12/2006, 19/2017, 19/2020

## Comportamenti comuni a tutti gli agenti

- Placeholder `[DATO MANCANTE: descrizione]` per ogni campo non fornito
- Placeholder `[CIG: DA RICHIEDERE]` se CIG assente
- Blocco **ATTENZIONE REDATTORE** obbligatorio se ambiguita o dati mancanti
- Mai inventare numeri, nomi, importi, riferimenti normativi
- Max 3 domande all'utente, poi generare comunque con placeholder
- Citazione norme: prima occorrenza estesa, successive abbreviate
- Pareri art. 49 TUEL: promemoria obbligatorio in ogni delibera

## Note

- LLM utilizzato per la generazione: **Claude Opus 4.6**
- I golden sample dei revisori sono inclusi nei rispettivi file revisore (sezione GOLDEN SAMPLE in coda)
- I prompt non contengono dati reali: tutti gli esempi usano placeholder
- La suite e progettata per comuni < 5.000 abitanti con organizzazione per aree
