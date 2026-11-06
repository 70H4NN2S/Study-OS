# EX-0040 — Undefined behavior audit

**Time:** ~20 min · **Skill:** `PROG-C-SECURITY`

**Task:** Read one word (≤20 chars); copy it into a second 21-byte array safely and print it.

**Cases (stdin → stdout):** `"safe\n"` → `"safe\n"` · `"C11\n"` → `"C11\n"`

**Rules:** Use bounded input plus `memcpy`/`strcpy` only after proving sizes; no UB examples executed.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0040`.
