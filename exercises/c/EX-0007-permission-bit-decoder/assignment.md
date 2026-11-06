# EX-0007 — Permission bit decoder

**Time:** ~10 min · **Skill:** `PROG-C-TYPES`

**Task:** Read integer 0..7; print the 3-character `rwx` mask with `-` for missing permissions.

**Cases (stdin → stdout):** `"5\n"` → `"r-x\n"` · `"0\n"` → `"---\n"`

**Rules:** Use bitwise `&`, not a lookup table.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0007`.
