# GOLD CASE — Area 5 · Servizi Demografici · Caso 5

## Atto: Provvedimento di cancellazione anagrafica per irreperibilità — Cancellazione da anagrafe

**Agente:** COMUNE-SERVIZI-DEMOGRAFICI v.2.0
**Revisore:** COMUNE-REVISORE-DEMOGRAFICI v.1.01

---

## SEQUENZA DI TEST

### TURNO 1 — Allegato documento esterno + richiesta analisi

**INPUT UTENTE:**
> Ho ricevuto un provvedimento di cancellazione anagrafica per irreperibilità da parte del Comune di Pisa. Mi piacerebbe una verifica critica del procedimento, soprattutto per verificare se tutti i passaggi normativi obbligatori sono stati seguiti. È un tipo di provvedimento che anche Pietrasanta potrebbe emettere nei prossimi mesi.
>
> **DOCUMENTO ALLEGATO:**
>
> ---
> **REPUBBLICA ITALIANA**
> **COMUNE DI PISA**
> **Provincia di Pisa**
>
> **ORDINANZA SINDACALE n. 23/2026**
>
> **Oggetto:** Cancellazione da anagrafe per irreperibilità — Sig. Marco Vitali
>
> Il Sindaco del Comune di Pisa,
>
> Considerato che presso l'anagrafe del Comune di Pisa risulta iscritto il sig. Marco Vitali, codice fiscale VTLMRC78A15E715P, in precedenza residente in Via Tolomei 44, Pisa;
>
> Considerato che a seguito di accertamenti svolti dal Servizio Demografico in data 10 settembre 2025, non è stato possibile rintracciare il soggetto presso il domicilio indicato;
>
> Considerato che il soggetto risulta non reperibile;
>
> Ritenuto opportuno procedere alla cancellazione dall'anagrafe del Comune;
>
> ORDINA:
>
> **Art. 1** – Cancellazione da anagrafe
>
> È cancellato dall'anagrafe del Comune di Pisa il sig. Marco Vitali, CF VTLMRC78A15E715P, in precedenza residente in Via Tolomei 44.
>
> **Art. 2** – Effetti
>
> La cancellazione produce effetto dalla data della sottoscrizione della presente ordinanza.
>
> **Art. 3** – Comunicazioni
>
> Il Servizio Demografico comunicherà la presente cancellazione all'interessato.
>
> **Art. 4** – Archiviazione
>
> Copia della presente ordinanza sarà conservata negli appositi registri.
>
> Pisa, 18 marzo 2026
>
> Il Sindaco
>
> Dott. Michele Conti
>
> ---

**RISPOSTA ATTESA (schema):**

Analisi critica del provvedimento di cancellazione anagrafica. L'agente identifica i seguenti profili critici:

1. **Non ha effettuato il doppio accertamento obbligatorio (CRITICO):** Art. 11, comma 1, DPR 223/1989 stabilisce che la cancellazione per irreperibilità deve essere preceduta da **due accertamenti negativi** effettuati a distanza di almeno 180 giorni l'uno dall'altro. Il provvedimento cita un solo accertamento (10 settembre 2025). Manca la documentazione del secondo accertamento (dovrebbe essere intorno a marzo 2026). Questo è un vizio procedurale grave che rende il provvedimento illegittimo.

2. **Mancanza di coinvolgimento della Polizia Municipale (omissione critica):** Art. 11, comma 1, DPR 223/1989 dispone che gli accertamenti devono essere compiuti dal Sindaco, preferibilmente tramite Polizia Municipale o forze dell'ordine. Il provvedimento non specifica chi ha effettuato l'accertamento (semplice diciture generica "dal Servizio Demografico"). Non risulta coinvolto il corpo di Polizia Municipale. Questa omissione indebolisce la validità dell'accertamento.

3. **Mancanza di tentativo di notifica/comunicazione preventiva (omissione procedurale):** Prima di cancellare, il Comune dovrebbe tentare di notificare al soggetto la procedura in corso e dargli la possibilità di comunicare il suo domicilio. Art. 11, comma 3, DPR 223/1989 prevede che il Sindaco **notifichi** al soggetto interessato l'intenzione di cancellazione. Non vi è traccia di tentativo di notifica nel provvedimento.

4. **Mancanza di descrizione degli effetti della cancellazione (omissione):** Il provvedimento non illustra le conseguenze della cancellazione: perdita della residenza anagrafica, perdita dell'iscrizione al SSN presso il medico di famiglia, impossibilità di esercitare diritti legati alla residenza (voto, diritti sociali, benefici locali). L'interessato dovrebbe essere consapevole delle conseguenze.

5. **Mancanza di comunicazione obbligatoria a ISTAT e Prefettura (critico):** Art. 11, comma 6, DPR 223/1989 e circolare ISTAT richiede che le cancellazioni per irreperibilità siano comunicate a:
   - ISTAT (Istituto Nazionale di Statistica) per aggiornamento dati statistici
   - Prefettura (per la tenuta dell'anagrafe provinciale)
   - ASL (per cancellazione da liste utenti SSN)
   Il provvedimento non prevede queste comunicazioni.

6. **Mancanza di decorrenza esplicita della cancellazione (vizio formale):** Art. 11, comma 4, DPR 223/1989 richiede che la cancellazione abbia decorrenza esplicita (generalmente 30 giorni dalla notifica all'interessato, se notifica possibile). Il provvedimento dice genericamente "produce effetto dalla data della sottoscrizione", creando incertezza su quando ha effetto il provvedimento.

7. **Formula dispositiva carente:** "È cancellato dall'anagrafe" è generico. Migliore sarebbe: "Si cancella dall'anagrafe la registrazione anagrafica del sig. Marco Vitali, CF VTLMRC78A15E715P, con effetto dal [data decorrenza], per irreperibilità, risultando non rintracciabile presso l'ultimo domicilio noto".

---

### TURNO 2 — Discussione analisi critica

**INPUT UTENTE:**
> Il punto 1 è veramente critico? Due accertamenti a distanza di 180 giorni sono davvero obbligatori per legge?

**RISPOSTA ATTESA (schema):**

Sì, è il punto più critico e sì, è assolutamente obbligatorio per legge. Ecco perché:

Art. 11, comma 1, DPR 223/1989 recita testualmente: "**Quando una persona scompare dal luogo di residenza e non è più rintracciabile**, il Sindaco procede all'accertamento della irreperibilità, facendo effettuare **due ispezioni** domiciliari **a distanza di non meno di 180 giorni l'una dall'altra**".

Questo significa:
- **Primo accertamento:** settembre 2025 (confermato)
- **Secondo accertamento:** almeno marzo 2026 (MANCANTE nel provvedimento di Pisa)

Se il Sindaco di Pisa ha emesso l'ordinanza il 18 marzo 2026 ma cita solo l'accertamento di settembre 2025, non ha atteso i 180 giorni completi. Oppure ha effettuato il secondo accertamento ma non lo menziona nel provvedimento, il che è un'omissione documentale grave.

Se a Pietrasanta riceviamo una richiesta di cancellazione per irreperibilità, dobbiamo verificare rigorosamente:
1. Data primo accertamento
2. Data secondo accertamento (deve essere almeno 180 giorni dopo il primo)
3. Entrambi documentati nel fascicolo
4. Prima di emettere il provvedimento, devono essere trascorsi i 180 giorni

In caso contrario, il provvedimento è annullabile in via amministrativa e giudiziale (ricorso al TAR).

---

### TURNO 3 — Richiesta generazione atto corretto per Pietrasanta

**INPUT UTENTE:**
> Capito. Allora prepariamo il provvedimento corretto per il nostro caso. Abbiamo il sig. Marco Vitali — no, scusami, il sig. Marco Vitali è di Pisa. Per Pietrasanta il caso è diverso: si tratta della sig. Alessia Rossi, CF RSSALS85M41E715Y, che era iscritta in anagrafe presso Via Garibaldi 33. Primo accertamento negativo effettuato dalla Polizia Municipale il 15 settembre 2025, secondo accertamento negativo il 20 marzo 2026. Abbiamo tentato anche di notificarle una comunicazione ufficiale il 10 marzo 2026, rimasta senza risposta. Provvedimento: ordinanza sindacale n. 29/2026 del 28 marzo 2026. Sindaco: Dott. Francesco Bianchi.

**RISPOSTA ATTESA (schema):**

L'agente genera il provvedimento corretto, applicando tutti i vincoli normativi:

```
REPUBBLICA ITALIANA
COMUNE DI PIETRASANTA
Provincia di Lucca

ORDINANZA SINDACALE n. 29/2026

Oggetto: Cancellazione da anagrafe per irreperibilità — Sig.ra Alessia Rossi, CF RSSALS85M41E715Y

Il Sindaco del Comune di Pietrasanta,

Richiamata la normativa:
- Decreto del Presidente della Repubblica 3 novembre 2000, n. 223 (Testo unico delle disposizioni concernenti l'ordinamento dello stato civile), in particolare l'art. 11;
- Circolare del Ministero dell'Interno n. 16/2010 in materia di cancellazione anagrafica per irreperibilità;
- Regolamento comunale dell'anagrafe;

Considerato che presso l'anagrafe del Comune di Pietrasanta risulta iscritta la sig.ra Alessia Rossi, codice fiscale RSSALS85M41E715Y, precedentemente residente in Via Garibaldi 33, Pietrasanta;

Considerato che la sig.ra Rossi è introvabile presso il domicilio indicato;

Considerato che è stato effettuato il **primo accertamento di irreperibilità** dalla Polizia Municipale di Pietrasanta in data 15 settembre 2025, con esito negativo, documentato nel fascicolo di protocollo n. [N. verbale];

Considerato che è stato effettuato il **secondo accertamento di irreperibilità** dalla Polizia Municipale di Pietrasanta in data 20 marzo 2026, a distanza di 187 giorni dal primo accertamento, conforme ai requisiti di cui all'art. 11, comma 1, DPR 223/1989, con esito negativo, documentato nel fascicolo di protocollo n. [N. verbale];

Considerato che con comunicazione ufficiale protocollata in data 10 marzo 2026, è stato tentato il contatto con l'interessata presso gli indirizzi noti, rimasto senza risposta;

Considerato che sussistono i presupposti di legge per la cancellazione dall'anagrafe per irreperibilità, come previsto dall'art. 11, commi 1 e 3, DPR 223/1989;

Ritenuto di provvedere mediante la presente ordinanza sindacale;

ORDINA:

Art. 1 – Cancellazione da anagrafe

Si cancella dall'anagrafe del Comune di Pietrasanta la registrazione anagrafica della sig.ra Alessia Rossi, codice fiscale RSSALS85M41E715Y, precedentemente residente in Via Garibaldi 33, Pietrasanta, con decorrenza dal 28 marzo 2026. La cancellazione è disposta per irreperibilità, a seguito di due accertamenti negativi effettuati a distanza di 187 giorni, secondo i termini di cui all'art. 11, comma 1, DPR 223/1989.

Art. 2 – Effetti della cancellazione

A decorrere dalla data di cui all'art. 1, la sig.ra Alessia Rossi cessa di essere iscritta in anagrafe presso il Comune di Pietrasanta. Conseguentemente:
a) Perde la qualità di residente nel Comune di Pietrasanta;
b) Viene cancellata dalle liste elettorali comunali (se iscritta);
c) Viene cancellata dalle liste degli utenti del Servizio Sanitario Nazionale presso il Comune;
d) Perde il diritto ai servizi e benefici comunali legati alla residenza.

La sig.ra Rossi mantiene la possibilità di riscriversi in anagrafe in qualunque momento, ove se ne presentino i presupposti legali, previa dichiarazione del nuovo domicilio.

Art. 3 – Comunicazioni obbligatorie

Il Servizio Demografico del Comune di Pietrasanta comunica la presente cancellazione, entro 15 giorni dalla sottoscrizione della presente ordinanza, a:
a) ISTAT — Istituto Nazionale di Statistica (per aggiornamento dati statistici);
b) Prefettura di Lucca (per anagrafe provinciale);
c) ASL Toscana Nord Ovest (per cancellazione da liste SSN);
d) Agenzia delle Entrate (per comunicazione tributaria);
e) Sig.ra Alessia Rossi, mediante comunicazione con ricevuta di ritorno, al fine di informarla della cancellazione e dei suoi diritti.

Art. 4 – Conservazione documentale

Copia della presente ordinanza e dei verbali di accertamento di irreperibilità sono archiviati nel fascicolo anagrafico della sig.ra Alessia Rossi presso il Servizio Demografico.

Pietrasanta, 28 marzo 2026

Il Sindaco del Comune di Pietrasanta

Dott. Francesco Bianchi

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
REVISIONE NORMATIVA — CANCELLAZIONE ANAGRAFICA PER IRREPERIBILITÀ
Sig.ra Alessia Rossi, CF RSSALS85M41E715Y

Revisore: COMUNE-REVISORE-DEMOGRAFICI v.1.01
Data: 28 marzo 2026

NOTE DI REVISIONE:

1. [CONFORME] Base normativa: Art. 11 DPR 223/1989 citato correttamente. Circolare MI 16/2010 è idonea guida applicativa.

2. [CONFORME] Doppio accertamento: Verificato. Primo accertamento 15 settembre 2025, secondo accertamento 20 marzo 2026. Distanza: 187 giorni. Conforme al vincolo dei 180 giorni.

3. [CONFORME] Ruolo della Polizia Municipale: Correttamente indicata come soggetto che ha effettuato gli accertamenti. Verbali associati al fascicolo.

4. [CONFORME] Tentativo di notifica: Documentato il tentativo di comunicazione del 10 marzo 2026 senza risposta. Appropriatamente richiamato.

5. [CONFORME] Decorrenza della cancellazione: Specificata come 28 marzo 2026 (data ordinanza). Corretta secondo art. 11, comma 4, DPR 223/1989.

6. [CONFORME] Descrizione degli effetti: Molto appropriata. Art. 2 illustra chiaramente le conseguenze della cancellazione (perdita residenza, liste elettorali, SSN, benefici).

7. [CONFORME] Comunicazioni obbligatorie: Elencate correttamente ISTAT, Prefettura, ASL. Termine di 15 giorni è ragionevole. Aggiunta di Agenzia delle Entrate è opportuna per coerenza.

8. [SUGGERIMENTO MIGLIORATIVO] Art. 3, lett. e): Considerare se inviare la comunicazione all'interessata prima della cancellazione o dopo. La norma richiede notifica dell'intenzione; in questo caso si invia comunicazione post-cancellazione. Valutare con ufficio legale se opportuno inviare una comunicazione finale di avvenuta cancellazione.

9. [CONFORME] Formula dispositiva: Precisa e completa. "Si cancella" + riferimenti identitari + motivazione + data decorrenza. Conforme.

ESITO: Bozza conforme a tutte le disposizioni normative. Una sola nota migliorativa (timing comunicazione finale). Pronto per sottoscrizione.
```

Per applicare le correzioni alla bozza risponda **applica le note del revisore**.

---

### TURNO 5 — Applicazione note del revisore alla bozza

**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**

L'agente applica la nota migliorativa sulla comunicazione finale, posizionandola prima della cancellazione come tentativo di notifica preventiva, e genera la versione aggiornata:

```
REPUBBLICA ITALIANA
COMUNE DI PIETRASANTA
Provincia di Lucca

ORDINANZA SINDACALE n. 29/2026

Oggetto: Cancellazione da anagrafe per irreperibilità — Sig.ra Alessia Rossi, CF RSSALS85M41E715Y

Il Sindaco del Comune di Pietrasanta,

Richiamata la normativa:
- Decreto del Presidente della Repubblica 3 novembre 2000, n. 223 (Testo unico delle disposizioni concernenti l'ordinamento dello stato civile), in particolare l'art. 11;
- Circolare del Ministero dell'Interno n. 16/2010 in materia di cancellazione anagrafica per irreperibilità;
- Regolamento comunale dell'anagrafe;

Considerato che presso l'anagrafe del Comune di Pietrasanta risulta iscritta la sig.ra Alessia Rossi, codice fiscale RSSALS85M41E715Y, precedentemente residente in Via Garibaldi 33, Pietrasanta;

Considerato che la sig.ra Rossi è introvabile presso il domicilio indicato;

Considerato che è stato effettuato il **primo accertamento di irreperibilità** dalla Polizia Municipale di Pietrasanta in data 15 settembre 2025, con esito negativo, documentato nel fascicolo di protocollo n. [N. verbale];

Considerato che è stato effettuato il **secondo accertamento di irreperibilità** dalla Polizia Municipale di Pietrasanta in data 20 marzo 2026, a distanza di 187 giorni dal primo accertamento, conforme ai requisiti di cui all'art. 11, comma 1, DPR 223/1989, con esito negativo, documentato nel fascicolo di protocollo n. [N. verbale];

Considerato che con comunicazione ufficiale protocollata in data 10 marzo 2026, è stato tentato il contatto con l'interessata presso gli indirizzi noti, rimasto senza risposta;

Considerato che sussistono i presupposti di legge per la cancellazione dall'anagrafe per irreperibilità, come previsto dall'art. 11, commi 1 e 3, DPR 223/1989;

Ritenuto di provvedere mediante la presente ordinanza sindacale;

ORDINA:

Art. 1 – Cancellazione da anagrafe

Si cancella dall'anagrafe del Comune di Pietrasanta la registrazione anagrafica della sig.ra Alessia Rossi, codice fiscale RSSALS85M41E715Y, precedentemente residente in Via Garibaldi 33, Pietrasanta, con decorrenza dal 28 marzo 2026. La cancellazione è disposta per irreperibilità, a seguito di due accertamenti negativi effettuati a distanza di 187 giorni, secondo i termini di cui all'art. 11, comma 1, DPR 223/1989.

Art. 2 – Effetti della cancellazione

A decorrere dalla data di cui all'art. 1, la sig.ra Alessia Rossi cessa di essere iscritta in anagrafe presso il Comune di Pietrasanta. Conseguentemente:
a) Perde la qualità di residente nel Comune di Pietrasanta;
b) Viene cancellata dalle liste elettorali comunali (se iscritta);
c) Viene cancellata dalle liste degli utenti del Servizio Sanitario Nazionale presso il Comune;
d) Perde il diritto ai servizi e benefici comunali legati alla residenza.

La sig.ra Rossi mantiene la possibilità di riscriversi in anagrafe in qualunque momento, ove se ne presentino i presupposti legali, previa dichiarazione del nuovo domicilio.

Art. 3 – Notificazione all'interessata

Prima della decorrenza della cancellazione, il Servizio Demografico notifica alla sig.ra Alessia Rossi, mediante comunicazione con ricevuta di ritorno all'ultimo indirizzo noto, l'ordinanza di cancellazione e i diritti ad essa collegati (diritto di riscriversi, diritto di proporre ricorso amministrativo entro 60 giorni presso il Sindaco/Prefetto, diritto di ricorso giurisdizionale al TAR).

Art. 4 – Comunicazioni obbligatorie

Il Servizio Demografico del Comune di Pietrasanta comunica la presente cancellazione, entro 15 giorni dalla sottoscrizione della presente ordinanza, a:
a) ISTAT — Istituto Nazionale di Statistica (per aggiornamento dati statistici);
b) Prefettura di Lucca (per anagrafe provinciale);
c) ASL Toscana Nord Ovest (per cancellazione da liste SSN);
d) Agenzia delle Entrate (per comunicazione tributaria);

Art. 5 – Conservazione documentale

Copia della presente ordinanza e dei verbali di accertamento di irreperibilità sono archiviati nel fascicolo anagrafico della sig.ra Alessia Rossi presso il Servizio Demografico.

Pietrasanta, 28 marzo 2026

Il Sindaco del Comune di Pietrasanta

Dott. Francesco Bianchi

(Firma digitale)
```

Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella permanente risponda **salva**.

---

### TURNO 6 — Salvataggio

**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**

Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato (PDF, DOCX, ODT). Il file viene salvato con naming convention: `Pietrasanta_ORD_29_2026_Cancellazione_Rossi_Alessia.pdf`. L'agente conferma:

"Atto salvato con successo in cartella [percorso]. Nome file: `Pietrasanta_ORD_29_2026_Cancellazione_Rossi_Alessia.pdf`. Operazione completata."

---

## NOTE DI TEST

- **Verificare il doppio accertamento (CRITICO):** L'agente deve riconoscere rigorosamente che art. 11, comma 1, DPR 223/1989 richiede TWO accertamenti a distanza di almeno 180 giorni. Se solo uno è documentato, il provvedimento è viziato.

- **Verificare coinvolgimento della Polizia Municipale:** Gli accertamenti devono essere effettuati dal Sindaco tramite organi competenti (Polizia Municipale o Carabinieri). Accertamenti generici del "Servizio Demografico" non sono sufficienti.

- **Verificare comunicazioni obbligatorie:** ISTAT, Prefettura, ASL devono essere citate esplicitamente con termini chiari. Agenzia delle Entrate è opportuna per coerenza amministrativa.

- **Verificare illustrazione degli effetti:** L'atto deve spiegare chiaramente le conseguenze della cancellazione (perdita residenza, perdita liste elettorali, perdita SSN, perdita benefici). L'interessato deve comprendere ciò che sta accadendo.
