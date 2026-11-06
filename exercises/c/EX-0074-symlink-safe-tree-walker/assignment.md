# EX-0074 — Symlink-safe tree walker

**Time:** ~45 min · **Skill:** `PROG-C-POSIX-FS` · **Platform:** POSIX/Linux

**Task:** In your private temp directory create a file and symlink to it; use `lstat` on the symlink and print `link`.

**Cases (stdin → stdout):** `""` → `"link\n"`

**Rules:** Never follow the symlink; clean up both entries and directory.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0074`.
