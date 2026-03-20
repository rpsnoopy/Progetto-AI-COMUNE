#!/usr/bin/env python3
"""
fix_stato_b.py
Rimuove SAVE_TEMP da STATO B in tutti i file agenti COMUNE- v.2.0.

PROBLEMA: STATO B contiene SAVE_TEMP prima della presentazione della revisione.
Ogni comando [SUITE:*] forza un ulteriore turno nel ReAct loop (AgentRuntime.vb:161).
Il testo di presentazione della revisione finisce in un turno intermedio (non FinalResponse)
e viene scartato. L'utente non vede mai il testo revisionato.

FIX: Eliminare SAVE_TEMP da STATO B. La presentazione diventa un turno senza comandi
(FinalResponse) e viene mostrata all'utente. Il salvataggio resta disponibile
su richiesta esplicita ('salva') tramite SAVE_FILE — turno separato.
"""

import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = [
    "ComuneSegreteriaGenerale-v.2.0.md",
    "ComuneServiziDemografici-v.2.0.md",
    "ComuneServiziSociali-v.2.0.md",
    "ComuneUfficioTecnico-v.2.0.md",
    "ComuneIstruzioneCultura-v.2.0.md",
    "ComunePersonaleRisorseUmane-v.2.0.md",
    "ComunePoliziaMunicipale-v.2.0.md",
    "ComuneRagioneriaServizioFinanziario-v.2.0.md",
]


def fix_stato_b(content: str) -> str:
    # 1. Update STATO B header: "FASE 2 → FASE 3 → FASE 4" → "FASE 2 → FASE 3"
    content = content.replace(
        "Esegui immediatamente FASE 2 → FASE 3 → FASE 4 nell'ordine,",
        "Esegui immediatamente FASE 2 → FASE 3 nell'ordine,"
    )

    # 2. Remove entire FASE 2 SAVE_TEMP block (SALVATAGGIO OUTPUT REVISORE)
    #    Pattern: "FASE 2 — SALVATAGGIO OUTPUT REVISORE\n\n[SUITE:SAVE_TEMP...][/SUITE:SAVE_TEMP]\n\n"
    content = re.sub(
        r'FASE 2 — SALVATAGGIO OUTPUT REVISORE\n\n'
        r'\[SUITE:SAVE_TEMP filename="revisione-\[nome-generato\]\.md"\]\n'
        r'\[output completo ricevuto dal Revisore, senza modifiche\]\n'
        r'\[/SUITE:SAVE_TEMP\]\n\n',
        '',
        content
    )

    # 3. Rename FASE 3 → FASE 2 (presentazione), FASE 4 → FASE 3 (offerta salvataggio)
    #    Only in STATO B context (after the removal, these are the remaining phases)
    #    Use targeted strings to avoid touching STATO A phases
    content = content.replace(
        "FASE 3 — PRESENTAZIONE REVISIONE ALL'UTENTE",
        "FASE 2 — PRESENTAZIONE REVISIONE ALL'UTENTE"
    )
    content = content.replace(
        "FASE 4 — OFFERTA SALVATAGGIO E CONTINUAZIONE",
        "FASE 3 — OFFERTA SALVATAGGIO E CONTINUAZIONE"
    )

    # 4. Remove "Bozza di lavoro" and "Revisione salvata" lines from the
    #    REVISIONE COMPLETATA header block (no longer saved to workspace)
    content = re.sub(
        r'Bozza di lavoro: \[nome file bozza\] \(workspace\)\n'
        r'Revisione salvata: \[nome file revisione\] \(workspace\)\n',
        '',
        content
    )

    # 5. Update the "Esegui immediatamente" reference in the intro if still using old numbering
    content = content.replace(
        "Esegui immediatamente FASE 2 → FASE 3 nell'ordine,\nsenza attendere istruzioni dall'utente.)",
        "Esegui immediatamente FASE 2 → FASE 3 nell'ordine,\nsenza attendere istruzioni dall'utente.)"
    )

    return content


def process(filename: str) -> None:
    path = os.path.join(BASE, filename)
    if not os.path.exists(path):
        print(f"SKIP (not found): {filename}")
        return

    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    fixed = fix_stato_b(original)

    if fixed == original:
        print(f"NO CHANGE: {filename}")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(fixed)

    # Quick verification
    if "FASE 2 — SALVATAGGIO OUTPUT REVISORE" in fixed:
        print(f"ERROR: SALVATAGGIO still present in {filename}")
    elif "SAVE_TEMP" in fixed.split("STATO B")[1] if "STATO B" in fixed else True:
        # Check STATO B section only
        stato_b_start = fixed.find("### STATO B")
        if stato_b_start != -1 and "SAVE_TEMP" in fixed[stato_b_start:]:
            print(f"ERROR: SAVE_TEMP still present in STATO B of {filename}")
        else:
            print(f"OK: {filename}")
    else:
        print(f"OK: {filename}")


if __name__ == "__main__":
    for fn in FILES:
        process(fn)
