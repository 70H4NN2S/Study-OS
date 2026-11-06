# EX-0044 — Amortized growth experiment

**Time:** ~20 min · **Skill:** `PROG-C-PERFORMANCE`

**Task:** Read n (0..100); compute capacity after appending n items to a vector starting capacity 1 and doubling only when full.

**Cases (stdin → stdout):** `"0\n"` → `"1\n"` · `"5\n"` → `"8\n"` · `"16\n"` → `"16\n"`

**Rules:** Print final capacity. No allocation required for this model.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0044`.
