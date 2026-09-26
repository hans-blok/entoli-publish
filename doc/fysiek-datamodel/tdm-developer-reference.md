# Technisch datamodel — naslag voor ontwikkelaars

Geschreven voor: ontwikkelaars die bouwen op de Entoli PostgreSQL-database, die bevragen of die laden.

Dit document beschrijft elke tabel van de huidige PostgreSQL Technical Data Models (TDM), gegroepeerd per Logical Instance. De TDM-JSON-bestanden zijn de bron voor de fysieke structuur. De Logical Data Models (LDM) zijn de bron voor de logische namen van entiteiten en relaties. De tabeldefinities ("Eén rij") zijn samenvattingen die voor deze naslag zijn geschreven; de definities in het LDM blijven leidend. Dit document wordt niet door een script in de repository gegenereerd en niet automatisch bijgewerkt: als een TDM verandert, moet dit document worden herzien.

> **Let op:** dit is een vertaling van de Engelse versie. Er kunnen vertaalfouten in zitten. Voorbeelddata, kolomnamen, constraintnamen en de namen van LDM-entiteiten en -relaties zijn onvertaald gebleven.

## Zo lees je dit document

- **Verplicht** `ja` betekent dat de kolom `NOT NULL` is.
- **Sleutel** `PK` markeert een primaire-sleutelkolom en `FK` een kolom van een foreign key.
- **Logische verwijzing** markeert een codekolom die verwijst naar een rij in een andere Logical Instance. Er zit geen foreign key achter: PostgreSQL dwingt de verwijzing niet af. De applicatie houdt haar consistent.
- Constraintnamen worden opgebouwd uit de tabelcode (`PK_<table>`, `FK_<child>_<parent>_<nn>`, `UC_<table>_<nn>`, `CK_<table>_<nn>`); zie `physical-naming-convention.md` (niet gepubliceerd op deze site).
- De relatie die bij een foreign key of een logische verwijzing staat, is de LDM-relatie die het TDM als bron vastlegt.
- Foreign keys gebruiken `ON DELETE NO ACTION` en `ON UPDATE NO ACTION`, tenzij anders vermeld.

**Voorbeeldrijen zijn illustratief.** Het is geen database-inhoud en geen voorgeschreven seed data. Eén scenario loopt door alle tabellen: de NIAM Analyst inventariseert bronnen, waarna de Logical Data Modeller een logisch datamodel afleidt. Rijen die naar elkaar verwijzen gebruiken dezelfde sleutels, ook over Logical Instances heen. Waarden van surrogaatsleutels zijn illustratief; de database kent ze toe. Codes van referentietabellen komen uit de LDM-posities waar het LDM die definieert. Waar uit de bronnen geen waarde volgt, is een herkenbare fictieve waarde gebruikt en staat er een opmerking bij. Lange tekst is ingekort met `…`; `↵` markeert een regeleinde.

## Bronnen

| Logical Instance | Tabelcodes | Technical Data Model | Versie | Versie Logical Data Model |
|---|---|---|---|---|
| semantic-foundation | 100–199 | `entoli-agent-development-semantic-foundation-postgresql` | 2.0.0 | 2.0.0 |
| agent-definition | 200–299 | `entoli-agent-development-agent-definition-postgresql` | 2.0.0 | 2.0.0 |
| execution-configuration | 300–399 | `entoli-agent-development-execution-configuration-postgresql` | 2.2.0 | 2.2.0 |
| work-execution | 400–499 | `entoli-agent-development-work-execution-postgresql` | 4.0.0 | 4.0.0 |
| orchestration-definition | 500–599 | `entoli-agent-development-orchestration-definition-postgresql` | 4.0.0 | 4.0.0 |

## Inhoud

- [semantic-foundation](#semantic-foundation) (22 tabellen): `artifact_type`, `canon`, `canon_rule`, `element`, `element_canon_rule`, `element_regime_rule`, `element_universal_rule`, `execution_profile`, `knowledge_domain`, `knowledge_specification`, `ref_development_phase`, `ref_reasoning_regime`, `ref_rule_status`, `ref_rule_type`, `ref_source_regime`, `ref_synthesis_regime`, `ref_task_regime`, `regime_rule`, `relationship`, `semantic_model`, `template`, `universal_rule`
- [agent-definition](#agent-definition) (8 tabellen): `agent`, `agent_intent`, `agent_package`, `entoli_agent_intent_rule`, `entoli_agent_rule`, `intent_instruction`, `ref_rule_status`, `ref_rule_type`
- [execution-configuration](#execution-configuration) (9 tabellen): `entoli_context`, `entoli_context_orchestration_specification`, `llm_account`, `llm_model`, `llm_provider`, `llm_provider_thinking_effort`, `model_assignment`, `ref_thinking_effort`, `step_model_selection`
- [work-execution](#work-execution) (17 tabellen): `artifact`, `artifact_derivation`, `execution`, `handoff`, `human_context`, `human_context_parameter`, `instruction_set`, `instruction_set_artifact`, `instruction_set_element`, `instruction_set_entoli_agent_intent_rule`, `instruction_set_intent_instruction`, `instruction_set_parameter_value`, `instruction_set_regime_rule`, `instruction_set_relationship`, `instruction_set_universal_rule`, `ref_instruction_set_artifact_role`, `ref_termination_reason`
- [orchestration-definition](#orchestration-definition) (6 tabellen): `orchestration_specification`, `orchestration_specification_version`, `orchestration_step`, `orchestration_step_definition`, `orchestration_step_precedence`, `orchestration_version_step`

## semantic-foundation

Technical Data Model `entoli-agent-development-semantic-foundation-postgresql` versie 2.0.0, afgeleid van Logical Data Model `entoli-agent-development-semantic-foundation` versie 2.0.0.

### `artifact_type`

**Eén rij:** Eén soort artefact dat een canon definieert, zoals een logisch datamodel of een broninventarisatie.  
**Tabelcode:** 120 · **LDM-bron:** entiteit **ARTIFACT TYPE** (`artifact-type`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `artifact_type_id` | integer | ja | PK |
| `code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `canon_id` | integer | ja | FK |

**Primaire sleutel:** `PK_120` (`artifact_type_id`)

**Uniciteitsconstraints:**

- `UC_120_01` (`code`)

**Foreign keys:**

- `FK_120_121_01`: (`canon_id`) → `canon` (`canon_id`) · relatie CANON defines ARTIFACT TYPE (`canon-defines-artifact-type`)

**Illustratieve voorbeeldrijen (2):**

| artifact_type_id | code | name | description | canon_id |
|---|---|---|---|---|
| 1 | logical-data-model | Logical Data Model | NULL | 1 |
| 2 | source-survey | Source Survey | A demarcated subset of cited external sources. | 1 |

### `canon`

**Eén rij:** Eén canon: een geversioneerd geheel van normatieve kennis dat een semantisch model, regels, artefacttypen en templates definieert.  
**Tabelcode:** 121 · **LDM-bron:** entiteit **CANON** (`canon`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `canon_id` | integer | ja | PK |
| `code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `version` | text | ja |  |
| `status` | text | ja |  |
| `semantic_model_id` | integer | ja | FK |

**Primaire sleutel:** `PK_121` (`canon_id`)

**Uniciteitsconstraints:**

- `UC_121_01` (`code`)

**Foreign keys:**

- `FK_121_133_01`: (`semantic_model_id`) → `semantic_model` (`semantic_model_id`) · relatie CANON defines SEMANTIC MODEL (`canon-defines-semantic-model`)

**Illustratieve voorbeeldrijen (1):**

| canon_id | code | name | description | version | status | semantic_model_id |
|---|---|---|---|---|---|---|
| 1 | entoli-agent-development-canon | Entoli Agent Development Canon | Normative knowledge for developing Entoli agents … | 2.6.0 | current | 1 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `current` is een aangenomen waarde.

### `canon_rule`

**Eén rij:** Eén regel die een canon stelt. Het is een concrete soort Entoli Rule en draagt de gedeelde regelcode, tekst, status en type.  
**Tabelcode:** 122 · **LDM-bron:** entiteit **CANON RULE** (`canon-rule`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `entoli_rule_id` | integer | ja | PK |
| `rule_code` | text | ja |  |
| `rule_text` | text | ja |  |
| `reference` | text | nee |  |
| `canon_id` | integer | ja | FK |
| `ref_rule_status_id` | integer | ja | FK |
| `ref_rule_type_id` | integer | ja | FK |

**Primaire sleutel:** `PK_122` (`entoli_rule_id`)

**Uniciteitsconstraints:**

- `UC_122_01` (`rule_code`)

**Foreign keys:**

- `FK_122_121_01`: (`canon_id`) → `canon` (`canon_id`) · relatie CANON defines CANON RULE (`canon-defines-canon-rule`)
- `FK_122_106_01`: (`ref_rule_status_id`) → `ref_rule_status` (`ref_rule_status_id`) · relatie ENTOLI RULE has RULE STATUS (REF) (`entoli-rule-has-rule-status`)
- `FK_122_107_01`: (`ref_rule_type_id`) → `ref_rule_type` (`ref_rule_type_id`) · relatie ENTOLI RULE has RULE TYPE (REF) (`entoli-rule-has-rule-type`)

**Illustratieve voorbeeldrijen (1):**

| entoli_rule_id | rule_code | rule_text | reference | canon_id | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|---|
| 1 | CR-TRM-001 | Every canonical term MUST be used without synonyms. | constitution.md#Article 7 | 1 | 2 | 1 |

*Opmerking:* De bronnen noemen geen codes van Canon Rules; `CR-TRM-001` is fictief.

### `element`

**Eén rij:** Eén element van een semantisch model: een benoemd begrip met zijn definitie, zoals Agent of Instruction Set.  
**Tabelcode:** 124 · **LDM-bron:** entiteit **ELEMENT** (`element`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `element_id` | integer | ja | PK |
| `element_code` | text | ja |  |
| `element_name` | text | ja |  |
| `definition` | text | ja |  |
| `semantic_model_id` | integer | ja | FK |

**Primaire sleutel:** `PK_124` (`element_id`)

**Uniciteitsconstraints:**

- `UC_124_01` (`element_code`)

**Foreign keys:**

- `FK_124_133_01`: (`semantic_model_id`) → `semantic_model` (`semantic_model_id`) · relatie SEMANTIC MODEL consists of ELEMENT (`semantic-model-consists-of-element`)

**Illustratieve voorbeeldrijen (4):**

| element_id | element_code | element_name | definition | semantic_model_id |
|---|---|---|---|---|
| 1 | agent | Agent | An explicitly defined, autonomous executor … | 1 |
| 2 | agent-intent | Agent Intent | One invocable capability of an Agent … | 1 |
| 3 | instruction-set | Instruction Set | The assembled instructions for one Execution … | 1 |
| 4 | execution | Execution | One run of an orchestration step by an LLM … | 1 |

### `element_canon_rule`

**Eén rij:** Eén gebruik van een Element in een Canon Rule: de regel noemt dat Element of hangt ervan af.  
**Tabelcode:** 130 · **LDM-bron:** relatie **ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `element_canon_rule_id` | integer | ja | PK |
| `element_id` | integer | ja | FK |
| `entoli_rule_id` | integer | ja | FK |

**Primaire sleutel:** `PK_130` (`element_canon_rule_id`)

**Uniciteitsconstraints:**

- `UC_130_01` (`element_id`, `entoli_rule_id`)

**Foreign keys:**

- `FK_130_124_01`: (`element_id`) → `element` (`element_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)
- `FK_130_122_01`: (`entoli_rule_id`) → `canon_rule` (`entoli_rule_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)

**Illustratieve voorbeeldrijen (1):**

| element_canon_rule_id | element_id | entoli_rule_id |
|---|---|---|
| 1 | 1 | 1 |

### `element_regime_rule`

**Eén rij:** Eén gebruik van een Element in een Regime Rule: de regel noemt dat Element of hangt ervan af.  
**Tabelcode:** 131 · **LDM-bron:** relatie **ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `element_regime_rule_id` | integer | ja | PK |
| `element_id` | integer | ja | FK |
| `regime_rule_id` | integer | ja | FK |

**Primaire sleutel:** `PK_131` (`element_regime_rule_id`)

**Uniciteitsconstraints:**

- `UC_131_01` (`element_id`, `regime_rule_id`)

**Foreign keys:**

- `FK_131_124_01`: (`element_id`) → `element` (`element_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)
- `FK_131_123_01`: (`regime_rule_id`) → `regime_rule` (`regime_rule_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)

**Illustratieve voorbeeldrijen (1):**

| element_regime_rule_id | element_id | regime_rule_id |
|---|---|---|
| 1 | 2 | 3 |

### `element_universal_rule`

**Eén rij:** Eén gebruik van een Element in een Universal Rule: de regel noemt dat Element of hangt ervan af.  
**Tabelcode:** 137 · **LDM-bron:** relatie **ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `element_universal_rule_id` | integer | ja | PK |
| `element_id` | integer | ja | FK |
| `universal_rule_id` | integer | ja | FK |

**Primaire sleutel:** `PK_137` (`element_universal_rule_id`)

**Uniciteitsconstraints:**

- `UC_137_01` (`element_id`, `universal_rule_id`)

**Foreign keys:**

- `FK_137_124_01`: (`element_id`) → `element` (`element_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)
- `FK_137_136_01`: (`universal_rule_id`) → `universal_rule` (`universal_rule_id`) · relatie ELEMENT is used in ENTOLI RULE (`element-is-used-in-entoli-rule`)

**Illustratieve voorbeeldrijen (2):**

| element_universal_rule_id | element_id | universal_rule_id |
|---|---|---|
| 1 | 4 | 1 |
| 2 | 3 | 2 |

### `execution_profile`

**Eén rij:** Eén kenmerkende combinatie van een Development Phase en één positie op elk van de vier Execution Regime-assen.  
**Tabelcode:** 135 · **LDM-bron:** entiteit **EXECUTION PROFILE** (`execution-profile`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `execution_profile_id` | integer | ja | PK |
| `execution_profile_code` | text | ja |  |
| `execution_profile_name` | text | ja |  |
| `execution_profile_description` | text | ja |  |
| `ref_development_phase_id` | integer | ja | FK |
| `ref_reasoning_regime_id` | integer | ja | FK |
| `ref_source_regime_id` | integer | ja | FK |
| `ref_synthesis_regime_id` | integer | ja | FK |
| `ref_task_regime_id` | integer | ja | FK |

**Primaire sleutel:** `PK_135` (`execution_profile_id`)

**Uniciteitsconstraints:**

- `UC_135_01` (`execution_profile_code`)

**Foreign keys:**

- `FK_135_101_01`: (`ref_development_phase_id`) → `ref_development_phase` (`ref_development_phase_id`) · relatie DEVELOPMENT PHASE (REF) guides EXECUTION PROFILE (`development-phase-guides-execution-profile`)
- `FK_135_102_01`: (`ref_reasoning_regime_id`) → `ref_reasoning_regime` (`ref_reasoning_regime_id`) · relatie EXECUTION PROFILE declares REASONING REGIME (REF) (`execution-profile-declares-reasoning-regime`)
- `FK_135_103_01`: (`ref_source_regime_id`) → `ref_source_regime` (`ref_source_regime_id`) · relatie EXECUTION PROFILE declares SOURCE REGIME (REF) (`execution-profile-declares-source-regime`)
- `FK_135_104_01`: (`ref_synthesis_regime_id`) → `ref_synthesis_regime` (`ref_synthesis_regime_id`) · relatie EXECUTION PROFILE declares SYNTHESIS REGIME (REF) (`execution-profile-declares-synthesis-regime`)
- `FK_135_105_01`: (`ref_task_regime_id`) → `ref_task_regime` (`ref_task_regime_id`) · relatie EXECUTION PROFILE declares TASK REGIME (REF) (`execution-profile-declares-task-regime`)

**Illustratieve voorbeeldrijen (2):**

| execution_profile_id | execution_profile_code | execution_profile_name | execution_profile_description | ref_development_phase_id | ref_reasoning_regime_id | ref_source_regime_id | ref_synthesis_regime_id | ref_task_regime_id |
|---|---|---|---|---|---|---|---|---|
| 1 | DPG-EXP-C2 | Source survey | The Intent surveys named external sources, each cited … | 1 | 2 | 3 | 1 | 1 |
| 2 | DPG-SPE-C2 | Formalising a structure | The Intent makes the architecture of canonical material explicit … | 3 | 3 | 2 | 2 | 2 |

### `knowledge_domain`

**Eén rij:** Eén kennisgebied waarin agents werken, zoals agentontwikkeling of datamodellering.  
**Tabelcode:** 125 · **LDM-bron:** entiteit **KNOWLEDGE DOMAIN** (`knowledge-domain`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `knowledge_domain_id` | integer | ja | PK |
| `code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |

**Primaire sleutel:** `PK_125` (`knowledge_domain_id`)

**Uniciteitsconstraints:**

- `UC_125_01` (`code`)

**Illustratieve voorbeeldrijen (2):**

| knowledge_domain_id | code | name | description |
|---|---|---|---|
| 1 | agent-development | Agent Development | NULL |
| 2 | data-modelling | Data Modelling | Conceptual, logical and technical data modelling. |

### `knowledge_specification`

**Eén rij:** Eén specificatie van de kennis die binnen een Knowledge Domain geldt, optioneel gerealiseerd door een canon.  
**Tabelcode:** 126 · **LDM-bron:** entiteit **KNOWLEDGE SPECIFICATION** (`knowledge-specification`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `knowledge_specification_id` | integer | ja | PK |
| `code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `canon_id` | integer | nee | FK |
| `knowledge_domain_id` | integer | ja | FK |

**Primaire sleutel:** `PK_126` (`knowledge_specification_id`)

**Uniciteitsconstraints:**

- `UC_126_01` (`code`)

**Foreign keys:**

- `FK_126_121_01`: (`canon_id`) → `canon` (`canon_id`) · relatie KNOWLEDGE SPECIFICATION is realized by CANON (`knowledge-specification-is-realized-by-canon`)
- `FK_126_125_01`: (`knowledge_domain_id`) → `knowledge_domain` (`knowledge_domain_id`) · relatie KNOWLEDGE SPECIFICATION specifies KNOWLEDGE DOMAIN (`knowledge-specification-specifies-knowledge-domain`)

**Illustratieve voorbeeldrijen (2):**

| knowledge_specification_id | code | name | description | canon_id | knowledge_domain_id |
|---|---|---|---|---|---|
| 1 | ks-agent-development | Agent development knowledge | NULL | 1 | 1 |
| 2 | ks-data-modelling | Data modelling knowledge | Not yet realized by a canon. | NULL | 2 |

### `ref_development_phase`

**Eén rij:** Eén positie van Development Phase die een agent classificeert, zoals Exploration of Specification.  
**Tabelcode:** 101 · **LDM-bron:** entiteit **DEVELOPMENT PHASE (REF)** (`development-phase`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_development_phase_id` | integer | ja | PK |
| `development_phase_code` | text | ja |  |
| `development_phase_description` | text | ja |  |

**Primaire sleutel:** `PK_101` (`ref_development_phase_id`)

**Uniciteitsconstraints:**

- `UC_101_01` (`development_phase_code`)

**Illustratieve voorbeeldrijen (5):**

| ref_development_phase_id | development_phase_code | development_phase_description |
|---|---|---|
| 1 | EXP | Exploration |
| 2 | ORD | Ordering |
| 3 | SPC | Specification |
| 4 | RLS | Realisation |
| 5 | TST | Testing |

*Opmerking:* Vijf van de zeven posities zijn weergegeven; `REG` (Registering) en `OPR` (Operationalisation) zijn weggelaten.

### `ref_reasoning_regime`

**Eén rij:** Eén positie van Reasoning Regime: hoeveel cognitieve vrijheid het LLM heeft.  
**Tabelcode:** 102 · **LDM-bron:** entiteit **REASONING REGIME (REF)** (`reasoning-regime`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_reasoning_regime_id` | integer | ja | PK |
| `execution_regime_code` | text | ja |  |
| `execution_regime_description` | text | ja |  |

**Primaire sleutel:** `PK_102` (`ref_reasoning_regime_id`)

**Uniciteitsconstraints:**

- `UC_102_01` (`execution_regime_code`)

**Illustratieve voorbeeldrijen (4):**

| ref_reasoning_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | EXP | Explorative |
| 2 | ITP | Interpretive |
| 3 | CNS | Constrained |
| 4 | DTM | Deterministic |

### `ref_rule_status`

**Eén rij:** Eén status die een Canon Rule, Regime Rule of Universal Rule kan hebben (inactief of actief).  
**Tabelcode:** 106 · **LDM-bron:** entiteit **RULE STATUS (REF)** (`rule-status`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_rule_status_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_106` (`ref_rule_status_id`)

**Uniciteitsconstraints:**

- `UC_106_01` (`code`)

**Illustratieve voorbeeldrijen (2):**

| ref_rule_status_id | code | description |
|---|---|---|
| 1 | 0 | Inactive |
| 2 | 1 | Active |

### `ref_rule_type`

**Eén rij:** Eén regeltype voor Canon Rules, Regime Rules en Universal Rules: gebod, verbod of toestemming.  
**Tabelcode:** 107 · **LDM-bron:** entiteit **RULE TYPE (REF)** (`rule-type`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_rule_type_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_107` (`ref_rule_type_id`)

**Uniciteitsconstraints:**

- `UC_107_01` (`code`)

**Illustratieve voorbeeldrijen (3):**

| ref_rule_type_id | code | description |
|---|---|---|
| 1 | obl | Obligation |
| 2 | prh | Prohibition |
| 3 | prm | Permission |

### `ref_source_regime`

**Eén rij:** Eén positie van Source Regime: welke kennis toelaatbaar is.  
**Tabelcode:** 103 · **LDM-bron:** entiteit **SOURCE REGIME (REF)** (`source-regime`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_source_regime_id` | integer | ja | PK |
| `execution_regime_code` | text | ja |  |
| `execution_regime_description` | text | ja |  |

**Primaire sleutel:** `PK_103` (`ref_source_regime_id`)

**Uniciteitsconstraints:**

- `UC_103_01` (`execution_regime_code`)

**Illustratieve voorbeeldrijen (4):**

| ref_source_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | INB | Input-bound |
| 2 | CNB | Canon-bound |
| 3 | EXB | External-source-bound |
| 4 | OPN | Open |

### `ref_synthesis_regime`

**Eén rij:** Eén positie van Synthesis Regime: wat er met betekenis mag gebeuren.  
**Tabelcode:** 104 · **LDM-bron:** entiteit **SYNTHESIS REGIME (REF)** (`synthesis-regime`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_synthesis_regime_id` | integer | ja | PK |
| `execution_regime_code` | text | ja |  |
| `execution_regime_description` | text | ja |  |

**Primaire sleutel:** `PK_104` (`ref_synthesis_regime_id`)

**Uniciteitsconstraints:**

- `UC_104_01` (`execution_regime_code`)

**Illustratieve voorbeeldrijen (3):**

| ref_synthesis_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | PRV | Preserving |
| 2 | REL | Relating |
| 3 | GEN | Generating |

### `ref_task_regime`

**Eén rij:** Eén positie van Task Regime: het type bewerking en de structuur van de uitvoer.  
**Tabelcode:** 105 · **LDM-bron:** entiteit **TASK REGIME (REF)** (`task-regime`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_task_regime_id` | integer | ja | PK |
| `execution_regime_code` | text | ja |  |
| `execution_regime_description` | text | ja |  |

**Primaire sleutel:** `PK_105` (`ref_task_regime_id`)

**Uniciteitsconstraints:**

- `UC_105_01` (`execution_regime_code`)

**Illustratieve voorbeeldrijen (5):**

| ref_task_regime_id | execution_regime_code | execution_regime_description |
|---|---|---|
| 1 | EXT | Extracting |
| 2 | STR | Structuring |
| 3 | TRF | Transforming |
| 4 | EVL | Evaluating |
| 5 | ORI | Originating |

### `regime_rule`

**Eén rij:** Eén Operational Rule die via precies één Execution Regime-as geldt. Precies één van de vier regimeverwijzingen is gevuld.  
**Tabelcode:** 123 · **LDM-bron:** entiteit **REGIME RULE** (`regime-rule`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `regime_rule_id` | integer | ja | PK |
| `rule_code` | text | ja |  |
| `rule_text` | text | ja |  |
| `reference` | text | nee |  |
| `ref_rule_status_id` | integer | ja | FK |
| `ref_rule_type_id` | integer | ja | FK |
| `ref_reasoning_regime_id` | integer | nee | FK |
| `ref_source_regime_id` | integer | nee | FK |
| `ref_synthesis_regime_id` | integer | nee | FK |
| `ref_task_regime_id` | integer | nee | FK |

**Primaire sleutel:** `PK_123` (`regime_rule_id`)

**Uniciteitsconstraints:**

- `UC_123_01` (`rule_code`)

**Foreign keys:**

- `FK_123_106_01`: (`ref_rule_status_id`) → `ref_rule_status` (`ref_rule_status_id`) · relatie ENTOLI RULE has RULE STATUS (REF) (`entoli-rule-has-rule-status`)
- `FK_123_107_01`: (`ref_rule_type_id`) → `ref_rule_type` (`ref_rule_type_id`) · relatie ENTOLI RULE has RULE TYPE (REF) (`entoli-rule-has-rule-type`)
- `FK_123_102_01`: (`ref_reasoning_regime_id`) → `ref_reasoning_regime` (`ref_reasoning_regime_id`) · relatie REGIME RULE governs REASONING REGIME (REF) (`regime-rule-governs-reasoning-regime`)
- `FK_123_103_01`: (`ref_source_regime_id`) → `ref_source_regime` (`ref_source_regime_id`) · relatie REGIME RULE governs SOURCE REGIME (REF) (`regime-rule-governs-source-regime`)
- `FK_123_104_01`: (`ref_synthesis_regime_id`) → `ref_synthesis_regime` (`ref_synthesis_regime_id`) · relatie REGIME RULE governs SYNTHESIS REGIME (REF) (`regime-rule-governs-synthesis-regime`)
- `FK_123_105_01`: (`ref_task_regime_id`) → `ref_task_regime` (`ref_task_regime_id`) · relatie REGIME RULE governs TASK REGIME (REF) (`regime-rule-governs-task-regime`)

**Check-constraints:**

- `CK_123_01`: `num_nonnulls(ref_reasoning_regime_id, ref_source_regime_id, ref_synthesis_regime_id, ref_task_regime_id) = 1`

**Illustratieve voorbeeldrijen (3):**

| regime_rule_id | rule_code | rule_text | reference | ref_rule_status_id | ref_rule_type_id | ref_reasoning_regime_id | ref_source_regime_id | ref_synthesis_regime_id | ref_task_regime_id |
|---|---|---|---|---|---|---|---|---|---|
| 1 | SR-CNB-001 | The LLM MUST NOT load or rely on Work-Sources beyond what is derivable from the canonical sources provided. … | doctrine.source-regime.md#§5.2 | 2 | 2 | NULL | 2 | NULL | NULL |
| 2 | SY-REL-001 | The LLM MUST NOT change the meaning of existing content. | doctrine.synthesis-regime.md#§3.2 | 2 | 2 | NULL | NULL | 2 | NULL |
| 3 | TM-STR-001 | The LLM MUST produce output whose primary content is relationships, organisation, or architecture made explicit. | NULL | 2 | 1 | NULL | NULL | NULL | 2 |

*Opmerking:* Regelcodes en -teksten komen uit de Operational Rules; de teksten zijn ingekort.

### `relationship`

**Eén rij:** Eén benoemde relatie tussen twee Elements van een semantisch model.  
**Tabelcode:** 127 · **LDM-bron:** entiteit **RELATIONSHIP** (`relationship`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `relationship_id` | integer | ja | PK |
| `relationship_code` | text | ja |  |
| `name` | text | ja |  |
| `from_element_id` | integer | ja | FK |
| `to_element_id` | integer | ja | FK |
| `semantic_model_id` | integer | ja | FK |

**Primaire sleutel:** `PK_127` (`relationship_id`)

**Uniciteitsconstraints:**

- `UC_127_01` (`relationship_code`)

**Foreign keys:**

- `FK_127_124_01`: (`from_element_id`) → `element` (`element_id`) · relatie RELATIONSHIP from ELEMENT (`relationship-from-element`)
- `FK_127_124_02`: (`to_element_id`) → `element` (`element_id`) · relatie RELATIONSHIP to ELEMENT (`relationship-to-element`)
- `FK_127_133_01`: (`semantic_model_id`) → `semantic_model` (`semantic_model_id`) · relatie SEMANTIC MODEL consists of RELATIONSHIP (`semantic-model-consists-of-relationship`)

**Illustratieve voorbeeldrijen (2):**

| relationship_id | relationship_code | name | from_element_id | to_element_id | semantic_model_id |
|---|---|---|---|---|---|
| 1 | agent-exposes-agent-intent | exposes capabilities via | 1 | 2 | 1 |
| 2 | execution-is-instructed-by-instruction-set | is instructed by | 4 | 3 | 1 |

### `semantic_model`

**Eén rij:** Eén semantisch model: de verzameling Elements en Relationships die een canon definieert.  
**Tabelcode:** 133 · **LDM-bron:** entiteit **SEMANTIC MODEL** (`semantic-model`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `semantic_model_id` | integer | ja | PK |
| `semantic_model_code` | text | ja |  |
| `semantic_model_name` | text | ja |  |
| `semantic_model_description` | text | nee |  |

**Primaire sleutel:** `PK_133` (`semantic_model_id`)

**Uniciteitsconstraints:**

- `UC_133_01` (`semantic_model_code`)

**Illustratieve voorbeeldrijen (1):**

| semantic_model_id | semantic_model_code | semantic_model_name | semantic_model_description |
|---|---|---|---|
| 1 | entoli-agent-development | Entoli Agent Development | Elements and relationships of agent development … |

### `template`

**Eén rij:** Eén template dat de inhoud van een Artifact Type structureert.  
**Tabelcode:** 134 · **LDM-bron:** entiteit **TEMPLATE** (`template`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `template_id` | integer | ja | PK |
| `code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `content_format` | text | ja |  |
| `template_content` | text | ja |  |
| `artifact_type_id` | integer | ja | FK |

**Primaire sleutel:** `PK_134` (`template_id`)

**Uniciteitsconstraints:**

- `UC_134_01` (`code`)

**Foreign keys:**

- `FK_134_120_01`: (`artifact_type_id`) → `artifact_type` (`artifact_type_id`) · relatie ARTIFACT TYPE is structured by TEMPLATE (`artifact-type-is-structured-by-template`)

**Illustratieve voorbeeldrijen (1):**

| template_id | code | name | description | content_format | template_content | artifact_type_id |
|---|---|---|---|---|---|---|
| 1 | ldm-json | Logical Data Model (JSON) | NULL | json | {"model": {…}, "entities": [ … ]} | 1 |

*Opmerking:* `content_format` heeft in de bronnen geen codelijst; `json` is een aangenomen waarde.

### `universal_rule`

**Eén rij:** Eén Operational Rule die geldt voor elke Agent en elke Agent Intent, ongeacht hun Execution Regimes.  
**Tabelcode:** 136 · **LDM-bron:** entiteit **UNIVERSAL RULE** (`universal-rule`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `universal_rule_id` | integer | ja | PK |
| `rule_code` | text | ja |  |
| `rule_text` | text | ja |  |
| `reference` | text | nee |  |
| `ref_rule_status_id` | integer | ja | FK |
| `ref_rule_type_id` | integer | ja | FK |

**Primaire sleutel:** `PK_136` (`universal_rule_id`)

**Uniciteitsconstraints:**

- `UC_136_01` (`rule_code`)

**Foreign keys:**

- `FK_136_106_01`: (`ref_rule_status_id`) → `ref_rule_status` (`ref_rule_status_id`) · relatie ENTOLI RULE has RULE STATUS (REF) (`entoli-rule-has-rule-status`)
- `FK_136_107_01`: (`ref_rule_type_id`) → `ref_rule_type` (`ref_rule_type_id`) · relatie ENTOLI RULE has RULE TYPE (REF) (`entoli-rule-has-rule-type`)

**Illustratieve voorbeeldrijen (3):**

| universal_rule_id | rule_code | rule_text | reference | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|
| 1 | UNI-001 | The LLM MUST NOT present a fact, a source, a decision or a result as established unless … . | constitution.md#Article 3 §1 | 2 | 2 |
| 2 | UNI-002 | Where the work depends on information that is neither supplied nor obtainable …, the LLM MUST identify … . | constitution.md#Article 3 §1 | 2 | 1 |
| 3 | UNI-003 | The LLM MUST NOT resolve a material ambiguity or a decisive gap silently. … | constitution.md#Proposition | 2 | 2 |

## agent-definition

Technical Data Model `entoli-agent-development-agent-definition-postgresql` versie 2.0.0, afgeleid van Logical Data Model `entoli-agent-development-agent-definition` versie 2.0.0.

### `agent`

**Eén rij:** Eén Entoli-agent: een expliciet gedefinieerde, autonome uitvoerder met een eigen grens, geclassificeerd door één Development Phase.  
**Tabelcode:** 220 · **LDM-bron:** entiteit **AGENT** (`agent`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `agent_id` | integer | ja | PK |
| `agent_code` | text | ja |  |
| `agent_name` | text | ja |  |
| `boundary` | text | nee |  |
| `knowledge_specification_code` | text | nee | logical reference |
| `development_phase_code` | text | ja | logical reference |
| `entoli_context_code` | text | ja | logical reference |
| `agent_package_id` | integer | nee | FK |

**Primaire sleutel:** `PK_220` (`agent_id`)

**Uniciteitsconstraints:**

- `UC_220_01` (`agent_code`)

**Foreign keys:**

- `FK_220_222_01`: (`agent_package_id`) → `agent_package` (`agent_package_id`) · relatie AGENT belongs to AGENT PACKAGE (`agent-belongs-to-agent-package`)

**Logische verwijzingen (geen databaseconstraint):**

- `knowledge_specification_code` → `knowledge_specification`.`code` in semantic-foundation · relatie AGENT specifies knowledge for KNOWLEDGE SPECIFICATION (`agent-specifies-knowledge-for-knowledge-specification`)
- `development_phase_code` → `ref_development_phase`.`development_phase_code` in semantic-foundation · relatie DEVELOPMENT PHASE (REF) classifies AGENT (`development-phase-classifies-agent`)
- `entoli_context_code` → `entoli_context`.`entoli_context_code` in execution-configuration · relatie ENTOLI CONTEXT owns AGENT (`entoli-context-owns-agent`)

**Illustratieve voorbeeldrijen (2):**

| agent_id | agent_code | agent_name | boundary | knowledge_specification_code | development_phase_code | entoli_context_code | agent_package_id |
|---|---|---|---|---|---|---|---|
| 1 | niam-analyst | NIAM Analyst | Analyses domain statements and source material … | ks-data-modelling | EXP | entoli-dev | 1 |
| 2 | ldm-modeller | Logical Data Modeller | Translates conceptual meaning into a logical data model … | NULL | SPC | entoli-dev | 1 |

### `agent_intent`

**Eén rij:** Eén aanroepbaar vermogen van een agent, met zijn gedeclareerde positie op elke Execution Regime-as.  
**Tabelcode:** 221 · **LDM-bron:** entiteit **AGENT INTENT** (`agent-intent`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `agent_intent_id` | integer | ja | PK |
| `agent_intent_code` | text | ja |  |
| `agent_intent_name` | text | ja |  |
| `reasoning_regime_code` | text | ja | logical reference |
| `source_regime_code` | text | nee | logical reference |
| `synthesis_regime_code` | text | nee | logical reference |
| `task_regime_code` | text | nee | logical reference |
| `agent_id` | integer | ja | FK |

**Primaire sleutel:** `PK_221` (`agent_intent_id`)

**Uniciteitsconstraints:**

- `UC_221_01` (`agent_intent_code`)
- `UC_221_02` (`agent_id`, `agent_intent_id`)

**Foreign keys:**

- `FK_221_220_01`: (`agent_id`) → `agent` (`agent_id`) · relatie AGENT exposes capabilities via AGENT INTENT (`agent-exposes-capabilities-via-agent-intent`)

**Logische verwijzingen (geen databaseconstraint):**

- `reasoning_regime_code` → `ref_reasoning_regime`.`execution_regime_code` in semantic-foundation · relatie AGENT INTENT declares REASONING REGIME (REF) (`agent-intent-declares-reasoning-regime`)
- `source_regime_code` → `ref_source_regime`.`execution_regime_code` in semantic-foundation · relatie AGENT INTENT declares SOURCE REGIME (REF) (`agent-intent-declares-source-regime`)
- `synthesis_regime_code` → `ref_synthesis_regime`.`execution_regime_code` in semantic-foundation · relatie AGENT INTENT declares SYNTHESIS REGIME (REF) (`agent-intent-declares-synthesis-regime`)
- `task_regime_code` → `ref_task_regime`.`execution_regime_code` in semantic-foundation · relatie AGENT INTENT declares TASK REGIME (REF) (`agent-intent-declares-task-regime`)

**Illustratieve voorbeeldrijen (2):**

| agent_intent_id | agent_intent_code | agent_intent_name | reasoning_regime_code | source_regime_code | synthesis_regime_code | task_regime_code | agent_id |
|---|---|---|---|---|---|---|---|
| 1 | niam-analyst.survey-sources | Survey sources | ITP | EXB | PRV | EXT | 1 |
| 2 | ldm-modeller.derive-ldm | Derive logical data model | CNS | CNB | REL | STR | 2 |

### `agent_package`

**Eén rij:** Eén pakket dat agents groepeert onder een gemeenschappelijke Knowledge Specification.  
**Tabelcode:** 222 · **LDM-bron:** entiteit **AGENT PACKAGE** (`agent-package`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `agent_package_id` | integer | ja | PK |
| `package_code` | text | ja |  |
| `package_name` | text | ja |  |
| `version` | text | ja |  |
| `status` | text | ja |  |
| `description` | text | nee |  |
| `knowledge_specification_code` | text | ja | logical reference |

**Primaire sleutel:** `PK_222` (`agent_package_id`)

**Uniciteitsconstraints:**

- `UC_222_01` (`package_code`)

**Logische verwijzingen (geen databaseconstraint):**

- `knowledge_specification_code` → `knowledge_specification`.`code` in semantic-foundation · relatie KNOWLEDGE SPECIFICATION scopes AGENT PACKAGE (`knowledge-specification-scopes-agent-package`)

**Illustratieve voorbeeldrijen (1):**

| agent_package_id | package_code | package_name | version | status | description | knowledge_specification_code |
|---|---|---|---|---|---|---|
| 1 | modelling-agents | Modelling agents | 1.0.0 | active | NULL | ks-agent-development |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

### `entoli_agent_intent_rule`

**Eén rij:** Eén regel die één Agent Intent begrenst en één Entoli Agent Rule van dezelfde agent operationaliseert.  
**Tabelcode:** 223 · **LDM-bron:** entiteit **ENTOLI AGENT INTENT RULE** (`entoli-agent-intent-rule`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `entoli_rule_id` | integer | ja | PK |
| `rule_code` | text | ja |  |
| `rule_text` | text | ja |  |
| `reference` | text | nee |  |
| `agent_intent_id` | integer | ja | FK |
| `agent_rule_id` | integer | ja | FK |
| `ref_rule_status_id` | integer | ja | FK |
| `ref_rule_type_id` | integer | ja | FK |
| `agent_id` | integer | ja | FK |

**Primaire sleutel:** `PK_223` (`entoli_rule_id`)

**Uniciteitsconstraints:**

- `UC_223_01` (`rule_code`)

**Foreign keys:**

- `FK_223_221_01`: (`agent_intent_id`) → `agent_intent` (`agent_intent_id`) · relatie ENTOLI AGENT INTENT RULE constraints AGENT INTENT (`entoli-agent-intent-rule-constraints-agent-intent`)
- `FK_223_224_01`: (`agent_rule_id`) → `entoli_agent_rule` (`entoli_rule_id`) · relatie ENTOLI AGENT RULE is operationalized by ENTOLI AGENT INTENT RULE (`entoli-agent-rule-is-operationalized-by-entoli-agent-intent-rule`)
- `FK_223_201_01`: (`ref_rule_status_id`) → `ref_rule_status` (`ref_rule_status_id`) · relatie ENTOLI RULE has RULE STATUS (REF) (`entoli-rule-has-rule-status`)
- `FK_223_202_01`: (`ref_rule_type_id`) → `ref_rule_type` (`ref_rule_type_id`) · relatie ENTOLI RULE has RULE TYPE (REF) (`entoli-rule-has-rule-type`)
- `FK_223_221_02`: (`agent_id`, `agent_intent_id`) → `agent_intent` (`agent_id`, `agent_intent_id`) · relatie ENTOLI AGENT INTENT RULE constraints AGENT INTENT (`entoli-agent-intent-rule-constraints-agent-intent`)
- `FK_223_224_02`: (`agent_id`, `agent_rule_id`) → `entoli_agent_rule` (`agent_id`, `entoli_rule_id`) · relatie ENTOLI AGENT RULE is operationalized by ENTOLI AGENT INTENT RULE (`entoli-agent-rule-is-operationalized-by-entoli-agent-intent-rule`)

**Illustratieve voorbeeldrijen (1):**

| entoli_rule_id | rule_code | rule_text | reference | agent_intent_id | agent_rule_id | ref_rule_status_id | ref_rule_type_id | agent_id |
|---|---|---|---|---|---|---|---|---|
| 11 | EAIR-LDM-001 | When deriving an LDM, the LLM MUST keep every conceptual name … | NULL | 2 | 1 | 2 | 1 | 2 |

*Opmerking:* `agent_id` herhaalt de agent van zowel de Agent Intent als de Entoli Agent Rule; de samengestelde foreign keys eisen dat het dezelfde agent is. De regelcode is fictief.

### `entoli_agent_rule`

**Eén rij:** Eén regel die voor één agent geldt en optioneel een Canon Rule concretiseert.  
**Tabelcode:** 224 · **LDM-bron:** entiteit **ENTOLI AGENT RULE** (`entoli-agent-rule`), gematerialiseerd als zelfstandig concreet subtype

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `entoli_rule_id` | integer | ja | PK |
| `rule_code` | text | ja |  |
| `rule_text` | text | ja |  |
| `reference` | text | nee |  |
| `canon_rule_code` | text | nee | logical reference |
| `agent_id` | integer | ja | FK |
| `ref_rule_status_id` | integer | ja | FK |
| `ref_rule_type_id` | integer | ja | FK |

**Primaire sleutel:** `PK_224` (`entoli_rule_id`)

**Uniciteitsconstraints:**

- `UC_224_01` (`rule_code`)
- `UC_224_02` (`agent_id`, `entoli_rule_id`)

**Foreign keys:**

- `FK_224_220_01`: (`agent_id`) → `agent` (`agent_id`) · relatie ENTOLI AGENT RULE governs AGENT (`entoli-agent-rule-governs-agent`)
- `FK_224_201_01`: (`ref_rule_status_id`) → `ref_rule_status` (`ref_rule_status_id`) · relatie ENTOLI RULE has RULE STATUS (REF) (`entoli-rule-has-rule-status`)
- `FK_224_202_01`: (`ref_rule_type_id`) → `ref_rule_type` (`ref_rule_type_id`) · relatie ENTOLI RULE has RULE TYPE (REF) (`entoli-rule-has-rule-type`)

**Logische verwijzingen (geen databaseconstraint):**

- `canon_rule_code` → `canon_rule`.`rule_code` in semantic-foundation · relatie CANON RULE is concretized by ENTOLI AGENT RULE (`canon-rule-is-concretized-by-entoli-agent-rule`)

**Illustratieve voorbeeldrijen (1):**

| entoli_rule_id | rule_code | rule_text | reference | canon_rule_code | agent_id | ref_rule_status_id | ref_rule_type_id |
|---|---|---|---|---|---|---|---|
| 1 | EAR-LDM-001 | The Logical Data Modeller MUST NOT change conceptual meaning. | NULL | CR-TRM-001 | 2 | 2 | 2 |

*Opmerking:* De regelcodes zijn fictief.

### `intent_instruction`

**Eén rij:** Eén instructie van een Agent Intent, op een vaste positie in de volgorde van de instructies van die intent.  
**Tabelcode:** 225 · **LDM-bron:** entiteit **INTENT INSTRUCTION** (`intent-instruction`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `intent_instruction_id` | integer | ja | PK |
| `intent_instruction_code` | text | ja |  |
| `instruction` | text | ja |  |
| `sequence` | integer | ja |  |
| `agent_intent_id` | integer | ja | FK |

**Primaire sleutel:** `PK_225` (`intent_instruction_id`)

**Uniciteitsconstraints:**

- `UC_225_01` (`intent_instruction_code`)
- `UC_225_02` (`agent_intent_id`, `sequence`)

**Foreign keys:**

- `FK_225_221_01`: (`agent_intent_id`) → `agent_intent` (`agent_intent_id`) · relatie AGENT INTENT performed through INTENT INSTRUCTION (`agent-intent-performed-through-intent-instruction`)

**Check-constraints:**

- `CK_225_01`: `sequence > 0`

**Illustratieve voorbeeldrijen (3):**

| intent_instruction_id | intent_instruction_code | instruction | sequence | agent_intent_id |
|---|---|---|---|---|
| 1 | niam-analyst.survey-sources.01 | List every external source and cite it … | 1 | 1 |
| 2 | ldm-modeller.derive-ldm.01 | Read the conceptual model and the source survey … | 1 | 2 |
| 3 | ldm-modeller.derive-ldm.02 | Record every modelling decision with its ground … | 2 | 2 |

*Opmerking:* Het formaat van codes van intent instructions ligt in de bronnen niet vast; de codes zijn fictief.

### `ref_rule_status`

**Eén rij:** Eén status die een agentregel of agent-intentregel kan hebben (inactief of actief).  
**Tabelcode:** 201 · **LDM-bron:** entiteit **RULE STATUS (REF)** (`rule-status`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_rule_status_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_201` (`ref_rule_status_id`)

**Uniciteitsconstraints:**

- `UC_201_01` (`code`)

**Illustratieve voorbeeldrijen (2):**

| ref_rule_status_id | code | description |
|---|---|---|
| 1 | 0 | Inactive |
| 2 | 1 | Active |

### `ref_rule_type`

**Eén rij:** Eén regeltype voor agentregels en agent-intentregels: gebod, verbod of toestemming.  
**Tabelcode:** 202 · **LDM-bron:** entiteit **RULE TYPE (REF)** (`rule-type`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_rule_type_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_202` (`ref_rule_type_id`)

**Uniciteitsconstraints:**

- `UC_202_01` (`code`)

**Illustratieve voorbeeldrijen (3):**

| ref_rule_type_id | code | description |
|---|---|---|
| 1 | obl | Obligation |
| 2 | prh | Prohibition |
| 3 | prm | Permission |

## execution-configuration

Technical Data Model `entoli-agent-development-execution-configuration-postgresql` versie 2.2.0, afgeleid van Logical Data Model `entoli-agent-development-execution-configuration` versie 2.2.0.

### `entoli_context`

**Eén rij:** Eén Entoli Context: een omgeving die agents, LLM-accounts en modelselecties bezit.  
**Tabelcode:** 320 · **LDM-bron:** entiteit **ENTOLI CONTEXT** (`entoli-context`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `entoli_context_id` | integer | ja | PK |
| `entoli_context_code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `status` | text | ja |  |

**Primaire sleutel:** `PK_320` (`entoli_context_id`)

**Uniciteitsconstraints:**

- `UC_320_01` (`entoli_context_code`)

**Illustratieve voorbeeldrijen (1):**

| entoli_context_id | entoli_context_code | name | description | status |
|---|---|---|---|---|
| 1 | entoli-dev | Entoli development | NULL | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

### `entoli_context_orchestration_specification`

**Eén rij:** Eén Orchestration Specification die in één Entoli Context beschikbaar is gesteld.  
**Tabelcode:** 329 · **LDM-bron:** relatie **ENTOLI CONTEXT uses ORCHESTRATION SPECIFICATION (`entoli-context-orchestration-specification`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `entoli_context_orchestration_specification_id` | integer | ja | PK |
| `orchestration_specification_code` | text | ja | logical reference |
| `entoli_context_id` | integer | ja | FK |

**Primaire sleutel:** `PK_329` (`entoli_context_orchestration_specification_id`)

**Uniciteitsconstraints:**

- `UC_329_01` (`entoli_context_id`, `orchestration_specification_code`)

**Foreign keys:**

- `FK_329_320_01`: (`entoli_context_id`) → `entoli_context` (`entoli_context_id`) · relatie ENTOLI CONTEXT uses ORCHESTRATION SPECIFICATION (`entoli-context-orchestration-specification`)

**Logische verwijzingen (geen databaseconstraint):**

- `orchestration_specification_code` → `orchestration_specification`.`specification_code` in orchestration-definition · relatie ENTOLI CONTEXT uses ORCHESTRATION SPECIFICATION (`entoli-context-orchestration-specification`)

**Illustratieve voorbeeldrijen (1):**

| entoli_context_orchestration_specification_id | orchestration_specification_code | entoli_context_id |
|---|---|---|
| 1 | model-derivation | 1 |

### `llm_account`

**Eén rij:** Eén account bij een LLM Provider dat een Entoli Context beschikbaar stelt, met de versleutelde API-sleutel.  
**Tabelcode:** 322 · **LDM-bron:** entiteit **LLM ACCOUNT** (`llm-account`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `llm_account_id` | integer | ja | PK |
| `account_code` | text | ja |  |
| `account_name` | text | ja |  |
| `description` | text | nee |  |
| `api_key_ciphertext` | bytea | nee |  |
| `created_at` | timestamptz (default `CURRENT_TIMESTAMP`) | ja |  |
| `api_key_rotated_at` | timestamptz | nee |  |
| `entoli_context_id` | integer | ja | FK |
| `llm_provider_id` | integer | ja | FK |

**Primaire sleutel:** `PK_322` (`llm_account_id`)

**Uniciteitsconstraints:**

- `UC_322_01` (`account_code`)

**Foreign keys:**

- `FK_322_320_01`: (`entoli_context_id`) → `entoli_context` (`entoli_context_id`) · relatie ENTOLI CONTEXT makes available LLM ACCOUNT (`entoli-context-makes-available-llm-account`)
- `FK_322_324_01`: (`llm_provider_id`) → `llm_provider` (`llm_provider_id`) · relatie LLM ACCOUNT is provided by LLM PROVIDER (`llm-account-is-provided-by-llm-provider`)

**Illustratieve voorbeeldrijen (1):**

| llm_account_id | account_code | account_name | description | api_key_ciphertext | created_at | api_key_rotated_at | entoli_context_id | llm_provider_id |
|---|---|---|---|---|---|---|---|---|
| 1 | entoli-dev-anthropic | Development account | NULL | \x8f3a… | 2026-09-01 08:00:00+00 | NULL | 1 | 1 |

*Opmerking:* `api_key_ciphertext` bevat versleutelde bytes; de waarde is een placeholder, nooit een echte sleutel.

### `llm_model`

**Eén rij:** Eén model dat een LLM Provider aanbiedt.  
**Tabelcode:** 323 · **LDM-bron:** entiteit **LLM MODEL** (`llm-model`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `llm_model_id` | integer | ja | PK |
| `model_code` | text | ja |  |
| `context_window_size` | integer | nee |  |
| `description` | text | nee |  |
| `llm_provider_id` | integer | ja | FK |

**Primaire sleutel:** `PK_323` (`llm_model_id`)

**Uniciteitsconstraints:**

- `UC_323_01` (`model_code`)

**Foreign keys:**

- `FK_323_324_01`: (`llm_provider_id`) → `llm_provider` (`llm_provider_id`) · relatie LLM PROVIDER provides LLM MODEL (`llm-provider-provides-llm-model`)

**Illustratieve voorbeeldrijen (2):**

| llm_model_id | model_code | context_window_size | description | llm_provider_id |
|---|---|---|---|---|
| 1 | claude-opus-5-5 | NULL | NULL | 1 |
| 2 | claude-sonnet-5 | 200000 | Faster model for extraction work. | 1 |

*Opmerking:* `context_window_size` is een illustratieve waarde, geen gedocumenteerde eigenschap van het model.

### `llm_provider`

**Eén rij:** Eén aanbieder van LLM-modellen.  
**Tabelcode:** 324 · **LDM-bron:** entiteit **LLM PROVIDER** (`llm-provider`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `llm_provider_id` | integer | ja | PK |
| `provider_code` | text | ja |  |
| `name` | text | ja |  |
| `status` | text | nee |  |

**Primaire sleutel:** `PK_324` (`llm_provider_id`)

**Uniciteitsconstraints:**

- `UC_324_01` (`provider_code`)

**Illustratieve voorbeeldrijen (1):**

| llm_provider_id | provider_code | name | status |
|---|---|---|---|
| 1 | anthropic | Anthropic | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

### `llm_provider_thinking_effort`

**Eén rij:** De waarde die één LLM Provider verwacht voor één positie van Thinking Effort.  
**Tabelcode:** 328 · **LDM-bron:** entiteit **PROVIDER THINKING EFFORT** (`provider-thinking-effort`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `llm_provider_thinking_effort_id` | integer | ja | PK |
| `provider_value` | text | ja |  |
| `llm_provider_id` | integer | ja | FK |
| `ref_thinking_effort_id` | integer | ja | FK |

**Primaire sleutel:** `PK_328` (`llm_provider_thinking_effort_id`)

**Uniciteitsconstraints:**

- `UC_328_01` (`llm_provider_id`, `ref_thinking_effort_id`)

**Foreign keys:**

- `FK_328_324_01`: (`llm_provider_id`) → `llm_provider` (`llm_provider_id`) · relatie PROVIDER THINKING EFFORT concerns LLM PROVIDER (`provider-thinking-effort-concerns-llm-provider`)
- `FK_328_301_01`: (`ref_thinking_effort_id`) → `ref_thinking_effort` (`ref_thinking_effort_id`) · relatie PROVIDER THINKING EFFORT concerns THINKING EFFORT (REF) (`provider-thinking-effort-concerns-thinking-effort`)

**Illustratieve voorbeeldrijen (3):**

| llm_provider_thinking_effort_id | provider_value | llm_provider_id | ref_thinking_effort_id |
|---|---|---|---|
| 1 | low | 1 | 1 |
| 2 | medium | 1 | 2 |
| 3 | high | 1 | 3 |

*Opmerking:* De providerwaarden zijn fictief.

### `model_assignment`

**Eén rij:** Eén gepubliceerde keuze van een LLM-model en de bijbehorende generatie-instellingen die één Execution Profile realiseert.  
**Tabelcode:** 325 · **LDM-bron:** entiteit **MODEL ASSIGNMENT** (`model-assignment`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `model_assignment_id` | integer | ja | PK |
| `assignment_code` | text | ja |  |
| `temperature` | numeric | nee |  |
| `top_p` | numeric | nee |  |
| `maximum_output_tokens` | integer | nee |  |
| `publication_timestamp` | timestamptz | nee |  |
| `execution_profile_code` | text | ja | logical reference |
| `llm_model_id` | integer | ja | FK |
| `ref_thinking_effort_id` | integer | nee | FK |

**Primaire sleutel:** `PK_325` (`model_assignment_id`)

**Uniciteitsconstraints:**

- `UC_325_01` (`assignment_code`)

**Foreign keys:**

- `FK_325_323_01`: (`llm_model_id`) → `llm_model` (`llm_model_id`) · relatie LLM MODEL is selected by MODEL ASSIGNMENT (`llm-model-is-selected-by-model-assignment`)
- `FK_325_301_01`: (`ref_thinking_effort_id`) → `ref_thinking_effort` (`ref_thinking_effort_id`) · relatie MODEL ASSIGNMENT declares THINKING EFFORT (REF) (`model-assignment-declares-thinking-effort`)

**Logische verwijzingen (geen databaseconstraint):**

- `execution_profile_code` → `execution_profile`.`execution_profile_code` in semantic-foundation · relatie MODEL ASSIGNMENT realises EXECUTION PROFILE (`model-assignment-realises-execution-profile`)

**Illustratieve voorbeeldrijen (2):**

| model_assignment_id | assignment_code | temperature | top_p | maximum_output_tokens | publication_timestamp | execution_profile_code | llm_model_id | ref_thinking_effort_id |
|---|---|---|---|---|---|---|---|---|
| 1 | ma-survey-sources | NULL | NULL | 8000 | 2026-09-10 12:00:00+00 | DPG-EXP-C2 | 2 | NULL |
| 2 | ma-derive-ldm | 0.2 | NULL | 16000 | 2026-09-10 12:00:00+00 | DPG-SPE-C2 | 1 | 3 |

### `ref_thinking_effort`

**Eén rij:** Eén positie van Thinking Effort: hoeveel redeneerinspanning van het model wordt gevraagd.  
**Tabelcode:** 301 · **LDM-bron:** entiteit **THINKING EFFORT (REF)** (`thinking-effort`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_thinking_effort_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_301` (`ref_thinking_effort_id`)

**Uniciteitsconstraints:**

- `UC_301_01` (`code`)

**Illustratieve voorbeeldrijen (3):**

| ref_thinking_effort_id | code | description |
|---|---|---|
| 1 | standard | The standard effort; no increased effort is requested. |
| 2 | medium | More effort than standard, without asking for the maximum. |
| 3 | high | The highest effort the model and its provider allow. |

*Opmerking:* De omschrijvingen zijn ingekorte Engelse weergaven van de Nederlandse LDM-posities.

### `step_model_selection`

**Eén rij:** De Model Assignment die één Entoli Context kiest voor één Orchestration Step.  
**Tabelcode:** 330 · **LDM-bron:** entiteit **STEP MODEL SELECTION** (`step-model-selection`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `step_model_selection_id` | integer | ja | PK |
| `orchestration_step_code` | text | ja | logical reference |
| `entoli_context_id` | integer | ja | FK |
| `model_assignment_id` | integer | ja | FK |

**Primaire sleutel:** `PK_330` (`step_model_selection_id`)

**Uniciteitsconstraints:**

- `UC_330_01` (`entoli_context_id`, `orchestration_step_code`)

**Foreign keys:**

- `FK_330_320_01`: (`entoli_context_id`) → `entoli_context` (`entoli_context_id`) · relatie STEP MODEL SELECTION is made in ENTOLI CONTEXT (`step-model-selection-is-made-in-entoli-context`)
- `FK_330_325_01`: (`model_assignment_id`) → `model_assignment` (`model_assignment_id`) · relatie STEP MODEL SELECTION selects MODEL ASSIGNMENT (`step-model-selection-selects-model-assignment`)

**Logische verwijzingen (geen databaseconstraint):**

- `orchestration_step_code` → `orchestration_step`.`orchestration_step_code` in orchestration-definition · relatie STEP MODEL SELECTION concerns ORCHESTRATION STEP (`step-model-selection-concerns-orchestration-step`)

**Illustratieve voorbeeldrijen (2):**

| step_model_selection_id | orchestration_step_code | entoli_context_id | model_assignment_id |
|---|---|---|---|
| 1 | survey-sources | 1 | 1 |
| 2 | derive-ldm | 1 | 2 |

## work-execution

Technical Data Model `entoli-agent-development-work-execution-postgresql` versie 4.0.0, afgeleid van Logical Data Model `entoli-agent-development-work-execution` versie 4.0.0.

### `artifact`

**Eén rij:** Eén artefact dat een Execution heeft voortgebracht, geclassificeerd door een Artifact Type.  
**Tabelcode:** 420 · **LDM-bron:** entiteit **ARTIFACT** (`artifact`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `artifact_id` | integer | ja | PK |
| `artifact_code` | text | ja |  |
| `origin_code` | text | nee |  |
| `status` | text | ja |  |
| `artifact_content` | text | nee |  |
| `artifact_type_code` | text | ja | logical reference |
| `execution_id` | integer | ja | FK |

**Primaire sleutel:** `PK_420` (`artifact_id`)

**Uniciteitsconstraints:**

- `UC_420_01` (`artifact_code`)

**Foreign keys:**

- `FK_420_421_01`: (`execution_id`) → `execution` (`execution_id`) · relatie EXECUTION produces ARTIFACT (`execution-produces-artifact`)

**Logische verwijzingen (geen databaseconstraint):**

- `artifact_type_code` → `artifact_type`.`code` in semantic-foundation · relatie ARTIFACT TYPE classifies ARTIFACT (`artifact-type-classifies-artifact`)

**Illustratieve voorbeeldrijen (2):**

| artifact_id | artifact_code | origin_code | status | artifact_content | artifact_type_code | execution_id |
|---|---|---|---|---|---|---|
| 1 | art-2609.0001 | 2609.A1B2 | final | Survey of three cited sources … | source-survey | 1 |
| 2 | art-2609.0002 | 2609.C3D4 | draft | {"model": {"id": "ldm-agent-definition"}, …} | logical-data-model | 2 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `final` en `draft` zijn aangenomen waarden. Het formaat van de artefactcodes is fictief.

### `artifact_derivation`

**Eén rij:** Eén afleiding: het afgeleide artefact is gebaseerd op het bronartefact.  
**Tabelcode:** 428 · **LDM-bron:** relatie **ARTIFACT is based on ARTIFACT (`artifact-is-based-on-source-artifact`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `artifact_derivation_id` | integer | ja | PK |
| `derived_artifact_id` | integer | ja | FK |
| `source_artifact_id` | integer | ja | FK |

**Primaire sleutel:** `PK_428` (`artifact_derivation_id`)

**Uniciteitsconstraints:**

- `UC_428_01` (`derived_artifact_id`, `source_artifact_id`)

**Foreign keys:**

- `FK_428_420_01`: (`derived_artifact_id`) → `artifact` (`artifact_id`) · relatie ARTIFACT is based on ARTIFACT (`artifact-is-based-on-source-artifact`)
- `FK_428_420_02`: (`source_artifact_id`) → `artifact` (`artifact_id`) · relatie ARTIFACT is based on ARTIFACT (`artifact-is-based-on-source-artifact`)

**Check-constraints:**

- `CK_428_01`: `derived_artifact_id <> source_artifact_id`

**Illustratieve voorbeeldrijen (1):**

| artifact_derivation_id | derived_artifact_id | source_artifact_id |
|---|---|---|
| 1 | 2 | 1 |

### `execution`

**Eén rij:** Eén uitvoering van een orchestration step definition door een LLM, geïnstrueerd door precies één Instruction Set.  
**Tabelcode:** 421 · **LDM-bron:** entiteit **EXECUTION** (`execution`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `execution_id` | integer | ja | PK |
| `execution_code` | text | ja |  |
| `start_timestamp` | timestamptz | ja |  |
| `status` | text | ja |  |
| `model_assignment_code` | text | ja | logical reference |
| `orchestration_step_definition_code` | uuid | ja | logical reference |
| `entoli_context_code` | text | ja | logical reference |
| `orchestration_specification_version_code` | uuid | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |
| `handoff_id` | integer | nee | FK |
| `ref_termination_reason_id` | integer | nee | FK |

**Primaire sleutel:** `PK_421` (`execution_id`)

**Uniciteitsconstraints:**

- `UC_421_01` (`execution_code`)

**Foreign keys:**

- `FK_421_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie EXECUTION is instructed by INSTRUCTION SET (`execution-is-instructed-by-instruction-set`)
- `FK_421_422_01`: (`handoff_id`) → `handoff` (`handoff_id`) · relatie EXECUTION produces HANDOFF (`execution-produces-handoff`)
- `FK_421_402_01`: (`ref_termination_reason_id`) → `ref_termination_reason` (`ref_termination_reason_id`) · relatie EXECUTION has TERMINATION REASON (REF) (`execution-has-termination-reason`)

**Logische verwijzingen (geen databaseconstraint):**

- `model_assignment_code` → `model_assignment`.`assignment_code` in execution-configuration · relatie EXECUTION uses MODEL ASSIGNMENT (`execution-uses-model-assignment`)
- `orchestration_step_definition_code` → `orchestration_step_definition`.`orchestration_step_definition_code` in orchestration-definition · relatie ORCHESTRATION STEP DEFINITION is executed as EXECUTION (`orchestration-step-definition-is-executed-as-execution`)
- `entoli_context_code` → `entoli_context`.`entoli_context_code` in execution-configuration · relatie EXECUTION is performed in ENTOLI CONTEXT (`execution-is-performed-in-entoli-context`)
- `orchestration_specification_version_code` → `orchestration_specification_version`.`orchestration_specification_version_code` in orchestration-definition · relatie EXECUTION follows ORCHESTRATION SPECIFICATION VERSION (`execution-follows-orchestration-specification-version`)

**Illustratieve voorbeeldrijen (2):**

| execution_id | execution_code | start_timestamp | status | model_assignment_code | orchestration_step_definition_code | entoli_context_code | orchestration_specification_version_code | instruction_set_id | handoff_id | ref_termination_reason_id |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | exec-2609.A1B2 | 2026-09-25 09:01:00+00 | completed | ma-survey-sources | 8a3f1c22-7b44-4e0d-a9c1-6e2b5f7d9c10 | entoli-dev | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 1 | 1 | NULL |
| 2 | exec-2609.C3D4 | 2026-09-25 09:15:00+00 | terminated | ma-derive-ldm | c41e9b07-3d5a-4f82-b6e3-0a9d8c7b6e21 | entoli-dev | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 2 | NULL | 1 |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `completed` en `terminated` zijn aangenomen waarden.

### `handoff`

**Eén rij:** Eén handoff die een Execution voortbrengt en die in een latere Instruction Set wordt opgenomen, mogelijk met een verzoek om menselijke tussenkomst.  
**Tabelcode:** 422 · **LDM-bron:** entiteit **HANDOFF** (`handoff`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `handoff_id` | integer | ja | PK |
| `handoff_code` | text | ja |  |
| `human_intervention` | boolean | ja |  |
| `timestamp` | timestamptz | ja |  |
| `content_message` | text | nee |  |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_422` (`handoff_id`)

**Uniciteitsconstraints:**

- `UC_422_01` (`handoff_code`)

**Foreign keys:**

- `FK_422_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie HANDOFF is included in INSTRUCTION SET (`handoff-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (1):**

| handoff_id | handoff_code | human_intervention | timestamp | content_message | instruction_set_id |
|---|---|---|---|---|---|
| 1 | hf-2609.0001 | false | 2026-09-25 09:12:00+00 | Source survey complete; three sources cited. | 2 |

*Opmerking:* De handoff die execution 1 voortbrengt, is opgenomen in Instruction Set 2, die de volgende stap instrueert.

### `human_context`

**Eén rij:** Eén definitie van de invoer die een mens levert, opgebouwd uit Human Context Parameters.  
**Tabelcode:** 423 · **LDM-bron:** entiteit **HUMAN CONTEXT** (`human-context`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `human_context_id` | integer | ja | PK |
| `human_context_code` | text | ja |  |
| `name` | text | ja |  |
| `description` | text | nee |  |
| `status` | text | ja |  |

**Primaire sleutel:** `PK_423` (`human_context_id`)

**Uniciteitsconstraints:**

- `UC_423_01` (`human_context_code`)

**Illustratieve voorbeeldrijen (1):**

| human_context_id | human_context_code | name | description | status |
|---|---|---|---|---|
| 1 | hc-modelling-request | Modelling request | NULL | active |

*Opmerking:* `status` heeft in de bronnen geen codelijst; `active` is een aangenomen waarde.

### `human_context_parameter`

**Eén rij:** Eén veld van een Human Context, met label, datatype en weergavevolgorde.  
**Tabelcode:** 429 · **LDM-bron:** entiteit **HUMAN CONTEXT PARAMETER** (`human-context-parameter`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `human_context_parameter_id` | integer | ja | PK |
| `parameter_code` | text | ja |  |
| `label` | text | ja |  |
| `description` | text | nee |  |
| `data_type` | text | ja |  |
| `required` | boolean | ja |  |
| `display_order` | integer | ja |  |
| `human_context_id` | integer | ja | FK |

**Primaire sleutel:** `PK_429` (`human_context_parameter_id`)

**Uniciteitsconstraints:**

- `UC_429_01` (`human_context_id`, `parameter_code`)
- `UC_429_02` (`human_context_id`, `display_order`)

**Foreign keys:**

- `FK_429_423_01`: (`human_context_id`) → `human_context` (`human_context_id`) · relatie HUMAN CONTEXT PARAMETER belongs to HUMAN CONTEXT (`human-context-parameter-belongs-to-human-context`)

**Illustratieve voorbeeldrijen (2):**

| human_context_parameter_id | parameter_code | label | description | data_type | required | display_order | human_context_id |
|---|---|---|---|---|---|---|---|
| 1 | subject-area | Subject area | NULL | text | true | 1 | 1 |
| 2 | target-release | Target release | Release the model is meant for. | date | false | 2 | 1 |

*Opmerking:* `data_type` heeft in de bronnen geen codelijst; `text` en `date` zijn aangenomen waarden.

### `instruction_set`

**Eén rij:** Eén samengestelde set instructies voor één Execution, aangestuurd door één Agent Intent.  
**Tabelcode:** 424 · **LDM-bron:** entiteit **INSTRUCTION SET** (`instruction-set`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_id` | integer | ja | PK |
| `instruction_set_code` | uuid | ja |  |
| `content` | text | nee |  |
| `created_at` | timestamptz (default `CURRENT_TIMESTAMP`) | ja |  |
| `agent_intent_code` | text | ja | logical reference |

**Primaire sleutel:** `PK_424` (`instruction_set_id`)

**Uniciteitsconstraints:**

- `UC_424_01` (`instruction_set_code`)

**Logische verwijzingen (geen databaseconstraint):**

- `agent_intent_code` → `agent_intent`.`agent_intent_code` in agent-definition · relatie AGENT INTENT drives assembly of INSTRUCTION SET (`agent-intent-drives-assembly-of-instruction-set`)

**Illustratieve voorbeeldrijen (2):**

| instruction_set_id | instruction_set_code | content | created_at | agent_intent_code |
|---|---|---|---|---|
| 1 | 0b6e4d2a-1f3c-4e5b-9a7d-8c2f6e4a1d01 | ## Instructions ↵ 1. List every external source … | 2026-09-25 09:00:00+00 | niam-analyst.survey-sources |
| 2 | 7e9a1c3b-5d2f-4a6e-8b0c-9d1e3f5a7c02 | ## Instructions ↵ 1. Read the conceptual model … | 2026-09-25 09:14:00+00 | ldm-modeller.derive-ldm |

### `instruction_set_artifact`

**Eén rij:** Eén Artifact waarop een Instruction Set betrekking heeft, in één rol (werkbron of uitvoer).  
**Tabelcode:** 426 · **LDM-bron:** entiteit **INSTRUCTION SET ARTIFACT** (`instruction-set-artifact`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_artifact_id` | integer | ja | PK |
| `artifact_id` | integer | ja | FK |
| `instruction_set_id` | integer | ja | FK |
| `ref_instruction_set_artifact_role_id` | integer | ja | FK |

**Primaire sleutel:** `PK_426` (`instruction_set_artifact_id`)

**Uniciteitsconstraints:**

- `UC_426_01` (`instruction_set_id`, `artifact_id`, `ref_instruction_set_artifact_role_id`)

**Foreign keys:**

- `FK_426_420_01`: (`artifact_id`) → `artifact` (`artifact_id`) · relatie INSTRUCTION SET ARTIFACT concerns ARTIFACT (`instruction-set-artifact-concerns-artifact`)
- `FK_426_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie INSTRUCTION SET ARTIFACT concerns INSTRUCTION SET (`instruction-set-artifact-concerns-instruction-set`)
- `FK_426_401_01`: (`ref_instruction_set_artifact_role_id`) → `ref_instruction_set_artifact_role` (`ref_instruction_set_artifact_role_id`) · relatie INSTRUCTION SET ARTIFACT has INSTRUCTION SET ARTIFACT ROLE (REF) (`instruction-set-artifact-has-role`)

**Illustratieve voorbeeldrijen (2):**

| instruction_set_artifact_id | artifact_id | instruction_set_id | ref_instruction_set_artifact_role_id |
|---|---|---|---|
| 1 | 1 | 2 | 1 |
| 2 | 2 | 2 | 2 |

### `instruction_set_element`

**Eén rij:** Eén Element dat in één Instruction Set is opgenomen.  
**Tabelcode:** 431 · **LDM-bron:** relatie **ELEMENT is included in INSTRUCTION SET (`element-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_element_id` | integer | ja | PK |
| `element_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_431` (`instruction_set_element_id`)

**Uniciteitsconstraints:**

- `UC_431_01` (`element_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_431_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie ELEMENT is included in INSTRUCTION SET (`element-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `element_code` → `element`.`element_code` in semantic-foundation · relatie ELEMENT is included in INSTRUCTION SET (`element-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (2):**

| instruction_set_element_id | element_code | instruction_set_id |
|---|---|---|
| 1 | agent | 2 |
| 2 | agent-intent | 2 |

### `instruction_set_entoli_agent_intent_rule`

**Eén rij:** Eén Entoli Agent Intent Rule die in één Instruction Set is opgenomen.  
**Tabelcode:** 436 · **LDM-bron:** relatie **ENTOLI AGENT INTENT RULE is included in INSTRUCTION SET (`entoli-agent-intent-rule-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_entoli_agent_intent_rule_id` | integer | ja | PK |
| `entoli_agent_intent_rule_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_436` (`instruction_set_entoli_agent_intent_rule_id`)

**Uniciteitsconstraints:**

- `UC_436_01` (`entoli_agent_intent_rule_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_436_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie ENTOLI AGENT INTENT RULE is included in INSTRUCTION SET (`entoli-agent-intent-rule-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `entoli_agent_intent_rule_code` → `entoli_agent_intent_rule`.`rule_code` in agent-definition · relatie ENTOLI AGENT INTENT RULE is included in INSTRUCTION SET (`entoli-agent-intent-rule-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (1):**

| instruction_set_entoli_agent_intent_rule_id | entoli_agent_intent_rule_code | instruction_set_id |
|---|---|---|
| 1 | EAIR-LDM-001 | 2 |

### `instruction_set_intent_instruction`

**Eén rij:** Eén Intent Instruction die in één Instruction Set is opgenomen.  
**Tabelcode:** 427 · **LDM-bron:** relatie **INTENT INSTRUCTION is included in INSTRUCTION SET (`intent-instruction-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_intent_instruction_id` | integer | ja | PK |
| `intent_instruction_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_427` (`instruction_set_intent_instruction_id`)

**Uniciteitsconstraints:**

- `UC_427_01` (`intent_instruction_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_427_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie INTENT INSTRUCTION is included in INSTRUCTION SET (`intent-instruction-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `intent_instruction_code` → `intent_instruction`.`intent_instruction_code` in agent-definition · relatie INTENT INSTRUCTION is included in INSTRUCTION SET (`intent-instruction-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (3):**

| instruction_set_intent_instruction_id | intent_instruction_code | instruction_set_id |
|---|---|---|
| 1 | niam-analyst.survey-sources.01 | 1 |
| 2 | ldm-modeller.derive-ldm.01 | 2 |
| 3 | ldm-modeller.derive-ldm.02 | 2 |

### `instruction_set_parameter_value`

**Eén rij:** De waarde die voor één Human Context Parameter in één Instruction Set is geleverd.  
**Tabelcode:** 430 · **LDM-bron:** entiteit **INSTRUCTION SET PARAMETER VALUE** (`instruction-set-parameter-value`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_parameter_value_id` | integer | ja | PK |
| `parameter_value` | text | ja |  |
| `instruction_set_id` | integer | ja | FK |
| `human_context_parameter_id` | integer | ja | FK |

**Primaire sleutel:** `PK_430` (`instruction_set_parameter_value_id`)

**Uniciteitsconstraints:**

- `UC_430_01` (`instruction_set_id`, `human_context_parameter_id`)

**Foreign keys:**

- `FK_430_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie INSTRUCTION SET PARAMETER VALUE concerns INSTRUCTION SET (`instruction-set-parameter-value-concerns-instruction-set`)
- `FK_430_429_01`: (`human_context_parameter_id`) → `human_context_parameter` (`human_context_parameter_id`) · relatie INSTRUCTION SET PARAMETER VALUE concerns HUMAN CONTEXT PARAMETER (`instruction-set-parameter-value-concerns-human-context-parameter`)

**Illustratieve voorbeeldrijen (2):**

| instruction_set_parameter_value_id | parameter_value | instruction_set_id | human_context_parameter_id |
|---|---|---|---|
| 1 | Agent definition | 2 | 1 |
| 2 | 2026-10-01 | 2 | 2 |

### `instruction_set_regime_rule`

**Eén rij:** Eén Regime Rule die in één Instruction Set is opgenomen.  
**Tabelcode:** 435 · **LDM-bron:** relatie **REGIME RULE is included in INSTRUCTION SET (`regime-rule-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_regime_rule_id` | integer | ja | PK |
| `regime_rule_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_435` (`instruction_set_regime_rule_id`)

**Uniciteitsconstraints:**

- `UC_435_01` (`regime_rule_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_435_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie REGIME RULE is included in INSTRUCTION SET (`regime-rule-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `regime_rule_code` → `regime_rule`.`rule_code` in semantic-foundation · relatie REGIME RULE is included in INSTRUCTION SET (`regime-rule-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (3):**

| instruction_set_regime_rule_id | regime_rule_code | instruction_set_id |
|---|---|---|
| 1 | SR-CNB-001 | 2 |
| 2 | SY-REL-001 | 2 |
| 3 | TM-STR-001 | 2 |

*Opmerking:* Dit zijn de Regime Rules voor de posities CNB, REL en STR die de Agent Intent `ldm-modeller.derive-ldm` declareert.

### `instruction_set_relationship`

**Eén rij:** Eén Relationship die in één Instruction Set is opgenomen.  
**Tabelcode:** 432 · **LDM-bron:** relatie **RELATIONSHIP is included in INSTRUCTION SET (`relationship-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_relationship_id` | integer | ja | PK |
| `relationship_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_432` (`instruction_set_relationship_id`)

**Uniciteitsconstraints:**

- `UC_432_01` (`relationship_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_432_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie RELATIONSHIP is included in INSTRUCTION SET (`relationship-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `relationship_code` → `relationship`.`relationship_code` in semantic-foundation · relatie RELATIONSHIP is included in INSTRUCTION SET (`relationship-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (1):**

| instruction_set_relationship_id | relationship_code | instruction_set_id |
|---|---|---|
| 1 | agent-exposes-agent-intent | 2 |

### `instruction_set_universal_rule`

**Eén rij:** Eén Universal Rule die in één Instruction Set is opgenomen.  
**Tabelcode:** 434 · **LDM-bron:** relatie **UNIVERSAL RULE is included in INSTRUCTION SET (`universal-rule-is-included-in-instruction-set`)**, gerealiseerd als koppeltabel

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `instruction_set_universal_rule_id` | integer | ja | PK |
| `universal_rule_code` | text | ja | logical reference |
| `instruction_set_id` | integer | ja | FK |

**Primaire sleutel:** `PK_434` (`instruction_set_universal_rule_id`)

**Uniciteitsconstraints:**

- `UC_434_01` (`universal_rule_code`, `instruction_set_id`)

**Foreign keys:**

- `FK_434_424_01`: (`instruction_set_id`) → `instruction_set` (`instruction_set_id`) · relatie UNIVERSAL RULE is included in INSTRUCTION SET (`universal-rule-is-included-in-instruction-set`)

**Logische verwijzingen (geen databaseconstraint):**

- `universal_rule_code` → `universal_rule`.`rule_code` in semantic-foundation · relatie UNIVERSAL RULE is included in INSTRUCTION SET (`universal-rule-is-included-in-instruction-set`)

**Illustratieve voorbeeldrijen (4):**

| instruction_set_universal_rule_id | universal_rule_code | instruction_set_id |
|---|---|---|
| 1 | UNI-001 | 1 |
| 2 | UNI-001 | 2 |
| 3 | UNI-002 | 2 |
| 4 | UNI-003 | 2 |

*Opmerking:* Elke Instruction Set bevat elke actieve Universal Rule. De rijen tonen maar een deel van die opnames.

### `ref_instruction_set_artifact_role`

**Eén rij:** Eén rol die een Artifact voor een Instruction Set kan spelen: werkbron of uitvoer.  
**Tabelcode:** 401 · **LDM-bron:** entiteit **INSTRUCTION SET ARTIFACT ROLE (REF)** (`instruction-set-artifact-role`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_instruction_set_artifact_role_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_401` (`ref_instruction_set_artifact_role_id`)

**Uniciteitsconstraints:**

- `UC_401_01` (`code`)

**Illustratieve voorbeeldrijen (2):**

| ref_instruction_set_artifact_role_id | code | description |
|---|---|---|
| 1 | working-source | The Instruction Set uses the Artifact as a working source. |
| 2 | output | The Artifact was produced by the Execution this Instruction Set instructs. |

*Opmerking:* De omschrijvingen zijn ingekorte Engelse weergaven van de Nederlandse LDM-posities.

### `ref_termination_reason`

**Eén rij:** Eén reden waarom een Execution voortijdig is beëindigd.  
**Tabelcode:** 402 · **LDM-bron:** entiteit **TERMINATION REASON (REF)** (`termination-reason`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `ref_termination_reason_id` | integer | ja | PK |
| `code` | text | ja |  |
| `description` | text | ja |  |

**Primaire sleutel:** `PK_402` (`ref_termination_reason_id`)

**Uniciteitsconstraints:**

- `UC_402_01` (`code`)

**Illustratieve voorbeeldrijen (2):**

| ref_termination_reason_id | code | description |
|---|---|---|
| 1 | blocked | The affected work was recorded as blocked. |
| 2 | failed | The Execution failed before it produced its output. |

*Opmerking:* Het LDM legt de posities van Termination Reason nog niet vast; beide codes zijn fictief.

## orchestration-definition

Technical Data Model `entoli-agent-development-orchestration-definition-postgresql` versie 4.0.0, afgeleid van Logical Data Model `entoli-agent-development-orchestration-definition` versie 4.0.0.

### `orchestration_specification`

**Eén rij:** Eén orchestration specification: een benoemde, herbruikbare stroom van stappen met een inhoudelijk doel.  
**Tabelcode:** 522 · **LDM-bron:** entiteit **ORCHESTRATION SPECIFICATION** (`orchestration-specification`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_specification_id` | integer | ja | PK |
| `specification_code` | text | ja |  |
| `specification_name` | text | ja |  |
| `content_goal` | text | nee |  |

**Primaire sleutel:** `PK_522` (`orchestration_specification_id`)

**Uniciteitsconstraints:**

- `UC_522_01` (`specification_code`)

**Illustratieve voorbeeldrijen (1):**

| orchestration_specification_id | specification_code | specification_name | content_goal |
|---|---|---|---|
| 1 | model-derivation | Model derivation | Derive a logical data model from surveyed sources. |

### `orchestration_specification_version`

**Eén rij:** Eén genummerde versie van een Orchestration Specification.  
**Tabelcode:** 524 · **LDM-bron:** entiteit **ORCHESTRATION SPECIFICATION VERSION** (`orchestration-specification-version`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_specification_version_id` | integer | ja | PK |
| `orchestration_specification_version_code` | uuid | ja |  |
| `version_number` | integer | ja |  |
| `publication_timestamp` | timestamptz | nee |  |
| `orchestration_specification_id` | integer | ja | FK |

**Primaire sleutel:** `PK_524` (`orchestration_specification_version_id`)

**Uniciteitsconstraints:**

- `UC_524_01` (`orchestration_specification_version_code`)
- `UC_524_02` (`orchestration_specification_id`, `version_number`)
- `UC_524_03` (`orchestration_specification_id`, `orchestration_specification_version_id`)

**Foreign keys:**

- `FK_524_522_01`: (`orchestration_specification_id`) → `orchestration_specification` (`orchestration_specification_id`) · relatie ORCHESTRATION SPECIFICATION VERSION belongs to ORCHESTRATION SPECIFICATION (`orchestration-specification-version-belongs-to-orchestration-specification`)

**Illustratieve voorbeeldrijen (1):**

| orchestration_specification_version_id | orchestration_specification_version_code | version_number | publication_timestamp | orchestration_specification_id |
|---|---|---|---|---|
| 1 | 5d0c8f5e-2a61-4c1e-9f0a-1b7e3c2d4a01 | 1 | 2026-09-10 12:00:00+00 | 1 |

### `orchestration_step`

**Eén rij:** Eén stap van een Orchestration Specification, los van zijn geversioneerde definitie.  
**Tabelcode:** 520 · **LDM-bron:** entiteit **ORCHESTRATION STEP** (`orchestration-step`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_step_id` | integer | ja | PK |
| `orchestration_step_code` | text | ja |  |
| `orchestration_specification_id` | integer | ja | FK |

**Primaire sleutel:** `PK_520` (`orchestration_step_id`)

**Uniciteitsconstraints:**

- `UC_520_01` (`orchestration_step_code`)
- `UC_520_02` (`orchestration_specification_id`, `orchestration_step_id`)

**Foreign keys:**

- `FK_520_522_01`: (`orchestration_specification_id`) → `orchestration_specification` (`orchestration_specification_id`) · relatie ORCHESTRATION STEP is part of ORCHESTRATION SPECIFICATION (`orchestration-step-is-part-of-orchestration-specification`)

**Illustratieve voorbeeldrijen (2):**

| orchestration_step_id | orchestration_step_code | orchestration_specification_id |
|---|---|---|
| 1 | survey-sources | 1 |
| 2 | derive-ldm | 1 |

### `orchestration_step_definition`

**Eén rij:** Eén genummerde versie van de definitie van een Orchestration Step, met de Agent Intent die de stap aanroept.  
**Tabelcode:** 521 · **LDM-bron:** entiteit **ORCHESTRATION STEP DEFINITION** (`orchestration-step-definition`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_step_definition_id` | integer | ja | PK |
| `orchestration_step_definition_code` | uuid | ja |  |
| `version_number` | integer | ja |  |
| `publication_timestamp` | timestamptz | nee |  |
| `step_name` | text | ja |  |
| `content_description` | text | nee |  |
| `agent_intent_code` | text | ja | logical reference |
| `orchestration_step_id` | integer | ja | FK |

**Primaire sleutel:** `PK_521` (`orchestration_step_definition_id`)

**Uniciteitsconstraints:**

- `UC_521_01` (`orchestration_step_definition_code`)
- `UC_521_02` (`orchestration_step_id`, `version_number`)
- `UC_521_03` (`orchestration_step_id`, `orchestration_step_definition_id`)

**Foreign keys:**

- `FK_521_520_01`: (`orchestration_step_id`) → `orchestration_step` (`orchestration_step_id`) · relatie ORCHESTRATION STEP DEFINITION belongs to ORCHESTRATION STEP (`orchestration-step-definition-belongs-to-orchestration-step`)

**Logische verwijzingen (geen databaseconstraint):**

- `agent_intent_code` → `agent_intent`.`agent_intent_code` in agent-definition · relatie AGENT INTENT is invoked by ORCHESTRATION STEP DEFINITION (`agent-intent-is-invoked-by-orchestration-step-definition`)

**Illustratieve voorbeeldrijen (3):**

| orchestration_step_definition_id | orchestration_step_definition_code | version_number | publication_timestamp | step_name | content_description | agent_intent_code | orchestration_step_id |
|---|---|---|---|---|---|---|---|
| 1 | 8a3f1c22-7b44-4e0d-a9c1-6e2b5f7d9c10 | 1 | 2026-09-10 12:00:00+00 | Survey sources | NULL | niam-analyst.survey-sources | 1 |
| 2 | c41e9b07-3d5a-4f82-b6e3-0a9d8c7b6e21 | 1 | 2026-09-10 12:00:00+00 | Derive LDM | Derive entities and relationships … | ldm-modeller.derive-ldm | 2 |
| 3 | f2d7a6b3-9e1c-4a05-8b4d-3c6e2f1a0b32 | 2 | NULL | Derive LDM | Draft: also derive constraints … | ldm-modeller.derive-ldm | 2 |

*Opmerking:* Versie 2 van de definitie `derive-ldm` is nog niet gepubliceerd (`publication_timestamp` is NULL).

### `orchestration_step_precedence`

**Eén rij:** Eén volgordebeperking in een specificatieversie: de voorgaande stap loopt vóór de volgende stap.  
**Tabelcode:** 523 · **LDM-bron:** entiteit **ORCHESTRATION STEP PRECEDENCE** (`orchestration-step-precedence`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_step_precedence_id` | integer | ja | PK |
| `orchestration_specification_version_id` | integer | ja | FK |
| `preceding_step_id` | integer | ja | FK |
| `following_step_id` | integer | ja | FK |

**Primaire sleutel:** `PK_523` (`orchestration_step_precedence_id`)

**Uniciteitsconstraints:**

- `UC_523_01` (`orchestration_specification_version_id`, `preceding_step_id`, `following_step_id`)

**Foreign keys:**

- `FK_523_524_01`: (`orchestration_specification_version_id`) → `orchestration_specification_version` (`orchestration_specification_version_id`) · relatie ORCHESTRATION STEP PRECEDENCE belongs to ORCHESTRATION SPECIFICATION VERSION (`orchestration-step-precedence-belongs-to-orchestration-specification-version`)
- `FK_523_525_02`: (`orchestration_specification_version_id`, `preceding_step_id`) → `orchestration_version_step` (`orchestration_specification_version_id`, `orchestration_step_id`) · relatie ORCHESTRATION STEP PRECEDENCE has preceding ORCHESTRATION STEP (`orchestration-step-precedence-has-preceding-orchestration-step`)
- `FK_523_525_01`: (`orchestration_specification_version_id`, `following_step_id`) → `orchestration_version_step` (`orchestration_specification_version_id`, `orchestration_step_id`) · relatie ORCHESTRATION STEP PRECEDENCE has following ORCHESTRATION STEP (`orchestration-step-precedence-has-following-orchestration-step`)

**Check-constraints:**

- `CK_523_01`: `preceding_step_id <> following_step_id`

**Illustratieve voorbeeldrijen (1):**

| orchestration_step_precedence_id | orchestration_specification_version_id | preceding_step_id | following_step_id |
|---|---|---|---|
| 1 | 1 | 1 | 2 |

### `orchestration_version_step`

**Eén rij:** Eén stap die in één specificatieversie is opgenomen, met de stapdefinitie die die versie gebruikt.  
**Tabelcode:** 525 · **LDM-bron:** entiteit **ORCHESTRATION VERSION STEP** (`orchestration-version-step`)

| Kolom | PostgreSQL-type | Verplicht | Sleutel |
|---|---|---|---|
| `orchestration_version_step_id` | integer | ja | PK |
| `orchestration_specification_version_id` | integer | ja | FK |
| `orchestration_step_id` | integer | ja | FK |
| `orchestration_step_definition_id` | integer | ja | FK |
| `orchestration_specification_id` | integer | ja | FK |

**Primaire sleutel:** `PK_525` (`orchestration_version_step_id`)

**Uniciteitsconstraints:**

- `UC_525_01` (`orchestration_specification_version_id`, `orchestration_step_id`)

**Foreign keys:**

- `FK_525_524_01`: (`orchestration_specification_id`, `orchestration_specification_version_id`) → `orchestration_specification_version` (`orchestration_specification_id`, `orchestration_specification_version_id`) · relatie ORCHESTRATION VERSION STEP belongs to ORCHESTRATION SPECIFICATION VERSION (`orchestration-version-step-belongs-to-orchestration-specification-version`)
- `FK_525_520_01`: (`orchestration_specification_id`, `orchestration_step_id`) → `orchestration_step` (`orchestration_specification_id`, `orchestration_step_id`) · relatie ORCHESTRATION VERSION STEP concerns ORCHESTRATION STEP (`orchestration-version-step-concerns-orchestration-step`)
- `FK_525_521_01`: (`orchestration_step_id`, `orchestration_step_definition_id`) → `orchestration_step_definition` (`orchestration_step_id`, `orchestration_step_definition_id`) · relatie ORCHESTRATION VERSION STEP uses ORCHESTRATION STEP DEFINITION (`orchestration-version-step-uses-orchestration-step-definition`)

**Illustratieve voorbeeldrijen (2):**

| orchestration_version_step_id | orchestration_specification_version_id | orchestration_step_id | orchestration_step_definition_id | orchestration_specification_id |
|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 1 |
