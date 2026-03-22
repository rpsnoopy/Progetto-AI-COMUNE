#!/usr/bin/env python3
"""
fix_turni.py
Corregge tutti i gold case: il revisore produce un REPORT con note,
non un documento rivisto. Aggiunge TURNO 5 (applica note) e rinomina
il vecchio TURNO 5 (salvataggio) in TURNO 6.
"""
import os, glob

BASE = os.path.dirname(os.path.abspath(__file__))

# Testo da sostituire alla fine di TURNO 4 (offerta salvataggio errata)
OLD_OFFER = '"Per salvare il documento revisionato in cartella permanente risponda \'salva\'."'
NEW_OFFER  = '"Per applicare le correzioni alla bozza risponda **applica le note del revisore**."'

# Testo da inserire tra fine TURNO 4 e TURNO 6 (salvataggio)
NEW_TURNO5 = """
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

"""

OLD_T5_HEADER = "### TURNO 5 — Salvataggio"
NEW_T6_HEADER = "### TURNO 6 — Salvataggio"

files = sorted(glob.glob(os.path.join(BASE, "esempio_*.md")))
if not files:
    print("Nessun file trovato.")
    exit(1)

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # 1. Sostituisci l'offerta errata di salvataggio in TURNO 4
    if OLD_OFFER in content:
        content = content.replace(OLD_OFFER, NEW_OFFER)
        changed = True
    else:
        print(f"WARN: offerta salvataggio non trovata in {os.path.basename(path)}")

    # 2. Rinomina TURNO 5 → TURNO 6
    if OLD_T5_HEADER in content:
        content = content.replace(OLD_T5_HEADER, NEW_T6_HEADER)
        changed = True
    else:
        print(f"WARN: TURNO 5 header non trovato in {os.path.basename(path)}")

    # 3. Inserisci il nuovo TURNO 5 prima di TURNO 6
    if NEW_T6_HEADER in content and NEW_TURNO5.strip() not in content:
        content = content.replace(NEW_T6_HEADER, NEW_TURNO5 + NEW_T6_HEADER)
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"OK: {os.path.basename(path)}")
    else:
        print(f"NO CHANGE: {os.path.basename(path)}")
