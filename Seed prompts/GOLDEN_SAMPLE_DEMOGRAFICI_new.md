# GOLDEN SAMPLE — AREA SERVIZI DEMOGRAFICI
## Suite Comunale AI v2.0 | Comune di Pieve Ligure

---

## INPUT UTENTE 1 — Dichiarazione di nascita + iscrizione anagrafica

```
Agente Servizi Demografici, devo iscrivere un nuovo nato in
anagrafe e stato civile.

Dati:
- Nato il 10 marzo 2026 alle ore 14:30 all'Ospedale San Martino
  di Genova.
- Genitori: Mario Rossi (CF RSSMRA85B10L219X, residente Pieve Ligure),
  Anna Verdi (CF VRDNNA88T45D123F, residente Pieve Ligure).
- Nome scelto: Giulia.
- Attestazione nascita dell'ostetrica già acquisita.
- Nessun altro nato quello giorno.

Genera la dichiarazione di nascita e l'atto di iscrizione anagrafica.
```

---

## OUTPUT AGENTE 1 — Atto di nascita + iscrizione anagrafica

```
ATTENZIONE REDATTORE
1. Completare tutti i [DATO MANCANTE] prima della firma.
2. Verificare attestazione nascita originale dell'ostetrica allegata.
3. Acquisire documenti di identità di entrambi i genitori.
4. Comunicare all'ANPR entro 24 ore per allineamento.
5. Trasmettere comunicazione ISTAT entro il 5 del mese successivo.
6. Numerare e protocollare l'atto nel registro di stato civile.
7. Dati identificativi genitori: conservare in fascicolo riservato.
   Non pubblicare sull'albo pretorio (GDPR art.6, dati personali).

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMUNE DI PIEVE LIGURE
Città Metropolitana di Genova
Ufficio di Stato Civile
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ATTO DI NASCITA
Parte I — Serie A — N. [DATO MANCANTE] / 2026

L'anno duemilaventisei, il giorno [DATO MANCANTE] del mese di
[DATO MANCANTE], alle ore [DATO MANCANTE], avanti a me
[DATO MANCANTE], Ufficiale dello Stato Civile del Comune di
Pieve Ligure, è comparso/a [DATO MANCANTE: dichiarante —
padre/madre/delegato ospedale], il/la quale mi ha dichiarato
che il giorno 10 marzo 2026, alle ore 14:30, presso
l'Ospedale Policlinico San Martino di Genova,
è nata una bambina.

DATI DEL NEONATO
Nome:               GIULIA
Cognome:            ROSSI
Sesso:              F
Data di nascita:    10 marzo 2026
Ora di nascita:     14:30
Luogo di nascita:   Genova (GE)
Ospedale:           Policlinico San Martino, Genova

DATI DEL PADRE
Cognome e nome:     ROSSI MARIO
Codice Fiscale:     RSSMRA85B10L219X
Luogo di nascita:   [DATO MANCANTE]
Data di nascita:    [DATO MANCANTE]
Residenza:          Pieve Ligure (GE)
Cittadinanza:       Italiana

DATI DELLA MADRE
Cognome e nome:     VERDI ANNA
Codice Fiscale:     VRDNNA88T45D123F
Luogo di nascita:   [DATO MANCANTE]
Data di nascita:    [DATO MANCANTE]
Residenza:          Pieve Ligure (GE)
Cittadinanza:       Italiana

ATTESTAZIONE OSTETRICA
Prot. n. [DATO MANCANTE] — Ospedale San Martino

Visti:
- DPR 3 novembre 2000, n. 396, artt. 29-30
  (dichiarazione di nascita entro 10 giorni);
- DPR 30 maggio 1989, n. 223, art. 7
  (iscrizione anagrafica neonato);
- D.Lgs. 7 marzo 2005, n. 82 (CAD), art. 23-ter
  (validità atto digitale se firmato digitalmente);

Letto al dichiarante, che lo ha approvato e sottoscritto
con me Ufficiale di Stato Civile.

IL DICHIARANTE                    L'UFFICIALE DI STATO CIVILE
_____________________             _____________________
[DATO MANCANTE]                   [DATO MANCANTE]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROVVEDIMENTO DI ISCRIZIONE ANAGRAFICA
Prot. n. [DATO MANCANTE] del [GG/MM/AAAA]

IL RESPONSABILE DEI SERVIZI DEMOGRAFICI

Visto l'atto di nascita n. [DATO MANCANTE] / 2026;
Visto il DPR 30 maggio 1989, n. 223, art. 7 co. 1:
iscrizione d'ufficio del neonato nell'anagrafe del Comune
di residenza dei genitori;
Visto il DPR 30 maggio 1989, n. 223, art. 18:
obbligo iscrizione entro 2 giorni dall'accertamento;
Vista la L. 24 dicembre 1954, n. 1228, art. 1;

DISPONE
1. L'iscrizione anagrafica di ROSSI GIULIA, nata il 10 marzo 2026
   a Genova, nel Comune di Pieve Ligure, nucleo familiare
   ROSSI MARIO — VERDI ANNA;
2. L'allineamento con l'ANPR (Anagrafe Nazionale Popolazione
   Residente) entro 24 ore dal presente provvedimento;
3. La trasmissione della comunicazione ISTAT nella rilevazione
   mensile entro il 5 del mese successivo;
4. La conservazione dell'atto nel registro di stato civile
   e nel fascicolo di famiglia.

Pieve Ligure, [GG/MM/AAAA]

IL RESPONSABILE SERVIZI DEMOGRAFICI
_____________________
[DATO MANCANTE]
```

---

## OUTPUT AGENTE REVISORE DEMOGRAFICI — Atto 1

```
REPORT DI REVISIONE NORMATIVA
Atto: Dichiarazione di nascita + iscrizione anagrafica
Comune: Pieve Ligure

ESITO: APPROVATO

ANOMALIE NORMATIVE
[OK] DPR 396/2000 artt. 29-30 — corretti (dichiarazione nascita)
[OK] DPR 223/1989 art. 7 co.1 — corretto (iscrizione d'ufficio)
[OK] DPR 223/1989 art. 18 — corretto (termine 2 giorni)
[OK] L. 1228/1954 art. 1 — corretto (obbligo anagrafico)
[OK] D.Lgs. 82/2005 art. 23-ter — pertinente se atto digitale

ITER PROCEDIMENTALE
[OK] Attestazione ostetrica prevista come allegato
[OK] Termine dichiarazione: 10 giorni da nascita (art.29 DPR 396/00)
[OK] Termine iscrizione: 2 giorni (art.18 DPR 223/89)
[OK] Allineamento ANPR previsto
[OK] Comunicazione ISTAT prevista
[ATTENZIONE] Verificare: se entrambi i genitori residenti a
             Pieve Ligure, competenza certa; se residenti in
             Comuni diversi, applicare art. 7 co.2 DPR 223/89
             (iscrizione nel Comune di residenza della madre)

COERENZA INTERNA
[OK] Atto di nascita e iscrizione anagrafica coerenti
[OK] Dati neonato uniformi nei due documenti
[OK] Competenza Ufficiale di Stato Civile corretta

PRIVACY
[OK] Atti di stato civile non pubblicati su albo pretorio
[OK] ATTENZIONE REDATTORE richiama conservazione riservata
[OK] Dati CF genitori nel fascicolo riservato, non in atti pubblici

APPALTI
Non applicabile.

AZIONE RICHIESTA
Atto approvabile. Completare tutti i [DATO MANCANTE].
Verificare residenza genitori per competenza art.7 co.2
DPR 223/89 se residenti in Comuni diversi.
```

---

## INPUT UTENTE 2 — Iscrizione anagrafica cittadino straniero

```
Agente Servizi Demografici, devo iscrivere in anagrafe
un cittadino straniero che ha presentato domanda di residenza.

Dati:
- Nome: Ahmed Ben Salah
- Nazionalità: marocchina
- Permesso di soggiorno: lavoro subordinato, scadenza 30/06/2027
- Domicilio dichiarato: Via Roma 12, Pieve Ligure
- Accertamento Polizia Municipale: eseguito con esito positivo
- Documentazione presentata: passaporto, permesso soggiorno,
  contratto di locazione.
```

---

## OUTPUT AGENTE 2 — Iscrizione anagrafica straniero

```
ATTENZIONE REDATTORE
1. Verificare validità permesso di soggiorno (scadenza 30/06/2027).
2. Acquisire copia passaporto e permesso di soggiorno.
3. Verificare verbale accertamento PM (prot. n. [DATO MANCANTE]).
4. Comunicare all'ANPR entro 24 ore.
5. Comunicare alla Questura di Genova entro 48 ore
   (art. 6 co.7 D.Lgs. 286/1998).
6. Conservare documentazione in fascicolo riservato (GDPR).
7. Dati personali straniero: non pubblicare su albo pretorio.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMUNE DI PIEVE LIGURE
Ufficio Anagrafe
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROVVEDIMENTO DI ISCRIZIONE ANAGRAFICA
Prot. n. [DATO MANCANTE] del [GG/MM/AAAA]

IL RESPONSABILE DEI SERVIZI DEMOGRAFICI

Premesso che:
- in data [DATO MANCANTE] il sig. BEN SALAH AHMED ha presentato
  domanda di iscrizione anagrafica per cambio di residenza
  con elezione di domicilio in Via Roma 12, Pieve Ligure;
- il richiedente è cittadino marocchino titolare di permesso
  di soggiorno per lavoro subordinato, scadenza 30 giugno 2027,
  rilasciato dalla Questura di [DATO MANCANTE];
- la Polizia Municipale ha eseguito accertamento in data
  [DATO MANCANTE], prot. n. [DATO MANCANTE], con esito positivo
  circa l'effettiva dimora abituale del richiedente;

Visti:
- L. 24 dicembre 1954, n. 1228 (Legge Anagrafica);
- DPR 30 maggio 1989, n. 223, artt. 6 e 18
  (procedura iscrizione e termini);
- D.Lgs. 25 luglio 1998, n. 286, art. 6 co. 7
  (comunicazione all'Autorità di Pubblica Sicurezza);
- Circolare Ministero Interno n. [DATO MANCANTE]
  (iscrizioni anagrafe cittadini stranieri);
- Reg. UE 2016/679 (GDPR), art. 6 (base giuridica trattamento);

Accertata la dimora abituale ex art. 3 co. 1 DPR 223/1989;

DISPONE
1. L'iscrizione anagrafica del sig. BEN SALAH AHMED,
   nato il [DATO MANCANTE] a [DATO MANCANTE] (Marocco),
   cittadino marocchino, in Via Roma 12, Pieve Ligure (GE),
   con decorrenza dalla data dell'accertamento positivo;
2. La comunicazione alla Questura di Genova entro 48 ore
   ex art. 6 co. 7 D.Lgs. 286/1998;
3. L'allineamento con ANPR entro 24 ore;
4. La trasmissione della comunicazione ISTAT nella rilevazione
   mensile entro il 5 del mese successivo;
5. La conservazione della documentazione nel fascicolo
   anagrafico riservato ex Reg. UE 2016/679.

Pieve Ligure, [GG/MM/AAAA]

IL RESPONSABILE SERVIZI DEMOGRAFICI
_____________________
[DATO MANCANTE]
```

---

## OUTPUT AGENTE REVISORE DEMOGRAFICI — Atto 2

```
REPORT DI REVISIONE NORMATIVA
Atto: Iscrizione anagrafica cittadino straniero
Comune: Pieve Ligure

ESITO: APPROVATO

ANOMALIE NORMATIVE
[OK] L. 1228/1954 — corretta (legge anagrafica)
[OK] DPR 223/1989 artt. 6 e 18 — corretti
     (procedura e termine 2 giorni accertamento)
[OK] D.Lgs. 286/1998 art. 6 co.7 — corretto
     (comunicazione Questura entro 48 ore)
[OK] GDPR art. 6 — corretto (base giuridica trattamento dati)
[ATTENZIONE Basso] Circolare Ministero Interno:
     inserire numero circolare specifico di riferimento
     per iscrizioni stranieri se disponibile

ITER PROCEDIMENTALE
[OK] Accertamento PM eseguito e citato (condizione necessaria)
[OK] Verifica validità permesso soggiorno
[OK] Termine iscrizione 2 giorni da accertamento (art.18 DPR 223/89)
[OK] Comunicazione Questura prevista entro 48 ore
[OK] Allineamento ANPR previsto
[OK] Comunicazione ISTAT prevista

COERENZA INTERNA
[OK] Dispositivo coerente con le premesse
[OK] Decorrenza iscrizione: data accertamento positivo (corretto)
[OK] Competenza Responsabile Demografici corretta

PRIVACY
[OK] Dati personali straniero non pubblicati
[OK] ATTENZIONE REDATTORE richiama fascicolo riservato
[OK] Base giuridica GDPR art.6 citata nel provvedimento

APPALTI
Non applicabile.

AZIONE RICHIESTA
Atto approvabile. Completare [DATO MANCANTE].
Inserire numero circolare Ministero Interno se disponibile.
Verificare che verbale PM sia già acquisito agli atti.
```

---

Fine golden sample Servizi Demografici.
