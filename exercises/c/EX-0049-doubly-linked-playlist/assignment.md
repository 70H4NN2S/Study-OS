# EX-0049 — Doubly linked playlist

**Time:** ~45 min · **Skill:** `PROG-C-LISTS`

**Task:** Read three integers, allocate three doubly linked nodes, link in input order, and print values from tail to head.

**Cases (stdin → stdout):** `"1 2 3\n"` → `"3 2 1\n"` · `"5 5 7\n"` → `"7 5 5\n"`

**Rules:** Use `prev` and `next`; free nodes after traversal.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0049`.
