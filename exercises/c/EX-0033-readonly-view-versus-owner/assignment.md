# EX-0033 — Readonly view versus owner

**Time:** ~20 min · **Skill:** `PROG-C-POINTERS`

**Task:** Implement `long sum(const int *a,size_t n)`; read n (0..20) and n integers, print sum.

**Cases (stdin → stdout):** `"3 1 -3 10\n"` → `"8\n"` · `"0\n"` → `"0\n"`

**Rules:** Never modify the array; n=0 yields 0.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0033`.
