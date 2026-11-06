# EX-0073 — Directory snapshot

**Time:** ~40 min · **Skill:** `PROG-C-POSIX-FS` · **Platform:** POSIX/Linux

**Task:** Create a temporary directory with `mkdtemp`, create two empty files, count entries using `opendir`/`readdir` (excluding `.` and `..`) and print count.

**Cases (stdin → stdout):** `""` → `"2\n"`

**Rules:** Remove both files and directory before exiting; no user-path writes.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0073`.
