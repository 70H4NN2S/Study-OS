# EX-0047 — Ownership graph challenge

**Time:** ~30 min · **Skill:** `PROG-C-HEAP`

**Task:** Create a heap-allocated `struct node {int value; struct node *child;}` with root and one child from two input integers. Print their sum; free both.

**Cases (stdin → stdout):** `"2 9\n"` → `"11\n"` · `"-3 1\n"` → `"-2\n"`

**Rules:** Each object has exactly one owner; check both allocations.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0047`.
