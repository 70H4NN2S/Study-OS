# EX-0054 — Macro side-effect trap

**Time:** ~20 min · **Skill:** `PROG-C-PREPROCESSOR`

**Task:** Define `SQUARE(x)` with correctly parenthesized argument/expression. Read a and b, print `SQUARE(a+b)`.

**Cases (stdin → stdout):** `"1 2\n"` → `"9\n"` · `"-2 3\n"` → `"1\n"`

**Rules:** Use a and b without side effects; explain macro expansion in a source comment.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0054`.
