# EX-0077 — Parent-child result pipe

**Time:** ~35 min · **Skill:** `PROG-C-IPC` · **Platform:** POSIX/Linux

**Task:** Create one pipe; child writes `42`, parent reads and prints `42`, then waits for child.

**Cases (stdin → stdout):** `""` → `"42\n"`

**Rules:** Close unused ends to reach EOF; child does not print.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0077`.
