# Chen and EER — quick notation reference

These are the symbols used throughout this Study OS track, aligned with the classic Chen style in the lecture.

| Symbol | Meaning |
| --- | --- |
| Rectangle | Entity type |
| Double rectangle | Weak entity type |
| Oval | Attribute |
| Underlined attribute name | Key attribute (a key can consist of multiple attributes) |
| Double oval | Multivalued attribute |
| Dashed oval | Derived attribute |
| Oval linked to smaller ovals | Composite attribute |
| Diamond with a relationship name | Relationship type |
| Double diamond | Identifying relationship for a weak type |
| Two role labels on the same entity type | Recursive relationship participation |
| `(minimum,maximum)` at an entity end | How often *each entity of that type* participates in this relationship |
| EER circle `d` / `o` | Disjoint / overlapping specialization, together with total/partial participation |
| EER category / `u` | Union of entities from different owner types; use course-specific symbol details |

**Important:** some ER texts reverse where they place cardinalities. In this course, the classic Chen interpretation applies: if `Rack — contains — Pallet` has `(1,4)` next to Rack, each Rack contains 1–4 Pallets. `(1,1)` next to Pallet means each Pallet belongs to one Rack. For n-ary relationships, do not reinterpret these as binary arrow notation.

**Identity:** a *key* is a minimal set of identifying attributes. A *key value* is the value tuple identifying one concrete entity. A weak entity is identified with an owner's key plus a partial key; obligatory participation alone does not make an entity weak.

**Attribute types** have three largely independent classification axes: simple vs composite; single vs multivalued; stored vs derived. Decide based on the stated miniworld, not the attribute's spelling alone.

**Mini-example (not an exercise solution):** `Classroom(room_id [key], capacity)` is a rectangle connected to two ovals; underline `room_id` in the drawing.

**Verification method:** Read every entity and relationship out loud, construct valid and invalid entity instances, check key uniqueness and every min/max, confirm subtype coverage/overlap, and write separate prose for arithmetic, cross-record or time-based constraints that cannot be expressed in Chen.
