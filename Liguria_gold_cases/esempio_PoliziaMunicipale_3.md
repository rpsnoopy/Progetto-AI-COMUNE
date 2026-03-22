# GOLD CASE — Area 7 · Polizia Municipale · Caso 3

## Atto: Comunicazione di Notizia di Reato — Truffa ai danni di anziano

**Agente:** COMUNE-POLIZIA-MUNICIPALE v.2.0
**Revisore:** COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0

---

## SEQUENZA DI TEST

### TURNO 1 — Domanda informativa

**INPUT UTENTE:**
> La Polizia Municipale ha l'obbligo di trasmettere una notizia di reato
> alla Procura? In che forma e entro quanto tempo?

**RISPOSTA ATTESA (schema):**
L'agente illustra l'obbligo ex art. 347 c.p.p.: la PG (inclusa la Polizia
Municipale nella sua qualità di PG) ha l'obbligo di riferire senza ritardo
la notizia di reato al Pubblico Ministero, con la relativa documentazione.
La comunicazione avviene con rapporto scritto (CNR). Il ritardo ingiustificato
configura reato (art. 361 c.p. per il pubblico ufficiale). Indica che la PG
deve operare ex art. 55 c.p.p. e trasmettere anche in via telematica al
fascicolo informatico.

---

### TURNO 2 — Richiesta generazione atto

**INPUT UTENTE:**
> Genera la comunicazione di notizia di reato per una truffa ai danni di
> un anziano. Persona offesa: sig. Aldo Bruni, 82 anni, CF BRNLDA44A05A261H,
> Via Pascoli 3, Ameglia. Fatto: il 18/03/2026 si è presentato a casa
> sua un sedicente tecnico del gas che, con il pretesto di un controllo,
> lo ha convinto a consegnare € 800,00 in contanti e alcuni monili in oro.
> Ignoto il soggetto attivo. Querela sporta il 20/03/2026 prot. 4892.
> Verbalizzazione dell'Ag. Sc. Lucia Riva (matr. 021), con raccolta deposizioni
> e acquisizione immagini telecamere di zona. Fattispecie: art. 640 c.p.
> (truffa), art. 61 n. 5 c.p. (aggravante: vittima anziana). CNR n. 12/2026.

**RISPOSTA ATTESA (schema):**
L'agente genera: intestazione alla Procura della Repubblica della Spezia, oggetto,
dati della persona offesa, descrizione del fatto, qualificazione giuridica
(art. 640 c.p. + aggravante art. 61 n. 5), atti allegati (verbale di querela,
deposizioni, immagini telecamere), autore ignoto (X), richiesta di iscrivere
la notizia nel registro degli atti (art. 335 c.p.p.), firma ufficiale.
Schema: [CNR n. 12/2026 — testo generato]

Al termine: "Bozza pronta. Come desidera procedere?
• risponda **salva** per salvare in cartella permanente
• risponda **revisione** per richiedere la revisione normativa specializzata"

---

### TURNO 3 — Interazione / modifica

**INPUT UTENTE:**
> Le telecamere di una farmacia vicina hanno ripreso il soggetto attivo:
> uomo, circa 40 anni, capelli scuri, giacca grigia, auto bianca
> (targa parziale AB***). Aggiungi queste informazioni nella descrizione
> del soggetto attivo.

**RISPOSTA ATTESA (schema):**
L'agente aggiorna la sezione soggetto attivo: "Il soggetto attivo, allo stato
non identificato, risulta dalle immagini acquisite dalle telecamere della
farmacia 'Farmacia Centrale' sita in Via Aurelia 12: individuo di sesso maschile,
apparente età 35-45 anni, corporatura media, capelli scuri, abbigliamento con
giacca grigia, visto allontanarsi a bordo di autovettura di colore bianco con
targa parzialmente rilevata 'AB***' (immagini in all. B)."
Ripresenta la bozza aggiornata.

---

### TURNO 4 — Richiesta revisione normativa

**INPUT UTENTE:**
> revisione

**RISPOSTA ATTESA (schema):**
L'agente invia la bozza al revisore. Ricevuta la risposta, presenta:

```
REVISIONE NORMATIVA — CNR n. 12/2026
Prodotto da: COMUNE-POLIZIA-MUNICIPALE v.2.0
Revisionato da: COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0
---
[Output del revisore: verifica art. 347 c.p.p. (obbligo di riferire senza
ritardo); controllo qualificazione giuridica art. 640 c.p. (truffa) con
aggravante art. 61 n. 5 c.p. (approfittamento di condizioni di minorata
difesa — anziano); nota su possibile concorso art. 640-bis c.p. se importo
rilevante; verifica completezza allegati (querela, verbale, immagini);
controllo che la targa parziale sia stata già inoltrata al CED interforze;
nota su privacy immagini telecamere (autorizzazione o sequestro in atti).]
```

"Per applicare le correzioni alla bozza risponda **applica le note del revisore**."

---


---

### TURNO 5 — Applicazione note del revisore alla bozza

**INPUT UTENTE:**
> applica le note del revisore alla bozza

**RISPOSTA ATTESA (schema):**
La LLM rilegge la bozza originale e il report del revisore, applica tutte le
correzioni e le integrazioni indicate e genera la versione finale dell'atto,
che presenta all'utente integralmente.
Al termine aggiunge:

"Atto aggiornato con le indicazioni del revisore. Per salvarlo in cartella
permanente risponda **salva**."

### TURNO 6 — Salvataggio

**INPUT UTENTE:**
> salva

**RISPOSTA ATTESA (schema):**
Si apre la finestra AgentSaveDialog. L'utente seleziona cartella e formato.
Il file viene salvato. L'agente conferma.

---

## NOTE DI TEST

- Verificare che la bozza indichi correttamente la Procura competente (La Spezia)
  e l'art. 335 c.p.p. per l'iscrizione nel registro.
- Verificare che il revisore segnali la questione della privacy delle immagini
  acquisite dalle telecamere private (necessità di autorizzazione o sequestro).
