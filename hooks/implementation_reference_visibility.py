"""Keep directly linked agent references out of the website search index.

Only MkDocs page metadata changes. The Markdown remains available to the
separate agent knowledge builder, which does not run website hooks.
"""


def on_page_markdown(markdown, *, page, config, files):
    if page.file.src_uri.startswith("pro/reference/"):
        page.meta["search"] = {**(page.meta.get("search") or {}), "exclude": True}
    return markdown
