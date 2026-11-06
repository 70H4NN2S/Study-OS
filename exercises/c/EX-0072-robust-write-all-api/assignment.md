# EX-0072 — Robust write-all API

**Time:** ~30 min · **Skill:** `PROG-C-POSIX-FS` · **Platform:** POSIX/Linux

**Task:** Write `write_all(fd,buf,n)` that loops over writes of at most 2 bytes. Read ≤20 bytes from stdin and echo to stdout.

**Cases (stdin → stdout):** `"abcde"` → `"abcde"` · `"X"` → `"X"`

**Rules:** Handle partial writes and EINTR; preserve exact bytes.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0072`.
