# EX-0096 — Checksummed event journal

**Time:** ~20 min · **Skill:** `PROG-C-TYPES` · **Platform:** Linux/POSIX

**Task:** Read a word ≤20 ASCII bytes; sum its unsigned byte values modulo 256 and print the checksum.

**Cases (stdin → stdout):** `"ABC\n"` → `"198\n"` · `"hello\n"` → `"20\n"`

**Rules:** This is an error-detection exercise, not a cryptographic hash.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0096`.
