# EX-0053 — Build-time feature switches

**Time:** ~20 min · **Skill:** `PROG-C-PREPROCESSOR`

**Task:** Read one int and print its double; add `#if TRACE` branch printing `trace` to stderr when built with `-DTRACE=1`.

**Cases (stdin → stdout):** `"5\n"` → `"10\n"` · `"-4\n"` → `"-8\n"`

**Rules:** Stdout identical with TRACE on/off; default TRACE=0.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0053`.
