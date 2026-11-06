# EX-0062 — Arbitrarily long line reader

**Time:** ~25 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read stdin with repeated `fgets` (buffer 8 bytes); count total input bytes excluding any `\n`.

**Cases (stdin → stdout):** `"abcdefghijkl\n"` → `"12\n"` · `"hi"` → `"2\n"`

**Rules:** A long line must not be truncated; stop at EOF.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0062`.
