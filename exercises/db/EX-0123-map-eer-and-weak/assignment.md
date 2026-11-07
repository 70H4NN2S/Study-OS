# EX-0123 — Map EER specialization and weak identity

**Time:** ~35 min · **Skill:** `DB-ERM-MAPPING`

**Task:** Project(project_id,title) has 0..* weak Tasks(task_no unique only inside Project, description). Person(person_id,name) is specialized totally and disjointly into Student(major) and Instructor(office). Produce one valid relational mapping with keys and FKs.

**Checks:** Explain composite task identification and subtype constraints not enforced solely by PKs/FKs.

**Submit:** answer.md. Send a clear photo/export in chat, or commit it in this exercise's `submission/` folder and link the exact GitHub commit/PR. See [track rules](../README.md); no mandatory reflection.
