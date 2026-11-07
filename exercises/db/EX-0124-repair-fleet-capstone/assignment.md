# EX-0124 — Independent exam-style EER challenge

**Time:** ~50 min · **Skill:** `DB-ER-CHEN`

**Task:** A fleet uses Depot(depot_id, address{street,city}) and Vehicle(VIN,type); each Depot has 1..* Vehicles, each Vehicle exactly one Depot. Each Vehicle has 0..* ServiceEvents, numbered only within its Vehicle, with date and labor_minutes. Each event is handled by exactly one Technician(tech_id,name), and each Technician may handle 0..* events. Every technician is exactly one of StaffTechnician(salary_grade) or ContractTechnician(contract_no). Part(part_id,name) can occur in 0..* events and each event uses 0..* parts, with quantity_used per pairing. Draw the Chen EER model and state how positive labor_minutes is enforced.

**Checks:** Demonstrate weak keys, composite address, relationship attributes, min–max, total-disjoint specialization and one residual integrity rule.

**Submit:** diagram/PDF/photo + short note. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
