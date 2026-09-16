---
title: Canon Datamodelleren
---

# Canon Datamodelleren

De Canon Datamodelleren legt vast wat binnen Entoli onder datamodelleren wordt
verstaan: welke begrippen er zijn, hoe ze zich tot elkaar verhouden, en welke
regels een agent moet volgen wanneer hij een datamodel afleidt of beoordeelt.

De canon bestaat uit drie gepubliceerde bestanden. Samen vormen ze de begrippen,
de regels en de grafiek die de samenhang tussen beide vastlegt.

## De drie bestanden

<div class="entoli-canon-files" markdown="1">

### [Begrippen](concepts-datamodelling.md)

`concepts-datamodelling.md` — het register van de kennisdomein Data Modelling.
Het beschrijft het metamodel (informatiemodel, logisch datamodel, technisch
datamodel en hun onderlinge afleiding) en waaruit een logisch datamodel is
opgebouwd: entiteit, attribuut, referentie-entiteit, attribuutclassificatie,
datatype, tijd en status. Elk begrip heeft een definitie, kenmerken, relaties en
afbakening.

### [LLM-constraints](llm-constraints.md)

`data-modelling.llm-constraints.yaml` — de regels die gelden voor een agent die
met datamodellen werkt. De diagnostische DAMA-regels leggen vast welke kennis de
agent geacht wordt te bezitten en correct toe te passen; de operationele
LDM-regels sturen de afleiding van een logisch datamodel uit een aangeleverd
conceptueel of informatiemodel.

### [Canon-grafiek](canon-graph.md)

`data-modelling-canon.graph.json` — de grafiekweergave van de canon: welke
elementen deze canon bezit, hoe ze in de brongrafiek aan elkaar hangen, en welke
elementen (nog) niet konden worden opgelost.

</div>
