# EX-0079 — Timed child supervisor

**Time:** ~35 min · **Skill:** `PROG-C-PROCESSES` · **Platform:** POSIX/Linux

**Task:** Fork a child blocked on `read` from a pipe; while pipe remains open, parent calls `waitpid(child,&status,WNOHANG)` and prints `running`.

**Cases (stdin → stdout):** `""` → `"running\n"`

**Rules:** Then close write-end to unblock child and wait for it; no sleeps/timeouts.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0079`.
