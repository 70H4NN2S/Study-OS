# EX-0041 — Allocation failure discipline

**Time:** ~20 min · **Skill:** `PROG-C-HEAP`

**Task:** Read n (0..20); allocate n `int` using `calloc`, fill with values 1..n and print their sum.

**Cases (stdin → stdout):** `"3\n"` → `"6\n"` · `"0\n"` → `"0\n"`

**Rules:** Check allocation failures, free once, and treat n=0 as sum 0.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0041`.
