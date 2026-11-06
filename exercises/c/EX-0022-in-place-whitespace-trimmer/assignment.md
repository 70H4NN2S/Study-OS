# EX-0022 — In-place whitespace trimmer

**Time:** ~20 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read a line; remove leading/trailing ASCII spaces and tabs, then print it.

**Cases (stdin → stdout):** `"  C is fun  \n"` → `"C is fun\n"` · `"   \n"` → `"\n"`

**Rules:** Modify a `char[]` in place; preserve spaces inside.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0022`.
