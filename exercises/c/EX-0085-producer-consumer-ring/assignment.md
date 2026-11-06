# EX-0085 — Producer-consumer ring

**Time:** ~50 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Use one producer thread, one consumer thread, mutex and condition variable to transfer the integer 5 through a 1-slot buffer.

**Cases (stdin → stdout):** `""` → `"5\n"`

**Rules:** Consumer prints only after receiving; signal/broadcast under correct locking.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0085`.
