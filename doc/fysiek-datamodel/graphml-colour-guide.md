# Kleurgids GraphML (TDM)

Geschreven voor: ontwikkelaars die de gegenereerde GraphML-diagrammen van het technisch datamodel (TDM) in yEd lezen, of die de renderer aanpassen.

> **Let op:** deze gids is een vertaalde en ingekorte samenvatting van de TDM-renderer zoals die op 2026-09-25 was. Er kunnen fouten in zitten. De code is leidend: bij twijfel gelden `scripts/graphml_render_tdm.py` en de legenda die in elk diagram als graafdata is opgeslagen (`presentation.legend`).

Kleur wordt altijd afgeleid uit feiten in het modelbestand. Als meerdere vulklassen van toepassing zijn, wint de klasse die het hoogst in de tabel staat. De rand van een tabel is altijd grijsblauw.

| Vulklasse | Vulling | Betekenis |
|---|---|---|
| `junction` | wit | Koppeltabel: realiseert een relatie (`source.kind: relationship`) of een associatieve entiteit. |
| `reference` | groen | Referentietabel: `entityKind: reference`, of een naam die begint met `ref_`. |
| `cross-instance-parent` | sterk roze | Een tabel in een andere Logical Instance verwijst via een code naar een attribuut van deze tabel. Alleen zichtbaar als de TDM vanuit zijn gebruikelijke map wordt gerenderd, naast de andere TDM-bestanden. |
| `cross-instance-child` | lichtroze | Deze tabel bevat een codeverwijzing naar een tabel in een andere Logical Instance (logische verwijzing zonder foreign key). |
| `without-parents` | geel | De tabel heeft geen uitgaande foreign key (zelfverwijzingen tellen mee) en geen codeverwijzing naar een andere instance. |
| `remaining` | lichtblauw | Alle overige tabellen. |

Foreign-keylijnen zijn grijsblauw.

De knoopdata `derived.role` wijkt af van de vulling: die gebruikt nog de oudere vier rollen (`parent`, `reference`, `junction`, `ordinary`). Lees de kleur daarom af met `presentation.legend`, niet met `derived.role`.
