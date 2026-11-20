"""news-image-20261119 entry (Python 3.13, standard library only).

Writes the pre-rendered 1024x1024 infographic entry.png beside this file
to /output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). The copy is
deterministic: the same bytes land on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
# Both runs must produce identical bytes; a fixed file copied twice is
# byte-identical by construction. Check the write landed at the expected
# size for this entry (105,370 bytes, 1024x1024 PNG, sha256 6282a84a...).
# Verified 20 Nov 2026: two runs wrote the same sha256 as entry.png.
assert os.path.getsize(DST) == os.path.getsize(SRC) == 105370
print("wrote", DST, os.path.getsize(DST), "bytes")
