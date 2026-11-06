# EX-0052 — Make rebuild rules

**Time:** ~40 min · **Skill:** `PROG-C-TOOLCHAIN`

**Task:** Using `src/main.c` (and an optional helper), create a `Makefile` with `all`, `clean`, `test`; program reads an int and prints its square.

**Cases (stdin → stdout):** `"3\n"` → `"9\n"` · `"-2\n"` → `"4\n"`

**Rules:** `make` builds; `make test` runs a supplied example; use C11 warnings. Submit Makefile too.

**Submit:** `src/main.c` and `Makefile`. Check: `python3 tools/check_c.py EX-0052`.
