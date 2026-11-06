# EX-0005 — Tiered bandwidth billing

**Time:** ~15 min · **Skill:** `PROG-C-CONTROL`

**Task:** Read nonnegative GiB `n`; print bill in cents: first 10 free, next 40 cost 2 each, remainder 1 each.

**Cases (stdin → stdout):** `"10\n"` → `"0\n"` · `"50\n"` → `"80\n"` · `"55\n"` → `"85\n"`

**Rules:** Whole-number arithmetic only.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0005`.
