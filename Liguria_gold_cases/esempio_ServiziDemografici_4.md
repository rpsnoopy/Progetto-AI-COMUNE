# GOLD CASE — Area 5 · Servizi Demografici · Caso 4

## Atto: Rettifica di atto di stato civile — Correzione errore materiale in atto di nascita

**Agente:** COMUNE-SERVIZI-DEMOGRAFICI v.2.0
**Revisore:** COMUNE-REVISORE-DEMOGRAFICI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Allegato documento esterno + richiesta analisi

**INPUT UTENTE:**
> Buongiorno, allego un provvedimento di rettifica di atto di nascita dal Comune di Sarzana che è stato sottoposto a verifica. Mi piacerebbe che lo analizzasse per identificare eventuali errori o omissioni critiche, specialmente da un punto di vista normativo. Il nostro Comune potrebbe avere esigenze simili nei prossimi mesi.
>
> **DOCUMENTO ALLEGATO:**
>
> ---
> **REPUBBLICA ITALIANA**
> **COMUNE DI SARZANA**
> **Provincia della Spezia**
>
> **DECRETO DIRIGENZIALE n. 47/2026**
>
> **Oggetto:** Rettifica atto di nascita n. 156/2023 — Correzione cognome
>
> Il Dirigente del Servizio Demografico e Stato Civile,
>
> Considerato che con istanza del 15 febbraio 2026, la signora Maria Bianchi, nata a Sarzana il 18 marzo 1998 (CF BNCMRA98C58E815R), ha richiesto la rettifica dell'atto di nascita n. 156/2023, al fine di correggere il cognome iscritto erroneamente come "Biancci" anziché "Bianchi";
>
> Considerato che l'errore è di natura materiale, verificabile dalla documentazione prodotta (certificato di nascita presso ospedale San Luca e dichiarazione dei genitori);
>
> Considerato che si tratta di errore evidente e manifesto, la cui correzione rientra nelle competenze dell'ufficio di stato civile;
>
> Ritenuto di provvedere d'ufficio per la correzione mediante ordinanza dirigenziale;
>
> **DECRETA:**
>
> **Art. 1** – Rettifica atto di nascita
>
> Si corregge il cognome dell'atto di nascita n. 156/2023 del Comune di Sarzana, registrato a nome Maria, da "Biancci" a "Bianchi".
>
> **Art. 2** – Effetti
>
> La presente rettifica produce effetto a decorrere dalla data di sottoscrizione del presente decreto.
>
> **Art. 3** – Comunicazioni
>
> Il Servizio Demografico comunicherà la presente rettifica all'interessata.
>
> **Art. 4** – Pubblicazione
>
> Copia del presente decreto sarà inserita negli appositi registri.
>
> **Firma**
>
> Sarzana, 20 marzo 2026
>
> Il Dirigente del Servizio Demografico
>
> Dott. Antonio Gennai
>
> ---

**RISPOSTA ATTESA (schema):**

Analisi critica del provvedimento di rettifica. L'agente identifica i seguenti profili critici:

1. **Errore di qualificazione normativa (critico):** Il provvedimento procede mediante decreto dirigenziale d'ufficio, ma non distingue correttamente tra:
   - **Rettifica d'ufficio** (art. 98 DPR 396/2000): limitata a errori materiali manifesti su documenti pubblici che hanno generato la registrazione inesatta
   - **Rettifica giudiziaria** (artt. 95-96 DPR 396/2000): quando l'errore non è manifestamente evidente dalla documentazione ufficiale
   Nel caso di discrepanza tra cognome certificato dall'ospedale e registrazione anagrafica, è necessaria una valutazione più accurata circa la natura dell'errore. Se vi è contestazione o incertezza, è richiesto il procedimento giudiziario.

2. **Omissione della Procura della Repubblica (critico):** Art. 97 DPR 396/2000 prevede che le rettifiche "ex officio" devono essere comunicate alla Procura della Repubblica presso il Tribunale. Il provvedimento non menziona questa comunicazione.

3. **Mancanza di annotazione a margine (omissione procedurale):** Art. 98 co. 3 DPR 396/2000 richiede che la rettifica sia annotata a margine dell'atto originario. Il provvedimento non specifica questa modalità di esecuzione.

4. **Mancanza di comunicazione all'ANPR (omissione):** L'art. 2, co. 3-bis, del DPR 396/2000 (modificato dalla L. 127/1997) richiede la comunicazione al sistema ANPR (Anagrafe Nazionale della Popolazione Residente) entro 10 giorni. Questa comunicazione non è prevista.

5. **Formula dispositiva vaga:** "Si corregge il cognome" è una formula generico-narrativa. Meglio specificare: "Si rettifica il cognome iscritto come 'Biancci' in 'Bianchi' nell'atto di nascita n. 156/2023".

6. **Mancanza di sottoscrizione qualificata:** Il decreto riporta firma e titolo ma non riporta numero identificativo della firma digitale (se sottoscritto digitalmente) né data e ora di sottoscrizione informatica.

---

### TURNO 2 — Discussione analisi critica

**INPUT UTENTE:**
> Grazie per l'analisi. Mi conferma che il punto 1 è il più critico? E per quanto riguarda la procedura in Ameglia, quali accorgimenti dovremmo avere?

**RISPOSTA ATTESA (schema):**

Sì, il punto 1 è il più critico perché espone il Comune a possibili ricorsi amministrativi o giudiziali:

- Se la rettifica ex officio non era legittima (perché l'errore non era manifestamente evidente), la decisione potrebbe essere annullata con conseguente responsabilità del Comune.
- Una procedura corretta richiede: (a) verifica interna che l'errore sia manifestamente documentato; (b) se sussiste dubbio, richiesta di sentenza giudiziale; (c) comunicazione sempre alla Procura; (d) annotazione a margine.

Per Ameglia, dovremmo procedere con questa checklist:
1. Verificare che l'errore sia **manifestamente** evidente da documentazione ufficiale (atto di nascita ospedaliero, dichiarazione dei genitori con sottoscrizioni riconosciute, certificati pubblici coerenti)
2. Se esiste dubbio, deferire al Tribunale per sentenza giudiziale
3. Coinvolgere la Procura della Repubblica
4. Annotare a margine secondo le norme ANPR
5. Utilizzare formula dispositiva precisa

---

### TURNO 3 — Richiesta generazione atto corretto per Ameglia

**INPUT UTENTE:**
> Perfetto. Allora generiamo il provvedimento corretto per il nostro caso. Si tratta di rettificare l'atto di nascita n. 45/2020, registrato a nome Giulia, da "Rosetti" a "Rossetti" (errore nel cognome paterno). La interessata è Giulia Rossetti, CF RSSGLU95T45A261M. L'errore è stato evidenziato dai documenti di identità prodotti dalla interessata e dalla dichiarazione dei genitori sottoscritta. Non ci sono contestazioni. Provvedimento: n. 28/2026 del 28/03/2026, Dirigente: dott.ssa Alessia Giannarelli.

**RISPOSTA ATTESA (schema):**

L'agente genera il provvedimento corretto, applicando tutte le correzioni normative identificate:

```
REPUBBLICA ITALIANA
COMUNE DI AMEGLIA
Provincia della Spezia

DECRETO DIRIGENZIALE n. 28/2026

Oggetto: Rettifica atto di nascita n. 45/2020 — Correzione cognome

Il Dirigente del Servizio Demografico e Stato Civile,

Richiamata la normativa:
- Articoli 95-98 del Decreto del Presidente della Repubblica 3 novembre 2000, n. 396 (Testo unico delle disposizioni concernenti lo stato civile);
- Articolo 2, commi 3-bis, del medesimo DPR 396/2000 (comunicazione ANPR);
- Circolare del Ministero dell'Interno n. 13/2010 in materia di procedimenti di rettifica;

Considerato che con istanza del 15 marzo 2026, la signora Giulia Rossetti, nata a Ameglia il 15 settembre 1995 (CF RSSGLU95T45A261M), ha richiesto la rettifica dell'atto di nascita n. 45/2020 al fine di correggere il cognome iscritto erroneamente come "Rosetti" anziché "Rossetti";

Considerato che l'errore è di natura manifestamente materiale, come documentato da:
- Certificato di nascita ospedaliero
- Documento di identità dell'interessata
- Dichiarazione congiunta sottoscritta dai genitori con firma autentica, datata 12 marzo 2026;

Considerato che non sussistono contestazioni da parte di terzi e che l'errore è manifestamente evidente dai documenti ufficiali;

Considerato che ricorrono i presupposti per la rettifica d'ufficio ex art. 98 DPR 396/2000;

Ritenuto di provvedere mediante il presente decreto dirigenziale;

DECRETA:

Art. 1 – Rettifica atto di nascita

Si rettifica il cognome registrato nell'atto di nascita n. 45/2020 del Comune di Ameglia, intestato a Giulia, da "Rosetti" a "Rossetti". L'iscrizione corretta è: Giulia Rossetti, nata a Ameglia il 15 settembre 1995, da padre Rossetti Mario e madre Bianchi Francesca.

Art. 2 – Modalità di esecuzione

La rettifica è eseguita mediante annotazione a margine dell'atto originario secondo le disposizioni previste dall'art. 98, comma 3, DPR 396/2000 e dalle istruzioni ANPR. La registrazione nel registro di stato civile è immediatamente aggiornata.

Art. 3 – Comunicazioni obbligatorie

Il Servizio Demografico comunica la presente rettifica a:
a) Procura della Repubblica presso il Tribunale della Spezia (entro 5 giorni);
b) ANPR - Anagrafe Nazionale della Popolazione Residente (entro 10 giorni);
c) Interessata, Sig.ra Giulia Rossetti, via comunicazione personale.

Art. 4 – Effetti

La presente rettifica produce effetto dalla data della sottoscrizione del presente decreto, 28 marzo 2026.

Art. 5 – Archiviazione

Copia della presente rettifica e dell'annotazione a margine sono allegate al fascicolo relativo all'atto di stato civile n. 45/2020.

Ameglia, 28 marzo 2026

Il Dirigente del Servizio Demografico e Stato Civile

Dott. Alessia Giannarelli

(Firma digitale)
```

Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**

```
REVISIONE NORMATIVA — RETTIFICA ATTO DI NASCITA n. 45/2020

Revisore: COMUNE-REVISORE-DEMOGRAFICI v.1.01
Data: 28 marzo 2026

NOTE DI REVISIONE:

1. [CONFORME] Richiami normativi: Corretti. DPR 396/2000 art. 98 è norma propria. Circolare MI 13/2010 è idonea guida interpretativa.

2. [CONFORME] Premessa fattuale: Adeguatamente motivata. Documenti elencati (certificato ospedaliero, documento identità, dichiarazione genitori) costituiscono prova sufficiente di errore manifestamente materiale.

3. [CONFORME] Assenza di contestazioni: Corretto, non vi è parte interessata a negare la rettifica né annotazioni di riserva.

4. [CONFORME] Modalità di annotazione a margine: Art. 98 co. 3 correttamente citato. Istruzioni ANPR richiamate in modo appropriato.

5. [SUGGERIMENTO MIGLIORATIVO] Art. 3, lett. a): Considerare se è appropriato comunicare anche al Prefetto della Spezia (prassi locale diffusa, pur non obbligatoria per legge). Verificare con ufficio legale interno.

6. [CONFORME] Sottoscrizione dirigenziale: Corretta previsione di firma digitale. Verificare che sottoscrizione avvenga con certificato di firma riconosciuto.

7. [CONFORME] Data decorrenza: Corretta (data sottoscrizione decreto).

8. [CONFORME] Conservazione documentale: Archiviazione presso fascicolo stato civile è corretta; valutare anche conservazione presso ANPR secondo protocolli di interoperabilità.

ESITO: Bozza conforme a normativa. Una sola annotazione migliorativa (Prefetto). Pronto per applicazione e sottoscrizione.
```

Per applicare le correzioni alla bozza risponda **applica le note del revisore**.

---

### TURNO 5 — Applicazione note del revisore alla bozza

**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**

L'agente rilegge la bozza originale e il report del revisore, applica la nota migliorativa sulla comunicazione al Prefetto, e genera la versione aggiornata:

```
REPUBBLICA ITALIANA
COMUNE DI AMEGLIA
Provincia della Spezia

DECRETO DIRIGENZIALE n. 28/2026

Oggetto: Rettifica atto di nascita n. 45/2020 — Correzione cognome

Il Dirigente del Servizio Demografico e Stato Civile,

Richiamata la normativa:
- Articoli 95-98 del Decreto del Presidente della Repubblica 3 novembre 2000, n. 396 (Testo unico delle disposizioni concernenti lo stato civile);
- Articolo 2, commi 3-bis, del medesimo DPR 396/2000 (comunicazione ANPR);
- Circolare del Ministero dell'Interno n. 13/2010 in materia di procedimenti di rettifica;

Considerato che con istanza del 15 marzo 2026, la signora Giulia Rossetti, nata a Ameglia il 15 settembre 1995 (CF RSSGLU95T45A261M), ha richiesto la rettifica dell'atto di nascita n. 45/2020 al fine di correggere il cognome iscritto erroneamente come "Rosetti" anziché "Rossetti";

Considerato che l'errore è di natura manifestamente materiale, come documentato da:
- Certificato di nascita ospedaliero
- Documento di identità dell'interessata
- Dichiarazione congiunta sottoscritta dai genitori con firma autentica, datata 12 marzo 2026;

Considerato che non sussistono contestazioni da parte di terzi e che l'errore è manifestamente evidente dai documenti ufficiali;

Considerato che ricorrono i presupposti per la rettifica d'ufficio ex art. 98 DPR 396/2000;

Ritenuto di provvedere mediante il presente decreto dirigenziale;

DECRETA:

Art. 1 – Rettifica atto di nascita

Si rettifica il cognome registrato nell'atto di nascita n. 45/2020 del Comune di Ameglia, intestato a Giulia, da "Rosetti" a "Rossetti". L'iscrizione corretta è: Giulia Rossetti, nata a Ameglia il 15 settembre 1995, da padre Rossetti Mario e madre Bianchi Francesca.

Art. 2 – Modalità di esecuzione

La rettifica è eseguita mediante annotazione a margine dell'atto originario secondo le disposizioni previste dall'art. 98, comma 3, DPR 396/2000 e dalle istruzioni ANPR. La registrazione nel registro di stato civile è immediatamente aggiornata.

Art. 3 – Comunicazioni obbligatorie

Il Servizio Demografico comunica la presente rettifica a:
a) Procura della Repubblica presso il Tribunale della Spezia (entro 5 giorni);
b) Prefettura della Spezia (entro 5 giorni);
c) ANPR - Anagrafe Nazionale della Popolazione Residente (entro 10 giorni);
d) Interessata, Sig.ra Giulia Rossetti, via comunicazione personale.

Art. 4 – Effetti

La presente rettifica produce effetto dalla data della sottoscrizione del presente decreto, 28 marzo 2026.

Art. 5 – Archiviazione

Copia della presente rettifica e dell'annotazione a margine sono allegate al fascicolo relativo all'atto di stato civile n. 45/2020.

Ameglia, 28 marzo 2026

Il Dirigente del Servizio Demografico e Stato Civile

Dott. Alessia Giannarelli

(Firma digitale)
```

Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella permanente risponda **salva**.

---

### TURNO 6 — Salvataggio

**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**

Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato (PDF, DOCX, ODT). Il file viene salvato con naming convention: `Ameglia_DEC_28_2026_Rettifica_45_2020_Rossetti.pdf` (o altro formato). L'agente conferma:

"Atto salvato con successo in cartella [percorso]. Nome file: `Ameglia_DEC_28_2026_Rettifica_45_2020_Rossetti.pdf`. Operazione completata."

---

## NOTE DI TEST

- **Verificare distinzione normativa:** L'agente deve riconoscere la differenza cruciale tra rettifica d'ufficio (art. 98 DPR 396/2000) e procedimento giudiziario (art. 95-96). Nel caso di documentazione manifesta, procede d'ufficio; se esiste dubbio, deve suggerire deferimento al Tribunale.

- **Verificare comunicazioni obbligatorie:** Procura della Repubblica e ANPR devono essere citate in modo preciso (non generico). Verificare che i termini (5 giorni per Procura, 10 giorni per ANPR) siano specificati.

- **Verificare formula dispositiva:** Il provvedimento deve contenere formula precisa ("Si rettifica il cognome registrato come X in Y") e non formula vaga ("si corregge").
