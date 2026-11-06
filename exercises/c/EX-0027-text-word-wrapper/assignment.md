# EX-0027 — Text word wrapper

**Time:** ~25 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read width (4..20) followed by two words; print both on one line if `len1+1+len2<=width`, otherwise one word per line.

**Cases (stdin → stdout):** `"8 one two\n"` → `"one two\n"` · `"5 hello a\n"` → `"hello\na\n"`

**Rules:** No word is longer than width; use `strlen`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0027`.
