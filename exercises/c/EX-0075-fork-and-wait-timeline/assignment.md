# EX-0075 — Fork and wait timeline

**Time:** ~25 min · **Skill:** `PROG-C-PROCESSES` · **Platform:** POSIX/Linux

**Task:** Fork one child that calls `_exit(7)`; parent calls `waitpid` and prints the child's exit code.

**Cases (stdin → stdout):** `""` → `"7\n"`

**Rules:** Only parent prints; check `WIFEXITED`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0075`.
