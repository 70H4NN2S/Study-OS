# EX-0067 — Bytewise file comparator

**Time:** ~35 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read two whitespace-free words, write each to a separate `tmpfile()`, rewind and compare their contents bytewise.

**Cases (stdin → stdout):** `"hello hello"` → `"same\n"` · `"abc abd"` → `"different\n"`

**Rules:** Print `same` or `different`; close both files.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0067`.
