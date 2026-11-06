# EX-0087 — Read-mostly cache

**Time:** ~30 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Store one int behind `pthread_rwlock_t`. Writer thread changes 1 to 9; join writer; reader thread reads and prints it.

**Cases (stdin → stdout):** `""` → `"9\n"`

**Rules:** Use write lock for update and read lock for read; destroy lock.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0087`.
