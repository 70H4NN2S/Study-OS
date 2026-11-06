# EX-0028 — CSV two-field reader

**Time:** ~25 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read one line containing `left,right` (exactly one comma); print the two fields on separate lines.

**Cases (stdin → stdout):** `"red,blue\n"` → `"red\nblue\n"` · `",tail\n"` → `"\ntail\n"`

**Rules:** Fields may be empty; max 100 input bytes; no quoting.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0028`.
