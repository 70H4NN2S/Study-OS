# EX-0084 — Thread-safe counter

**Time:** ~40 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Start 2 pthreads, each incrementing one shared counter 1000 times under `pthread_mutex_t`; print final value.

**Cases (stdin → stdout):** `""` → `"2000\n"`

**Rules:** Join both threads; no unsynchronized access.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0084`.
