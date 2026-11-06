# EX-0076 — Exec argument runner

**Time:** ~35 min · **Skill:** `PROG-C-PROCESSES` · **Platform:** POSIX/Linux

**Task:** Read token `true` or `false`; fork and `execl` matching `/bin/true` or `/bin/false`; parent prints exit code.

**Cases (stdin → stdout):** `"true\n"` → `"0\n"` · `"false\n"` → `"1\n"`

**Rules:** Check fork, exec and wait errors; never invoke a shell.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0076`.
