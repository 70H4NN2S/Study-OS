# EX-0036 — Comparator clinic

**Time:** ~35 min · **Skill:** `PROG-C-FUNCTIONS`

**Task:** Read n (1..10) pairs `id value`; `qsort` pairs by value, tie-break by id; print sorted IDs.

**Cases (stdin → stdout):** `"3 3 7 2 -1 1 7\n"` → `"2 1 3\n"` · `"2 4 0 1 0\n"` → `"1 4\n"`

**Rules:** Comparator must not subtract potentially overflowing integers.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0036`.
