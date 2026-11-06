# EX-0023 — Case-insensitive frequency

**Time:** ~25 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read a line of ASCII text; count letters ignoring case; print only nonzero counts in a..z order.

**Cases (stdin → stdout):** `"AaB!\n"` → `"a 2\nb 1\n"` · `"zzz\n"` → `"z 3\n"`

**Rules:** Each row is `letter count`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0023`.
