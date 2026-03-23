# Progetto AI COMUNE

Suite di agenti AI specializzati per la redazione, analisi, verifica, correzione e revisione di atti amministrativi destinati a **Comuni italiani con popolazione inferiore a 5.000 abitanti**.

Il progetto nasce dall'esigenza concreta di supportare gli operatori comunali — spesso soli o in organici ridottissimi — nella produzione di atti formalmente corretti, normativamente fondati e strutturalmente completi.

---

## Architettura

La suite opera con una **pipeline a due stadi**:

```
Operatore comunale
       │
       ▼
┌──────────────────┐     ┌──────────────────┐
│  Agente di Area  │────▶│ Revisore Normativo│────▶ Bozza validata
│  (redazione)     │     │ (controllo)       │     pronta per firma
└──────────────────┘     └──────────────────┘
```

1. **Agente di Area** — Redige, analizza, verifica, corregge e revisiona atti amministrativi. Risponde a domande e dubbi dell'operatore, inclusa la ricerca normativa via web.
2. **Revisore Normativo** — Controlla l'atto prodotto: citazioni normative, coerenza premesse-dispositivo, iter procedurale, privacy, appalti.

### Aree coperte (8)

| # | Area | Normativa chiave |
|---|------|-----------------|
| 1 | Segreteria Generale | TUEL artt. 36-57, L. 241/90, D.Lgs. 33/2013, FOIA |
| 2 | Servizi Sociali | L. 328/2000, D.Lgs. 117/2017 (CTS), GDPR |
| 3 | Ufficio Tecnico | DPR 380/2001, NTC 2018, D.Lgs. 152/2006 |
| 4 | Ragioneria - Servizio Finanziario | D.Lgs. 118/2011, TUEL Titolo VI |
| 5 | Servizi Demografici | DPR 223/1989, DPR 396/2000 |
| 6 | Personale - Risorse Umane | D.Lgs. 165/2001, CCNL FL, DPR 487/1994 |
| 7 | Polizia Municipale | D.Lgs. 285/1992 (CdS), TULPS, L. 65/1986 |
| 8 | Istruzione e Cultura | D.Lgs. 65/2017, L. 107/2015, D.Lgs. 42/2004 |

Normativa trasversale: **TUEL** (D.Lgs. 267/2000), **L. 241/90**, **D.Lgs. 33/2013** (trasparenza), **D.Lgs. 36/2023** (appalti).

### Revisori normativi (9)

Un **Revisore Core** trasversale (controlli comuni a tutti gli atti) + **8 Revisori di Area** che estendono il Core con verifiche settoriali specifiche.

---

## Cosa fa ogni agente

Ogni agente di area:

- **Redige** bozze di atti amministrativi (determine, delibere, ordinanze, convenzioni, ecc.) secondo un catalogo predefinito di tipologie
- **Analizza e corregge** bozze esistenti fornite dall'operatore (modalita analisi-bozza)
- **Revisiona** atti verificando struttura, coerenza e completezza
- **Assiste l'operatore** rispondendo a domande, dubbi e richieste di chiarimento su tematiche pertinenti l'area, inclusa la ricerca di norme, prassi, esempi e orientamenti via web search
- **Non inventa mai** dati, nomi, importi o riferimenti normativi — usa placeholder `[DATO MANCANTE]` e `[NORMA DA VERIFICARE]`
- Produce sempre un blocco **ATTENZIONE REDATTORE** con le criticita da verificare prima della firma

---

## Struttura del repository

```
Progetto AI COMUNE/
│
├── Agenti Comune Revisione 3.0/    ← VERSIONE CORRENTE
│   ├── Comune*-v.3.0.md            8 agenti di area
│   └── ComuneRevisore*-v.2.0.md    9 revisori normativi
│
├── Agenti Comune Revisione 2.0/    ← versione precedente
│   ├── 2.0/                         8 agenti v2.0
│   └── 1.02/                        agenti e report v1.02
│
├── Agenti Comune Revisione 1.0/    ← prima versione
│   ├── v.1.01/                      agenti + report PromptForge
│   └── v.1.02/                      agenti + report raffinamento
│
├── METAPROMPT AREA/                 ← istruzioni per generare gli agenti
│   ├── AREA 1-8 — *.md              metaprompt per agenti di area
│   ├── REVISORE *.md                metaprompt per revisori
│   ├── SUITE_COMUNALE_CONTESTO_v2.md contesto architetturale
│   └── legenda.md                   indice dei metaprompt
│
├── Seed prompts/                    ← prompt grezzi generati da Opus
│   ├── AREA 1-8 — *.md              seed agenti
│   ├── REVISORE *.md                seed revisori
│   └── GOLDEN SAMPLE — *.md         esempi completi pipeline
│
├── Liguria_gold_cases/              ← test suite Liguria (5 casi × 8 aree)
├── Toscana_gold_cases/              ← test suite Toscana (5 casi × 8 aree)
│
├── Archived/                        ← esperimenti iniziali (mar 2026)
│
└── README.md                        ← questo file
```

---

## Versioni

### Revisione 3.0 (corrente)

- **8 agenti di area v3.0** + **9 revisori v2.0**
- Compliance TSF (Token-Saving Format) per efficienza token
- Sistema di scoring multi-dimensionale con dashboard di consistenza
- Gate-0: rilevamento automatico bozze esistenti (modalita analisi)
- Protezione sistema multi-livello (L1-L4) contro prompt injection
- Chain-of-Thought obbligatoria pre-output con scoring
- **Scope ampliato**: redazione + analisi + verifica + correzione + revisione + assistenza operatore con web search
- Knowledge base normativa stratificata (Core, Appalti, Area, Regionale)
- Riferimento regionale primario: **Liguria** (adattabile ad altre regioni)

### Revisione 2.0

- 8 agenti di area v2.0 con catalogo atti strutturato
- Introduzione del sistema di scoring per decisioni
- Prima versione dei vincoli negativi formalizzati

### Revisione 1.0

- v1.01: prima generazione completa (8 agenti + 9 revisori) via metaprompt + PromptForge
- v1.02: raffinamento post-report con correzioni normative

---

## Pipeline di sviluppo

```
SUITE_COMUNALE_CONTESTO_v2.md     Metaprompt di Area/Revisore
(contesto architetturale)         (istruzioni specifiche)
         │                                  │
         └──────────┐    ┌─────────────────┘
                    ▼    ▼
              ┌─────────────────┐
              │  Claude Opus    │  ← generazione seed prompt
              │  4.6            │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  PromptForge    │  ← ottimizzazione industriale
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  Test con       │  ← gold cases Liguria/Toscana
              │  gold cases     │
              └────────┬────────┘
                       ▼
              ┌─────────────────┐
              │  Prompt finale  │  ← Revisione 3.0
              │  (produzione)   │
              └─────────────────┘
```

---

## Gold cases (test suite)

Le cartelle `Liguria_gold_cases/` e `Toscana_gold_cases/` contengono scenari di test realistici: **5 casi per area, 8 aree = 40 scenari per regione**. Ogni caso simula una richiesta tipica di un operatore comunale e permette di verificare il comportamento dell'agente in termini di:

- Corretta classificazione del tipo di atto
- Completezza della struttura output
- Gestione dei dati mancanti
- Accuratezza dei riferimenti normativi
- Presenza e qualita del blocco ATTENZIONE REDATTORE

---

## Note tecniche

- **LLM**: Claude Opus 4.6 (Anthropic)
- **Target**: Comuni italiani < 5.000 abitanti
- **Regione di riferimento**: Liguria (con possibilita di adattamento)
- **Lingua**: italiano (unica lingua per atti amministrativi)
- **Nessun dato reale**: tutti gli esempi usano placeholder e dati fittizi
- I prompt sono file Markdown (`.md`) utilizzabili come system prompt su qualsiasi piattaforma che supporti Claude

---

## Licenza

Da definire.
