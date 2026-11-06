# EX-0051 — Multi-file library boundary

**Time:** ~35 min · **Skill:** `PROG-C-TOOLCHAIN`

**Task:** Move `int add(int,int)` into `src/math.c`, declare it in `include/math.h`, and call it from `src/main.c` reading two ints.

**Cases (stdin → stdout):** `"2 3\n"` → `"5\n"` · `"-4 8\n"` → `"4\n"`

**Rules:** Use an include guard; do not include `.c` files.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0051`.
