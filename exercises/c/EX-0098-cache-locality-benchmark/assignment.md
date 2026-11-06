# EX-0098 — Cache locality benchmark

**Time:** ~20 min · **Skill:** `PROG-C-PERFORMANCE` · **Platform:** Linux/POSIX

**Task:** Read 6 ints as a 2×3 matrix; compute sum once row-major and once column-major; print `equal` if results match.

**Cases (stdin → stdout):** `"1 2 3 4 5 6\n"` → `"equal\n"` · `"0 0 0 0 0 0\n"` → `"equal\n"`

**Rules:** Print no timing claims; in a source comment explain which traversal has better locality.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0098`.
