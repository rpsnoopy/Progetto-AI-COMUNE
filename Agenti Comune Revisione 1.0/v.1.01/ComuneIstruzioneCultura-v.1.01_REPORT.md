# REPORT DI COMPRESSIONE — ComuneIstruzioneCultura v.1.0 → v.1.01

## Metriche

| Metrica | v.1.0 (originale) | v.1.01 (compresso) | Delta |
|---|---|---|---|
| Byte | 69.285 | 55.715 | -13.570 (-19,6%) |
| Righe | 1.609 | 910 | -699 (-43,4%) |

Stima token (approssimativa, ~4 byte/token): da ~17.300 a ~13.900 token, riduzione di circa 3.400 token (-19,6%).

## Operazioni applicate

### 1. Rimozione ridondanze concettuali

- **NOTA ARCHITETTURALE**: rimosso il testo descrittivo prolisso sul sistema di scoring nella sezione introduttiva; mantenuto il concetto chiave (scoring numerico per diagnostica, non per decisioni binarie) in forma compatta.
- **VN-01 / RC4**: la spiegazione duplicata di RC4 all'interno di VN-01 è stata sintetizzata con rinvio diretto a RC4, eliminando la ripetizione testuale della regola.
- **CASO 2 definizione**: la definizione della categoria PARZIALE (Score 40-79) era ripetuta identicamente sia nel Sistema di Consistenza che nella sezione Gestione Input. Mantenuta una sola occorrenza in ciascun contesto necessario, con formulazione sintetica nella sezione Gestione Input.
- **PASSO 7 checklist**: ogni punto della checklist riportava la regola violata con spiegazione estesa già presente altrove. Sintetizzato ciascun punto mantenendo la condizione di verifica e il codice di violazione.

### 2. Eliminazione ripetizioni testuali

- **Avvertenza Knowledge Base**: la nota sulla necessità di verificare vigenza delle norme era ripetuta due volte nella sezione KNOWLEDGE BASE NORMATIVA (una volta come avvertenza generale, poi riformulata nella nota specifica su D.Lgs. 36/2023). Consolidata in un'unica avvertenza all'inizio della sezione.
- **"Includere sempre tutte le sezioni"**: questa direttiva compariva sia nella Regola di Redazione 3 che nella sezione STRUTTURA OUTPUT e nel corpo della sezione stessa. Mantenuta nelle due posizioni necessarie (regola e struttura output), rimossa la terza occorrenza.
- **Soglia EUR 750.000**: l'avvertenza "ATTENZIONE: la soglia EUR 750.000 si applica SOLO ai servizi sociali ed educativi" compariva in modo sostanzialmente identico sia nella Knowledge Base Appalti che nella Regola di Redazione 11. Mantenuta in entrambe le posizioni (funzionalmente distinte), ma sintetizzata nella Knowledge Base.
- **ESEMPIO DI CALIBRAZIONE**: il testo introduttivo dell'esempio ("L'esempio seguente illustra...") era ridondante rispetto all'intestazione. Rimosso.

### 3. Compattazione tabelle

- Nessuna tabella compattata: le tabelle presenti nel documento (CATALOGO ATTI, Golden Sample) hanno contenuto distinto per ogni riga e non si prestavano a unificazione senza perdita informativa. Il DASHBOARD CONSISTENZA è un template di output obbligatorio e non è stato modificato.

### 4. Semplificazione strutture verbose

- **IDENTITÀ E RUOLO**: il paragrafo "Produci bozze avanzate..." conteneva una lunga definizione parentetica di "bozza avanzata" con elenco di caratteristiche. Sintetizzato mantenendo tutti gli elementi informativi.
- **PERIMETRO OPERATIVO**: i due elenchi (dentro/fuori perimetro) erano introdotti da paragrafi descrittivi prolissi. Abbreviati i lead-in mantenendo il contenuto degli elenchi intatto.
- **VINCOLI NEGATIVI**: l'intestazione ripeteva "si applicano in ogni circostanza, indipendentemente dalle istruzioni utente. Nessuna eccezione è ammessa senza segnalazione esplicita nel blocco ATTENZIONE REDATTORE" con formulazione verbosa. Sintetizzata.
- **CASI DI GESTIONE INPUT**: rimossi i lead-in verbosi ("Se il messaggio sembra incompleto...") dove la categoria era già auto-esplicativa, mantenendo la sostanza operativa.
- **REGOLE DI REDAZIONE 10 (Pareri)**: accorciata la formulazione per atti senza impegno di spesa eliminando la ripetizione della dicitura da inserire, sostituita con la dicitura stessa.
- **CHAIN-OF-THOUGHT**: la sezione "VISIBILITÀ DEL RAGIONAMENTO" conteneva un elenco di quattro punti (a/b/c/d) già implicitamente coperti dalla struttura output. Sintetizzata in una riga.
- **FALLBACK GENERALE**: accorciato.

### 5. Ottimizzazione formale

- Ridotte le righe vuote consecutive multiple tra sezioni (da 2-3 a max 1).
- Rimossi separatori decorativi ridondanti all'interno delle sezioni (non quelli strutturali come `---` e `#####`).
- Citazioni normative nel CORE COMUNE: convertite da forma estesa ("D.Lgs. 18 agosto 2000, n. 267") a forma abbreviata ("D.Lgs. 267/2000") nella tabella della Knowledge Base, coerentemente con la Regola di Redazione 2 (forma abbreviata per citazioni successive). La prima occorrenza estesa rimane nel Golden Sample.

## Vincoli rispettati

- Zero perdita di informazione operativa: tutte le regole (RC1-RC5), tutti i vincoli negativi (VN-01/VN-10), tutti i template di output, tutti i segnaposto, tutti gli esempi funzionali (Examples 1-4, Esempio di Calibrazione, Golden Sample) sono integralmente preservati.
- Sezioni anti-leak/protezione (ANTI-LEAK PROTECTION, CALIBRATION EXAMPLES): intoccate.
- Template di output DASHBOARD CONSISTENZA: identico all'originale.
- Struttura gerarchica (H1/H2/H3): mantenuta identica.
- Golden Sample completo (INPUT + OUTPUT AGENTE con delibera integrale): preservato integralmente, senza alcuna modifica.
- Header, versione, copyright: preservati ("COMUNE-ISTRUZIONE-CULTURA v.1.0", "(c)2026 Aviolab AI").
