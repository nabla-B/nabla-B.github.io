"""Regenerate the QR codes of the digital business card (needs segno):

    uv run --with segno python3 make_qr.py

The QR codes point at the language-specific business-card URLs and are committed as static SVGs.
"""
import os, segno
from build import LANGS, url
root = os.path.dirname(os.path.abspath(__file__))
for lang in LANGS:
    qr = segno.make(url(lang, "visitenkarte"), error="m")
    qr.save(os.path.join(root, "assets", "img", f"qr-businesscard-{lang}.svg"), scale=8, border=2, dark="#323942")
    print("wrote qr-businesscard-%s.svg" % lang)
