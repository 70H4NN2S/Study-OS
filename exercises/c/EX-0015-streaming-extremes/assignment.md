# EX-0015 — Streaming extremes

**Time:** ~15 min · **Skill:** `PROG-C-ARRAYS`

**Task:** Read `n` (1..20), then n integers; print `min max average` with two decimal places.

**Cases (stdin → stdout):** `"4 1 9 -2 0\n"` → `"-2 9 2.00\n"` · `"1 -8\n"` → `"-8 -8 -8.00\n"`

**Rules:** Accumulate with a suitable type; count only supplied values.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0015`.
