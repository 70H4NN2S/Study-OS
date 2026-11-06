# EX-0082 — POSIX shared-memory scoreboard

**Time:** ~50 min · **Skill:** `PROG-C-IPC` · **Platform:** Linux/POSIX

**Task:** Create uniquely named POSIX shared memory with `shm_open`, map one int, fork child to set it to 7, wait and print the value.

**Cases (stdin → stdout):** `""` → `"7\n"`

**Rules:** Unmap, close and unlink; operate only on your private name.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0082`.
