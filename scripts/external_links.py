"""Laat navigatielinks die de site verlaten in een nieuw tabblad openen.

MkDocs ondersteunt externe URL's in `nav`, maar Material rendert die als een
kale ``<a href="...">``: zonder ``target`` en zonder ``rel``. Deze hook vult
dat aan.

Bewust een hook en geen template-override: daarvoor zouden Material's
``nav-item.html`` (170 regels) en ``tabs-item.html`` gekopieerd moeten worden,
die bij elke Material-update opnieuw kunnen afwijken. Er is geen JavaScript
bij betrokken; de attributen staan gewoon in de gegenereerde HTML.
"""

from __future__ import annotations

import re

# Interne navigatielinks zijn altijd relatief, dus een absolute http(s)-URL
# met een navigatieklasse wijst per definitie naar buiten de site.
_EXTERNAL_NAV_LINK = re.compile(
    r'<a href="(?P<url>https?://[^"]+)" class="(?P<cls>md-(?:tabs|nav)__link[^"]*)"'
)


def _mark_external(output: str) -> str:
    return _EXTERNAL_NAV_LINK.sub(
        lambda m: (
            f'<a href="{m["url"]}" target="_blank" rel="noopener noreferrer" '
            f'class="{m["cls"]}"'
        ),
        output,
    )


def on_post_page(output: str, page, config) -> str:
    return _mark_external(output)


def on_post_template(output_content: str, template_name: str, config) -> str:
    # Ook de losse themapagina's, zoals 404.html, tonen de navigatie.
    return _mark_external(output_content)
