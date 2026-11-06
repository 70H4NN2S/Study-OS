# EX-0078 — Two-stage pipeline

**Time:** ~50 min · **Skill:** `PROG-C-IPC` · **Platform:** POSIX/Linux

**Task:** Connect two child processes with pipes: child 1 sends integer 5 as ASCII, child 2 doubles it and sends result back to parent; parent prints 10.

**Cases (stdin → stdout):** `""` → `"10\n"`

**Rules:** Two pipes, two children, no shell; close unused fds and reap both.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0078`.
