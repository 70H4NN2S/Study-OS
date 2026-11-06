# EX-0006 — Cross-midnight timer

**Time:** ~15 min · **Skill:** `PROG-C-CONTROL`

**Task:** Read `start_hour start_min end_hour end_min`; print elapsed minutes.

**Cases (stdin → stdout):** `"23 50 0 10\n"` → `"20\n"` · `"9 0 9 0\n"` → `"0\n"`

**Rules:** Valid 24-hour times; if end precedes start, cross midnight; equal times = 0.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0006`.
