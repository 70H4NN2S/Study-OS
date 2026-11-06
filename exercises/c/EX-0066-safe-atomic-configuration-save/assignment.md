# EX-0066 — Safe atomic configuration save

**Time:** ~30 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read a word; write it to a `tmpfile()` using `fputs`, rewind, read back and print it.

**Cases (stdin → stdout):** `"mode"` → `"mode\n"` · `"safe"` → `"safe\n"`

**Rules:** Check stream errors and close the temporary stream; do not touch real configuration files.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0066`.
