# EX-0100 — Capstone: local telemetry service

**Time:** ~55 min · **Skill:** `PROG-C-DESIGN` · **Platform:** Linux/POSIX

**Task:** Read n (0..8) `(id,value)` pairs, IDs 0..2; store them in a malloc-allocated array of structs, `qsort` by id, and print sums for IDs 0,1,2.

**Cases (stdin → stdout):** `"4 0 5 2 -1 0 3 1 7\n"` → `"0:8 1:7 2:-1\n"` · `"0\n"` → `"0:0 1:0 2:0\n"`

**Rules:** Implement comparator callback and cleanup; output `0:x 1:y 2:z`.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0100`.
