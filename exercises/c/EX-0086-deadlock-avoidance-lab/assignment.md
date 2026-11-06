# EX-0086 — Deadlock avoidance lab

**Time:** ~45 min · **Skill:** `PROG-C-CONCURRENCY` · **Platform:** Linux/POSIX

**Task:** Create two balances initialized 10 each. Run two threads transferring 3 in opposite directions; lock two mutexes consistently by account index. Print final total.

**Cases (stdin → stdout):** `""` → `"20\n"`

**Rules:** Join both; same lock order everywhere.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0086`.
