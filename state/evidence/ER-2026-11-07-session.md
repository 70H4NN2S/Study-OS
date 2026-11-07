# ER/EER Chen modeling — study session, 2026-11-07

**Source/limitations:** Manual inspection of privately uploaded handwritten diagram photos, plus the learner's responses in a ChatGPT study session. The photos are **not** in this public repository; the following anonymized observations cannot be independently image-audited without the user's private originals. Scores reproduce feedback given during that conversation (formative rubric, not machine test results). The user explicitly ended the session and requested a single aggregated GitHub PR. Not an official university assignment, exam or grading record.

**Scope:** EX-0101–EX-0112 of the independent original 24-task ER/EER track. 12 distinct tasks assessed; 0101, 0102, 0108 and 0111 have assessment stages. Latest-per-task average = **94.9/100** (1139/1200). A score does *not* imply durable retention. No skill is rated level 4, because delayed independent transfer has not yet been measured.

| Exercise | Initial/intermediate | Final | Observable evidence | Follow-up |
| --- | --- | ---: | --- | --- |
| EX-0101 | Earlier standalone review 76; separate session diagram-only score 88 | **95** | Member/Storage Cabinet, attributes and rents correct; (0,1) each side assumed rather than specified. Learner explicitly justified 0..1 assumptions and classified password reset as an application action. | Check ungrounded assumptions in new scenario |
| EX-0102 | Diagram-only 90 | **95** | Exhibit with inventory_code underlined; title and acquisition_year; learner correctly explained global uniqueness. Distinguishing a type from an individual instance was explained by tutor, not separately answered by learner. | Delayed type/instance recall |
| EX-0103 | — | **82** | Correct age as derived, phone_numbers multivalued; classified birth_date composite (valid only if broken into components); assumed home_address multivalued despite one address in prompt. Expressed uncertainty about composite vs simple. | New attributes with explicit bounds; isolate three classification axes |
| EX-0104 | — | **100** | Device key serial_number, double oval safety_labels, location subattributes building/room, simple manufacture_date drawn correctly. | Delayed transfer; note min-one safety_label not enforced by oval |
| EX-0105 | — | **96** | Underlined both region_code and local_ticket_no as minimal composite key; initially included repair description in an example of a key value. Correct key tuple is only (region_code, local_ticket_no). | Key tuple vs whole record |
| EX-0106 | — | **100** | Meetup (1,1), Host (0,*), organized_by, both IDs correctly underlined; user explained host without meetup permitted, meetup without host forbidden. | Periodic min/max revisit |
| EX-0107 | — | **97** | Bicycle (1,1), Fleet (2,12) correctly 1:N; Device (1,3), Technician (0,*) correctly M:N. Explicit verbal description of every interval omitted. | Verbal reading of endpoints |
| EX-0108 | Diagram and explanation 97 | **100** | Judge and Product each (0,*); score and rated_on on rates diamond; explained scores differ by judge. After conceptual explanation, independently answered 3/3 on multiple judges, one rating per pair, and composite (judge_id, product_id) key. | Relationship instance uniqueness vs min/max constraints |
| EX-0109 | — | **100** | Rack (1,4), Pallet (1,1) with distinct PKs; correctly classified A invalid, B valid, C invalid, D invalid, E valid (two separate pallets). | Periodic retention |
| EX-0110 | — | **94** | Strong CampusBuilding, weak Room, identifying double diamond, composite global identity. Missing explicit Room (1,1) and weak partial-key dashed underline unclear. Conceptual answers 3/3, including obligatory relation != weak identity. | Weak symbol and partial-key drill |
| EX-0111 | **68** first submission | **100** corrected | First drew separate Employee and Supervisor entity types and classified as M:N; incorrectly expected unique ID to prohibit self-reference. After tutor explanation, redrew one Employee entity with TWO labeled roles supervisor (0,4), subordinate (0,1), and a single supervises relationship. Final was **assisted**; test with an unfamiliar self-relation before calling mastery independent. | Independent role/cardinality + no-self-loop/cycle drill |
| EX-0112 | — | **80** | Correct one ternary delivers diamond joining Supplier/Part/Warehouse, correct general explanation that pairwise links lose triple semantics. Incorrect proposed false triple (S2,P2,W1); its 3 pairs are absent. Valid counterexample (S1,P1,W2) was provided by tutor after submission. | **Top priority:** re-test pairwise projections with a fresh set; final score remains 80 |

## Spaced review priorities

1. **2026-11-08 (proposed, not automated):** Find a genuinely spurious ternary tuple by checking each of its three pairs; independently redraw the recursive employee case with role labels; classify composite/multivalued attributes in a new miniworld.
2. **2026-11-10:** Weak identifying relationship and partial-key notation, and relationship attribute / relational composite-key distinctions.
3. **2026-11-14:** Keys vs values, min/max and scope constraints in mixed tasks.
4. **2026-11-21:** Delayed basics recall for entity types, keys and instances.

**Next exercise:** EX-0113 — ternary relationship with unit_price, preferably after the corrective EX-0112 transfer drill. Unassessed skills (EER specialization, categories, schema integration/mapping) remain unassessed.

## Assessment methodology and integrity

- Grade and completion are separate from per-skill mastery; level 3 requires independent typical task, level 4 independent transfer plus delayed retention.
- Assistance is noted when demonstrated. An EX-0111 corrected score of 100 is not independent mastery; EX-0108 follow-up was 3/3 **after** a conceptual explanation.
- This record contains no real names, personal identifying information, raw photos, or university-owned assignment solutions.
