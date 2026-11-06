# EX-0097 — Small worker thread pool

**Time:** ~40 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Read two ints a,b (-100..100); run one pthread per number to compute its square, join, and print sum of both squares.

**Cases (stdin → stdout):** `"3 4\n"` → `"25\n"` · `"-2 5\n"` → `"29\n"`

**Rules:** Pass each thread separate argument/result storage.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0097`.
