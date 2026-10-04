"""Scarica la sitemap da digitalrunner.it e la salva qui solo se è valida.

Il sito è su Vercel, e da maggio 2026 Search Console non legge le sitemap servite da Vercel.
Questa copia identica, pubblicata da GitHub Pages su sitemap.digitalrunner.it, è quella
indicata nel robots.txt del sito.
"""
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

SORGENTE = "https://digitalrunner.it/sitemap.xml"
NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

req = urllib.request.Request(SORGENTE, headers={"User-Agent": "digitalrunner-sitemap-mirror"})
with urllib.request.urlopen(req, timeout=30) as r:
    dati = r.read()

radice = ET.fromstring(dati)
url = [u.findtext(f"{NS}loc", "") for u in radice.findall(f"{NS}url")]
if radice.tag != f"{NS}urlset" or len(url) < 20:
    sys.exit(f"Sitemap sospetta ({radice.tag}, {len(url)} URL): non la sostituisco")
if any(not u.startswith("https://digitalrunner.it/") for u in url):
    sys.exit("Sitemap con URL fuori da digitalrunner.it: non la sostituisco")

file = Path(__file__).resolve().parent.parent / "sitemap.xml"
if file.exists() and file.read_bytes() == dati:
    print(f"Invariata ({len(url)} URL)")
else:
    file.write_bytes(dati)
    print(f"Aggiornata ({len(url)} URL)")
