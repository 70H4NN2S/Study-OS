# EX-0083 — Semaphore gate

**Time:** ~30 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Initialize unnamed semaphore with count 2; wait twice, show third `sem_trywait` fails by printing `full`; post once, then successful try prints `ok`.

**Cases (stdin → stdout):** `""` → `"full\nok\n"`

**Rules:** Linux only. Destroy semaphore before exit.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0083`.
