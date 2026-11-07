# EX-0122 — Map a small ER model into relations

**Time:** ~30 min · **Skill:** `DB-ERM-MAPPING`

**Task:** Department(dept_id,name) and Employee(emp_id,name,{phone_number}). Each Employee belongs to exactly one Department; each Department has 0..* Employees. A mentor Employee can mentor 0..* Employees; each mentee has 0..1 mentor. Produce relational schemas with PKs, FKs and phone-number representation.

**Checks:** Mention a cardinality constraint that ordinary PK/FK declarations alone do not guarantee.

**Submit:** answer.md. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
