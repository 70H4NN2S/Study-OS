# Chen ER/EER modeling — Study OS track

**Objective:** start from zero and independently build, explain, inspect, and translate Chen ER/EER models at lecture/exam level. **24 original, short exercises**, not rewritten versions of university homework. Begin with **[EX-0101](EX-0101-spot-the-model/assignment.md)**. Do only one exercise at a time, request a grade, then proceed. Estimated duration: 8–50 minutes.

## Submission and grading

**Recommended: paper + pen for the first 10 tasks.** Photograph from directly above with all labels readable; send the image here in chat. Alternatively use [diagrams.net](https://app.diagrams.net/) / draw.io or Dia; export PNG/PDF and ideally retain the optional editable .drawio source. Written tasks can be answered in chat or in answer.md. For formal repository evidence, place the artifact inside the exercise folder's submission/ directory and link its **exact commit/PR**. Do not invest time in visual polish.

Study OS's strict 100-point rubric is adapted to diagrams: **semantic correctness 50; min–max, integrity, edge/counterexamples 25; notation/legibility 15; independent explanation 10**. Review each diagram semantically; the repository validator only checks file records, **not** whether an image is a correct diagram. Ask for hint tier 1 (nudge) or 2 (concept); tier 3/4 only if explicitly requested, as in [STUDY_OS.md](../../STUDY_OS.md). No answer keys or fabricated grades will be committed. Grading and mastery changes require actual submitted evidence. A good first attempt does not alone establish durable mastery.

After an assessed attempt, schedule fresh exercises with approximately 1/3/7/14-day review gaps as warranted by mistakes and retention; not automatically scheduled merely because the task exists. Weak areas get new scenarios, not rote repetition.

## Progression

| Stage | Exercises | What you will master |
| --- | --- | --- |
| A — Fundamentals | 0101–0105 | miniworld, entities, keys, attributes and Chen symbols |
| B — Relationships | 0106–0109 | min–max on each side, relationship attributes, bound checks |
| C — Advanced ER | 0110–0114 | weak entities, recursive and ternary relationships, integrity |
| D — Extended ER | 0115–0118 | inheritance, partial/total, disjoint/overlap, categories/union |
| E — Exam transfer | 0119–0124 | complete modeling, critique, view integration, relational mapping, capstone |

## Assignments

- [EX-0101 — Separate entities, attributes and actions](EX-0101-spot-the-model/assignment.md) (8 min, `DB-ERM-SCOPE`)
- [EX-0102 — Your first Chen entity](EX-0102-first-chen-entity/assignment.md) (10 min, `DB-ERM-ENTITIES`)
- [EX-0103 — Classify attribute kinds](EX-0103-attribute-classifier/assignment.md) (10 min, `DB-ERM-ATTRIBUTES`)
- [EX-0104 — Draw composite and multivalued ovals](EX-0104-draw-complex-attributes/assignment.md) (12 min, `DB-ERM-ATTRIBUTES`)
- [EX-0105 — Find the minimal composite key](EX-0105-composite-keys/assignment.md) (12 min, `DB-ERM-KEYS`)
- [EX-0106 — Model the first binary relationship](EX-0106-host-and-event/assignment.md) (15 min, `DB-ERM-CARDINALITY`)
- [EX-0107 — Translate natural language into min–max](EX-0107-cardinality-translator/assignment.md) (10 min, `DB-ERM-CARDINALITY`)
- [EX-0108 — Give relationship data its correct owner](EX-0108-relationship-attributes/assignment.md) (15 min, `DB-ERM-REL-ATTRS`)
- [EX-0109 — Model exact upper and lower bounds](EX-0109-bounded-participation/assignment.md) (15 min, `DB-ERM-CARDINALITY`)
- [EX-0110 — Identify a weak entity](EX-0110-weak-room/assignment.md) (20 min, `DB-ERM-WEAK`)
- [EX-0111 — Name roles in recursive relationships](EX-0111-recursive-supervision/assignment.md) (18 min, `DB-ERM-RECURSIVE`)
- [EX-0112 — Find invented facts from binary projections](EX-0112-ternary-counterexample/assignment.md) (18 min, `DB-ERM-NARY`)
- [EX-0113 — Draw a ternary relationship with an attribute](EX-0113-ternary-with-price/assignment.md) (22 min, `DB-ERM-NARY`)
- [EX-0114 — Identify rules ER cannot encode](EX-0114-residual-constraints/assignment.md) (25 min, `DB-ERM-INTEGRITY`)
- [EX-0115 — Reason about EER subtype sets](EX-0115-specialization-set-logic/assignment.md) (15 min, `DB-EER-SPECIALIZATION`)
- [EX-0116 — Draw total disjoint specialization](EX-0116-total-disjoint-workers/assignment.md) (20 min, `DB-EER-SPECIALIZATION`)
- [EX-0117 — Model an EER union/category type](EX-0117-union-destination/assignment.md) (23 min, `DB-EER-CATEGORY`)
- [EX-0118 — Use an attribute-defined specialization](EX-0118-attribute-defined-subtypes/assignment.md) (20 min, `DB-EER-SPECIALIZATION`)
- [EX-0119 — Design a complete ER diagram](EX-0119-climbing-gym/assignment.md) (35 min, `DB-ER-CHEN`)
- [EX-0120 — Audit and repair a broken ER model](EX-0120-spot-model-bugs/assignment.md) (25 min, `DB-ERM-VALIDATION`)
- [EX-0121 — Integrate two overlapping ER views](EX-0121-merge-library-views/assignment.md) (35 min, `DB-ERM-INTEGRATION`)
- [EX-0122 — Map a small ER model into relations](EX-0122-map-er-to-relations/assignment.md) (30 min, `DB-ERM-MAPPING`)
- [EX-0123 — Map EER specialization and weak identity](EX-0123-map-eer-and-weak/assignment.md) (35 min, `DB-ERM-MAPPING`)
- [EX-0124 — Independent exam-style EER challenge](EX-0124-repair-fleet-capstone/assignment.md) (50 min, `DB-ER-CHEN`)

## Connection to the course

The sequence is calibrated against the uploaded TU Braunschweig lecture PDFs *Data Modeling I*, *Data Modeling II*, *View Integration*, and the first two Große Übungen, their Musterlösungen, and the current *Datenmodellierung I/II* homework sheets. Their central topics include classic Chen notation (rather than swapping in crow's foot), attribute classification, weak entities, min–max, n-ary relationships, EER specializations and union types, and unmodelled integrity constraints. These are independently written scenarios and contain no reproduced homework solutions or uploaded PDFs.

**Academic integrity:** the official graded sheets explicitly prohibit using generative AI to produce homework answers (zero points for AI-generated content). Use this track for independent practice; do not repurpose its generated text/diagrams as submitted homework. The existing public Study OS repository should not receive names, student IDs, university PDFs or unapproved personal material.
