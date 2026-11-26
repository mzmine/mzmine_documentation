"""Prepare the old guide addresses for the existing Pages root publisher."""

from pathlib import Path
import re


SITE_PREFIX = "/mzmine_documentation/latest/"
SITE_ORIGIN = "https://mzmine.github.io"
PAGES_ROOT = Path(".github/pages-root")
MANIFEST = Path(__file__).with_name("legacy-guide-paths.txt")

# One path per line from the last unversioned sitemap (gh-pages dd3e8f50).
# A second path can specify a replacement when a current guide is renamed.
for line in MANIFEST.read_text(encoding="utf-8").splitlines():
    old, *replacement = line.split()
    target = replacement[0] if replacement else old
    if len(replacement) > 1 or not all(
        re.fullmatch(r"(?:[A-Za-z0-9_][-\w.]*/)*[A-Za-z0-9_][-\w.]*\.html", path, re.ASCII)
        for path in (old, target)
    ):
        raise SystemExit(f"Invalid guide mapping: {line}")
    if old in {"index.html", "404.html"} or old.split("/")[0] == "latest" or old[0].isdigit():
        raise SystemExit(f"Reserved Pages path: {old}")
    if not (Path("site") / target).is_file():
        raise SystemExit(f"Missing destination for {old}: site/{target}")

    href = SITE_PREFIX + target
    page = PAGES_ROOT / old
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Guide moved | mzmine documentation</title>
  <link rel="canonical" href="{SITE_ORIGIN}{href}">
  <meta http-equiv="refresh" content="0; url={href}">
  <script>
    if (location.search || location.hash) {{
      location.replace("{href}" + location.search + location.hash);
    }}
  </script>
</head>
<body><p>This guide has moved. <a href="{href}">Open the current mzmine guide</a>.</p></body>
</html>
""", encoding="utf-8")
