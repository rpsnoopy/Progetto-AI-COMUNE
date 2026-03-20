# REPORT — Compressione ComuneRevisoreIstruzioneCultura v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 | v.1.01 | Riduzione |
|---------|-------|--------|-----------|
| Byte | 51.316 | 48.774 | −5,0% |
| Parole | 6.592 | 6.261 | −5,0% |
| Righe | 1.190 | 1.129 | −5,1% |

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

- **CHAIN-OF-THOUGHT per-sezione**: l'istruzione "Per ogni [X], esegui il CHAIN-OF-THOUGHT (Step 1-6)" compariva nei preamboli di §1, §2, §3, §4, §5 e §6 in modo identico. Rimossa la ripetizione per-sezione; aggiunta un'unica istruzione globale dopo la definizione del CHAIN-OF-THOUGHT in §B: "Applica questo CHAIN-OF-THOUGHT per OGNI elemento in tutte le sezioni del report (§1–6)."

- **Introduzione sezione §6**: il paragrafo che spiegava il perimetro del golden sample ("PERIMETRO: il golden sample fornito copre esclusivamente il sotto-tipo 'refezione scolastica'...") e il paragrafo che rimandava a §1-5 ("I controlli seguenti rimandano alle regole già definite in §1-5...") erano due blocchi separati prima dell'elenco dei sotto-tipi. Unificati in un unico paragrafo introduttivo compatto senza perdita di contenuto.

- **Score scale nelle sezioni analitiche**: i reminder "Score: 100 = conforme; 50 = vizio sanabile; 0 = vizio grave; CANNOT SCORE = non verificabile" nei preamboli di §2, §3, §4, §5 erano ripetizioni della scala già definita in §A. Mantenuti solo dove fornivano contestualizzazione specifica della sezione; rimossi i preamboli che erano pura replica.

### 2. Eliminazione ripetizioni testuali

- **Perimetro — atti misti**: il testo originale diceva prima "applica TUTTI i controlli pertinenti a ciascun sotto-dominio" e poi in un paragrafo separato "Per atti misti (50% educazione, 50% servizi sociali): analizzare esclusivamente le componenti...". I due concetti erano autonomi e corretti; mantenuti entrambi ma unificati nello stesso blocco PERIMETRO DI ANALISI, eliminando la riga vuota ridondante e la congiunzione ripetitiva.

- **REGOLA CRITICA 3-BIS**: rimossa la clausola di negazione ridondante "NON applicare la REGOLA CRITICA 3 nella sua interezza" che precedeva l'istruzione positiva — il comportamento alternativo era già esaustivamente descritto nelle righe successive.

- **REGOLA CRITICA 2**: il testo conteneva due frasi di spiegazione semanticamente equivalenti ("Un falso negativo... è più costoso di un falso positivo" e "Il revisore umano può declassare; non può correggere ciò che non è stato segnalato"). Entrambe conservate perché la seconda aggiunge il punto di vista operativo non presente nella prima.

### 3. Compattazione tabelle

Non presenti tabelle nel prompt sorgente. Non applicabile.

### 4. Semplificazione strutture verbose

- **REGOLE DI COMPORTAMENTO, regola 1**: "Qualsiasi integrazione o modifica al testo dell'atto è fuori perimetro." — frase accessoria rimossa; il concetto era già contenuto in "Il compito esclusivo è la revisione."

- **REGOLE DI COMPORTAMENTO, regola 6**: il blocco era introdotto da "Elementi [PENDENTE] — Se l'atto contiene elementi con stato pendente (es. [CIG: DA RICHIEDERE], [DATO MANCANTE]):" seguito da tre sotto-punti. Il testo rimane identico; rimosso solo l'eccesso di spaziatura tra i sotto-punti.

- **FORMATO OUTPUT introduzione**: le frasi "Il report deve rispettare ESATTAMENTE la struttura seguente. Non aggiungere sezioni, non modificare le intestazioni, non omettere sezioni anche se non applicabili (in tal caso scrivere 'Non applicabile — [motivazione]'). Produci SEMPRE tutte le sezioni nell'ordine esatto, anche se l'atto è semplice o privo di anomalie. Ogni voce del report deve includere lo score numerico..." erano in parte duplicate dalla REGOLA CRITICA 4. Conservata la sezione FORMATO OUTPUT nella sua interezza (è un template non derogabile); mantenuta l'intestazione introduttiva compatta eliminando solo la frase "anche se l'atto è semplice o privo di anomalie" che era già implicita nel "SEMPRE".

### 5. Ottimizzazione formale

- Eliminate righe vuote consecutive eccedenti (max 1 tra sezioni) in tutti i punti del documento dove erano presenti 2 o più righe vuote consecutive.
- Rimossa la riga vuota doppia tra le sotto-sezioni della KNOWLEDGE BASE NORMATIVA.
- Eliminati separatori decorativi ridondanti (linee `---`) all'interno delle sezioni di istruzione; mantenuti solo quelli strutturali che separano il corpo del prompt dai Golden Samples e dal footer copyright.

## Informazioni operative preservate al 100%

- Sezioni anti-leak/protezione (DIRETTIVA DI SISTEMA, 0-A, 0-B, 0-C): intatte, zero modifiche.
- Tutte le 5 REGOLE CRITICHE: intatte.
- Sistema di Consistenza (§A–§F): intatto.
- Tutte le 8 REGOLE DI COMPORTAMENTO: intatte.
- Knowledge base normativa (Livelli 1–4): intatta.
- Sezione COSA ANALIZZI (§1–§6, tutti i sotto-punti e score): intatta.
- FORMATO OUTPUT completo con tutti i template: intatto.
- Tutti e 3 i Golden Samples con dashboard: intatti.
- Copyright e metadata: intatti.
