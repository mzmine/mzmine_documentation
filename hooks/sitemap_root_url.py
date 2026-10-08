"""Add the bare site root to sitemap.xml so version switching keeps the page.

The version selector of mkdocs-material keeps the reader on the page they are
on when they switch to another version. To do that it downloads the other
version's ``sitemap.xml``, derives its base URL as the longest common prefix of
all ``<loc>`` entries, and only continues when that base URL is itself listed in
the sitemap.

This documentation is built with ``use_directory_urls: false``, so the start
page is listed as ``.../index.html`` and the bare ``.../`` never appears. The
check therefore fails and every version switch silently drops the reader on the
start page of the other version. Listing the bare URL as well restores it, and
it is a real URL: a request for a directory is answered with its index.html.
"""

import gzip
import io
import os

SITEMAP = "sitemap.xml"


def on_post_build(config):
    site_url = config.get("site_url")
    if not site_url:
        return
    if not site_url.endswith("/"):
        site_url += "/"

    path = os.path.join(config["site_dir"], SITEMAP)
    if not os.path.exists(path):
        return

    # newline="" everywhere, so the file and its gzipped copy stay byte identical
    with open(path, encoding="utf-8", newline="") as handle:
        sitemap = handle.read()

    entry = "<loc>" + site_url + "</loc>"
    if entry in sitemap or "</urlset>" not in sitemap:
        return

    newline = "\r\n" if "\r\n" in sitemap else "\n"
    block = "    <url>" + newline + "         " + entry + newline + "    </url>" + newline
    sitemap = sitemap.replace("</urlset>", block + "</urlset>")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(sitemap)

    # keep the gzipped copy mkdocs writes next to it in sync (mtime=0 like mkdocs)
    gz_path = path + ".gz"
    if os.path.exists(gz_path):
        buffer = io.BytesIO()
        with gzip.GzipFile(fileobj=buffer, mode="wb", mtime=0) as handle:
            handle.write(sitemap.encode("utf-8"))
        with open(gz_path, "wb") as handle:
            handle.write(buffer.getvalue())
