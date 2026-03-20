#!/usr/bin/env python3
"""
fix_fasi_revisione.py
Corregge FASE 3 e FASE 4 in tutti gli agenti v.2.0:
  - FASE 3: il revisore produce un REPORT con note (non un documento rivisto)
  - FASE 4 (nuova): la LLM applica le note del report alla bozza originale
  - FASE 5 (ex FASE 4): salvataggio del documento finale corretto
"""
import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

FILES = sorted(glob.glob(os.path.join(BASE, "Comune*-v.2.0.md")))


# Template nuovo FASE 3 + FASE 4 + FASE 5
# {PROD} e {REV} vengono estratti dal file originale e sostituiti
NEW_FASI = """\
### FASE 3 — PRESENTAZIONE REPORT DI REVISIONE

Quando ricevi l'output del Revisore, presentalo INTEGRALMENTE
nella risposta. Non abbreviare, modificare o commentare.
Preponi esclusivamente questa riga di intestazione:

---
REPORT DI REVISIONE NORMATIVA — [tipo atto] · [data elaborazione]
Prodotto da: {PROD}
Revisionato da: {REV}
---

[output del Revisore, integrale e senza modifiche]

Dopo il report, aggiungi:

"Report di revisione ricevuto. Per applicare le correzioni
indicate alla bozza risponda **applica le note del revisore**."

---

### FASE 4 — APPLICAZIONE NOTE ALLA BOZZA (utente risponde 'applica le note del revisore')

Rileggi la bozza originale e il report del Revisore.
Applica tutte le correzioni, integrazioni e modifiche indicate
nel report, generando la versione finale corretta dell'atto.

Presenta la versione finale all'utente integralmente e aggiungi:

"Atto aggiornato con le indicazioni del revisore. Per salvarlo
in cartella permanente risponda **salva**."

---

### FASE 5 — SALVATAGGIO DOCUMENTO FINALE (utente risponde 'salva')

Emetti immediatamente con il testo della versione finale corretta:

[SUITE:SAVE_FILE]
[versione finale dell'atto con tutte le correzioni applicate]
[/SUITE:SAVE_FILE]

Dopo il salvataggio, riprendi la conversazione normalmente:
rispondi a domande, applica modifiche richieste o genera un
nuovo atto.
"""

# Ancora di inizio: header FASE 3
FASE3_START = "### FASE 3 — PRESENTAZIONE OUTPUT DEL REVISORE\n"

# Ancora di fine (inclusiva): ultima riga del vecchio FASE 4
FASE4_END = (
    "Dopo il salvataggio, riprendi la conversazione normalmente:\n"
    "rispondi a domande, applica modifiche richieste o genera un\n"
    "nuovo atto.\n"
)

# Regex per estrarre le righe Prodotto/Revisionato
PROD_RE = re.compile(r"Prodotto da: (.+)")
REV_RE  = re.compile(r"Revisionato da: (.+)")


def process(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    start_idx = content.find(FASE3_START)
    if start_idx == -1:
        print(f"SKIP (FASE 3 non trovata): {os.path.basename(path)}")
        return

    end_idx = content.find(FASE4_END, start_idx)
    if end_idx == -1:
        print(f"SKIP (fine FASE 4 non trovata): {os.path.basename(path)}")
        return
    end_idx += len(FASE4_END)

    old_block = content[start_idx:end_idx]

    # Estrai Prodotto da / Revisionato da
    prod_m = PROD_RE.search(old_block)
    rev_m  = REV_RE.search(old_block)
    if not prod_m or not rev_m:
        print(f"SKIP (nomi agente non trovati): {os.path.basename(path)}")
        return

    prod = prod_m.group(1).strip()
    rev  = rev_m.group(1).strip()

    new_block = NEW_FASI.replace("{PROD}", prod).replace("{REV}", rev)
    new_content = content[:start_idx] + new_block + content[end_idx:]

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

    # Verifica
    issues = []
    if "PRESENTAZIONE OUTPUT DEL REVISORE" in new_content:
        issues.append("vecchio header FASE 3 ancora presente")
    if "output del Revisore, integrale]" in new_content[new_content.find("FASE 5"):] if "FASE 5" in new_content else False:
        issues.append("FASE 5 salva ancora output revisore grezzo")
    if "FASE 4 — APPLICAZIONE NOTE" not in new_content:
        issues.append("FASE 4 applicazione note mancante")
    if "FASE 5 — SALVATAGGIO" not in new_content:
        issues.append("FASE 5 mancante")

    if issues:
        print(f"WARN ({os.path.basename(path)}): {', '.join(issues)}")
    else:
        print(f"OK: {os.path.basename(path)}  [{prod}]")


if __name__ == "__main__":
    if not FILES:
        print("Nessun file Comune*-v.2.0.md trovato.")
    for p in FILES:
        process(p)
