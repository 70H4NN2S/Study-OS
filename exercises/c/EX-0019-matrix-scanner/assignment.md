# EX-0019 — Matrix scanner

**Time:** ~25 min · **Skill:** `PROG-C-ARRAYS`

**Task:** Read rows r, columns c (1..5), then r*c integers; print row sums on one line.

**Cases (stdin → stdout):** `"2 3 1 2 3 4 5 6\n"` → `"6 15\n"` · `"1 2 -1 8\n"` → `"7\n"`

**Rules:** Iterate in row-major order; space-separated sums.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0019`.
