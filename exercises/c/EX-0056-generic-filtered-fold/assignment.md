# EX-0056 — Generic filtered fold

**Time:** ~40 min · **Skill:** `PROG-C-GENERIC`

**Task:** Read n (0..8) and n ints; use a callback `int is_positive(const void *)` to sum positive values through an array of `void *` pointers.

**Cases (stdin → stdout):** `"4 -2 5 0 7\n"` → `"12\n"` · `"2 -1 -4\n"` → `"0\n"`

**Rules:** Call through a function pointer; no arithmetic on `void *`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0056`.
