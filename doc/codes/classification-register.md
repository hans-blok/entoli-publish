---
type: classification-register
name: Entoli Classification Register
version: 1.0.0
date: 2026-07-24
status: current
source: foundations/.canonical/general/entoli-concepts.md v4.13.0
origin-position: derivative
---
# Entoli Classification Register

Canonical register of all Classification Elements and their Position Elements within the Entoli semantic model.

---

## Code scheme

| Prefix | Element classification |
|--------|----------------------|
| `CLA`  | Classification Element |
| `POS`  | Position Element |

Position Element codes follow the pattern `POS-{parent-code}-{position-abbreviation}`.

---

## Part 1 — Classification Elements

| code    | name                   | element_classification |
|---------|------------------------|-------------------------|
| CLA-DPO | Derivation position    | Classification Element |
| CLA-AFA | Artifact-function-axis | Classification Element |
| CLA-SRG | Source-regime          | Classification Element |
| CLA-TMD | Task Mode              | Classification Element |
| CLA-SYR | Synthesis regime       | Classification Element |
| CLA-SRL | Source-role            | Classification Element |
| CLA-OPO | Origin-position        | Classification Element |
| CLA-DEP | Development phase      | Classification Element |
| CLA-MOO | Mode of operation      | Classification Element |
| CLA-EXS | Execution Strategy     | Classification Element |

---

## Part 2 — Position Elements

| code        | name                         | element_classification | parent_classification  |
|-------------|-------------------------------|-------------------------|-------------------------|
| POS-DPO-LED | Leading                      | Position Element       | Derivation position    |
| POS-DPO-DRV | Derived                      | Position Element       | Derivation position    |
| POS-AFA-GOV | Governance artifact          | Position Element       | Artifact-function-axis |
| POS-AFA-DIR | Directive artifact           | Position Element       | Artifact-function-axis |
| POS-AFA-IMP | Implementing artifact        | Position Element       | Artifact-function-axis |
| POS-AFA-STR | Structuring artifact         | Position Element       | Artifact-function-axis |
| POS-AFA-REG | Registering artifact         | Position Element       | Artifact-function-axis |
| POS-SRG-INB | Input-bound                  | Position Element       | Source-regime          |
| POS-SRG-CNB | Canon-bound                  | Position Element       | Source-regime          |
| POS-SRG-EXB | External-source-bound        | Position Element       | Source-regime          |
| POS-SRG-OPN | Open                         | Position Element       | Source-regime          |
| POS-TMD-EXT | Extracting                   | Position Element       | Task Mode              |
| POS-TMD-STR | Structuring                  | Position Element       | Task Mode              |
| POS-TMD-TRF | Transforming                 | Position Element       | Task Mode              |
| POS-TMD-EVL | Evaluating                   | Position Element       | Task Mode              |
| POS-TMD-ORI | Originating                  | Position Element       | Task Mode              |
| POS-SYR-PRV | Preserving                   | Position Element       | Synthesis regime       |
| POS-SYR-REL | Relating                     | Position Element       | Synthesis regime       |
| POS-SYR-GEN | Generating                   | Position Element       | Synthesis regime       |
| POS-SRL-NRM | Normative source             | Position Element       | Source-role            |
| POS-SRL-WRK | Work-source                  | Position Element       | Source-role            |
| POS-OPO-INI | Initiating                   | Position Element       | Origin-position        |
| POS-OPO-DRV | Derivative                   | Position Element       | Origin-position        |
| POS-DEP-EXP | Exploration                  | Position Element       | Development phase      |
| POS-DEP-ORD | Ordering                     | Position Element       | Development phase      |
| POS-DEP-SPC | Specification                | Position Element       | Development phase      |
| POS-DEP-RLS | Realisation                  | Position Element       | Development phase      |
| POS-DEP-TST | Testing                      | Position Element       | Development phase      |
| POS-DEP-REG | Registering                  | Position Element       | Development phase      |
| POS-DEP-OPR | Operationalisation           | Position Element       | Development phase      |
| POS-MOO-CNT | Content                      | Position Element       | Mode of operation      |
| POS-MOO-RTR | Representation-transforming  | Position Element       | Mode of operation      |
| POS-MOO-CON | Conditional                  | Position Element       | Mode of operation      |
| POS-EXS-LIN | Linear Execution             | Position Element       | Execution Strategy     |
| POS-EXS-EXP | Exploratory Execution        | Position Element       | Execution Strategy     |
| POS-EXS-CNV | Convergent Execution         | Position Element       | Execution Strategy     |
