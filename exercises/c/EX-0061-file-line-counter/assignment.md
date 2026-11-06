# EX-0061 — File line counter

**Time:** ~20 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read all stdin with `fgetc`; print logical line count.

**Cases (stdin → stdout):** `"a\nb\n"` → `"2\n"` · `"a\nb"` → `"2\n"` · `""` → `"0\n"`

**Rules:** A trailing unterminated line counts; an empty stream has 0 lines.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0061`.
