# GOLD CASE — Area 7 · Polizia Municipale · Caso 6

## Atto: Ordinanza Sindacale — Chiusura Sentiero per Motivi di Sicurezza

**Agente:** COMUNE-POLIZIA-MUNICIPALE v.2.0
**Revisore:** COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa
**INPUT UTENTE:**
> Buongiorno, abbiamo un problema di sicurezza. Il sentiero 432 che collega Montemarcello a Bocca di Magra all'interno del Parco Regionale Montemarcello-Magra-Vara presenta una frana importante dopo gli ultimi temporali. Il nostro ufficio Protezione Civile ha fatto un sopralluogo il 24 marzo e ha riscontrato cedimento di terreno e rischio di crollo. Come procediamo per una chiusura temporanea con ordinanza sindacale?

**RISPOSTA ATTESA (schema):**
L'agente deve riconoscere la competenza di chiusura ordinanze sindacali in materia di sicurezza pubblica ai sensi dell'art. 54 D.Lgs. 267/2000, richiedere informazioni specifiche sul sentiero (ubicazione precisa, lunghezza, afflusso, segnaletica attuale), verificare il coinvolgimento dell'Ente Parco Regionale, e proporre il flusso di generazione dell'ordinanza sindacale con coordinate geografiche, perimetrazione della zona interdetta, e obbligo di comunicazione agli enti competenti (Ente Parco, Prefettura della Spezia, Capitaneria di Porto per questioni litoranee).

---

### TURNO 2 — Richiesta generazione atto
**INPUT UTENTE:**
> Procediamo con l'ordinanza. Ecco i dati:
> - Sentiero 432 nel Parco di Montemarcello
> - Ubicazione: tratto da quota 180 m (Montemarcello centro) a quota 45 m (Bocca di Magra marina)
> - Lunghezza: circa 2,3 km, larghezza media 1,2 m
> - Data sopralluogo: 24 marzo 2026
> - Operatore: Vice-Sindaco Emanuele Cadeddu (Protezione Civile)
> - Frana estensione: circa 380 mq, cedimento verticale 1,5-2,0 m, rimozione copertura vegetale
> - Rischio: crollo massi, distacco spallette, instabilità substrato
> - Segnaletica di chiusura: cartelli con pittogramma vietato l'accesso e coordinamento con Ente Parco
> - Data ordinanza: 28 marzo 2026
> - Numero ordinanza: 8/2026

**RISPOSTA ATTESA (schema):**
L'agente genera la bozza dell'ordinanza sindacale con:
- Intestazione: Comune di Ameglia (SP), Sindaco Andrea De Ranieri
- Numero e data ordinanza
- Considerando: rischio idrogeologico, verbale di sopralluogo, competenza ordinanze urgenti
- Dispositivo: interdizione del sentiero 432 dal punto X al punto Y, obbligo rimozione accesso, segnaletica permanente
- Obbligo comunicazione a: Ente Parco Regionale, Prefettura della Spezia, Capitaneria di Porto, Provincia della Spezia, Regione Liguria (Protezione Civile)
- Durata: fino a data da destinarsi o revoca espressa
- Data decorrenza e sottoscrizione

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica
**INPUT UTENTE:**
> Nella sezione comunicazioni, aggiungi anche la comunicazione ai gestori di strutture ricettive di Montemarcello e un avviso pubblico da pubblicare all'albo pretorio on-line. Il sentiero è abbastanza frequentato in primavera. Meglio mettere in evidenza il pericolo.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna la bozza aggiungendo:
- Comunicazione a: Associazione Albergatori Montemarcello, strutture ricettive private della frazione
- Obbligo affissione avviso all'albo pretorio telematico e cartaceo presso la sede municipale (Via Maestà 30)
- Revisione della segnaletica per includere cartelli di colore rosso standardizzati con simbolo pericolo + divieto accesso + area interclusa per frana
- Possibile integrazione: valutazione di riapertura ordinanza sottoposta a sopralluogo congiunto (Ente Parco + Protezione Civile) entro 60 giorni
- Testo aggiornato della bozza visualizzato nuovamente

---

### TURNO 4 — Richiesta revisione normativa
**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
```
REVISIONE NORMATIVA — Ordinanza Sindacale n. 8/2026
Chiusura Sentiero 432 Parco Regionale Montemarcello-Magra-Vara
Prodotto da: COMUNE-POLIZIA-MUNICIPALE v.2.0
Revisionato da: COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0
---

CONTROLLI NORMATIVI EFFETTUATI:

1. FONDAMENTO GIURIDICO
   ✓ Art. 54 D.Lgs. 267/2000 (Testo Unico Enti Locali): ordinanze in caso di urgenza e per
     motivi di sicurezza pubblica — APPLICABILE
   ✓ D.Lgs. 112/1998 artt. 117-118: competenze ordinanze in materia protezione civile — OK
   ✓ Normativa sentieristica Liguria: sentieri comunali rientranti in perimetri protetti
     richiedono coordinamento Ente Parco — VERIFICATO

2. PROCEDURA E COMUNICAZIONI
   ✓ Comunicazione a Ente Parco Regionale Montemarcello-Magra-Vara (ente competente per
     aree protette): OBBLIGATORIA entro 24h dalla firma ordinanza
   ✓ Comunicazione Prefettura della Spezia: CONSIGLIATO (sicurezza pubblica su territorio)
   ✓ Comunicazione Capitaneria di Porto La Spezia: CONSIGLIATO (area litoranea Bocca di Magra)
   ✓ Affissione albo pretorio: OBBLIGATORIA (entro 5 giorni dalla firma)
   ✓ Comunicazione strutture ricettive: CORRETTA (informazione pubblica)

3. CONTENUTI SOSTANZIALI
   ✓ Descrizione perimetrazione zona interdetta: NECESSITA INTEGRAZIONE con coordinate
     geografiche precise (lat./long. o descrizione con riferimenti catastali)
   ✓ Obbligo segnaletica secondo normativa stradale: MANCA DETTAGLIO su standard D.M.
     Infrastrutture 30/11/1999 per cartelli — SUGGERITO aggiunta: "cartelli conformi a
     standard ministeriali per zone interdette"
   ✓ Durata ordinanza: VAGA ("fino a revoca espressa") — SUGGERITO fissare termine di 60
     giorni con riesame automatico

4. ASPETTI AMBIENTALI (Parco)
   ✓ Valutazione impatto: ASSENTE — Il coinvolgimento Ente Parco deve includere valutazione
     ripercussioni sulla sentieristica turistica
   ✓ Eventuale percorso alternativo: SUGGERITO specificare se esiste rotta secondaria disponibile

5. ASPETTI IDROGEOLOGICI
   ✓ Riferimento a documento tecnico di sopralluogo: PRESENTE (24/03/2026 Protezione Civile)
     — OK
   ✓ Valutazione rischio: ADEGUATA (cedimento 1,5-2,0 m, 380 mq) — COERENTE con art. 54
   ✓ Periodictà monitoraggio: SUGGERITO includere "rivalutazione area ogni 30 giorni fino a
     stabilizzazione substrato"

6. RISERVE NORMATIVE
   ⚠ NOTA CRITICA: Ordinanza ordinaria vs. Ordinanza contingibile e urgente
     L'art. 54 D.Lgs. 267/2000 per "urgenza e motivi di sicurezza pubblica" consente
     ordinanza ordinaria, non obbliga ordinanza contingibile/urgente. Tuttavia, dato il
     rischio geomorfologico acuto, è APPROPRIATO procedere come ordinanza ordinaria con
     revisione a breve termine anzichè contingibile.

ESITO REVISIONE: ✓ APPROVAZIONE CON INTEGRAZIONI MINORI
```

"Per applicare le correzioni alla bozza risponda **applica le note del revisore**."

---

### TURNO 5 — Applicazione note del revisore alla bozza
**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**
La LLM rilegge la bozza originale e il report del revisore, applica tutte le correzioni:
- Integrazione coordinate geografiche UTM 32N (zona Bocca di Magra: ca. 542.000 E, 4.840.000 N)
- Aggiunta riferimento standard D.M. Infrastrutture 30/11/1999 per segnaletica
- Modifica durata: "La presente ordinanza rimane in vigore per 60 giorni dalla data di
  sottoscrizione. Entro 30 giorni, sarà effettuato sopralluogo congiunto (Ente Parco
  Regionale + Ufficio Protezione Civile) per valutazione stabilizzazione. Ordinanza soggetta
  a rinnovo o revoca in base agli esiti del monitoraggio"
- Aggiunta paragrafo: "Il Sindaco dispone rivalutazione area interessata ogni 30 giorni fino
  a stabilizzazione substrato, con comunicazione ad Ente Parco e Prefettura"
- Aggiunta valutazione impatto: "Ente Parco Regionale valuterà opportunità di percorso
  alternativo temporaneo per utenza escursionistica"
- Mantenimento di tutte le comunicazioni ai soggetti pubblici e privati

"Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella permanente risponda **salva**."

---

### TURNO 6 — Salvataggio
**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**
Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato (PDF, DOCX, ODT).
Il file viene salvato con nomenclatura: `ORD_8_2026_Sentiero432_Chiusura_28032026.pdf`
L'agente conferma:

"Ordinanza n. 8/2026 salvata in [percorso selezionato].
Prossimi passi automatizzati dal sistema:
✓ Generazione email di comunicazione a Ente Parco (pronta per firma Sindaco)
✓ Generazione avviso per albo pretorio on-line
✓ Reminder automatico revisione area: 28 aprile 2026 (30 giorni)
✓ Reminder automatico scadenza ordinanza: 27 maggio 2026 (60 giorni)
Ordinanza pronta per firma del Sindaco Andrea De Ranieri."

---

## NOTE DI TEST

1. **Verifica coordinamento Ente Parco**: L'agente deve riconoscere che il sentiero 432
   ricade interamente nel Parco Regionale Montemarcello-Magra-Vara, quindi comunicazione
   all'Ente Parco è OBBLIGATORIA (non facoltativa). Il revisore deve evidenziare questa
   criticità se assente.

2. **Geomorfologia e tempistiche**: La frana descritta (cedimento 1,5-2,0 m su 380 mq)
   è substrato di una ordinanza ordinaria a breve termine (60 gg) con riesame, non di una
   ordinanza contingibile/urgente permanente. L'agente deve spiegare questa distinzione.

3. **Segnaletica e responsabilità civile**: La revisione deve evidenziare che omissione
   di segnaletica adeguata secondo D.M. Infrastrutture espone il Comune a responsabilità
   civile. Cartelli rossi standard sono REQUISITO normativo, non facoltà.
