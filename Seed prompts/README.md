# Seed Prompts — Come sono stati generati

## Panoramica

I file contenuti in questa cartella sono **seed prompt**: system prompt funzionanti ma nella loro forma grezza, generati da Claude Opus 4.6 a partire dai **metaprompt** presenti nella cartella [`METAPROMPT AREA/`](../METAPROMPT%20AREA/). I seed prompt non sono destinati all'uso diretto in produzione: rappresentano la materia prima che viene successivamente raffinata attraverso **PromptForge** per diventare prompt industrialmente utilizzabili.

---

## Pipeline di generazione

```
 SUITE_COMUNALE_CONTESTO_v2.md          Metaprompt di Area/Revisore
 (contesto architetturale)              (istruzioni specifiche per Opus)
          │                                        │
          └──────────┐    ┌────────────────────────┘
                     ▼    ▼
               ┌─────────────────┐
               │  Claude Opus    │
               │  (generazione)  │
               └────────┬────────┘
                        ▼
               ┌─────────────────┐
               │  Seed Prompt    │  ← questa cartella
               │  (grezzo ma     │
               │   funzionante)  │
               └────────┬────────┘
                        ▼
               ┌─────────────────┐
               │  PromptForge    │
               │  (ottimizzazione│
               │   industriale)  │
               └────────┬────────┘
                        ▼
               ┌─────────────────┐
               │  Prompt finale  │
               │  (produzione)   │
               └─────────────────┘
```

---

## Step 1 — Il contesto: `SUITE_COMUNALE_CONTESTO_v2.md`

Il file [`METAPROMPT AREA/SUITE_COMUNALE_CONTESTO_v2.md`](../METAPROMPT%20AREA/SUITE_COMUNALE_CONTESTO_v2.md) e il documento fondamentale dell'intera suite. Contiene:

- **Architettura generale** della pipeline operativa (Agente di Area -> Revisore Normativo -> Operatore comunale)
- **Principi fondamentali** condivisi da tutti gli agenti (placeholder `[DATO MANCANTE]`, blocco `ATTENZIONE REDATTORE`, divieto di inventare dati)
- **Knowledge base stratificata** su 4 livelli:
  - Livello 1 — Core comune (TUEL, L. 241/90, D.Lgs. 33/2013) — 20%
  - Livello 2 — Appalti universali (D.Lgs. 36/2023) — 25%
  - Livello 3 — Specifica area (norme settoriali) — 45%
  - Livello 4 — Regionale Liguria — 10%
- **System prompt completi** per Segreteria Generale e Servizi Sociali (le prime due aree sviluppate)
- **System prompt del Revisore Normativo** trasversale
- **Golden sample** per Segreteria e Servizi Sociali (input -> output agente -> output revisore)
- **Template Master v2.0** (struttura da 130 righe da replicare per ogni nuova area)
- **Comandi pronti** per la generazione di ciascuna delle 6 aree rimanenti

Questo file viene **allegato come contesto** in ogni conversazione con Opus per la generazione dei seed prompt. Fornisce a Opus la conoscenza dell'architettura, le convenzioni obbligatorie e gli esempi concreti su cui basarsi.

---

## Step 2 — I metaprompt: istruzioni per Opus

Nella cartella [`METAPROMPT AREA/`](../METAPROMPT%20AREA/) sono presenti 17 metaprompt, uno per ciascun agente da generare. Ogni metaprompt e una **istruzione diretta a Claude Opus** che specifica:

### Metaprompt per Agenti di Area (8 file)

Formato tipico:

```
Allego il file SUITE_COMUNALE_CONTESTO_v2.md come contesto.

Genera il system prompt completo per l'Agente [NOME AREA]
usando il TEMPLATE MASTER v2.0 contenuto nel file allegato.

Normativa specifica area:
- [elenco norme settoriali]

Focus appalti:
[enfasi appalti per l'area]

Catalogo atti ordinari (almeno 10):
[elenco tipologie di atti]

Catalogo atti appalti (almeno 5):
[elenco atti specifici appalti]

Regole specifiche area:
- [regole operative particolari]

Genera anche il golden sample per:
[scenario di test specifico]
```

| Metaprompt | Normativa specifica | Focus appalti |
|---|---|---|
| `AREA 1 — SEGRETERIA GENERALE.md` | TUEL artt. 36-57, L. 241/90, D.Lgs. 33/2013, FOIA, anticorruzione | Gare sopra soglia, programmazione, centrali committenza |
| `AREA 2 — SERVIZI SOCIALI.md` | L. 328/2000, D.Lgs. 117/2017 (CTS), GDPR | ETS, cooperative sociali, co-progettazione |
| `AREA 3 — UFFICIO TECNICO.md` | DPR 380/2001, NTC 2018, D.Lgs. 152/2006 | Lavori manutenzione < 150.000 EUR |
| `AREA 4 — RAGIONERIA.md` | D.Lgs. 118/2011, TUEL Titolo VI | Liquidazioni, CIG in bilancio |
| `AREA 5 — SERVIZI DEMOGRAFICI.md` | DPR 223/1989, DPR 396/2000 | Forniture ufficio |
| `AREA 6 — PERSONALE.md` | D.Lgs. 165/2001, CCNL FL, DPR 487/1994 | POS, RUP interni, incarichi |
| `AREA 7 — POLIZIA MUNICIPALE.md` | D.Lgs. 285/1992 (CdS), TULPS, L. 65/1986 | Servizi sicurezza, noleggio veicoli |
| `AREA 8 — ISTRUZIONE - CULTURA.md` | D.Lgs. 65/2017, L. 107/2015, D.Lgs. 42/2004 | Refezione scolastica, trasporto alunni |

### Metaprompt per Revisori Normativi (9 file)

Il **Revisore Core** definisce i controlli trasversali (citazioni normative, iter, appalti, privacy, coerenza interna) con formato di output fisso. Ogni **Revisore di Area** estende il Core con controlli specifici per la normativa settoriale.

| Metaprompt | Controlli aggiuntivi |
|---|---|
| `REVISORE CORE.md` | Citazioni normative, iter, D.Lgs. 36/2023, privacy, coerenza |
| `REVISORE SEGRETERIA GENERALE.md` | Quorum CC/GC, competenze art. 42/48/107, FOIA vs documentale |
| `REVISORE SERVIZI SOCIALI.md` | Anonimizzazione, RUNTS, co-progettazione, allegato riservato |
| `REVISORE UFFICIO TECNICO.md` | DPR 380, SCIA, collaudi, sicurezza cantieri |
| `REVISORE RAGIONERIA.md` | Bilancio armonizzato, missioni/programmi, pareri contabili |
| `REVISORE DEMOGRAFICI.md` | DPR 223, stato civile, AIRE |
| `REVISORE PERSONALE.md` | CCNL, D.Lgs. 165/2001, dotazione organica |
| `REVISORE POLIZIA MUNICIPALE.md` | CdS, TULPS, art. 54 TUEL |
| `REVISORE ISTRUZIONE - CULTURA.md` | D.Lgs. 65/2017, soglia 750K servizi educativi |

---

## Step 3 — La generazione: da metaprompt a seed prompt

Per ogni area e revisore, il processo di generazione e stato:

1. Aprire una nuova conversazione con **Claude Opus 4.6**
2. **Allegare** il file `SUITE_COMUNALE_CONTESTO_v2.md` come contesto
3. **Incollare** il metaprompt dell'area o revisore corrispondente
4. Opus genera il **seed prompt completo** seguendo il Template Master v2.0

Opus utilizza il contesto allegato per:
- Rispettare l'architettura a pipeline (Agente -> Revisore -> Operatore)
- Applicare la knowledge base stratificata a 4 livelli
- Mantenere la struttura fissa del Template Master (~130 righe)
- Includere i comportamenti obbligatori (placeholder, blocco ATTENZIONE, max 3 domande)
- Generare il golden sample richiesto nel metaprompt

Il risultato sono i **25 file** presenti in questa cartella: 8 agenti di area, 9 revisori (1 core + 8 specifici), 8 golden sample.

---

## Step 4 — Da seed prompt a produzione: PromptForge

I seed prompt generati da Opus sono **funzionanti ma grezzi**. Contengono la logica corretta, la normativa pertinente e la struttura conforme al Template Master, ma non sono ottimizzati per l'uso industriale in termini di:

- Token efficiency (riduzione lunghezza senza perdere contenuto)
- Robustezza a input ambigui o malformati
- Consistenza del formato di output tra diverse invocazioni
- Gestione degli edge case

Per questo motivo, i seed prompt devono essere passati in **PromptForge**, che li trasforma in prompt production-ready: ottimizzati, testati e pronti per il deployment negli ambienti di produzione.

---

## Contenuto della cartella

### Agenti di Area (8)

| File | Area |
|---|---|
| `AREA 1 — SEGRETERIA GENERALE.md` | Segreteria, Affari Generali |
| `AREA 2 — SERVIZI SOCIALI.md` | Servizi Sociali, Terzo Settore |
| `AREA 3 — UFFICIO TECNICO.md` | Lavori Pubblici, Urbanistica, Edilizia |
| `AREA 4 — RAGIONERIA - SERVIZIO FINANZIARIO.md` | Bilancio, Tributi, Contabilita |
| `AREA 5 — SERVIZI DEMOGRAFICI.md` | Anagrafe, Stato Civile, Elettorale |
| `AREA 6 — PERSONALE - RISORSE UMANE.md` | Personale, Organizzazione |
| `AREA 7 — POLIZIA MUNICIPALE.md` | Viabilita, Sicurezza urbana |
| `AREA 8 — ISTRUZIONE - CULTURA.md` | Scuola, Cultura, Sport |

### Revisori Normativi (9)

| File | Ruolo |
|---|---|
| `REVISORE CORE.md` | Trasversale — controlli comuni a tutti gli atti |
| `REVISORE SEGRETERIA GENERALE.md` | Specifico Segreteria + golden sample revisore |
| `REVISORE SERVIZI SOCIALI.md` | Specifico Servizi Sociali + golden sample |
| `REVISORE UFFICIO TECNICO.md` | Specifico UTC + golden sample |
| `REVISORE RAGIONERIA.md` | Specifico Ragioneria + golden sample |
| `REVISORE DEMOGRAFICI.md` | Specifico Demografici + golden sample |
| `REVISORE PERSONALE.md` | Specifico Personale + golden sample |
| `REVISORE POLIZIA MUNICIPALE.md` | Specifico PM + golden sample |
| `REVISORE ISTRUZIONE - CULTURA.md` | Specifico Istruzione + golden sample |

### Golden Sample (8)

Ogni file contiene un esempio completo della pipeline: **input utente** -> **output agente** (bozza atto) -> **output revisore** (report di revisione).

| File | Scenario |
|---|---|
| `GOLDEN SAMPLE — AREA 1 — SEGRETERIA GENERALE.md` | Delibera GC procedura negoziata refezione, 120.000 EUR |
| `GOLDEN SAMPLE — AREA 2 — SERVIZI SOCIALI.md` | Determina affidamento diretto SAD, 25.000 EUR |
| `GOLDEN SAMPLE — AREA 3 — UFFICIO TECNICO.md` | Determina affidamento diretto manutenzione strade, 80.000 EUR |
| `GOLDEN SAMPLE — AREA 4 — RAGIONERIA.md` | Determina liquidazione fattura verde pubblico, 8.500 EUR |
| `GOLDEN SAMPLE — AREA 5 — SERVIZI DEMOGRAFICI.md` | Iscrizione anagrafica cittadino straniero |
| `GOLDEN SAMPLE — AREA 6 — PERSONALE.md` | Determina incarico avvocato esterno, 4.500 EUR |
| `GOLDEN SAMPLE — AREA 7 — POLIZIA MUNICIPALE.md` | Ordinanza viabilita temporanea per lavori stradali |
| `GOLDEN SAMPLE — AREA 8 — ISTRUZIONE - CULTURA.md` | Delibera GC affidamento diretto refezione, 180.000 EUR |

---

## Note tecniche

- **LLM utilizzato**: Claude Opus 4.6 (Anthropic)
- **Data generazione**: 13 marzo 2026
- **Target**: Comuni italiani < 5.000 abitanti
- **Comune di riferimento** nei golden sample: Pieve Ligure (GE)
- Nessun file contiene dati reali: tutti gli esempi usano placeholder `[DATO MANCANTE]`
