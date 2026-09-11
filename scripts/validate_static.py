"""Check local links and downloadable ZIP integrity."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import zipfile

ROOT = Path(__file__).resolve().parents[1]
missing = []

class LinkParser(HTMLParser):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def handle_starttag(self, _tag, attrs):
        values = dict(attrs)
        for key in ("href", "src"):
            value = values.get(key, "")
            parsed = urlparse(value)
            if not value or parsed.scheme or value.startswith(("#", "mailto:")):
                continue
            target = (self.page.parent / parsed.path).resolve()
            if parsed.path.endswith("/") or target.is_dir():
                target /= "index.html"
            if not target.exists():
                missing.append((str(self.page.relative_to(ROOT)), value))

pages = list(ROOT.rglob("*.html"))
for page in pages:
    LinkParser(page).feed(page.read_text(encoding="utf-8"))

archive = ROOT / "assets/benchmark-familiarity/results.zip"
with zipfile.ZipFile(archive) as bundle:
    bad_zip_member = bundle.testzip()
    bundle_members = bundle.namelist()

print(f"HTML pages: {len(pages)}")
print(f"Missing local links: {missing}")
print(f"Result bundle files: {len(bundle_members)}")
print(f"ZIP integrity failure: {bad_zip_member}")
if missing or bad_zip_member:
    raise SystemExit(1)
