# EX-0080 — Descriptor leak audit

**Time:** ~25 min · **Skill:** `PROG-C-POSIX-FS` · **Platform:** POSIX/Linux

**Task:** Create a pipe, set `FD_CLOEXEC` on read end with `fcntl`, read back flags and print `1` if bit set.

**Cases (stdin → stdout):** `""` → `"1\n"`

**Rules:** Close both descriptors; no exec needed.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0080`.
