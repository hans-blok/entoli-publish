---
type: concepts
name: Data Modelling — concepts
version: 0.4.0
date: 2026-09-15
knowledge-domain: Data Modelling
digest: tbd0
status: concept
---
# Data Modelling — concepts

---

## Provenance

**Compiled by**: Hans Blok (v0.1.0–v0.2.0). **Recalibrated** by Claude Opus 5 against `concepts-logical-data-model.md` v1.0.0, on explicit user instruction (2026-09-15).

**Purpose**: The single register of the Data Modelling knowledge domain, and the one entry point an agent needs. It covers two things that were previously held apart:

1. the **meta-model** — Information Model, Logical Data Model, Technical Data Model, how each derives from the one above it, and the traceability chain that grounds Level 1 in an authority text;
2. **what a Logical Data Model is built from** — Entity, Attribute, Reference entity, the Attribute classification and Data type axes, and the structural additions Time and Status.

Each concept is described as an Element with a definition, characteristics, relationships and delimitation.

**Merged (v0.4.0)**: `concepts-logical-data-model.md` v1.0.0 has been merged into this file and deleted, on explicit user instruction, so that agents have one register to read instead of two. All seven of its concepts moved across; the five that had no counterpart here — Reference entity, Attribute classification, Data type, Time and Status — moved verbatim, and `ENTITY` and `ATTRIBUTE` regained the full logical definition, merged with the derivation-chain facts this register already carried. Nothing was dropped in the merge.

**Sources consulted for this recalibration**:
- `canons/data-modelling-canon/elements/concepts-logical-data-model.md` v1.0.0 (`status: concept`) — merged into this file at v0.4.0 and deleted; its Provenance and Changelog are preserved in this file's Changelog
- `canons/data-modelling-canon/reference/doctrines/doctrine.logical-data-modelling.md` v1.0.2 (`status: current`) — the attribute classification axis (§5) and the layer separation (§2.2)
- `canons/data-modelling-canon/reference/doctrines/doctrine-niam-analysis.md` (`Status: Normative`, no frontmatter) — the grounding chain and the fact-based derivation layer

**The two overlaps the merged register had recorded are resolved**, in its favour in both cases:

1. **Entity and Attribute.** Both registers defined them. The logical-layer definition — logical identity, optionality, data type, the reference-entity specialisation — was the fuller one and grounded in a `status: current` doctrine, so it is the definition that survives. It is merged below with this register's own contribution: each concept's place in the derivation chain between the three levels.
2. **Attribute classification positions.** This register named them semantic / **time** / process / system; the doctrine names them semantic / **temporal** / process / system. Corrected to `temporal` throughout. The doctrine is `status: current` and settles it.

**Two findings, recorded and not resolved here** — both are matters for Agent `canon-curator`:

1. **The source artifact is gone.** This register was compiled from `features/01-datamodelling/ldm-datamodelling.md` v0.3.0, which no longer exists anywhere in the repository; only a GraphML rendering survives, at `docs/diagram/graphml/ldm-datamodelling.graphml`. The content below can therefore no longer be verified against its source, and was left as recorded rather than re-derived from a diagram. The same holds for the format reference `foundations/.canonical/general/entoli-concepts.md`, also retired.
2. **The entity names do not follow the current naming convention.** `INFORMATION_MODEL_ELEMENT` and its kin are written in `UPPER_SNAKE_CASE`, the form retired on 2026-09-13 in favour of upper case with single spaces and a parenthesised `(REF)` marker. Renaming them would mean renaming the entities of a model that no longer exists and cannot be checked; the divergence is disclosed rather than silently repaired.

---

## Table of contents

### Level 1 — Information Model
- [INFORMATION_MODEL](#information_model)
- [MODELLING_CONTEXT](#modelling_context)
- [INFORMATION_MODEL_ELEMENT](#information_model_element)
- [CHARACTERISTIC](#characteristic)

### Grounding context
- [SOURCE](#source)
- [SOURCE_TYPE_REF](#source_type_ref)
- [ISSUING_AUTHORITY](#issuing_authority)
- [REQUIREMENT](#requirement)

### NIAM Analysis — derivation method (between Grounding context and Level 1)
- [NIAM_ANALYSIS](#niam_analysis)
- [NIAM_FACT](#niam_fact)
- [NIAM_OBJECT](#niam_object)

### Level 2 — Logical Data Model
- [LOGICAL_DATA_MODEL](#logical_data_model)
- [ENTITY](#entity)
- [ATTRIBUTE](#attribute)
- [Reference entity](#reference-entity)

*Classification axes of the logical layer*
- [Attribute classification](#attribute-classification)
- [Data type](#data-type)

*Structural additions of the logical layer*
- [Time](#time)
- [Status](#status)

### Level 3 — Technical Data Model
- [TECHNICAL_DATA_MODEL](#technical_data_model)
- [TABLE](#table)
- [COLUMN](#column)

---

# Level 1 — Information Model

---

## INFORMATION_MODEL

**Element classification:** Domain Element

### Definition 📝
An **INFORMATION_MODEL** is Level 1 of the datamodelling meta-model: the customer-specific conceptual model of a domain, scoped by exactly one MODELLING_CONTEXT and grounded in one or more REQUIREMENTs.

### Characteristics ⭐
- `name` — the given name of the information model
- `version` — the version identifier of the information model
- `status` — the lifecycle status of the information model
- Is scoped by exactly one MODELLING_CONTEXT
- Is grounded by one or more REQUIREMENT (`derives-from`)
- Has one or more INFORMATION_MODEL_ELEMENT
- Leads to one or more LOGICAL_DATA_MODEL

### Relationships 🔗
- **scoped-by** → MODELLING_CONTEXT (1:1)
- **derives-from** → REQUIREMENT (N:M, one or more)
- **has** → INFORMATION_MODEL_ELEMENT (1:N)
- **leads-to** → LOGICAL_DATA_MODEL (1:N, one or more)

### What it is not ❌
- Not a LOGICAL_DATA_MODEL — that is its structured derivative, one level down
- Not a SOURCE — the authority text is what grounds it, indirectly, via REQUIREMENT
- Not a MODELLING_CONTEXT — that is the frame it is scoped by, not the model itself

---

## MODELLING_CONTEXT

**Element classification:** Domain Element

### Definition 📝
A **MODELLING_CONTEXT** is the customer-supplied frame — domain, purpose, scope boundary — within which exactly one INFORMATION_MODEL is built.

### Characteristics ⭐
- `domain` — the subject-matter domain the model addresses
- `purpose` — why the model exists
- `scope_boundary` — the explicit boundary of what falls inside versus outside the model
- Scopes exactly one INFORMATION_MODEL

### Relationships 🔗
- **scopes** → INFORMATION_MODEL (1:1)

### What it is not ❌
- Not part of the REQUIREMENT/SOURCE traceability chain — it frames the model, it does not ground it
- Not an INFORMATION_MODEL_ELEMENT

---

## INFORMATION_MODEL_ELEMENT

**Element classification:** Domain Element

### Definition 📝
An **INFORMATION_MODEL_ELEMENT** is a single concept inside an INFORMATION_MODEL — a unit of domain meaning, traceable to at least one REQUIREMENT.

### Characteristics ⭐
- `name`
- `definition`
- Is part-of exactly one INFORMATION_MODEL
- Derives from one or more REQUIREMENT — no INFORMATION_MODEL_ELEMENT may exist without at least one REQUIREMENT it derives from
- Has one or more CHARACTERISTIC

### Relationships 🔗
- **part-of** → INFORMATION_MODEL (N:1)
- **derives-from** → REQUIREMENT (N:M, one or more)
- **has** → CHARACTERISTIC (1:N, one or more)
- (target of, optional) **produces** ← NIAM_OBJECT

### What it is not ❌
- Not a CHARACTERISTIC — that is a property of it, not the element itself
- Not an ENTITY — ENTITY is its structured-layer counterpart; in this version of the schema, every ENTITY must derive from exactly one INFORMATION_MODEL_ELEMENT
- Not a NIAM_OBJECT — a NIAM_OBJECT is its optional method-layer origin, when NIAM Analysis was used to derive it

---

## CHARACTERISTIC

**Element classification:** Domain Element

### Definition 📝
A **CHARACTERISTIC** is a property of an INFORMATION_MODEL_ELEMENT.

### Characteristics ⭐
- `name`
- `definition`
- Belongs to exactly one INFORMATION_MODEL_ELEMENT
- May be the origin of zero or more ATTRIBUTE — not every CHARACTERISTIC needs to yield an ATTRIBUTE

### Relationships 🔗
- (target of) **has** ← INFORMATION_MODEL_ELEMENT
- (target of, optional) **derived-from** ← ATTRIBUTE
- (target of, optional) **produces** ← NIAM_FACT

### What it is not ❌
- Not an ATTRIBUTE — ATTRIBUTE is its structured-layer counterpart, when one exists
- Not itself an INFORMATION_MODEL_ELEMENT
- Not the product of every NIAM_FACT — only a binary, property-type NIAM_FACT produces a CHARACTERISTIC

---

# Grounding context

---

## SOURCE

**Element classification:** Domain Element

### Definition 📝
A **SOURCE** is a single external or internal authority text — a law, policy, standard or contract — that grounds an INFORMATION_MODEL via one or more REQUIREMENTs extracted from it.

### Characteristics ⭐
- `title`
- `citation`
- `effective_date`
- `jurisdiction`
- Is classified-as exactly one SOURCE_TYPE_REF
- Is issued-by exactly one ISSUING_AUTHORITY

### Relationships 🔗
- **classified-as** → SOURCE_TYPE_REF (N:1)
- **issued-by** → ISSUING_AUTHORITY (N:1)
- (target of) **cites** ← REQUIREMENT

### What it is not ❌
- Not a REQUIREMENT — REQUIREMENT is the atomic governable statement extracted from it
- Not an ISSUING_AUTHORITY — that is who published it, not the text itself

---

## SOURCE_TYPE_REF

**Element classification:** Domain Element

### Definition 📝
**SOURCE_TYPE_REF** is the Reference entity for SOURCE, enumerating the governed kinds of authority text: law, policy, standard, contract, or other.

### Characteristics ⭐
- Is a **Reference entity** in the sense registered in [Reference entity](#reference-entity), and carries the three Attribute kinds that concept prescribes: its identifier, a `code` and a `description`
- `code` — the stable value by which a position is referenced; unique, and an alternate identifier, never the entity identifier itself
- `description` — the readable explanation of that position

### Relationships 🔗
- (target of) **classified-as** ← SOURCE

### What it is not ❌
- Not a SOURCE itself — a classification value, not an authority text
- Not a precedence mechanism between sources — precedence (e.g. "policy MUST NOT contradict law") is a SOURCE-to-SOURCE relationship, not expressed through this reference entity

---

## ISSUING_AUTHORITY

**Element classification:** Domain Element

### Definition 📝
An **ISSUING_AUTHORITY** is the publisher of a SOURCE — a government body, a standards body, or the customer organisation itself.

### Characteristics ⭐
- `name`
- `authority_type`

### Relationships 🔗
- (target of) **issued-by** ← SOURCE

### What it is not ❌
- Not a SOURCE_TYPE_REF — that classifies the kind of source, not who published it

---

## REQUIREMENT

**Element classification:** Domain Element

### Definition 📝
A **REQUIREMENT** is an atomic governable statement — obligation, prohibition, or permission — extracted from a SOURCE. It is the bridge between a SOURCE (a document) and the INFORMATION_MODEL / INFORMATION_MODEL_ELEMENT it grounds.

### Characteristics ⭐
- `type` (obligation | prohibition | permission)
- `text`
- `condition`
- Cites exactly one SOURCE

### Relationships 🔗
- **cites** → SOURCE (N:1)
- **feeds** → NIAM_ANALYSIS (N:M)
- (target of) **derives-from** ← INFORMATION_MODEL
- (target of) **derives-from** ← INFORMATION_MODEL_ELEMENT
- (target of) **derives-from** ← NIAM_FACT

### What it is not ❌
- Not the SOURCE itself — a single extracted statement, not the document it comes from
- Not an INFORMATION_MODEL_ELEMENT — it grounds one (or more), it is not itself a domain concept
- Not a NIAM_ANALYSIS — REQUIREMENT is input to the method, not the method itself

---

# NIAM Analysis — derivation method

NIAM Analysis is the fact-based derivation method positioned between REQUIREMENT and INFORMATION_MODEL. It is transient: only its output, INFORMATION_MODEL, is a persistent recording layer. See `ldm-datamodelling.md` Scope for the full pipeline positioning: REQUIREMENT → NIAM_ANALYSIS → INFORMATION_MODEL → LOGICAL_DATA_MODEL → TECHNICAL_DATA_MODEL.

---

## NIAM_ANALYSIS

**Element classification:** Domain Element

### Definition 📝
A **NIAM_ANALYSIS** is a single instance of fact-based (NIAM) derivation: a transient method application, fed by one or more REQUIREMENT, that produces exactly one INFORMATION_MODEL.

### Characteristics ⭐
- `status`
- Is transient — it is a derivation-method instance, not a recording layer
- Is fed by one or more REQUIREMENT
- Has one or more NIAM_FACT
- Produces exactly one INFORMATION_MODEL

### Relationships 🔗
- (target of) **feeds** ← REQUIREMENT (N:M)
- **produces** → INFORMATION_MODEL (1:1)
- **has** → NIAM_FACT (1:N, one or more)

### What it is not ❌
- Not an INFORMATION_MODEL — that is its persistent output, not the method itself
- Not a REQUIREMENT — REQUIREMENT is its input
- Not a recording layer — meaning is bound at INFORMATION_MODEL, not here (see `doctrine-niam-analysis.md` §9 — that file carries the doctrine titled "Fact-Based Information Modelling"; the filename this entry previously cited does not exist)

---

## NIAM_FACT

**Element classification:** Domain Element

### Definition 📝
A **NIAM_FACT** is an elementary fact, expressed as a verbalised natural-language sentence, derived from one or more REQUIREMENT, within one NIAM_ANALYSIS.

### Characteristics ⭐
- `name`
- `verbalisation` — the natural-language sentence expressing the fact (see Verbalised fact)
- Is part-of exactly one NIAM_ANALYSIS
- Derives from one or more REQUIREMENT
- Involves one or more NIAM_OBJECT
- May produce zero or one CHARACTERISTIC — only when binary and property-type

### Relationships 🔗
- (target of) **has** ← NIAM_ANALYSIS
- **derives-from** → REQUIREMENT (N:M, one or more)
- (target of) **derives-from** ← NIAM_OBJECT
- **produces** → CHARACTERISTIC (N:0..1, binary property-facts only)

### What it is not ❌
- Not a REQUIREMENT — REQUIREMENT is what it is verbalised from
- Not a NIAM_OBJECT — an object type may play a role in the fact, but the fact and the object type are distinct
- Not always a CHARACTERISTIC-producing fact — an n-ary or associative fact produces no CHARACTERISTIC (see Transformation Rules)

---

## NIAM_OBJECT

**Element classification:** Domain Element

### Definition 📝
A **NIAM_OBJECT** is a NIAM object type, identified through one or more NIAM_FACT in which it plays a role.

### Characteristics ⭐
- `name`
- `definition`
- Is derived from (identified through) one or more NIAM_FACT
- Produces at most one INFORMATION_MODEL_ELEMENT, and only after ambiguity resolution (see Transformation Rules)

### Relationships 🔗
- **derives-from** → NIAM_FACT (N:M, one or more) — a traceability/identification relation, not the structural object-plays-role-in-fact relation of classic NIAM
- **produces** → INFORMATION_MODEL_ELEMENT (N:0..1, post ambiguity-resolution)

### What it is not ❌
- Not a NIAM_FACT — the fact is what identifies it, not the object type itself
- Not automatically an INFORMATION_MODEL_ELEMENT — the produces relation only holds once synonymous/duplicate NIAM_OBJECTs have been merged

---

## Verbalised fact

**Element classification:** Domain Element (realised as an attribute, not a separate entity)

### Definition 📝
A **verbalised fact** is the natural-language sentence form of a NIAM_FACT — the explicit, checkable expression of an elementary fact, following the fact-based modelling pattern of `doctrine-niam-analysis.md` §3.4 (e.g. "[Information Element] has [Characteristic]", "[Information Element] relates to [Information Element]").

### Characteristics ⭐
- Is realised as the `verbalisation` characteristic of NIAM_FACT — it is not a separate persisted entity in `ldm-datamodelling.md`
- Is grammatically correct and verifiable against the REQUIREMENT(s) the NIAM_FACT derives from

### Relationships 🔗
- (property of) NIAM_FACT

### What it is not ❌
- Not a separate ER entity — see NIAM_FACT.verbalisation
- Not a CHARACTERISTIC or an INFORMATION_MODEL_ELEMENT — it is a property of the fact, prior to and independent of whichever element/characteristic the fact may go on to produce

---

# Level 2 — Logical Data Model

---

## LOGICAL_DATA_MODEL

**Element classification:** Domain Element

### Definition 📝
A **LOGICAL_DATA_MODEL** is Level 2 of the datamodelling meta-model — the structured representation derived from exactly one INFORMATION_MODEL, expressed as ENTITY and ATTRIBUTE.

### Characteristics ⭐
- `name`
- `version`
- `status`
- Is based-on exactly one INFORMATION_MODEL
- Has one or more ENTITY
- Leads-to exactly one TECHNICAL_DATA_MODEL

### Relationships 🔗
- **based-on** → INFORMATION_MODEL (N:1)
- **has** → ENTITY (1:N, one or more)
- **leads-to** → TECHNICAL_DATA_MODEL (1:1)

### What it is not ❌
- Not the INFORMATION_MODEL itself — a structured derivative of exactly one such model
- Not a TECHNICAL_DATA_MODEL — that is its own derivative, one level down

---

## ENTITY

**Element classification:** Domain Element

### Definition 📝
An **ENTITY** is a distinguishable logical thing in a LOGICAL_DATA_MODEL about which data is recorded, described by one or more ATTRIBUTEs and identified by one or more of those ATTRIBUTEs.

### Characteristics ⭐
- Carries a `name` that expresses domain meaning, and a `definition` that states what, in the domain, it is
- Has one or more ATTRIBUTE
- Has exactly one primary identifier, and zero or more alternate identifiers, each formed from one or more of its own ATTRIBUTEs
- Belongs to exactly one Logical Data Model sub-model, assigned explicitly at the point it is introduced, never inferred from file placement (`doctrine.logical-data-modelling.md` §6.3, §7.1)
- Where it has a semantic counterpart, is derived from exactly one INFORMATION_MODEL_ELEMENT, whose meaning it preserves
- May exist with no semantic counterpart, where it is introduced for time, process or system structure and is traceable directly to a REQUIREMENT

### Relationships 🔗
- **part-of** → LOGICAL_DATA_MODEL (N:1)
- **has** → ATTRIBUTE (1:N, one or more)
- **identified-by** → ATTRIBUTE (1:N, one or more, through an identifier)
- **derived-from** → INFORMATION_MODEL_ELEMENT (N:0..1, only where a semantic counterpart exists)
- **specialised-by** → Reference entity
- (target of) **derived-from** ← TABLE

### What it is not ❌
- Not a TABLE — a table is its Technical Data Model derivative, and carries columns, indexes, storage and foreign keys that an ENTITY never does
- Not an INFORMATION_MODEL_ELEMENT — that is its conceptual origin, which records meaning without structure
- Not identified by its model-element identifier — that identifier exists to reference the ENTITY inside a model document, and says nothing about how an instance of the ENTITY is identified
- Not a junction introduced to implement a many-to-many relationship; an ENTITY that carries a relationship must have domain identity of its own

### Examples 💡
- `MEMBER`, `BOOK`, `LOAN` (`schemas/logical-data-model.example.json`)

**Correction (v0.3.0)**: this entry previously made a semantic counterpart mandatory (`derived-from` N:1). `doctrine.logical-data-modelling.md` §2.2 permits the logical layer to add time, process and system structure the Information Model does not express, so the cardinality is N:0..1.

---

## ATTRIBUTE

**Element classification:** Domain Element

### Definition 📝
An **ATTRIBUTE** is a logical property of exactly one ENTITY, carrying a Data type, an optionality, and exactly one position on the Attribute classification axis.

### Characteristics ⭐
- Carries a `name` that names the property, and, where the meaning is not evident from that name, a `definition`
- Carries exactly one Data type, drawn from the controlled logical vocabulary
- States its optionality explicitly: either every instance of its ENTITY must have a value, or an instance may have none
- Carries exactly one Attribute classification and is never left unclassified (`doctrine.logical-data-modelling.md` §5.5)
- May carry constraints on the values it admits — an allowed-value set, a value range, a length or a form — each of which states a rule of the domain
- May participate in one or more of its ENTITY's identifiers
- Where classified as semantic, is derived from exactly one CHARACTERISTIC of the Information Model, whose meaning it preserves; a temporal, process or system ATTRIBUTE has no such origin and is traceable directly to a REQUIREMENT

### Relationships 🔗
- **part-of** → ENTITY (N:1)
- **classified-as** → Attribute classification (N:1)
- **has** → Data type (N:1)
- **derived-from** → CHARACTERISTIC (N:0..1, only where classified as semantic)
- (target of) **derived-from** ← COLUMN

### What it is not ❌
- Not a COLUMN — a column is its Technical Data Model derivative, and carries storage size, encoding and database defaults that an ATTRIBUTE never does
- Not a CHARACTERISTIC — that is its conceptual origin, for semantic attributes only
- Not a foreign key — a relationship between ENTITYs is a model element in its own right and is never represented by adding an ATTRIBUTE that carries another ENTITY's identifier
- Not free to mix classifications — a structural ATTRIBUTE must never be presented, traced or verbalised as if it carried domain meaning

### Examples 💡
- `membership_number` (semantic), `joined_on` (temporal), `member_id` (system)

**Correction (v0.3.0)**: the classification position formerly named `time` is named **temporal**, following `doctrine.logical-data-modelling.md` §5 (`status: current`). The axis is a Classification Element in its own right — see Attribute classification, below — and is no longer described here as an attribute named `attribute_type`.

---

## Reference entity

**Element classification:** Domain Element

### Definition 📝
A **Reference entity** is an Entity whose sole purpose is to enumerate the valid positions of a closed, governed classification, so that those positions are carried as data rather than hard-coded into another Entity.

### Characteristics ⭐
- Is an Entity, and carries every characteristic of one
- Carries exactly three kinds of Attribute: its identifier, a `code` carrying the stable value by which a position is referenced, and a `description` explaining that position in readable language (`doctrine.logical-data-modelling.md` §3.2)
- Its `code` is unique and forms an alternate identifier; its `code` never replaces its identifier, and the two are never the same Attribute
- Is defined in exactly one sub-model; another sub-model that needs the same classification references it across the boundary and never redefines it (§6.3)
- Holds reference data: a relatively static, deliberately governed set whose extension is a classification decision, not a side effect of processing (`MRD-001`, `MRD-002`)

### Relationships 🔗
- **specialisation-of** → Entity
- **classifies** → Entity (1:N, through a relationship from the classified Entity)

### What it is not ❌
- Not master data — master data represents the core business things an organisation transacts about, with volume and ongoing lifecycle activity; a Reference entity carries low-volume, low-change classification values
- Not an enumeration on an Attribute — a classification that is open or extensible must be a Reference entity, never an allowed-value set written onto an Attribute
- Not identified by its `code` — `code` is a business key, and the entity identifier remains a separate Attribute
- Not every Entity whose name ends in a reference-like suffix; reference status follows from the source semantics, never from the name alone

### Examples 💡
- `LOAN_STATUS_REF`, carrying `loan_status_ref_id`, `code` and `description`

---

## Attribute classification

**Element classification:** Classification Element

### Definition 📝
**Attribute classification** is the axis that records the origin of an Attribute: whether it carries domain meaning taken from the Information Model, or was added by the logical layer to express time, process or system structure.

### Characteristics ⭐
- Every Attribute occupies exactly one position on this axis, and no Attribute is left unclassified (`doctrine.logical-data-modelling.md` §5.5)
- Distinguishes semantic lineage from structural lineage: only a semantic Attribute may be traced to a Characteristic of the Information Model; the three structural positions must be traceable directly to a requirement instead
- Is the axis on which the logical layer's licence to add structure is made visible — the Logical Data Model may add time, process and system structure that the Information Model does not and must not express (§2.2)
- Its positions are exclusive and exhaustive; an Attribute must never mix semantic and structural meaning

### Positions

| Position | Element classification | Records |
|---|---|---|
| **Semantic** | Position Element | Domain meaning, as the structured form of exactly one Characteristic of the Information Model |
| **Temporal** | Position Element | When a fact held, holds, or occurred — validity, history, or event time |
| **Process** | Position Element | Where an instance stands in a process — status or workflow state |
| **System** | Position Element | Identification or technical linkage, such as a surrogate key or a technical grouping |

### Relationships 🔗
- **classifies** → Attribute (1:N)
- **defines** → Position Element (Semantic, Temporal, Process, System)

### What it is not ❌
- Not the Data type axis — classification records where an Attribute came from, Data type records what values it admits; the two are independent
- Not a measure of importance — a structural Attribute is not a lesser Attribute, it is an Attribute with a different origin and a different traceability obligation

---

## Data type

**Element classification:** Classification Element

### Definition 📝
**Data type** is the axis that records the value space an Attribute admits, in terms independent of any database technology.

### Characteristics ⭐
- Every Attribute occupies exactly one position on this axis
- Its positions form a closed, controlled vocabulary; a value space not covered by a position is reported, never improvised
- Records the kind of value only: length, precision, encoding, collation and vendor mapping are Technical Data Model concerns and are never carried here
- Where the domain narrows the value space further — a range, a form, a maximum length — that narrowing is recorded as a constraint on the Attribute, not as a new Data type

### Positions

| Position | Element classification | Admits |
|---|---|---|
| **String** | Position Element | Text of any length |
| **Integer** | Position Element | A whole number |
| **Decimal** | Position Element | An exact number with a fractional part |
| **Boolean** | Position Element | True or false |
| **Date** | Position Element | A calendar date, without time of day |
| **Datetime** | Position Element | A point in time, date and time of day together |
| **Time** | Position Element | A time of day, without a date |
| **Duration** | Position Element | A length of time, independent of when it starts |
| **Uri** | Position Element | A reference identifying a resource |
| **Uuid** | Position Element | A globally unique identifier value |

### Relationships 🔗
- **classifies** → Attribute (1:N)
- **defines** → Position Element (the ten positions above)

### What it is not ❌
- Not a physical column type — `varchar`, `nvarchar`, `number(10,2)` and `timestamp with time zone` are Technical Data Model constructs and must never appear as a Data type
- Not a domain type — a postal code, an ISBN and a currency amount are a String, a String and a Decimal respectively, each narrowed by a constraint that states the domain rule
- Not a statement about storage — the same Data type may be implemented by different physical types in different technologies

---

## Time

**Element classification:** Domain Element

### Definition 📝
**Time**, in a Logical Data Model, is the recording of when a fact held, holds, or occurred, expressed as one or more Attributes classified as Temporal.

### Characteristics ⭐
- Is a structural addition of the logical layer: the Information Model records meaning without time, and the Logical Data Model adds it (`doctrine.logical-data-modelling.md` §2.2)
- Takes one of three shapes: the validity of a fact (from when, until when), the history of a fact (which values held when), or the moment of an event
- Is carried by Attributes whose Data type is Date, Datetime, Time or Duration, and whose Attribute classification is Temporal
- Is traceable directly to a requirement, never to a Characteristic of the Information Model
- Is introduced only where the domain requires it to be known; it is not a property every Entity carries by default

### Relationships 🔗
- **represented-by** → Attribute (1:N, each classified as Temporal)
- **grounded-in** → Requirement (N:1)

### What it is not ❌
- Not a database audit column — `created_at`, `updated_at`, `last_modified_by` and their kin are physical implementation patterns, and a logical model must not acquire them merely because a database commonly has them
- Not Status — Time records when something was so, Status records where an instance stands in a process; a date on which a status changed is Time, the status itself is not
- Not the version or date of the model artifact — that is metadata of the Logical Data Model, not data about an Entity instance
- Not derivable from a Characteristic — a temporal Attribute that is traced to the Information Model has been misclassified

### Examples 💡
- `loaned_on`, `due_on`, `returned_on` on `LOAN`; `joined_on` on `MEMBER`

---

## Status

**Element classification:** Domain Element

### Definition 📝
**Status**, in a Logical Data Model, is the position an instance of an Entity occupies in a process, expressed as an Attribute classified as Process and, where the set of positions is governed and closed, carried by a Reference entity reached through a relationship.

### Characteristics ⭐
- Is a structural addition of the logical layer: the Information Model records meaning without process state, and the Logical Data Model adds it (`doctrine.logical-data-modelling.md` §2.2, §5.3)
- Its set of positions is governed: a position is added by a deliberate classification decision, never incidentally
- Where that set is governed and may be extended, it is modelled as a Reference entity and reached through a relationship; only a genuinely fixed and small set may be written as an allowed-value set on the Attribute
- Is traceable directly to a requirement, never to a Characteristic of the Information Model
- Is introduced only where the domain runs a process over the Entity; an Entity that no process acts upon carries no Status

### Relationships 🔗
- **represented-by** → Attribute (1:N, each classified as Process)
- **governed-by** → Reference entity (N:0..1, where the position set is governed and extensible)
- **grounded-in** → Requirement (N:1)

### What it is not ❌
- Not Time — Status records where an instance stands, Time records when; the date a status was reached is a separate, temporal Attribute
- Not a lifecycle status of the model artifact — `current`, `stale` and `deprecated` classify a canonical artifact, not an instance of a modelled Entity
- Not a free-text remark — a status whose values are not governed is not a Status, it is an observation
- Not a derived indicator — a value computed from other Attributes, such as "overdue" read from a due date, is a derivation, and is recorded as one rather than stored as a process position

### Examples 💡
- `LOAN` classified by `LOAN_STATUS_REF`, whose `code` carries the governed positions of the lending process
---

# Level 3 — Technical Data Model

---

## TECHNICAL_DATA_MODEL

**Element classification:** Domain Element

### Definition 📝
A **TECHNICAL_DATA_MODEL** is Level 3 of the datamodelling meta-model — the implementation-level structure derived from exactly one LOGICAL_DATA_MODEL, expressed as TABLE and COLUMN.

### Characteristics ⭐
- `name`
- `version`
- `status`
- Is the `leads-to` target of exactly one LOGICAL_DATA_MODEL
- Has one or more TABLE

### Relationships 🔗
- (target of) **leads-to** ← LOGICAL_DATA_MODEL
- **has** → TABLE (1:N, one or more)

### What it is not ❌
- Not a LOGICAL_DATA_MODEL — that is its structural origin

---

## TABLE

**Element classification:** Domain Element

### Definition 📝
A **TABLE** is a single table inside a TECHNICAL_DATA_MODEL — the implementation form of exactly one ENTITY.

### Characteristics ⭐
- `name`
- `definition`
- Is derived-from exactly one ENTITY
- Has one or more COLUMN

### Relationships 🔗
- **derived-from** → ENTITY (N:1)
- **has** → COLUMN (1:N, one or more)

### What it is not ❌
- Not an ENTITY — that is its logical-layer origin
- Not a COLUMN — that is its constituent part

---

## COLUMN

**Element classification:** Domain Element

### Definition 📝
A **COLUMN** is a single column of a TABLE — the implementation form of exactly one ATTRIBUTE.

### Characteristics ⭐
- `name`
- `definition`
- Is derived-from exactly one ATTRIBUTE

### Relationships 🔗
- **derived-from** → ATTRIBUTE (N:1)

### What it is not ❌
- Not an ATTRIBUTE — that is its logical-layer origin
- Not a TABLE — that is the structure it belongs to

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 0.4.0 | 2026-09-15 | **`concepts-logical-data-model.md` merged in and deleted**, on explicit user instruction, so that the Data Modelling domain has one register and agents one entry point. All seven of its concepts moved across: `Reference entity`, `Attribute classification` (4 Position Elements), `Data type` (10 Position Elements), `Time` and `Status` verbatim, into Level 2; `ENTITY` and `ATTRIBUTE` restored from pointer entries to full definitions, merging that register's logical definition with this register's derivation-chain facts. Nothing dropped. The merged register was itself grounded in `doctrine.logical-data-modelling.md` v1.0.2 (`status: current`) and `schemas/logical-data-model.schema.json`; that grounding now applies here. File renamed in title only — `Datamodelling Meta-model — concepts` becomes `Data Modelling — concepts`, since it is no longer confined to the meta-model. Three referring artifacts repointed: `data-modelling.llm-constraints.yaml`, `.github/agents/ldm-modeller.agent.md` and this file's own cross-references |
| 0.3.0 | 2026-09-15 | **Recalibrated against `concepts-logical-data-model.md` v1.0.0**, on explicit user instruction, resolving both overlaps that file had recorded and handed to `canon-curator`. **Ownership settled** in the logical register's favour: `ENTITY` and `ATTRIBUTE` no longer carry a logical definition here — each entry is reduced to its place in the three-level derivation chain and points at the owning register. **Corrected**: the attribute classification position `time` is named `temporal` throughout, per `doctrine.logical-data-modelling.md` §5 (`status: current`); `ENTITY --derived-from--> INFORMATION_MODEL_ELEMENT` relaxed from N:1 to N:0..1, since §2.2 permits the logical layer to add entities with no semantic counterpart; `SOURCE_TYPE_REF` restated as a Reference entity in the registered sense. **Added**: a Concepts owned by the Logical Data Model register section, and `knowledge-domain: Data Modelling` in the frontmatter. **Reported, not resolved**: the source artifact `ldm-datamodelling.md` no longer exists, so this register's content can no longer be verified against it; and the `UPPER_SNAKE_CASE` entity names predate the 2026-09-13 naming decision. Both are recorded in Provenance for `canon-curator`. **Repaired**: two references to a non-existent `doctrine.fact-based-information-modelling.md` repointed to `doctrine-niam-analysis.md`, which carries that doctrine under a different filename |
| 0.2.0 | 2026-07-12 | Added NIAM Analysis derivation-method section, mirroring `ldm-datamodelling.md` v0.3.0: NIAM_ANALYSIS, NIAM_FACT, NIAM_OBJECT (all Domain Element) and Verbalised fact (documented as the `verbalisation` characteristic of NIAM_FACT, not a separate entity). Updated REQUIREMENT, INFORMATION_MODEL_ELEMENT and CHARACTERISTIC relationships/delimitations to cross-reference the new method layer |
| 0.1.0 | 2026-07-11 | Initial register: all 14 entities from `ldm-datamodelling.md` v0.2.1 (INFORMATION_MODEL, MODELLING_CONTEXT, INFORMATION_MODEL_ELEMENT, CHARACTERISTIC, SOURCE, SOURCE_TYPE_REF, ISSUING_AUTHORITY, REQUIREMENT, LOGICAL_DATA_MODEL, ENTITY, ATTRIBUTE, TECHNICAL_DATA_MODEL, TABLE, COLUMN) expressed in `entoli-concepts.md` register format |
