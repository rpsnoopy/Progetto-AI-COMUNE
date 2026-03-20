#!/usr/bin/env python3
"""
make_v21.py
1. Crea sottodirectory 2.0/ e vi archivia i file v.2.0 correnti (snapshot)
2. Crea file v.2.1 nella root: rinomina i file e aggiorna le occorrenze
   della versione dell'agente produttore (Comune*) da v.2.0 → v.2.1.
   NON tocca le versioni dei Revisori (v.1.xx).
"""
import os, re, shutil, glob

BASE = os.path.dirname(os.path.abspath(__file__))
DIR_20 = os.path.join(BASE, "2.0")

# File agenti produttori v2.0
AGENT_FILES = sorted(glob.glob(os.path.join(BASE, "Comune[^R]*-v.2.0.md")))
# index.md
INDEX_SRC = os.path.join(BASE, "index.md")

# ── 1. Crea dir 2.0 e archivia snapshot ────────────────────────────────────
os.makedirs(DIR_20, exist_ok=True)
for src in AGENT_FILES:
    dst = os.path.join(DIR_20, os.path.basename(src))
    shutil.copy2(src, dst)
    print(f"  archivio → 2.0/{os.path.basename(dst)}")
if os.path.exists(INDEX_SRC):
    shutil.copy2(INDEX_SRC, os.path.join(DIR_20, "index.md"))
    print(f"  archivio → 2.0/index.md")

print()

# ── 2. Costruisci le versioni v.2.1 ────────────────────────────────────────
# Regex: sostituisce v.2.0 SOLO nei nomi degli agenti produttori
# (es. "COMUNE-SEGRETERIA-GENERALE v.2.0") ma NON nei revisori ("v.1.xx")
# né nelle parti di testo generiche.
# Pattern: nome agente produttore = "COMUNE-" seguito da parole maiuscole/trattini
# che non inizia con "REVISORE-", seguito da " v.2.0"
PROD_VER_RE = re.compile(
    r'(COMUNE-(?!REVISORE-)[\w-]+ )v\.2\.0'
)

for src in AGENT_FILES:
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()

    # Sostituisci versione produttore
    new_content = PROD_VER_RE.sub(r'\g<1>v.2.1', content)

    # Nuovo nome file
    new_filename = os.path.basename(src).replace("-v.2.0.md", "-v.2.1.md")
    dst = os.path.join(BASE, new_filename)

    with open(dst, "w", encoding="utf-8") as f:
        f.write(new_content)

    count = len(PROD_VER_RE.findall(content))
    print(f"  v.2.1 → {new_filename}  ({count} sostituz.)")

# ── 3. Aggiorna index.md con i nuovi nomi v.2.1 ────────────────────────────
print()
if os.path.exists(INDEX_SRC):
    with open(INDEX_SRC, "r", encoding="utf-8") as f:
        idx = f.read()
    idx_new = idx.replace("-v.2.0.md", "-v.2.1.md")
    with open(INDEX_SRC, "w", encoding="utf-8") as f:
        f.write(idx_new)
    print(f"  index.md aggiornato → riferimenti v.2.1")

print("\nFatto.")
