# EX-0091 — poll-based chat relay

**Time:** ~30 min · **Skill:** `PROG-C-IPC` · **Platform:** Linux/POSIX

**Task:** Create a pipe, write one byte, then call `poll` on read end with timeout 0; print `ready` if readable.

**Cases (stdin → stdout):** `""` → `"ready\n"`

**Rules:** Check `POLLIN`; close fds.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0091`.
