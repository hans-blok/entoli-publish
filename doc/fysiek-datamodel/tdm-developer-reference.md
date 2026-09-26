# Technisch datamodel — naslag voor ontwikkelaars

Geschreven voor: ervaren architecten en ontwikkelaars die bouwen op de Entoli PostgreSQL-database, die bevragen of die laden.

Aanvulling op de [diagrammen](diagrammen.md): die tonen tabellen, kolommen, typen en foreign keys. Dit document geeft wat de diagrammen niet laten zien: de betekenis van tabellen en kolommen, de verwijzingen tussen instanties, de terminologie en de kleuren.

!!! warning "Er kunnen fouten in zitten"
    De omschrijvingen zijn met de hand geschreven op basis van de LDM-definities. Bij twijfel zijn de TDM- en LDM-bestanden in `entoli-canon` leidend.

## Opbouw

Het model is verdeeld over vijf Logical Instances. Elke instantie heeft een eigen TDM en een eigen reeks tabelcodes. Binnen een instantie zijn verwijzingen foreign keys; tussen instanties zijn het grensverwijzingen (zie [Terminologie](#terminologie)).

| Logical Instance | Inhoud | Tabelcodes | TDM-versie | LDM-versie |
|---|---|---|---|---|
| [semantic-foundation](#semantic-foundation) | De canon: semantisch model (elementen en relaties), kennisdomeinen, execution profiles en de regels uit de canon. | 100–199 | 2.0.0 | 2.0.0 |
| [agent-definition](#agent-definition) | De agents: packages, agents, agent intents met hun instructies, en de agentregels. | 200–299 | 2.0.0 | 2.0.0 |
| [execution-configuration](#execution-configuration) | De uitvoeringsomgeving: Entoli Contexts, LLM-providers, -accounts en -modellen, en de modelkeuze per stap. | 300–399 | 2.2.0 | 2.2.0 |
| [work-execution](#work-execution) | Het werk zelf: instruction sets en wat erin is opgenomen, executions, artefacten, handoffs en menselijke invoer. | 400–499 | 4.0.0 | 4.0.0 |
| [orchestration-definition](#orchestration-definition) | De orchestraties: specificaties, stappen, en hun geversioneerde definities en volgorde. | 500–599 | 4.0.0 | 4.0.0 |

## Terminologie

Deze termen gebruiken we in dit document, in de diagrammen en bij overdracht. Ze gaan over de fysieke tabellen, niet over de logische entiteiten.

| Term | Betekenis |
|---|---|
| **Logical Instance** | Afgebakend deel van het model met een eigen LDM en TDM, zoals `work-execution`. Kortweg *instantie*. |
| **parent-tabel** | Tabel waarnaar een foreign key uit een andere tabel van dezelfde instantie verwijst. |
| **child-tabel** | Tabel met ten minste één foreign key naar een parent-tabel in dezelfde instantie. |
| **worteltabel** | Tabel zonder parent: geen foreign key (ook geen verwijzing naar zichzelf) en geen grensverwijzing. |
| **junction-tabel** | Tabel die een veel-op-veelrelatie of een associatieve entiteit realiseert, zoals `instruction_set_element`. |
| **referentietabel** | Tabel met de posities van een gesloten classificatie: `id`, code en omschrijving. Naam begint met `ref_`. |
| **functionele sleutel** | Stabiele, betekenisdragende code die een rij buiten zijn eigen tabel identificeert, afgedwongen met een unique constraint. Grensverwijzingen wijzen altijd naar een functionele sleutel. |
| **grensverwijzing** | Kolom die met een functionele sleutel verwijst naar een rij in een andere instantie. Er zit geen foreign key achter: de applicatie houdt de verwijzing consistent. |
| **grensparent** | Tabel waarnaar een grensverwijzing uit een andere instantie wijst. Tegenhanger van parent-tabel, maar over de instantiegrens. |
| **grenschild** | Tabel met ten minste één grensverwijzing. Tegenhanger van child-tabel, maar over de instantiegrens. |
| **concreet subtype** | Subtype uit het LDM dat als zelfstandige tabel is gematerialiseerd, met de kolommen van het supertype erin. Er is geen supertypetabel; zo zijn `canon_rule`, `regime_rule` en `universal_rule` drie losse tabellen. |
| **surrogaatsleutel** | Betekenisloze `integer`-sleutel die de database toekent, meestal `<tabel>_id`. |

Rollen sluiten elkaar niet uit: `instruction_set` is bijvoorbeeld tegelijk parent-tabel en grenschild. Per tabel staan hieronder alle rollen.

## Conventies

- **Sleutel**: `PK` primaire sleutel, `FK` deel van een foreign key, `UK` deel van een unique constraint, `GV` grensverwijzing.
- Constraintnamen volgen de tabelcode: `PK_<tabel>`, `FK_<child>_<parent>_<nn>`, `UC_<tabel>_<nn>`, `CK_<tabel>_<nn>`. Alle foreign keys zijn `NO ACTION`.
- Kolommen met de naam `status`, `data_type` of `content_format` zijn vrije tekst: het model kent er geen codelijst voor.
- **Publicatiepatroon.** `model_assignment`, `orchestration_specification_version` en `orchestration_step_definition` hebben een `publication_timestamp`. Leeg betekent in bewerking; gevuld betekent gepubliceerd en onveranderlijk. Een wijziging is een nieuwe rij. De database dwingt die onveranderlijkheid niet af.
- **UUID-codes.** Versies en instruction sets hebben een `uuid`-code die bij aanmaak wordt toegekend en nooit verandert. Andere instanties verwijzen met die code.

## Kleuren in de diagrammen

De [diagrammen](diagrammen.md) geven elke tabel één vulkleur. Omdat een tabel meerdere rollen kan hebben, kiest de renderer de eerste klasse die van toepassing is, in de volgorde van deze tabel. De rand is altijd grijsblauw; foreign-keylijnen zijn grijsblauw.

| Volgorde | Vulklasse | Kleur | Term | Wanneer |
|---|---|---|---|---|
| 1 | `junction` | wit | junction-tabel | De tabel realiseert een relatie of een associatieve entiteit. |
| 2 | `reference` | groen | referentietabel | Referentie-entiteit, of een naam die begint met `ref_`. |
| 3 | `cross-instance-parent` | sterk roze | grensparent | Een grensverwijzing uit een andere instantie wijst naar een kolom van deze tabel. |
| 4 | `cross-instance-child` | lichtroze | grenschild | De tabel heeft een grensverwijzing. |
| 5 | `without-parents` | geel | worteltabel | Geen foreign key (een verwijzing naar zichzelf telt als foreign key) en geen grensverwijzing. |
| 6 | `remaining` | lichtblauw | overige tabel | Alle andere tabellen. |

Gevolgen van die volgorde: een tabel die zowel grensparent als grenschild is, wordt sterk roze. Een junction- of referentietabel blijft wit of groen, ook als andere instanties ernaar verwijzen.

Twee kanttekeningen:

- De renderer herkent een grensparent aan het LDM-attribuut waarnaar de grensverwijzing wijst, inclusief geërfde attributen. Verwijst een grensverwijzing naar `rule_code` van het supertype Entoli Rule, dan kleuren alle regeltabellen van die instantie sterk roze, ook een regeltabel waar niemand echt naar verwijst, zoals `entoli_agent_rule`. De rollen per tabel in dit document volgen de werkelijke verwijzing.
- In de GraphML staat per knoop ook `derived.role`. Dat veld gebruikt nog een ouder schema met vier rollen (`parent`, `reference`, `junction`, `ordinary`) en wijkt af van de vulkleur. Lees de kleur af met de graafeigenschap `presentation.legend`.

## semantic-foundation

De canon: semantisch model (elementen en relaties), kennisdomeinen, execution profiles en de regels uit de canon. TDM `entoli-agent-development-semantic-foundation-postgresql` versie 2.0.0.

### `artifact_type` { #semantic-foundation-artifact-type }

Soort professioneel werkproduct dat een canon definieert, zoals een logisch datamodel of een broninventarisatie. Classificeert de artefacten in work-execution en krijgt zijn vorm via templates.

**Tabelcode** 120 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `artifact_type_id` | PK | Surrogaatsleutel. |
| `code` | UK | Functionele sleutel van het artefacttype. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op het soort werkproduct. |
| `canon_id` | FK | De canon die dit artefacttype definieert. → `canon` |

**Grenschildren** [`artifact.artifact_type_code`](#work-execution-artifact) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| artifact_type_id | code | name | description | canon_id |
|---|---|---|---|---|
| 1 | logical-data-model | Logical Data Model | NULL | 1 |
| 2 | source-survey | Source Survey | A demarcated subset of cited external sources. | 1 |

</details>

### `canon` { #semantic-foundation-canon }

Autoritatieve semantische grondslag van een domein: een geversioneerd geheel van normatieve kennis dat precies één semantisch model definieert, met de bijbehorende canon rules, artefacttypen en templates. Tijdens uitvoering niet muteerbaar.

**Tabelcode** 121 · **Rollen** parent, child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `canon_id` | PK | Surrogaatsleutel. |
| `code` | UK | Functionele sleutel van de canon. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op de canon. |
| `version` |  | Versie van de canon als tekst, bijvoorbeeld `2.6.0`. |
| `status` |  | Levenscyclustoestand van de canon. Vrije tekst: er is geen codelijst. |
| `semantic_model_id` | FK | Het semantisch model dat deze canon definieert. Een canon definieert precies één semantisch model. → `semantic_model` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| canon_id | code | name | description | version | status | semantic_model_id |
|---|---|---|---|---|---|---|
| 1 | entoli-agent-development-canon | Entoli Agent Development Canon | Normative knowledge for developing Entoli agents … | 2.6.0 | current | 1 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `current` is een aangenomen waarde.

</details>

### `canon_rule` { #semantic-foundation-canon-rule }

Regel die haar normatieve gezag ontleent aan de canon en systeemintegriteit en architecturale invarianten bewaakt. Concreet subtype van Entoli Rule: de gedeelde regelkolommen staan in deze tabel zelf; er is geen supertypetabel.

**Tabelcode** 122 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `entoli_rule_id` | PK | Surrogaatsleutel. De naam komt van het supertype Entoli Rule. |
| `rule_code` | UK | Functionele sleutel van de regel, uniek binnen deze tabel. |
| `rule_text` |  | De regeltekst. |
| `reference` |  | Vindplaats van de regel in de canonbron, bijvoorbeeld document en artikel. |
| `canon_id` | FK | De canon die de regel stelt. → `canon` |
| `ref_rule_status_id` | FK | Levenscyclustoestand van de regel (actief of inactief). → `ref_rule_status` |
| `ref_rule_type_id` | FK | Modaliteit van de regel: gebod, verbod of toestemming. → `ref_rule_type` |

**Grenschildren** [`entoli_agent_rule.canon_rule_code`](#agent-definition-entoli-agent-rule) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| entoli_rule_id | rule_code | rule_text | reference | canon_id | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|---|
| 1 | CR-TRM-001 | Every canonical term MUST be used without synonyms. | constitution.md#Article 7 | 1 | 2 | 1 |

*Opmerking:* De bronnen noemen geen codes van Canon Rules; `CR-TRM-001` is fictief.

</details>

### `element` { #semantic-foundation-element }

Benoemde betekeniseenheid in de semantische graaf, zoals Agent of Instruction Set. Hoort bij precies één semantisch model.

**Tabelcode** 124 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `element_id` | PK | Surrogaatsleutel. |
| `element_code` | UK | Functionele sleutel: de `id` die de canonieke semantische graaf voor dit element publiceert, bijvoorbeeld `agent` of `instruction-set`. |
| `element_name` |  | Naam van het begrip. |
| `definition` |  | Definitie van het begrip. |
| `semantic_model_id` | FK | Het semantisch model waartoe het element behoort. → `semantic_model` |

**Grenschildren** [`instruction_set_element.element_code`](#work-execution-instruction-set-element) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (4), illustratief</summary>

| element_id | element_code | element_name | definition | semantic_model_id |
|---|---|---|---|---|
| 1 | agent | Agent | An explicitly defined, autonomous executor … | 1 |
| 2 | agent-intent | Agent Intent | One invocable capability of an Agent … | 1 |
| 3 | instruction-set | Instruction Set | The assembled instructions for one Execution … | 1 |
| 4 | execution | Execution | One run of an orchestration step by an LLM … | 1 |

</details>

### `element_canon_rule` { #semantic-foundation-element-canon-rule }

Junction-tabel tussen `element` en `canon_rule`: de canon rule noemt het element of hangt ervan af. Het LDM kent één relatie ELEMENT is used in ENTOLI RULE. Omdat de regelsubtypen als losse tabellen zijn gematerialiseerd, is die relatie verdeeld over `element_canon_rule`, `element_regime_rule` en `element_universal_rule`.

**Tabelcode** 130 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `element_canon_rule_id` | PK | Surrogaatsleutel. |
| `element_id` | FK, UK | Het gebruikte element. → `element` |
| `entoli_rule_id` | FK, UK | De canon rule die het element gebruikt. → `canon_rule` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| element_canon_rule_id | element_id | entoli_rule_id |
|---|---|---|
| 1 | 1 | 1 |

</details>

### `element_regime_rule` { #semantic-foundation-element-regime-rule }

Junction-tabel tussen `element` en `regime_rule`: de regime rule noemt het element of hangt ervan af. Het LDM kent één relatie ELEMENT is used in ENTOLI RULE. Omdat de regelsubtypen als losse tabellen zijn gematerialiseerd, is die relatie verdeeld over `element_canon_rule`, `element_regime_rule` en `element_universal_rule`.

**Tabelcode** 131 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `element_regime_rule_id` | PK | Surrogaatsleutel. |
| `element_id` | FK, UK | Het gebruikte element. → `element` |
| `regime_rule_id` | FK, UK | De regime rule die het element gebruikt. → `regime_rule` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| element_regime_rule_id | element_id | regime_rule_id |
|---|---|---|
| 1 | 2 | 3 |

</details>

### `element_universal_rule` { #semantic-foundation-element-universal-rule }

Junction-tabel tussen `element` en `universal_rule`: de universal rule noemt het element of hangt ervan af. Het LDM kent één relatie ELEMENT is used in ENTOLI RULE. Omdat de regelsubtypen als losse tabellen zijn gematerialiseerd, is die relatie verdeeld over `element_canon_rule`, `element_regime_rule` en `element_universal_rule`.

**Tabelcode** 137 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `element_universal_rule_id` | PK | Surrogaatsleutel. |
| `element_id` | FK, UK | Het gebruikte element. → `element` |
| `universal_rule_id` | FK, UK | De universal rule die het element gebruikt. → `universal_rule` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| element_universal_rule_id | element_id | universal_rule_id |
|---|---|---|
| 1 | 4 | 1 |
| 2 | 3 | 2 |

</details>

### `execution_profile` { #semantic-foundation-execution-profile }

Benoemde combinatie van één Development Phase en één positie op elk van de vier Execution Regime-assen. Een model assignment in execution-configuration realiseert een execution profile.

**Tabelcode** 135 · **Rollen** child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `execution_profile_id` | PK | Surrogaatsleutel. |
| `execution_profile_code` | UK | Functionele sleutel van het profiel, bijvoorbeeld `DPG-EXP-C2`. |
| `execution_profile_name` |  | Weergavenaam. |
| `execution_profile_description` |  | Omschrijving van de semantische uitvoeringskenmerken die het profiel vastlegt. |
| `ref_development_phase_id` | FK | De ontwikkelfase waarbinnen het profiel geldt. → `ref_development_phase` |
| `ref_reasoning_regime_id` | FK | Positie op de Reasoning Regime-as (cognitieve vrijheid van het LLM). → `ref_reasoning_regime` |
| `ref_source_regime_id` | FK | Positie op de Source Regime-as (welke bronnen toelaatbaar zijn). → `ref_source_regime` |
| `ref_synthesis_regime_id` | FK | Positie op de Synthesis Regime-as (wat met betekenis mag gebeuren). → `ref_synthesis_regime` |
| `ref_task_regime_id` | FK | Positie op de Task Regime-as (type bewerking en structuur van de uitvoer). → `ref_task_regime` |

**Grenschildren** [`model_assignment.execution_profile_code`](#execution-configuration-model-assignment) (execution-configuration)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| execution_profile_id | execution_profile_code | execution_profile_name | execution_profile_description | ref_development_phase_id | ref_reasoning_regime_id | ref_source_regime_id | ref_synthesis_regime_id | ref_task_regime_id |
|---|---|---|---|---|---|---|---|---|
| 1 | DPG-EXP-C2 | Source survey | The Intent surveys named external sources, each cited … | 1 | 2 | 3 | 1 | 1 |
| 2 | DPG-SPE-C2 | Formalising a structure | The Intent makes the architecture of canonical material explicit … | 3 | 3 | 2 | 2 | 2 |

</details>

### `knowledge_domain` { #semantic-foundation-knowledge-domain }

Vakgebied of afgebakend kennisdomein, onafhankelijk van een framework of methode, zoals agentontwikkeling of datamodellering.

**Tabelcode** 125 · **Rollen** parent, worteltabel · **Kleur** geel

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `knowledge_domain_id` | PK | Surrogaatsleutel. |
| `code` | UK | Functionele sleutel van het domein. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op het domein. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| knowledge_domain_id | code | name | description |
|---|---|---|---|
| 1 | agent-development | Agent Development | NULL |
| 2 | data-modelling | Data Modelling | Conceptual, logical and technical data modelling. |

</details>

### `knowledge_specification` { #semantic-foundation-knowledge-specification }

Specificatie van de kennis uit één knowledge domain die voor een doel gerepresenteerd en gegoverneerd moet worden. Kan bestaan voordat een canon haar realiseert.

**Tabelcode** 126 · **Rollen** child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `knowledge_specification_id` | PK | Surrogaatsleutel. |
| `code` | UK | Functionele sleutel van de specificatie. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op de specificatie. |
| `canon_id` | FK | De canon die deze specificatie realiseert. Leeg zolang er geen canon is. → `canon` |
| `knowledge_domain_id` | FK | Het kennisdomein dat wordt gespecificeerd. → `knowledge_domain` |

**Grenschildren** [`agent.knowledge_specification_code`](#agent-definition-agent) (agent-definition), [`agent_package.knowledge_specification_code`](#agent-definition-agent-package) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| knowledge_specification_id | code | name | description | canon_id | knowledge_domain_id |
|---|---|---|---|---|---|
| 1 | ks-agent-development | Agent development knowledge | NULL | 1 | 1 |
| 2 | ks-data-modelling | Data modelling knowledge | Not yet realized by a canon. | NULL | 2 |

</details>

### `ref_development_phase` { #semantic-foundation-ref-development-phase }

Referentietabel met de posities van Development Phase, zoals Exploration en Specification. Classificeert agents en execution profiles.

**Tabelcode** 101 · **Rollen** referentietabel, parent, grensparent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_development_phase_id` | PK | Surrogaatsleutel. |
| `development_phase_code` | UK | Code van de fase, bijvoorbeeld `EXP`. |
| `development_phase_description` |  | Omschrijving van de fase. |

**Grenschildren** [`agent.development_phase_code`](#agent-definition-agent) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (5), illustratief</summary>

| ref_development_phase_id | development_phase_code | development_phase_description |
|---|---|---|
| 1 | EXP | Exploration |
| 2 | ORD | Ordering |
| 3 | SPC | Specification |
| 4 | RLS | Realisation |
| 5 | TST | Testing |

*Opmerking:* Vijf van de zeven posities zijn weergegeven; `REG` (Registering) en `OPR` (Operationalisation) zijn weggelaten.

</details>

### `ref_reasoning_regime` { #semantic-foundation-ref-reasoning-regime }

Referentietabel met de posities op de Reasoning Regime-as (cognitieve vrijheid van het LLM). Concreet subtype van EXECUTION REGIME (REF); de vier regimetabellen hebben daarom dezelfde kolomnamen.

**Tabelcode** 102 · **Rollen** referentietabel, parent, grensparent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_reasoning_regime_id` | PK | Surrogaatsleutel. |
| `execution_regime_code` | UK | Code van de positie, bijvoorbeeld `EXP` of `CNB`. |
| `execution_regime_description` |  | Omschrijving van de positie. |

**Grenschildren** [`agent_intent.reasoning_regime_code`](#agent-definition-agent-intent) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (4), illustratief</summary>

| ref_reasoning_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | EXP | Explorative |
| 2 | ITP | Interpretive |
| 3 | CNS | Constrained |
| 4 | DTM | Deterministic |

</details>

### `ref_rule_status` { #semantic-foundation-ref-rule-status }

Referentietabel met de levenscyclustoestanden van een regel (actief, inactief). Gebruikt door canon rules, regime rules en universal rules.

**Tabelcode** 106 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_rule_status_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de toestand. |
| `description` |  | Omschrijving van de toestand. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| ref_rule_status_id | code | description |
|---|---|---|
| 1 | 0 | Inactive |
| 2 | 1 | Active |

</details>

### `ref_rule_type` { #semantic-foundation-ref-rule-type }

Referentietabel met de modaliteiten van een regel: gebod, verbod of toestemming. Gebruikt door canon rules, regime rules en universal rules.

**Tabelcode** 107 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_rule_type_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de modaliteit. |
| `description` |  | Omschrijving van de modaliteit. |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| ref_rule_type_id | code | description |
|---|---|---|
| 1 | obl | Obligation |
| 2 | prh | Prohibition |
| 3 | prm | Permission |

</details>

### `ref_source_regime` { #semantic-foundation-ref-source-regime }

Referentietabel met de posities op de Source Regime-as (welke bronnen toelaatbaar zijn). Concreet subtype van EXECUTION REGIME (REF); de vier regimetabellen hebben daarom dezelfde kolomnamen.

**Tabelcode** 103 · **Rollen** referentietabel, parent, grensparent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_source_regime_id` | PK | Surrogaatsleutel. |
| `execution_regime_code` | UK | Code van de positie, bijvoorbeeld `EXP` of `CNB`. |
| `execution_regime_description` |  | Omschrijving van de positie. |

**Grenschildren** [`agent_intent.source_regime_code`](#agent-definition-agent-intent) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (4), illustratief</summary>

| ref_source_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | INB | Input-bound |
| 2 | CNB | Canon-bound |
| 3 | EXB | External-source-bound |
| 4 | OPN | Open |

</details>

### `ref_synthesis_regime` { #semantic-foundation-ref-synthesis-regime }

Referentietabel met de posities op de Synthesis Regime-as (wat met betekenis mag gebeuren). Concreet subtype van EXECUTION REGIME (REF); de vier regimetabellen hebben daarom dezelfde kolomnamen.

**Tabelcode** 104 · **Rollen** referentietabel, parent, grensparent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_synthesis_regime_id` | PK | Surrogaatsleutel. |
| `execution_regime_code` | UK | Code van de positie, bijvoorbeeld `EXP` of `CNB`. |
| `execution_regime_description` |  | Omschrijving van de positie. |

**Grenschildren** [`agent_intent.synthesis_regime_code`](#agent-definition-agent-intent) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| ref_synthesis_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | PRV | Preserving |
| 2 | REL | Relating |
| 3 | GEN | Generating |

</details>

### `ref_task_regime` { #semantic-foundation-ref-task-regime }

Referentietabel met de posities op de Task Regime-as (type bewerking en structuur van de uitvoer). Concreet subtype van EXECUTION REGIME (REF); de vier regimetabellen hebben daarom dezelfde kolomnamen.

**Tabelcode** 105 · **Rollen** referentietabel, parent, grensparent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_task_regime_id` | PK | Surrogaatsleutel. |
| `execution_regime_code` | UK | Code van de positie, bijvoorbeeld `EXP` of `CNB`. |
| `execution_regime_description` |  | Omschrijving van de positie. |

**Grenschildren** [`agent_intent.task_regime_code`](#agent-definition-agent-intent) (agent-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (5), illustratief</summary>

| ref_task_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | EXT | Extracting |
| 2 | STR | Structuring |
| 3 | TRF | Transforming |
| 4 | EVL | Evaluating |
| 5 | ORI | Originating |

</details>

### `regime_rule` { #semantic-foundation-regime-rule }

Operationele regel uit de canon die de integriteit van precies één Execution Regime bewaakt. Niet door de gebruiker te wijzigen. Concreet subtype van Entoli Rule. Van de vier regimekolommen is er precies één gevuld (`CK_123_01`).

**Tabelcode** 123 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `regime_rule_id` | PK | Surrogaatsleutel. |
| `rule_code` | UK | Functionele sleutel van de regel, uniek binnen deze tabel. |
| `rule_text` |  | De regeltekst. |
| `reference` |  | Vindplaats van de regel in de canonbron. |
| `ref_rule_status_id` | FK | Levenscyclustoestand van de regel. → `ref_rule_status` |
| `ref_rule_type_id` | FK | Modaliteit van de regel. → `ref_rule_type` |
| `ref_reasoning_regime_id` | FK | Gevuld als de regel een positie op de Reasoning Regime-as (cognitieve vrijheid van het LLM) bewaakt. → `ref_reasoning_regime` |
| `ref_source_regime_id` | FK | Gevuld als de regel een positie op de Source Regime-as (welke bronnen toelaatbaar zijn) bewaakt. → `ref_source_regime` |
| `ref_synthesis_regime_id` | FK | Gevuld als de regel een positie op de Synthesis Regime-as (wat met betekenis mag gebeuren) bewaakt. → `ref_synthesis_regime` |
| `ref_task_regime_id` | FK | Gevuld als de regel een positie op de Task Regime-as (type bewerking en structuur van de uitvoer) bewaakt. → `ref_task_regime` |

**Grenschildren** [`instruction_set_regime_rule.regime_rule_code`](#work-execution-instruction-set-regime-rule) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| regime_rule_id | rule_code | rule_text | reference | ref_rule_status_id | ref_rule_type_id | ref_reasoning_regime_id | ref_source_regime_id | ref_synthesis_regime_id | ref_task_regime_id |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SR-CNB-001 | The LLM MUST NOT load or rely on Work-Sources beyond what is derivable from the canonical sources provided. … | doctrine.source-regime.md#§5.2 | 2 | 2 | NULL | 2 | NULL | NULL |
| 2 | SY-REL-001 | The LLM MUST NOT change the meaning of existing content. | doctrine.synthesis-regime.md#§3.2 | 2 | 2 | NULL | NULL | 2 | NULL |
| 3 | TM-STR-001 | The LLM MUST produce output whose primary content is relationships, organisation, or architecture made explicit. | NULL | 2 | 1 | NULL | NULL | NULL | 2 |

*Opmerking:* Regelcodes en -teksten komen uit de Operational Rules; de teksten zijn ingekort.

</details>

### `relationship` { #semantic-foundation-relationship }

Gerichte, benoemde semantische verbinding tussen twee elementen van hetzelfde semantisch model.

**Tabelcode** 127 · **Rollen** child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `relationship_id` | PK | Surrogaatsleutel. |
| `relationship_code` | UK | Functionele sleutel: de `id` uit de canonieke graaf, in de vorm `<bron>--<type>--<doel>`. |
| `name` |  | Naam van de relatie, bijvoorbeeld `exposes capabilities via`. |
| `from_element_id` | FK | Het element waar de relatie begint. → `element` |
| `to_element_id` | FK | Het element waar de relatie eindigt. → `element` |
| `semantic_model_id` | FK | Het semantisch model waartoe de relatie behoort. → `semantic_model` |

**Grenschildren** [`instruction_set_relationship.relationship_code`](#work-execution-instruction-set-relationship) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| relationship_id | relationship_code | name | from_element_id | to_element_id | semantic_model_id |
|---|---|---|---|---|---|
| 1 | agent-exposes-agent-intent | exposes capabilities via | 1 | 2 | 1 |
| 2 | execution-is-instructed-by-instruction-set | is instructed by | 4 | 3 | 1 |

</details>

### `semantic_model` { #semantic-foundation-semantic-model }

De volledige semantische graaf die één canon definieert: de elementen en de relaties daartussen. Read-only tijdens uitvoering.

**Tabelcode** 133 · **Rollen** parent, worteltabel · **Kleur** geel

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `semantic_model_id` | PK | Surrogaatsleutel. |
| `semantic_model_code` | UK | Functionele sleutel van het model. |
| `semantic_model_name` |  | Weergavenaam. |
| `semantic_model_description` |  | Toelichting op het model. |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| semantic_model_id | semantic_model_code | semantic_model_name | semantic_model_description |
|---|---|---|---|
| 1 | entoli-agent-development | Entoli Agent Development | Elements and relationships of agent development … |

</details>

### `template` { #semantic-foundation-template }

Herbruikbare vormspecificatie voor artefacten van één artefacttype.

**Tabelcode** 134 · **Rollen** child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `template_id` | PK | Surrogaatsleutel. |
| `code` | UK | Functionele sleutel van het template. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op het template. |
| `content_format` |  | Formaat waarin de inhoud is geschreven, zoals Markdown, JSON of YAML. Vrije tekst: er is geen codelijst. |
| `template_content` |  | De volledige inhoud van het template, opgeslagen zoals geschreven. Wordt niet geparst of genormaliseerd; ook JSON en YAML staan hier als tekst. |
| `artifact_type_id` | FK | Het artefacttype waarvoor het template de vorm vastlegt. → `artifact_type` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| template_id | code | name | description | content_format | template_content | artifact_type_id |
|---|---|---|---|---|---|---|
| 1 | ldm-json | Logical Data Model (JSON) | NULL | json | {"model": {…}, "entities": [ … ]} | 1 |

*Opmerking:* `content_format` heeft in de bronnen geen codelijst; `json` is een aangenomen waarde.

</details>

### `universal_rule` { #semantic-foundation-universal-rule }

Operationele regel die geldt voor elke agent en elke agent intent, ongeacht hun execution regimes. Concreet subtype van Entoli Rule. Elke instruction set bevat elke universal rule die actief was toen de set werd samengesteld.

**Tabelcode** 136 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `universal_rule_id` | PK | Surrogaatsleutel. |
| `rule_code` | UK | Functionele sleutel van de regel, uniek binnen deze tabel. |
| `rule_text` |  | De regeltekst. |
| `reference` |  | Vindplaats van de regel in de canonbron. |
| `ref_rule_status_id` | FK | Levenscyclustoestand van de regel. → `ref_rule_status` |
| `ref_rule_type_id` | FK | Modaliteit van de regel. → `ref_rule_type` |

**Grenschildren** [`instruction_set_universal_rule.universal_rule_code`](#work-execution-instruction-set-universal-rule) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| universal_rule_id | rule_code | rule_text | reference | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|
| 1 | UNI-001 | The LLM MUST NOT present a fact, a source, a decision or a result as established unless … . | constitution.md#Article 3 §1 | 2 | 2 |
| 2 | UNI-002 | Where the work depends on information that is neither supplied nor obtainable …, the LLM MUST identify … . | constitution.md#Article 3 §1 | 2 | 1 |
| 3 | UNI-003 | The LLM MUST NOT resolve a material ambiguity or a decisive gap silently. … | constitution.md#Proposition | 2 | 2 |

</details>

## agent-definition

De agents: packages, agents, agent intents met hun instructies, en de agentregels. TDM `entoli-agent-development-agent-definition-postgresql` versie 2.0.0.

### `agent` { #agent-definition-agent }

Entoli-agent: expliciet gedefinieerde, autonome uitvoerder met een eigen boundary, geclassificeerd door één Development Phase en in eigendom van één Entoli Context.

**Tabelcode** 220 · **Rollen** parent, child, grenschild · **Kleur** lichtroze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `agent_id` | PK | Surrogaatsleutel. |
| `agent_code` | UK | Functionele sleutel van de agent. |
| `agent_name` |  | Weergavenaam. |
| `boundary` |  | Beschrijving van de agent-boundary: waar de verantwoordelijkheid van de agent begint en eindigt. |
| `knowledge_specification_code` | GV | De kennisspecificatie waarvoor de agent kennis specificeert. Grensverwijzing naar `knowledge_specification.code` in semantic-foundation. |
| `development_phase_code` | GV | De ontwikkelfase van de agent. Grensverwijzing naar `ref_development_phase.development_phase_code` in semantic-foundation. |
| `entoli_context_code` | GV | De Entoli Context die de agent bezit. Grensverwijzing naar `entoli_context.entoli_context_code` in execution-configuration. |
| `agent_package_id` | FK | Het package waartoe de agent behoort. → `agent_package` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| agent_id | agent_code | agent_name | boundary | knowledge_specification_code | development_phase_code | entoli_context_code | agent_package_id |
|---|---|---|---|---|---|---|---|
| 1 | niam-analyst | NIAM Analyst | Analyses domain statements and source material … | ks-data-modelling | EXP | entoli-dev | 1 |
| 2 | ldm-modeller | Logical Data Modeller | Translates conceptual meaning into a logical data model … | NULL | SPC | entoli-dev | 1 |

</details>

### `agent_intent` { #agent-definition-agent-intent }

Aanroepbare capability van een agent: één samenhangende eenheid werk binnen de agent-boundary, met per Execution Regime-as de gedeclareerde positie.

**Tabelcode** 221 · **Rollen** parent, child, grensparent, grenschild · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `agent_intent_id` | PK, UK | Surrogaatsleutel. |
| `agent_intent_code` | UK | Functionele sleutel, in de vorm `<agent>.<intent>`, bijvoorbeeld `ldm-modeller.derive-ldm`. |
| `agent_intent_name` |  | Weergavenaam. |
| `reasoning_regime_code` | GV | Positie op de Reasoning Regime-as. Verplicht: elke intent die een LLM uitvoert heeft een reasoning regime. Grensverwijzing naar `ref_reasoning_regime.execution_regime_code` in semantic-foundation. |
| `source_regime_code` | GV | Positie op de Source Regime-as. Leeg als de as niet van toepassing is. Grensverwijzing naar `ref_source_regime.execution_regime_code` in semantic-foundation. |
| `synthesis_regime_code` | GV | Positie op de Synthesis Regime-as. Leeg als de as niet van toepassing is. Grensverwijzing naar `ref_synthesis_regime.execution_regime_code` in semantic-foundation. |
| `task_regime_code` | GV | Positie op de Task Regime-as. Leeg als de as niet van toepassing is. Grensverwijzing naar `ref_task_regime.execution_regime_code` in semantic-foundation. |
| `agent_id` | FK, UK | De agent die de capability aanbiedt. → `agent` |

**Grenschildren** [`instruction_set.agent_intent_code`](#work-execution-instruction-set) (work-execution), [`orchestration_step_definition.agent_intent_code`](#orchestration-definition-orchestration-step-definition) (orchestration-definition)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| agent_intent_id | agent_intent_code | agent_intent_name | reasoning_regime_code | source_regime_code | synthesis_regime_code | task_regime_code | agent_id |
|---|---|---|---|---|---|---|---|
| 1 | niam-analyst.survey-sources | Survey sources | ITP | EXB | PRV | EXT | 1 |
| 2 | ldm-modeller.derive-ldm | Derive logical data model | CNS | CNB | REL | STR | 2 |

</details>

### `agent_package` { #agent-definition-agent-package }

Beheerde bundel van agents, gescoped door precies één knowledge specification. Een andere kennisscope betekent een ander package.

**Tabelcode** 222 · **Rollen** parent, grenschild · **Kleur** lichtroze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `agent_package_id` | PK | Surrogaatsleutel. |
| `package_code` | UK | Functionele sleutel van het package. |
| `package_name` |  | Weergavenaam. |
| `version` |  | Versie van het package als tekst. |
| `status` |  | Levenscyclustoestand. Vrije tekst: er is geen codelijst. |
| `description` |  | Toelichting op het package. |
| `knowledge_specification_code` | GV | De vaste kennisscope van het package. Grensverwijzing naar `knowledge_specification.code` in semantic-foundation. |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| agent_package_id | package_code | package_name | version | status | description | knowledge_specification_code |
|---|---|---|---|---|---|---|
| 1 | modelling-agents | Modelling agents | 1.0.0 | active | NULL | ks-agent-development |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

</details>

### `entoli_agent_intent_rule` { #agent-definition-entoli-agent-intent-rule }

Operationele regel die voor één agent intent één toetsbare verplichting of één toetsbaar verbod vastlegt, en daarmee precies één Entoli Agent Rule van dezelfde agent operationaliseert. Concreet subtype van Entoli Rule.

**Tabelcode** 223 · **Rollen** child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `entoli_rule_id` | PK | Surrogaatsleutel. De naam komt van het supertype Entoli Rule. |
| `rule_code` | UK | Functionele sleutel van de regel, uniek binnen deze tabel. |
| `rule_text` |  | De regeltekst. |
| `reference` |  | Vindplaats van de regel in de bron. |
| `agent_intent_id` | FK | De agent intent die de regel begrenst. → `agent_intent` |
| `agent_rule_id` | FK | De agentregel die deze regel operationaliseert. → `entoli_agent_rule` |
| `ref_rule_status_id` | FK | Levenscyclustoestand van de regel. → `ref_rule_status` |
| `ref_rule_type_id` | FK | Modaliteit van de regel. → `ref_rule_type` |
| `agent_id` | FK | Herhaalt de agent van zowel de intent als de agentregel. Beide foreign keys zijn samengesteld met deze kolom (`FK_223_221_01` naar `agent_intent`, `FK_223_224_01` naar `entoli_agent_rule`) en dwingen zo af dat intent en agentregel bij dezelfde agent horen. → `agent_intent`, `entoli_agent_rule` |

**Grenschildren** [`instruction_set_entoli_agent_intent_rule.entoli_agent_intent_rule_code`](#work-execution-instruction-set-entoli-agent-intent-rule) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| entoli_rule_id | rule_code | rule_text | reference | agent_intent_id | agent_rule_id | ref_rule_status_id | ref_rule_type_id | agent_id |
|---|---|---|---|---|---|---|---|---|
| 11 | EAIR-LDM-001 | When deriving an LDM, the LLM MUST keep every conceptual name … | NULL | 2 | 1 | 2 | 1 | 2 |

*Opmerking:* `agent_id` herhaalt de agent van zowel de Agent Intent als de Entoli Agent Rule; de samengestelde foreign keys eisen dat het dezelfde agent is. De regelcode is fictief.

</details>

### `entoli_agent_rule` { #agent-definition-entoli-agent-rule }

Normatieve regel voor precies één agent. Concretiseert optioneel één canon rule, zonder die te verzwakken of tegen te spreken.

**Tabelcode** 224 · **Rollen** parent, child, grenschild · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `entoli_rule_id` | PK, UK | Surrogaatsleutel. De naam komt van het supertype Entoli Rule. |
| `rule_code` | UK | Functionele sleutel van de regel, uniek binnen deze tabel. |
| `rule_text` |  | De regeltekst. |
| `reference` |  | Vindplaats van de regel in de bron. |
| `canon_rule_code` | GV | De canon rule die deze regel concretiseert. Leeg als de regel geen canonieke grondslag heeft. Grensverwijzing naar `canon_rule.rule_code` in semantic-foundation. |
| `agent_id` | FK, UK | De agent waarvoor de regel geldt. → `agent` |
| `ref_rule_status_id` | FK | Levenscyclustoestand van de regel. → `ref_rule_status` |
| `ref_rule_type_id` | FK | Modaliteit van de regel. → `ref_rule_type` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| entoli_rule_id | rule_code | rule_text | reference | canon_rule_code | agent_id | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|---|---|
| 1 | EAR-LDM-001 | The Logical Data Modeller MUST NOT change conceptual meaning. | NULL | CR-TRM-001 | 2 | 2 | 2 |

*Opmerking:* De regelcodes zijn fictief.

</details>

### `intent_instruction` { #agent-definition-intent-instruction }

Geordende, normatieve aanwijzing die beschrijft hoe een agent intent inhoudelijk door een LLM wordt uitgevoerd. Onafhankelijk van een concrete execution.

**Tabelcode** 225 · **Rollen** child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `intent_instruction_id` | PK | Surrogaatsleutel. |
| `intent_instruction_code` | UK | Functionele sleutel van de instructie. |
| `instruction` |  | De instructie zelf: welke inhoudelijke handeling het LLM op dit punt uitvoert. |
| `sequence` | UK | Positie in de uitvoeringsvolgorde binnen de agent intent. Positief (`CK_225_01`); gaten zijn toegestaan. |
| `agent_intent_id` | FK, UK | De agent intent waartoe de instructie behoort. → `agent_intent` |

**Grenschildren** [`instruction_set_intent_instruction.intent_instruction_code`](#work-execution-instruction-set-intent-instruction) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| intent_instruction_id | intent_instruction_code | instruction | sequence | agent_intent_id |
|---|---|---|---|---|
| 1 | niam-analyst.survey-sources.01 | List every external source and cite it … | 1 | 1 |
| 2 | ldm-modeller.derive-ldm.01 | Read the conceptual model and the source survey … | 1 | 2 |
| 3 | ldm-modeller.derive-ldm.02 | Record every modelling decision with its ground … | 2 | 2 |

*Opmerking:* Het formaat van codes van intent instructions ligt in de bronnen niet vast; de codes zijn fictief.

</details>

### `ref_rule_status` { #agent-definition-ref-rule-status }

Referentietabel met de levenscyclustoestanden van agentregels en agent-intentregels. Eigen kopie van de lijst in semantic-foundation.

**Tabelcode** 201 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_rule_status_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de toestand. |
| `description` |  | Omschrijving van de toestand. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| ref_rule_status_id | code | description |
|---|---|---|
| 1 | 0 | Inactive |
| 2 | 1 | Active |

</details>

### `ref_rule_type` { #agent-definition-ref-rule-type }

Referentietabel met de modaliteiten van agentregels en agent-intentregels: gebod, verbod of toestemming. Eigen kopie van de lijst in semantic-foundation.

**Tabelcode** 202 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_rule_type_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de modaliteit. |
| `description` |  | Omschrijving van de modaliteit. |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| ref_rule_type_id | code | description |
|---|---|---|
| 1 | obl | Obligation |
| 2 | prh | Prohibition |
| 3 | prm | Permission |

</details>

## execution-configuration

De uitvoeringsomgeving: Entoli Contexts, LLM-providers, -accounts en -modellen, en de modelkeuze per stap. TDM `entoli-agent-development-execution-configuration-postgresql` versie 2.2.0.

### `entoli_context` { #execution-configuration-entoli-context }

Omgeving waarin Entoli zijn agents, LLM-toegang en modelselecties beheert en herbruikbare orchestraties gebruikt.

**Tabelcode** 320 · **Rollen** parent, grensparent, worteltabel · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `entoli_context_id` | PK | Surrogaatsleutel. |
| `entoli_context_code` | UK | Functionele sleutel van de context. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op de context. |
| `status` |  | Levenscyclustoestand. Vrije tekst: er is geen codelijst. |

**Grenschildren** [`agent.entoli_context_code`](#agent-definition-agent) (agent-definition), [`execution.entoli_context_code`](#work-execution-execution) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| entoli_context_id | entoli_context_code | name | description | status |
|---|---|---|---|---|
| 1 | entoli-dev | Entoli development | NULL | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

</details>

### `entoli_context_orchestration_specification` { #execution-configuration-entoli-context-orchestration-specification }

Junction-tabel: welke orchestration specifications in een Entoli Context beschikbaar zijn. De orchestration specification ligt in een andere Logical Instance; die kant is daarom een grensverwijzing en geen foreign key.

**Tabelcode** 329 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `entoli_context_orchestration_specification_id` | PK | Surrogaatsleutel. |
| `orchestration_specification_code` | UK, GV | De beschikbaar gestelde orchestration specification. Grensverwijzing naar `orchestration_specification.specification_code` in orchestration-definition. |
| `entoli_context_id` | FK, UK | De context die de specificatie beschikbaar stelt. → `entoli_context` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| entoli_context_orchestration_specification_id | orchestration_specification_code | entoli_context_id |
|---|---|---|
| 1 | model-derivation | 1 |

</details>

### `llm_account` { #execution-configuration-llm-account }

Toegang bij een LLM Provider die een Entoli Context beschikbaar stelt, met de versleutelde API-sleutel.

**Tabelcode** 322 · **Rollen** child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `llm_account_id` | PK | Surrogaatsleutel. |
| `account_code` | UK | Functionele sleutel van het account. |
| `account_name` |  | Weergavenaam. |
| `description` |  | Toelichting op het account. |
| `api_key_ciphertext` |  | Versleutelde API-sleutel als bytes. Nooit de sleutel in klare tekst. Technische kolom, niet afkomstig uit het LDM. |
| `created_at` |  | Moment waarop het account is vastgelegd. Technische kolom, niet afkomstig uit het LDM. |
| `api_key_rotated_at` |  | Moment van de laatste sleutelrotatie; leeg als de sleutel nooit is geroteerd. Technische kolom, niet afkomstig uit het LDM. |
| `entoli_context_id` | FK | De context die het account beschikbaar stelt. → `entoli_context` |
| `llm_provider_id` | FK | De provider die het account verstrekt. → `llm_provider` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| llm_account_id | account_code | account_name | description | api_key_ciphertext | created_at | api_key_rotated_at | entoli_context_id | llm_provider_id |
|---|---|---|---|---|---|---|---|---|
| 1 | entoli-dev-anthropic | Development account | NULL | \x8f3a… | 2026-09-01 08:00:00+00 | NULL | 1 | 1 |

*Opmerking:* `api_key_ciphertext` bevat versleutelde bytes; de waarde is een placeholder, nooit een echte sleutel.

</details>

### `llm_model` { #execution-configuration-llm-model }

Specifiek taalmodel dat één LLM Provider aanbiedt en dat een model assignment kan selecteren.

**Tabelcode** 323 · **Rollen** parent, child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `llm_model_id` | PK | Surrogaatsleutel. |
| `model_code` | UK | Functionele sleutel van het model. |
| `context_window_size` |  | Omvang van het contextvenster in tokens. |
| `description` |  | Toelichting op het model. |
| `llm_provider_id` | FK | De provider die het model aanbiedt. → `llm_provider` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| llm_model_id | model_code | context_window_size | description | llm_provider_id |
|---|---|---|---|---|
| 1 | claude-opus-5-5 | NULL | NULL | 1 |
| 2 | claude-sonnet-5 | 200000 | Faster model for extraction work. | 1 |

*Opmerking:* `context_window_size` is een illustratieve waarde, geen gedocumenteerde eigenschap van het model.

</details>

### `llm_provider` { #execution-configuration-llm-provider }

Aanbieder van LLM-modellen, via wie ook LLM-accounts worden verstrekt.

**Tabelcode** 324 · **Rollen** parent, worteltabel · **Kleur** geel

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `llm_provider_id` | PK | Surrogaatsleutel. |
| `provider_code` | UK | Stabiele functionele sleutel. Verandert niet als de naam van de provider verandert. |
| `name` |  | Weergavenaam. Mag wijzigen zonder dat een andere provider wordt bedoeld. |
| `status` |  | Levenscyclustoestand. Vrije tekst: er is geen codelijst. |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| llm_provider_id | provider_code | name | status |
|---|---|---|---|
| 1 | anthropic | Anthropic | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

</details>

### `llm_provider_thinking_effort` { #execution-configuration-llm-provider-thinking-effort }

Junction-tabel (associatieve entiteit): de waarde die een provider in zijn API verwacht voor een Thinking Effort-positie. Per combinatie van provider en thinking effort ten hoogste één rij.

**Tabelcode** 328 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `llm_provider_thinking_effort_id` | PK | Surrogaatsleutel. |
| `provider_value` |  | De waarde die de provider verwacht, letterlijk zoals de provider die schrijft. Draagt zelf geen Entoli-betekenis. |
| `llm_provider_id` | FK, UK | De provider. → `llm_provider` |
| `ref_thinking_effort_id` | FK, UK | De Thinking Effort-positie die wordt vertaald. → `ref_thinking_effort` |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| llm_provider_thinking_effort_id | provider_value | llm_provider_id | ref_thinking_effort_id |
|---|---|---|---|
| 1 | low | 1 | 1 |
| 2 | medium | 1 | 2 |
| 3 | high | 1 | 3 |

*Opmerking:* De providerwaarden zijn fictief.

</details>

### `model_assignment` { #execution-configuration-model-assignment }

Keuze van een LLM-model met generatie-instellingen die één execution profile realiseert. Na publicatie onveranderlijk: een gewijzigde configuratie is een nieuwe model assignment.

**Tabelcode** 325 · **Rollen** parent, child, grensparent, grenschild · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `model_assignment_id` | PK | Surrogaatsleutel. |
| `assignment_code` | UK | Functionele sleutel van de assignment. |
| `temperature` |  | Sampling-temperatuur. Leeg als niet ingesteld. |
| `top_p` |  | Nucleus-sampling-drempel. Leeg als niet ingesteld. |
| `maximum_output_tokens` |  | Maximaal aantal uitvoertokens. Leeg als niet ingesteld. |
| `publication_timestamp` |  | Moment van publicatie. Leeg zolang de assignment in voorbereiding is; daarna wijzigt de rij niet meer. |
| `execution_profile_code` | GV | Het execution profile dat de assignment realiseert. Grensverwijzing naar `execution_profile.execution_profile_code` in semantic-foundation. |
| `llm_model_id` | FK | Het geselecteerde model. → `llm_model` |
| `ref_thinking_effort_id` | FK | De gevraagde denkinspanning. Leeg als niet ingesteld. → `ref_thinking_effort` |

**Grenschildren** [`execution.model_assignment_code`](#work-execution-execution) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| model_assignment_id | assignment_code | temperature | top_p | maximum_output_tokens | publication_timestamp | execution_profile_code | llm_model_id | ref_thinking_effort_id |
|---|---|---|---|---|---|---|---|---|
| 1 | ma-survey-sources | NULL | NULL | 8000 | 2026-09-10 12:00:00+00 | DPG-EXP-C2 | 2 | NULL |
| 2 | ma-derive-ldm | 0.2 | NULL | 16000 | 2026-09-10 12:00:00+00 | DPG-SPE-C2 | 1 | 3 |

</details>

### `ref_thinking_effort` { #execution-configuration-ref-thinking-effort }

Referentietabel met de posities van Thinking Effort: hoeveel redeneerinspanning van het model wordt gevraagd (`standard`, `medium`, `high`).

**Tabelcode** 301 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_thinking_effort_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de positie. |
| `description` |  | Omschrijving van de positie. |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| ref_thinking_effort_id | code | description |
|---|---|---|
| 1 | standard | The standard effort; no increased effort is requested. |
| 2 | medium | More effort than standard, without asking for the maximum. |
| 3 | high | The highest effort the model and its provider allow. |

*Opmerking:* De omschrijvingen zijn ingekorte Engelse weergaven van de Nederlandse LDM-posities.

</details>

### `step_model_selection` { #execution-configuration-step-model-selection }

Junction-tabel (associatieve entiteit): welke model assignment een Entoli Context gebruikt voor één orchestration step. Per context en stap ten hoogste één rij.

**Tabelcode** 330 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `step_model_selection_id` | PK | Surrogaatsleutel. |
| `orchestration_step_code` | UK, GV | De orchestration step waarvoor het model wordt gekozen. Grensverwijzing naar `orchestration_step.orchestration_step_code` in orchestration-definition. |
| `entoli_context_id` | FK, UK | De context die de keuze maakt. → `entoli_context` |
| `model_assignment_id` | FK | De gekozen model assignment. → `model_assignment` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| step_model_selection_id | orchestration_step_code | entoli_context_id | model_assignment_id |
|---|---|---|---|
| 1 | survey-sources | 1 | 1 |
| 2 | derive-ldm | 1 | 2 |

</details>

## work-execution

Het werk zelf: instruction sets en wat erin is opgenomen, executions, artefacten, handoffs en menselijke invoer. TDM `entoli-agent-development-work-execution-postgresql` versie 4.0.0.

### `artifact` { #work-execution-artifact }

Duurzame, expliciete vastlegging van een resultaat of beslissing. Voortgebracht door precies één execution en bruikbaar als werkbron voor latere instruction sets.

**Tabelcode** 420 · **Rollen** parent, child, grenschild · **Kleur** lichtroze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `artifact_id` | PK | Surrogaatsleutel. |
| `artifact_code` | UK | Workspace-brede identificatie: de `artifact-id` uit de YAML-frontmatter van het artefact. Uniek en nooit hergebruikt. |
| `origin_code` |  | Herkomstcode in de vorm `YYMM.XXXX`. Meerdere artefacten kunnen dezelfde herkomst delen, dus niet uniek. |
| `status` |  | Levenscyclustoestand, bijvoorbeeld `draft` of `final`. Vrije tekst: er is geen codelijst. |
| `artifact_content` |  | Tekstuele inhoud van het artefact. Eén inhoud per artefact, zonder versies. |
| `artifact_type_code` | GV | Het artefacttype dat het artefact classificeert. Grensverwijzing naar `artifact_type.code` in semantic-foundation. |
| `execution_id` | FK | De execution die het artefact heeft voortgebracht. → `execution` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| artifact_id | artifact_code | origin_code | status | artifact_content | artifact_type_code | execution_id |
|---|---|---|---|---|---|---|
| 1 | art-2609.0001 | 2609.A1B2 | final | Survey of three cited sources … | source-survey | 1 |
| 2 | art-2609.0002 | 2609.C3D4 | draft | {"model": {"id": "ldm-agent-definition"}, …} | logical-data-model | 2 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `final` en `draft` zijn aangenomen waarden. Het formaat van de artefactcodes is fictief.

</details>

### `artifact_derivation` { #work-execution-artifact-derivation }

Junction-tabel voor de relatie ARTIFACT is based on ARTIFACT: het afgeleide artefact is gebaseerd op het bronartefact. Een artefact kan niet van zichzelf zijn afgeleid (`CK_428_01`).

**Tabelcode** 428 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `artifact_derivation_id` | PK | Surrogaatsleutel. |
| `derived_artifact_id` | FK, UK | Het afgeleide artefact. → `artifact` |
| `source_artifact_id` | FK, UK | Het bronartefact. → `artifact` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| artifact_derivation_id | derived_artifact_id | source_artifact_id |
|---|---|---|
| 1 | 2 | 1 |

</details>

### `execution` { #work-execution-execution }

Tijdgebonden uitvoering van één gepubliceerde versie van één orchestration step, binnen één Entoli Context en volgens één gepubliceerde orchestratieversie, geïnstrueerd door één instruction set en met één model assignment.

**Tabelcode** 421 · **Rollen** parent, child, grenschild · **Kleur** lichtroze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `execution_id` | PK | Surrogaatsleutel. |
| `execution_code` | UK | Functionele sleutel van de execution. |
| `start_timestamp` |  | Moment waarop de execution begon. |
| `status` |  | Toestand, bijvoorbeeld `completed` of `terminated`. Vrije tekst: er is geen codelijst. |
| `model_assignment_code` | GV | De model assignment die daadwerkelijk is gebruikt. Grensverwijzing naar `model_assignment.assignment_code` in execution-configuration. |
| `orchestration_step_definition_code` | GV | De gepubliceerde stapversie die is uitgevoerd. Grensverwijzing naar `orchestration_step_definition.orchestration_step_definition_code` in orchestration-definition. |
| `entoli_context_code` | GV | De context waarin de execution plaatsvond. Grensverwijzing naar `entoli_context.entoli_context_code` in execution-configuration. |
| `orchestration_specification_version_code` | GV | De gepubliceerde orchestratieversie die de execution volgde. Grensverwijzing naar `orchestration_specification_version.orchestration_specification_version_code` in orchestration-definition. |
| `instruction_set_id` | FK | De instruction set die de execution instrueert. → `instruction_set` |
| `handoff_id` | FK | De handoff die de execution heeft voortgebracht. Leeg als er geen is. → `handoff` |
| `ref_termination_reason_id` | FK | Reden van voortijdige beëindiging. Leeg bij normale afloop. → `ref_termination_reason` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| execution_id | execution_code | start_timestamp | status | model_assignment_code | orchestration_step_definition_code | entoli_context_code | orchestration_specification_version_code | instruction_set_id | handoff_id | ref_termination_reason_id |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | exec-2609.A1B2 | 2026-09-25 09:01:00+00 | completed | ma-survey-sources | 8a3f1c22-7b44-4e0d-a9c1-6e2b5f7d9c10 | entoli-dev | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 1 | 1 | NULL |
| 2 | exec-2609.C3D4 | 2026-09-25 09:15:00+00 | terminated | ma-derive-ldm | c41e9b07-3d5a-4f82-b6e3-0a9d8c7b6e21 | entoli-dev | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 2 | NULL | 1 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `completed` en `terminated` zijn aangenomen waarden.

</details>

### `handoff` { #work-execution-handoff }

Expliciete overdracht van interpretatie en context van een afgeronde execution naar vervolgwerk. Opgenomen in precies één latere instruction set.

**Tabelcode** 422 · **Rollen** parent, child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `handoff_id` | PK | Surrogaatsleutel. |
| `handoff_code` | UK | Functionele sleutel van de handoff. |
| `human_intervention` |  | Waar als de overdracht om menselijke tussenkomst vraagt. |
| `timestamp` |  | Moment van de overdracht. |
| `content_message` |  | Inhoud van de overdracht. |
| `instruction_set_id` | FK | De latere instruction set waarin de handoff is opgenomen. De ontvangende execution vind je via die instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| handoff_id | handoff_code | human_intervention | timestamp | content_message | instruction_set_id |
|---|---|---|---|---|---|
| 1 | hf-2609.0001 | false | 2026-09-25 09:12:00+00 | Source survey complete; three sources cited. | 2 |

*Opmerking:* De handoff die execution 1 voortbrengt, is opgenomen in Instruction Set 2, die de volgende stap instrueert.

</details>

### `human_context` { #work-execution-human-context }

Definitie van de invoer die een mens levert om een agent intent te starten en inhoudelijk te sturen. De velden staan in `human_context_parameter`.

**Tabelcode** 423 · **Rollen** parent, worteltabel · **Kleur** geel

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `human_context_id` | PK | Surrogaatsleutel. |
| `human_context_code` | UK | Functionele sleutel van de human context. |
| `name` |  | Weergavenaam. |
| `description` |  | Toelichting op de human context. |
| `status` |  | Levenscyclustoestand. Vrije tekst: er is geen codelijst. |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| human_context_id | human_context_code | name | description | status |
|---|---|---|---|---|
| 1 | hc-modelling-request | Modelling request | NULL | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

</details>

### `human_context_parameter` { #work-execution-human-context-parameter }

Eén veld van een human context. Dit is de definitie van het veld, geen ingevulde waarde; ingevulde waarden staan in `instruction_set_parameter_value`.

**Tabelcode** 429 · **Rollen** parent, child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `human_context_parameter_id` | PK | Surrogaatsleutel. |
| `parameter_code` | UK | Code van het veld, uniek binnen de eigen human context (niet daarbuiten). |
| `label` |  | Tekst die de gebruiker naast het veld ziet. Mag wijzigen zonder dat het veld verandert. |
| `description` |  | Toelichting die naast het veld wordt getoond. |
| `data_type` |  | Type waarde dat het veld accepteert, bijvoorbeeld `text` of `date`. Bepaalt hoe een ingevulde waarde wordt gelezen. Vrije tekst: er is geen codelijst. |
| `required` |  | Waar als de gebruiker het veld moet invullen. |
| `display_order` | UK | Positie van het veld in de weergavevolgorde, uniek binnen de human context. |
| `human_context_id` | FK, UK | De human context waartoe het veld behoort. → `human_context` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| human_context_parameter_id | parameter_code | label | description | data_type | required | display_order | human_context_id |
|---|---|---|---|---|---|---|---|
| 1 | subject-area | Subject area | NULL | text | true | 1 | 1 |
| 2 | target-release | Target release | Release the model is meant for. | date | false | 2 | 1 |

*Opmerking:* `data_type` heeft in de bronnen geen codelijst; `text` en `date` zijn aangenomen waarden.

</details>

### `instruction_set` { #work-execution-instruction-set }

Execution-specifieke samenstelling van normatieve, semantische en aangeleverde context die één execution instrueert, aangestuurd door één agent intent. Wat erin is opgenomen, staat in de `instruction_set_*`-tabellen.

**Tabelcode** 424 · **Rollen** parent, grenschild · **Kleur** lichtroze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_id` | PK | Surrogaatsleutel. |
| `instruction_set_code` | UK | Stabiele identificatie (UUID), toegekend bij aanmaak, nooit gewijzigd of hergebruikt. |
| `content` |  | De samengestelde instructie-inhoud, inclusief ingevulde parameterwaarden. Leeg zolang de samenstelling loopt. Legt vast wat is verstuurd; vervangt de onderliggende rijen niet. |
| `created_at` |  | Moment van aanmaak. Technische kolom, niet afkomstig uit het LDM. |
| `agent_intent_code` | GV | De agent intent die de samenstelling aanstuurt. Grensverwijzing naar `agent_intent.agent_intent_code` in agent-definition. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| instruction_set_id | instruction_set_code | content | created_at | agent_intent_code |
|---|---|---|---|---|
| 1 | 0b6e4d2a-1f3c-4e5b-9a7d-8c2f6e4a1d01 | ## Instructions ↵ 1. List every external source … | 2026-09-25 09:00:00+00 | niam-analyst.survey-sources |
| 2 | 7e9a1c3b-5d2f-4a6e-8b0c-9d1e3f5a7c02 | ## Instructions ↵ 1. Read the conceptual model … | 2026-09-25 09:14:00+00 | ldm-modeller.derive-ldm |

</details>

### `instruction_set_artifact` { #work-execution-instruction-set-artifact }

Legt vast dat een artefact in een instruction set voorkomt, en in welke rol (werkbron of uitvoer). Het LDM modelleert dit als gewone entiteit, dus in de kleurregels geen junction-tabel.

**Tabelcode** 426 · **Rollen** child · **Kleur** lichtblauw

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_artifact_id` | PK | Surrogaatsleutel. |
| `artifact_id` | FK, UK | Het artefact. → `artifact` |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |
| `ref_instruction_set_artifact_role_id` | FK, UK | De rol van het artefact in de instruction set. → `ref_instruction_set_artifact_role` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| instruction_set_artifact_id | artifact_id | instruction_set_id | ref_instruction_set_artifact_role_id |
|---|---|---|---|
| 1 | 1 | 2 | 1 |
| 2 | 2 | 2 | 2 |

</details>

### `instruction_set_element` { #work-execution-instruction-set-element }

Junction-tabel: een element uit het semantisch model die in een instruction set is opgenomen. Die kant ligt in semantic-foundation; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 431 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_element_id` | PK | Surrogaatsleutel. |
| `element_code` | UK, GV | De opgenomen element uit het semantisch model. Grensverwijzing naar `element.element_code` in semantic-foundation. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| instruction_set_element_id | element_code | instruction_set_id |
|---|---|---|
| 1 | agent | 2 |
| 2 | agent-intent | 2 |

</details>

### `instruction_set_entoli_agent_intent_rule` { #work-execution-instruction-set-entoli-agent-intent-rule }

Junction-tabel: een Entoli Agent Intent Rule die in een instruction set is opgenomen. Die kant ligt in agent-definition; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 436 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_entoli_agent_intent_rule_id` | PK | Surrogaatsleutel. |
| `entoli_agent_intent_rule_code` | UK, GV | De opgenomen Entoli Agent Intent Rule. Grensverwijzing naar `entoli_agent_intent_rule.rule_code` in agent-definition. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| instruction_set_entoli_agent_intent_rule_id | entoli_agent_intent_rule_code | instruction_set_id |
|---|---|---|
| 1 | EAIR-LDM-001 | 2 |

</details>

### `instruction_set_intent_instruction` { #work-execution-instruction-set-intent-instruction }

Junction-tabel: een intent instruction die in een instruction set is opgenomen. Die kant ligt in agent-definition; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 427 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_intent_instruction_id` | PK | Surrogaatsleutel. |
| `intent_instruction_code` | UK, GV | De opgenomen intent instruction. Grensverwijzing naar `intent_instruction.intent_instruction_code` in agent-definition. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| instruction_set_intent_instruction_id | intent_instruction_code | instruction_set_id |
|---|---|---|
| 1 | niam-analyst.survey-sources.01 | 1 |
| 2 | ldm-modeller.derive-ldm.01 | 2 |
| 3 | ldm-modeller.derive-ldm.02 | 2 |

</details>

### `instruction_set_parameter_value` { #work-execution-instruction-set-parameter-value }

Junction-tabel (associatieve entiteit): de waarde die voor één veld van een human context is ingevuld bij het samenstellen van één instruction set. Per instruction set en veld ten hoogste één rij; een niet-ingevuld veld heeft geen rij.

**Tabelcode** 430 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_parameter_value_id` | PK | Surrogaatsleutel. |
| `parameter_value` |  | De ingevulde waarde als tekst, te lezen volgens `human_context_parameter.data_type`. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |
| `human_context_parameter_id` | FK, UK | Het veld waarvoor de waarde is ingevuld. → `human_context_parameter` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| instruction_set_parameter_value_id | parameter_value | instruction_set_id | human_context_parameter_id |
|---|---|---|---|
| 1 | Agent definition | 2 | 1 |
| 2 | 2026-10-01 | 2 | 2 |

</details>

### `instruction_set_regime_rule` { #work-execution-instruction-set-regime-rule }

Junction-tabel: een regime rule die in een instruction set is opgenomen. Die kant ligt in semantic-foundation; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 435 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_regime_rule_id` | PK | Surrogaatsleutel. |
| `regime_rule_code` | UK, GV | De opgenomen regime rule. Grensverwijzing naar `regime_rule.rule_code` in semantic-foundation. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| instruction_set_regime_rule_id | regime_rule_code | instruction_set_id |
|---|---|---|
| 1 | SR-CNB-001 | 2 |
| 2 | SY-REL-001 | 2 |
| 3 | TM-STR-001 | 2 |

*Opmerking:* Dit zijn de Regime Rules voor de posities CNB, REL en STR die de Agent Intent `ldm-modeller.derive-ldm` declareert.

</details>

### `instruction_set_relationship` { #work-execution-instruction-set-relationship }

Junction-tabel: een relatie uit het semantisch model die in een instruction set is opgenomen. Die kant ligt in semantic-foundation; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 432 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_relationship_id` | PK | Surrogaatsleutel. |
| `relationship_code` | UK, GV | De opgenomen relatie uit het semantisch model. Grensverwijzing naar `relationship.relationship_code` in semantic-foundation. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| instruction_set_relationship_id | relationship_code | instruction_set_id |
|---|---|---|
| 1 | agent-exposes-agent-intent | 2 |

</details>

### `instruction_set_universal_rule` { #work-execution-instruction-set-universal-rule }

Junction-tabel: een universal rule die in een instruction set is opgenomen. Die kant ligt in semantic-foundation; daarom is het een grensverwijzing en geen foreign key.

**Tabelcode** 434 · **Rollen** junction-tabel, child, grenschild · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `instruction_set_universal_rule_id` | PK | Surrogaatsleutel. |
| `universal_rule_code` | UK, GV | De opgenomen universal rule. Grensverwijzing naar `universal_rule.rule_code` in semantic-foundation. |
| `instruction_set_id` | FK, UK | De instruction set. → `instruction_set` |

<details class="example" markdown>
<summary>Voorbeeldrijen (4), illustratief</summary>

| instruction_set_universal_rule_id | universal_rule_code | instruction_set_id |
|---|---|---|
| 1 | UNI-001 | 1 |
| 2 | UNI-001 | 2 |
| 3 | UNI-002 | 2 |
| 4 | UNI-003 | 2 |

*Opmerking:* Elke Instruction Set bevat elke actieve Universal Rule. De rijen tonen maar een deel van die opnames.

</details>

### `ref_instruction_set_artifact_role` { #work-execution-ref-instruction-set-artifact-role }

Referentietabel met de rollen van een artefact in een instruction set: werkbron of uitvoer.

**Tabelcode** 401 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_instruction_set_artifact_role_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de rol. |
| `description` |  | Omschrijving van de rol. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| ref_instruction_set_artifact_role_id | code | description |
|---|---|---|
| 1 | working-source | The Instruction Set uses the Artifact as a working source. |
| 2 | output | The Artifact was produced by the Execution this Instruction Set instructs. |

*Opmerking:* De omschrijvingen zijn ingekorte Engelse weergaven van de Nederlandse LDM-posities.

</details>

### `ref_termination_reason` { #work-execution-ref-termination-reason }

Referentietabel met de Entoli-eigen redenen waarom een execution voortijdig eindigt.

**Tabelcode** 402 · **Rollen** referentietabel, parent, worteltabel · **Kleur** groen

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `ref_termination_reason_id` | PK | Surrogaatsleutel. |
| `code` | UK | Code van de reden. |
| `description` |  | Omschrijving van de reden. |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| ref_termination_reason_id | code | description |
|---|---|---|
| 1 | blocked | The affected work was recorded as blocked. |
| 2 | failed | The Execution failed before it produced its output. |

*Opmerking:* Het LDM legt de posities van Termination Reason nog niet vast; beide codes zijn fictief.

</details>

## orchestration-definition

De orchestraties: specificaties, stappen, en hun geversioneerde definities en volgorde. TDM `entoli-agent-development-orchestration-definition-postgresql` versie 4.0.0.

### `orchestration_specification` { #orchestration-definition-orchestration-specification }

Herbruikbare specificatie van een samenhangende reeks orchestration steps en hun volgorde, met een inhoudelijk doel. Onafhankelijk van een Entoli Context.

**Tabelcode** 522 · **Rollen** parent, grensparent, worteltabel · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_specification_id` | PK | Surrogaatsleutel. |
| `specification_code` | UK | Functionele sleutel van de specificatie. |
| `specification_name` |  | Weergavenaam. |
| `content_goal` |  | Het inhoudelijke doel van de orchestratie. |

**Grenschildren** [`entoli_context_orchestration_specification.orchestration_specification_code`](#execution-configuration-entoli-context-orchestration-specification) (execution-configuration)

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| orchestration_specification_id | specification_code | specification_name | content_goal |
|---|---|---|---|
| 1 | model-derivation | Model derivation | Derive a logical data model from surveyed sources. |

</details>

### `orchestration_specification_version` { #orchestration-definition-orchestration-specification-version }

Genummerde versie van een orchestration specification: welke stapversies erin zitten en welke volgorde geldt. Na publicatie onveranderlijk.

**Tabelcode** 524 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_specification_version_id` | PK, UK | Surrogaatsleutel. |
| `orchestration_specification_version_code` | UK | Stabiele identificatie (UUID), toegekend bij aanmaak, nooit gewijzigd of hergebruikt. |
| `version_number` | UK | Volgnummer vanaf 1, uniek binnen de specificatie en hoger dan dat van elke eerdere versie. |
| `publication_timestamp` |  | Moment van publicatie. Leeg zolang de versie wordt bewerkt; daarna wijzigt de rij niet meer. |
| `orchestration_specification_id` | FK, UK | De specificatie waarvan dit een versie is. → `orchestration_specification` |

**Grenschildren** [`execution.orchestration_specification_version_code`](#work-execution-execution) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| orchestration_specification_version_id | orchestration_specification_version_code | version_number | publication_timestamp | orchestration_specification_id |
|---|---|---|---|---|
| 1 | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 1 | 2026-09-10 12:00:00+00 | 1 |

</details>

### `orchestration_step` { #orchestration-definition-orchestration-step }

Stap van een orchestration specification, los van zijn geversioneerde inhoud. Naam en aangeroepen agent intent staan in `orchestration_step_definition`.

**Tabelcode** 520 · **Rollen** parent, child, grensparent · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_step_id` | PK, UK | Surrogaatsleutel. |
| `orchestration_step_code` | UK | Stabiele functionele sleutel, uniek over alle specificaties. Verandert niet bij hernoemen of herschikken en wordt nooit hergebruikt. |
| `orchestration_specification_id` | FK, UK | De specificatie waartoe de stap behoort. → `orchestration_specification` |

**Grenschildren** [`step_model_selection.orchestration_step_code`](#execution-configuration-step-model-selection) (execution-configuration)

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| orchestration_step_id | orchestration_step_code | orchestration_specification_id |
|---|---|---|
| 1 | survey-sources | 1 |
| 2 | derive-ldm | 1 |

</details>

### `orchestration_step_definition` { #orchestration-definition-orchestration-step-definition }

Genummerde versie van de inhoud van een orchestration step: naam, beschrijving en de agent intent die de stap aanroept. Na publicatie onveranderlijk.

**Tabelcode** 521 · **Rollen** parent, child, grensparent, grenschild · **Kleur** sterk roze

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_step_definition_id` | PK, UK | Surrogaatsleutel. |
| `orchestration_step_definition_code` | UK | Stabiele identificatie (UUID), toegekend bij aanmaak, nooit gewijzigd of hergebruikt. |
| `version_number` | UK | Volgnummer vanaf 1, uniek binnen de stap en hoger dan dat van elke eerdere versie. |
| `publication_timestamp` |  | Moment van publicatie. Leeg zolang de versie wordt bewerkt; daarna wijzigt de rij niet meer. |
| `step_name` |  | Naam van de stap in deze versie. |
| `content_description` |  | Inhoudelijke beschrijving van de stap. |
| `agent_intent_code` | GV | De agent intent die de stap aanroept. Grensverwijzing naar `agent_intent.agent_intent_code` in agent-definition. |
| `orchestration_step_id` | FK, UK | De stap waarvan dit een versie is. → `orchestration_step` |

**Grenschildren** [`execution.orchestration_step_definition_code`](#work-execution-execution) (work-execution)

<details class="example" markdown>
<summary>Voorbeeldrijen (3), illustratief</summary>

| orchestration_step_definition_id | orchestration_step_definition_code | version_number | publication_timestamp | step_name | content_description | agent_intent_code | orchestration_step_id |
|---|---|---|---|---|---|---|---|
| 1 | 8a3f1c22-7b44-4e0d-a9c1-6e2b5f7d9c10 | 1 | 2026-09-10 12:00:00+00 | Survey sources | NULL | niam-analyst.survey-sources | 1 |
| 2 | c41e9b07-3d5a-4f82-b6e3-0a9d8c7b6e21 | 1 | 2026-09-10 12:00:00+00 | Derive LDM | Derive entities and relationships … | ldm-modeller.derive-ldm | 2 |
| 3 | f2d7a6b3-9e1c-4a05-8b4d-3c6e2f1a0b32 | 2 | NULL | Derive LDM | Draft: also derive constraints … | ldm-modeller.derive-ldm | 2 |

*Opmerking:* Versie 2 van de definitie `derive-ldm` is nog niet gepubliceerd (`publication_timestamp` is NULL).

</details>

### `orchestration_step_precedence` { #orchestration-definition-orchestration-step-precedence }

Junction-tabel (associatieve entiteit): directe volgorde tussen twee stappen binnen één specificatieversie. De volgende stap start pas als de voorgaande is afgerond. Een stap gaat niet aan zichzelf vooraf (`CK_523_01`); kringloopvrijheid over meerdere rijen dwingt de database niet af.

**Tabelcode** 523 · **Rollen** junction-tabel, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_step_precedence_id` | PK | Surrogaatsleutel. |
| `orchestration_specification_version_id` | FK, UK | De specificatieversie waarin de volgorde geldt. → `orchestration_specification_version`, `orchestration_version_step` |
| `preceding_step_id` | FK, UK | De stap die eerst moet zijn afgerond. `FK_523_525_02` eist dat deze stap in dezelfde versie is opgenomen. → `orchestration_version_step` |
| `following_step_id` | FK, UK | De stap die daarna mag starten. `FK_523_525_01` eist dat deze stap in dezelfde versie is opgenomen. → `orchestration_version_step` |

<details class="example" markdown>
<summary>Voorbeeldrijen (1), illustratief</summary>

| orchestration_step_precedence_id | orchestration_specification_version_id | preceding_step_id | following_step_id |
|---|---|---|---|
| 1 | 1 | 1 | 2 |

</details>

### `orchestration_version_step` { #orchestration-definition-orchestration-version-step }

Junction-tabel (associatieve entiteit): legt vast dat een stap in een specificatieversie is opgenomen, en met welke stapversie. Een stap komt hoogstens één keer per versie voor.

**Tabelcode** 525 · **Rollen** junction-tabel, parent, child · **Kleur** wit

| Kolom | Sleutel | Omschrijving |
|---|---|---|
| `orchestration_version_step_id` | PK | Surrogaatsleutel. |
| `orchestration_specification_version_id` | FK, UK | De specificatieversie. → `orchestration_specification_version` |
| `orchestration_step_id` | FK, UK | De opgenomen stap. → `orchestration_step`, `orchestration_step_definition` |
| `orchestration_step_definition_id` | FK | De gebruikte stapversie. `FK_525_521_01` eist dat die versie bij deze stap hoort. → `orchestration_step_definition` |
| `orchestration_specification_id` | FK | Herhaalt de specificatie van de versie en van de stap. De samengestelde foreign keys `FK_525_524_01` en `FK_525_520_01` dwingen zo af dat stap en versie bij dezelfde specificatie horen. → `orchestration_specification_version`, `orchestration_step` |

<details class="example" markdown>
<summary>Voorbeeldrijen (2), illustratief</summary>

| orchestration_version_step_id | orchestration_specification_version_id | orchestration_step_id | orchestration_step_definition_id | orchestration_specification_id |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 1 |

</details>
