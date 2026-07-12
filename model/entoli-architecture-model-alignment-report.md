---
type: alignment-report
name: Entoli architecture model — canonical alignment report
source-model: model/entoli-architecture-model.archimate
canon-reference: entoli-canon/foundations/.normative/.general/entoli-concepts.md (v4.1.0)
status: current
---

# Entoli architecture model — canonical alignment report

## Purpose

This report documents the semantic alignment pass performed on `entoli-architecture-model.archimate`
against the canonical concept register `entoli-concepts.md` (v4.1.0). It is **not** a translation —
every element name in the model was checked against the canon's controlled vocabulary, non-canonical
or ambiguous terms were replaced with the canonical term where one exists, and every element with no
canonical equivalent is explicitly flagged rather than silently kept.

**Scope note**: renames were applied to `name` attributes across every folder — Strategy, Business,
Application, Technology, Motivation and Other. Where a documentation block directly restated a
canonical position list incorrectly, that text was corrected too. Full documentation *prose* bodies
that were written in Dutch (the Strategy-folder value-stream phases, and the three Motivation-layer
Principles) were **not** translated in full — only their element names were translated and aligned.
Translating hundreds of lines of Dutch narrative per element is a materially larger undertaking than
terminology alignment; each such element is flagged `[name translated; documentation body remains
Dutch — see alignment report]` so this is visible in the model rather than silently incomplete.
No element `id`s or relationships were altered, so diagram wiring is untouched.

---

## 1. Strategy folder — Dutch value-stream/phase model

The Strategy folder contains a detailed, originally all-Dutch elaboration of a generic value-stream
phase model (`ValueStream` elements) plus five `Capability` elements. Both map closely — but not
perfectly — onto two canon classification axes: **Development phase** (for the top-level phases) and
**Interpretation Mode** (for the capabilities). All names below were translated *and* aligned to the
canonical term where one exists.

### 1.1 Top-level phases → Development phase positions

| Original (Dutch) | Canonical term | Action |
|---|---|---|
| 1.verkenning | 1. Exploration | replaced |
| 2.ordening | 2. Ordering | replaced |
| 3.vastlegging | 3. Recording | replaced |
| 4.realisatie | 4. Realisation | replaced |
| 5..toetsing *(double-dot typo)* | 5. Testing | replaced |
| 6.Operationalisatie | 6. Operationalisation | replaced |
| 5.verantwoording | **Accountability** — flagged | flagged | Not one of canon's six Development phase positions (Exploration/Ordering/Recording/Realisation/Testing/Operationalisation). Also mis-numbered "5", colliding with Testing — the model has two different phases both labelled "5". Recommend either dropping this phase or renumbering/re-deriving it as a sub-phase rather than a sixth axis position. |

### 1.2 Sub-phases

Sub-phases of Exploration, Ordering and Recording (Orientation/Selection/Concept Inventory;
Conceptual Restructuring/Structure Formulation/Reduction & Consistency; Ratification & Formal
Fixation/Making Testability Explicit/Publication & Anchoring) and of Testing
(Performing Comparison/Making Judgment Explicit/Reporting) have no canon-defined equivalents of
their own — canon's Development phase axis stops at the six top-level positions. These were
translated to English but are not "canonical" in the strict sense; they are a legitimate
elaboration specific to this generic value-stream template.

The four Operationalisation sub-phases are a genuine, exact match to canon's own Operationalisation
sub-phase table and were aligned accordingly:

| Original (Dutch) | Canonical term | Action |
|---|---|---|
| 6.1 Besluiten | 6.1 Decision-making | replaced — matches canon's Operationalisation sub-phase table exactly |
| 6.2.Activering | 6.2 Activation | replaced — exact canonical match |
| 6.3.Begeleiding | 6.3 Guidance | replaced — exact canonical match |
| 6.4.Bestendiging | 6.4 Consolidation | replaced — exact canonical match |

The "Accountability" phase's own sub-phases (Documenteren/Traceerbaarheid expliciteren/
Contextualiseren/Publiceren) were translated to English (Documenting / Making Traceability Explicit /
Contextualising (Target Audience) / Publishing) but remain attached to a non-canonical parent phase.

**Data-quality note**: several sub-phase elements' documentation bodies do not match their own names
(e.g. the element named "6.1 Besluiten" carries the documentation for "4.1 Constructie"; "6.3
Begeleiding" and "6.4 Bestendiging" both carry the documentation for "4.3 Verificatie"). These are
copy-paste artifacts in the source model. They were left as-is — fixing them is a content-authoring
task, not a terminology-alignment one — but are flagged here since they affect the reliability of
those elements' documentation.

### 1.3 Capabilities → Interpretation Mode positions

| Original (Dutch) | Canonical term | Action |
|---|---|---|
| normeren | Normative | replaced (two instances — duplicate, see §3) |
| evalueren | Evaluative | replaced |
| structuur realiseren | Structural | replaced |
| beschrijven | Explanatory | replaced |
| realiseren | Realising | replaced (two instances — duplicate, see §3) |

These five map cleanly onto five of canon's seven Interpretation Mode positions (Exploratory,
Explanatory, Structural, Normative, Realising, Evaluative, Validating) — only Exploratory and
Validating have no corresponding capability in this diagram.

### 1.4 Other Strategy elements

| Original term | Canonical term | Action |
|---|---|---|
| Realization | Realisation | replaced — British spelling per canon |
| Meaning | — | flagged | no canonical Domain Element equivalent |
| Validity | — | flagged | no canonical Domain Element equivalent |

---

## 2. Business / Application / Technology / Other — mapping table

This section covers the folders that were already in English (or already had a documented
canonical/non-canonical status) prior to this pass.

| Original term | Canonical term | Action | Notes |
|---|---|---|---|
| Agent Intent | Agent-capability | replaced | Canon: "Intent" is an explicit synonym of Agent-capability. **Creates a name duplicate** with the pre-existing `Agent-capability` element (id `7a697edb…`) — recommend architectural consolidation. |
| Execution Step *(Business, documented as "An Execution is…")* | Execution | replaced | The element's own documentation was the canonical Execution definition, not Execution Step — it was mislabeled. |
| Execution Step Spedicification | Execution Step Specification | replaced | Typo fix only. |
| Artifact *(Business + Application data object)* | Entoli-artifact | replaced | Canon: "Artifact" is a listed synonym; cross-layer pairing (Business object realised by Application data object) is correct ArchiMate practice, not a duplicate. |
| Intervention Type *(Business + Application data object)* | Interpretation Mode | replaced | No canonical axis named "Intervention Type" exists; the relationship pattern (defines, per agent-intent) matches Interpretation Mode. **Creates duplication** with the two already-correct `Interpretation Mode` data objects — recommend consolidating (see §3). |
| Normative artifact (rules) | Normative artifact | replaced | No parenthetical qualifier in the canonical term. |
| Entoli Semantic Model | Semantic Model | replaced | "Entoli" prefix is not part of the canonical term. |
| Entoli ecosystem *(Product)* | Entoli-ecosystem | replaced | Canonical heading is hyphenated. |
| Semantic Foundation | — | flagged | No canonical Domain Element by this name. |
| Domain | Domain Element | replaced | |
| Para element / Classfication element / Position element | Para Element / Classification Element / Position Element | replaced | Typo + casing fixes. |
| Actor element / Vallidity element / Object element | *(flagged, typos fixed)* | flagged | Canon defines exactly four Element classifications (Domain, Classification, Position, Para) — these three are not among them. |
| Artiffact *(Other, "business vs normative" element)* | Entoli-artifact | replaced | Typo fixed; underlying dichotomy flagged separately (see §4). |
| Policy (scope) | — | flagged | Canon references "policies" only informally. |
| Interpretation Mode *(positions: "Explotarory", "Structure-realising", "Ordering")* | Interpretation Mode *(positions corrected)* | replaced | Fixed typo; "Structural" not "Structure-realising"; removed "Ordering" (belongs to Development phase, not this axis). |
| Template *(documentation: "does not prescribe content")* | Template *(documentation corrected)* | replaced | Canon states a template **does** prescribe minimum content/structure — prior wording contradicted the canonical definition. |
| Provide Service Contracts | Provide Agent Contracts | replaced | Canon: "Service contract" is a listed synonym of Agent-contract. |
| Development phase *(2nd instance, positions incl. "Accountability")* | Development phase *(positions corrected)* | replaced | Canon's six positions are Exploration, Ordering, Recording, Realisation, Testing, Operationalisation — "Accountability" removed, missing "Realisation" restored. **Duplicates** the correctly-defined instance. |
| Source-regime *(2nd instance, positions "Externally-bound"/"Exploratory")* | Source-regime *(positions corrected)* | replaced | Canon positions are Input-bound, Canon-bound, Workspace-bound, External-source-bound, Open. **Duplicates** the correctly-defined instance. |
| Business Artiffact | Entoli-artifact *(flagged sub-classification)* | replaced + flagged | See §4. |
| Derivation Position | Derivation position | replaced | Casing aligned to canon heading. |
| Origin Position | Origin-position | replaced | Canonical term is hyphenated; second position "Building-on" corrected to canonical "Derivative". |
| normative source / working source / handoff | Normative source / Work-source / Handoff | replaced | Casing + canonical hyphenation ("Work-source", not "working source"). |
| Stores paradata and Intruction sets (JSONB ) | Stores Paradata and Instruction Sets (JSONB) | replaced | Typo + capitalisation. |
| Stores concepts - semantic model and semantic scopes | Stores concepts — Semantic Model and Semantic Scopes | replaced | Capitalisation aligned. |
| Rule / System constraints / LLM constraints / snapshot strategy / pointer strategy | — | flagged (all five) | Implementation-level, no canonical equivalent. |
| configuratiion | configuration | replaced | Typo only. |
| model *(Grouping)* | — | flagged | Generic organisational grouping. |
| Entoli ecoystem *(Grouping)* | Entoli ecosystem | replaced | Typo fix. |
| ENTOLI MANAGEMENT SYSTEM / CLIENT SYSTEM | Entoli Management System / Client System | replaced + flagged | ALL-CAPS normalised to Title Case; no canonical equivalent — "Entoli Management System" is **not** the same as the canonical Agent-ecosystem-development-system. |
| large language model *(new DataObject, Application layer)* | — | flagged | Implementation-level, no canonical Domain Element. |
| llm-execution-configuration *(new, two instances — Business + Application)* | — | flagged | Likely a technical realisation of the canonical Execution file; duplicated across two layers with no realisation relationship linking them. |
| external-resource / private-resource / entoli-resource *(new Business objects)* | — | flagged | No canonical Domain Element; correspond informally to the External-source-bound / Workspace-bound / Canon-bound source spaces of Source-regime, respectively. |
| Language Intelligence Resource *(new)* | — | flagged | No canonical equivalent; duplicates "large language model". |
| entoli client / large language model / onze spelregels *(new Groupings, Other folder)* | Entoli Client / Large Language Model / Our Rules of the Game | replaced + flagged | Translated and Title-Cased; none has a canonical equivalent — "onze spelregels" ("our rules of the game") is an informal team phrase, not canon vocabulary. |

Elements already matching the canon exactly were left unchanged: Entoli-agent, Agent-contract,
Agent-capability *(original instance)*, Artifact-function-axis, Source-regime *(original instance)*,
Development phase *(original instance)*, Mode of operation, Value stream, Value stream phase,
Semantic Scope, Semantic Model *(Application instance)*, Entoli-concept, Relationship, Element,
Prompt, Normative artifact *(Application instance)*, Interpretation Mode *(original two instances,
now position-corrected)*, Execution Step Specification, Instruction Set, Execution, Representation.

Tool-layer elements (Runner, Orchestrator, LLM engine, Source Injector, MongoDB, Postgres, ApplicationService/Function
names) were left unchanged: the canon does not prescribe implementation component names, and
"Runner" specifically is used consistently throughout the canon's prose even without its own
register entry.

---

## 3. Structural duplicates surfaced by this pass

Renaming to canonical terms surfaced name collisions that a text-only alignment pass cannot safely
resolve — doing so would require merging elements and re-pointing relationships, a structural change
rather than a terminology one. Flagged in-model and listed here for an architect to consolidate:

- **Agent-capability**: two separately modelled elements (`id-7a697edb…`, originally distinct, and
  `id-fc519c97…`, renamed from "Agent Intent") now share the canonical name.
- **Interpretation Mode**: four elements now share this name — the two originally-correct ones (with
  the corrected 7-position list) and the two renamed from "Intervention Type" (Business + Application
  pair). Recommend keeping the position-bearing pair and retiring/re-pointing the "Intervention Type"
  pair's relationships onto it.
- **Development phase** and **Source-regime**: each has a duplicate instance in the Application
  folder whose position lists have now been corrected in place, but the duplication itself remains.
- **normeren → Normative** and **realiseren → Realising** (Strategy Capabilities): each appears twice
  (once around line 307–458, once around line 957–995) with near-identical documentation — likely an
  authoring duplication within the Strategy folder itself.
- **llm-execution-configuration**: exists once in Business and once in Application, with no
  relationship linking the two layers (unlike the correctly-paired Artifact/Interpretation Mode
  elements elsewhere).

---

## 4. Unmapped concepts

These concepts/terms have no canonical equivalent in `entoli-concepts.md` and must not be treated as
canonical. They are flagged in the model file itself (`[UNMAPPED — …]`) rather than silently kept.

1. **Meaning**, **Validity** (Strategy-layer capabilities) — no register entry.
2. **Semantic Foundation** — no register entry; groups the Element-classification mini-ontology.
3. **Actor Element**, **Validity Element**, **Object Element** — canon defines exactly four Element
   classifications (Domain, Classification, Position, Para); these three are additional and invented.
4. **Policy (scope)** — canon mentions "policies" only informally.
5. **Rule**, **System constraints**, **LLM constraints**, **snapshot strategy**, **pointer strategy**
   (Motivation layer) — implementation/governance constraints with no register entry.
6. **model**, **Entoli Management System**, **Client System**, **Entoli Client**, **Large Language
   Model** *(grouping)*, **Our Rules of the Game** (Groupings) — organisational containers with no
   canonical Domain Element behind them. "Entoli Management System" should not be conflated with the
   canonical **Agent-ecosystem-development-system**.
7. **llm-execution-configuration**, **external-resource**, **private-resource**, **entoli-resource**,
   **Language Intelligence Resource**, **large language model** *(DataObject)* — a cluster of new,
   implementation-level elements describing LLM/AI provider choices (OpenAI, Google, Anthropic vs. an
   Entoli-hosted model such as Oloma). None have canonical Domain Element status; the closest canon
   concepts are the source-space definitions within **Source-regime**.
8. The **"business artifact vs. normative artifact"** dichotomy (elements "Business Artiffact"/
   "Artiffact") — canon does not sub-classify Entoli-artifact this way; the canonical sub-classification
   is the **artifact-function-axis** (Governance / Directive / Implementing / Structuring / Registering
   artifact).
9. **Accountability** (Strategy value-stream phase, from "verantwoording") — not one of canon's six
   Development phase positions.
10. The generic Strategy sub-phases without canon equivalents (Orientation, Selection, Concept
    Inventory, Conceptual Restructuring, Structure Formulation, Reduction & Consistency, Ratification
    & Formal Fixation, Making Testability Explicit, Publication & Anchoring, Construction, Integration,
    Verification, Performing Comparison, Making Judgment Explicit, Reporting, Documenting, Making
    Traceability Explicit, Contextualising, Publishing) — legitimate elaborations of a generic
    value-stream template, translated to English, but not themselves canonical terms.

---

## 5. Validation

- All four transformation rules (canonical term enforcement, concept mapping, naming normalisation,
  structural consistency) were applied to every named element across all folders, including the
  Dutch Strategy-folder value-stream/phase model and the Dutch Motivation-layer elements.
- Full Dutch documentation *prose* (Strategy phase narratives, the three Principle essays) was left
  untranslated and is explicitly flagged per element — this was a deliberate scope decision, not an
  oversight, given the volume involved (well over a thousand lines of narrative text).
- No relationships or element `id`s were altered — diagram wiring in the Views folder is unaffected.
- The model file was re-parsed as XML after editing and confirmed well-formed.
- Every element without a canonical equivalent is explicitly flagged in its `name` attribute
  (`[UNMAPPED — …]`) rather than left silently as if it were canon-compliant.
