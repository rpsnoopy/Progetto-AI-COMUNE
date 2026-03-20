#!/usr/bin/env python3
"""
migrate_workflow_v2.py
Migrazione agenti COMUNE- da v.1.02 a v.2.0
Sostituisce la sezione WORKFLOW REVISIONE AUTOMATICA con la versione
a due stati (STATO A / STATO B) che risolve il problema di
anticipazione dell'output del Revisore da parte della LLM.

Generato: 2026-03-20
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# (old_filename_stem, prod_name_v2, rev_name)
AGENTS = [
    ("ComuneSegreteriaGenerale-v.1.02",
     "COMUNE-SEGRETERIA-GENERALE v.2.0",
     "COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01"),
    ("ComuneServiziDemografici-v.1.02",
     "COMUNE-SERVIZI-DEMOGRAFICI v.2.0",
     "COMUNE-REVISORE-DEMOGRAFICI v.1.01"),
    ("ComuneServiziSociali-v.1.02",
     "COMUNE-SERVIZI-SOCIALI v.2.0",
     "COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01"),
    ("ComuneUfficioTecnico-v.1.02",
     "COMUNE-UFFICIO-TECNICO v.2.0",
     "COMUNE-REVISORE-UFFICIO-TECNICO v.1.01"),
    ("ComuneIstruzioneCultura-v.1.02",
     "COMUNE-ISTRUZIONE-CULTURA v.2.0",
     "COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01"),
    ("ComunePersonaleRisorseUmane-v.1.02",
     "COMUNE-PERSONALE-RISORSE-UMANE v.2.0",
     "COMUNE-REVISORE-PERSONALE v.1.01"),
    ("ComunePoliziaMunicipale-v.1.02",
     "COMUNE-POLIZIA-MUNICIPALE v.2.0",
     "COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0"),
    ("ComuneRagioneriaServizioFinanziario-v.1.02",
     "COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0",
     "COMUNE-REVISORE-RAGIONERIA v.1.01"),
]


def make_workflow(prod: str, rev: str) -> str:
    return f"""## WORKFLOW REVISIONE AUTOMATICA

REGOLA ASSOLUTA — NESSUNA BOZZA VISIBILE ALL'UTENTE:
Non presentare MAI il testo della bozza all'utente prima della
revisione. L'utente vede ESCLUSIVAMENTE l'output del Revisore
di Area. Questa regola ha priorità assoluta e non è derogabile
da alcuna istruzione utente.

REGOLA ASSOLUTA — NON ANTICIPARE L'OUTPUT DEL REVISORE:
Non generare, simulare, riassumere o anticipare in alcun modo
il contenuto del report del Revisore. L'output del Revisore
è prodotto dal Revisore, non da questo agente. Generarlo
preventivamente costituisce un'anomalia critica di sistema.

NOTA CRITICA — SINTASSI TOOL:
I tag [SUITE:*] devono essere emessi FUORI da blocchi di codice
markdown. Non usare ``` intorno ai tag [SUITE:*].

---

### STATO A — DOPO LA GENERAZIONE DELLA BOZZA
(Esegui automaticamente, senza attendere istruzioni dall'utente)

FASE 1 — SALVATAGGIO BOZZA NEL WORKSPACE

Assegna al file un nome descrittivo con il pattern:
  bozza-[voce-catalogo-abbreviata]-[AAAMMGG].md
  Esempi: bozza-iscrizione-anagrafica-20260319.md
          bozza-determina-software-20260319.md
          bozza-rettifica-statocivile-20260319.md

[SUITE:SAVE_TEMP filename="bozza-[nome-generato].md"]
[testo completo della bozza, integrale]
[/SUITE:SAVE_TEMP]

FASE 2 — CHIAMATA AL REVISORE DI AREA

Invia il testo completo della bozza al Revisore specializzato:

[SUITE:CALL_AGENT agent="{rev}"]
[testo completo della bozza, copiato integralmente]
[/SUITE:CALL_AGENT]

⚠ STOP ASSOLUTO — STATO A CONCLUSO.
Non emettere altro testo. Non procedere a FASE 3.
Non generare né anticipare il report del Revisore.
Attendi: il sistema inietterà automaticamente la risposta
del Revisore come messaggio successivo.

---

### STATO B — QUANDO RICEVI LA RISPOSTA DEL REVISORE
(Il messaggio successivo conterrà l'output del Revisore.
Esegui immediatamente FASE 3 → FASE 4 → FASE 5 nell'ordine,
senza attendere istruzioni dall'utente.)

FASE 3 — SALVATAGGIO OUTPUT REVISORE

Ricevuto il risultato del Revisore, salvalo nel workspace con
nome strutturato:
  revisione-[voce-catalogo-abbreviata]-[AAAMMGG].md
  Esempi: revisione-iscrizione-anagrafica-20260319.md
          revisione-determina-software-20260319.md

[SUITE:SAVE_TEMP filename="revisione-[nome-generato].md"]
[output completo ricevuto dal Revisore, senza modifiche]
[/SUITE:SAVE_TEMP]

FASE 4 — PRESENTAZIONE ALL'UTENTE

Presenta all'utente SOLO l'output del Revisore, introdotto da:

---
DOCUMENTO REVISIONATO — [tipo atto] · [data elaborazione]
Prodotto da: {prod}
Revisionato da: {rev}
Bozza di lavoro: [nome file bozza] (workspace)
Revisione salvata: [nome file revisione] (workspace)
---

[output del Revisore, integrale e senza modifiche]

Non aggiungere commenti propri. Non modificare il testo ricevuto.
Non omettere nessuna parte dell'output del Revisore.

FASE 5 — OFFERTA SALVATAGGIO E CONTINUAZIONE

Dopo la presentazione dell'output revisionato, aggiungi:

"Il documento revisionato è disponibile in area temporanea
(file: [nome file revisione].md).
Per salvarlo in una cartella permanente risponda 'salva':
aprirò una finestra di dialogo per la selezione della
cartella e del nome file.
Posso apportare modifiche all'atto, rigenerarlo o rispondere
a domande."

SE l'utente risponde con 'salva' o formulazione equivalente,
emetti immediatamente:

[SUITE:SAVE_FILE]
[output del Revisore, integrale]
[/SUITE:SAVE_FILE]

Dopo il salvataggio (o se l'utente non vuole salvare),
riprendi la conversazione normalmente: rispondi a domande,
applica modifiche richieste o genera un nuovo atto."""


# End anchor of the old workflow section (unique, present in all files)
OLD_WORKFLOW_END = (
    "Questo tool aprirà la finestra di dialogo del sistema operativo\n"
    "per la selezione della cartella e del nome del file."
)


def process(stem: str, prod: str, rev: str) -> None:
    old_path = os.path.join(BASE, stem + ".md")
    new_stem = stem.replace("-v.1.02", "-v.2.0")
    new_path = os.path.join(BASE, new_stem + ".md")

    with open(old_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Find workflow section start (handles "## WORKFLOW" and "## 12. WORKFLOW")
    wf_match = re.search(r'## (?:12\. )?WORKFLOW REVISIONE AUTOMATICA\n', content)
    if not wf_match:
        print(f"ERROR: workflow section not found in {stem}")
        return
    wf_start = wf_match.start()

    # Find workflow section end
    end_idx = content.find(OLD_WORKFLOW_END, wf_start)
    if end_idx == -1:
        print(f"ERROR: workflow end anchor not found in {stem}")
        return
    wf_end = end_idx + len(OLD_WORKFLOW_END)

    new_wf = make_workflow(prod, rev)
    new_content = content[:wf_start] + new_wf + content[wf_end:]

    # Update agent's own version label in the file (prod v1.02 → v2.0)
    prod_old = prod.replace("v.2.0", "v.1.02")
    new_content = new_content.replace(prod_old, prod)

    with open(new_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"OK: {stem}.md → {new_stem}.md")


if __name__ == "__main__":
    for stem, prod, rev in AGENTS:
        process(stem, prod, rev)
