#!/usr/bin/env python3
"""
fix_workflow_v3.py  —  Workflow COMUNE- v.3.0

LOGICA:
  1. LLM genera bozza → FinalResponse (zero comandi): mostra bozza + chiede
     "salva o revisione?"
  2. Utente risponde "salva"  → SAVE_FILE con bozza
  3. Utente risponde "revisione" → SAVE_TEMP (bozza) + CALL_AGENT (reviewer)
     in un unico turno intermedio → output revisore iniettato → LLM copia
     verbatim in FinalResponse
  4. Utente risponde "salva" (dopo revisione) → SAVE_FILE con output revisore

Sostituisce tutta la sezione "## WORKFLOW REVISIONE AUTOMATICA" fino a
"⚠ RIEPILOGO REGOLE CRITICHE" (escluso) in ogni file v.2.0.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

# (filename, prod_name, rev_name)
AGENTS = [
    ("ComuneSegreteriaGenerale-v.2.0.md",
     "COMUNE-SEGRETERIA-GENERALE v.2.0",
     "COMUNE-REVISORE-SEGRETERIA-GENERALE v.1.01"),
    ("ComuneServiziDemografici-v.2.0.md",
     "COMUNE-SERVIZI-DEMOGRAFICI v.2.0",
     "COMUNE-REVISORE-DEMOGRAFICI v.1.01"),
    ("ComuneServiziSociali-v.2.0.md",
     "COMUNE-SERVIZI-SOCIALI v.2.0",
     "COMUNE-REVISORE-SERVIZI-SOCIALI v.1.01"),
    ("ComuneUfficioTecnico-v.2.0.md",
     "COMUNE-UFFICIO-TECNICO v.2.0",
     "COMUNE-REVISORE-UFFICIO-TECNICO v.1.01"),
    ("ComuneIstruzioneCultura-v.2.0.md",
     "COMUNE-ISTRUZIONE-CULTURA v.2.0",
     "COMUNE-REVISORE-ISTRUZIONE-CULTURA v.1.01"),
    ("ComunePersonaleRisorseUmane-v.2.0.md",
     "COMUNE-PERSONALE-RISORSE-UMANE v.2.0",
     "COMUNE-REVISORE-PERSONALE v.1.01"),
    ("ComunePoliziaMunicipale-v.2.0.md",
     "COMUNE-POLIZIA-MUNICIPALE v.2.0",
     "COMUNE-REVISORE-POLIZIA-MUNICIPALE v.1.0"),
    ("ComuneRagioneriaServizioFinanziario-v.2.0.md",
     "COMUNE-RAGIONERIA-SERVIZIO-FINANZIARIO v.2.0",
     "COMUNE-REVISORE-RAGIONERIA v.1.01"),
]


def make_workflow(prod: str, rev: str) -> str:
    return f"""\
## WORKFLOW GENERAZIONE ATTI E REVISIONE NORMATIVA

NOTA CRITICA — SINTASSI TOOL:
I tag [SUITE:*] devono essere emessi FUORI da blocchi di codice
markdown. Non usare ``` intorno ai tag [SUITE:*].

---

### FASE 1 — PRESENTAZIONE BOZZA ALL'UTENTE

Dopo aver generato la bozza, presentala INTEGRALMENTE all'utente.
Non emettere alcun tag [SUITE:*] in questo turno.
Concludi con:

"Bozza pronta. Come desidera procedere?
• risponda **salva** — per salvare il documento in cartella permanente
• risponda **revisione** — per richiedere la revisione normativa specializzata"

---

### FASE 2A — SALVATAGGIO PERMANENTE (utente risponde 'salva')

Emetti immediatamente:

[SUITE:SAVE_FILE]
[testo completo della bozza, integrale]
[/SUITE:SAVE_FILE]

---

### FASE 2B — REVISIONE NORMATIVA (utente risponde 'revisione')

Emetti nell'ordine, senza testo intermedio:

[SUITE:SAVE_TEMP filename="bozza-[nome-descrittivo]-[AAAMMGG].md"]
[testo completo della bozza, integrale]
[/SUITE:SAVE_TEMP]

[SUITE:CALL_AGENT agent="{rev}"]
[testo completo della bozza, integrale]
[/SUITE:CALL_AGENT]

Non emettere altro testo prima o dopo i tag.
Attendi: il sistema eseguirà i tool e inietterà la risposta
del Revisore come messaggio successivo.

---

### FASE 3 — PRESENTAZIONE OUTPUT DEL REVISORE

Quando ricevi l'output del Revisore, copialo INTEGRALMENTE
e VERBATIM nella risposta. Non abbreviare, modificare o
commentare il testo ricevuto. Non aggiungere commenti propri.
Preponi esclusivamente questa riga di intestazione:

---
REVISIONE NORMATIVA — [tipo atto] · [data elaborazione]
Prodotto da: {prod}
Revisionato da: {rev}
---

[output del Revisore, integrale e senza modifiche]

Dopo l'output del Revisore, aggiungi:

"Per salvare il documento revisionato in cartella permanente
risponda 'salva'."

---

### FASE 4 — SALVATAGGIO REVISIONE (utente risponde 'salva' dopo revisione)

Emetti immediatamente:

[SUITE:SAVE_FILE]
[output del Revisore, integrale]
[/SUITE:SAVE_FILE]

Dopo il salvataggio, riprendi la conversazione normalmente:
rispondi a domande, applica modifiche richieste o genera un
nuovo atto.

"""


# ─── Anchors ───────────────────────────────────────────────────────────────
# Start: any variant of the workflow header (old or new)
WF_START_RE = re.compile(
    r'^## WORKFLOW (?:REVISIONE AUTOMATICA|GENERAZIONE ATTI E REVISIONE NORMATIVA)\s*$',
    re.MULTILINE
)
# End: inclusive — last line of old workflow (same in all files), followed by \n
WF_END_ANCHOR = (
    "Dopo il salvataggio (o se l'utente non vuole salvare),\n"
    "riprendi la conversazione normalmente: rispondi a domande,\n"
    "applica modifiche richieste o genera un nuovo atto.\n"
)


def process(filename: str, prod: str, rev: str) -> None:
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    m = WF_START_RE.search(content)
    if not m:
        print(f"ERROR: workflow header not found in {filename}")
        return

    wf_start = m.start()
    end_idx = content.find(WF_END_ANCHOR, wf_start)
    # Fallback: alternate ending used in ComuneSegreteriaGenerale after previous edits
    WF_END_ALT = (
        "Dopo il salvataggio, riprendi la conversazione normalmente:\n"
        "rispondi a domande, applica modifiche richieste o genera un\n"
        "nuovo atto.\n"
    )
    if end_idx == -1:
        end_idx = content.find(WF_END_ALT, wf_start)
        if end_idx == -1:
            print(f"ERROR: end anchor not found in {filename}")
            return
        wf_end = end_idx + len(WF_END_ALT)
    else:
        wf_end = end_idx + len(WF_END_ANCHOR)  # inclusive

    new_wf = make_workflow(prod, rev)
    new_content = content[:wf_start] + new_wf + content[wf_end:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verify: new workflow should have exactly 1 SAVE_TEMP (in FASE 2B)
    wf_section_start = new_content.find("## WORKFLOW")
    wf_section_end = new_content.find("# GOLDEN SAMPLE", wf_section_start)
    if wf_section_end == -1:
        wf_section_end = wf_section_start + 3000
    wf_section = new_content[wf_section_start:wf_section_end]

    issues = []
    if "STATO A" in wf_section or "STATO B" in wf_section:
        issues.append("STATO A/B still present")
    save_temp_count = wf_section.count("SAVE_TEMP")
    if save_temp_count != 1:
        issues.append(f"SAVE_TEMP count={save_temp_count} (expected 1)")
    call_agent_count = wf_section.count("CALL_AGENT")
    if call_agent_count != 1:
        issues.append(f"CALL_AGENT count={call_agent_count} (expected 1)")

    if issues:
        print(f"WARN ({filename}): {', '.join(issues)}")
    else:
        print(f"OK: {filename}")


if __name__ == "__main__":
    for fn, prod, rev in AGENTS:
        process(fn, prod, rev)
