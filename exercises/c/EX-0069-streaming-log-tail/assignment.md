# EX-0069 — Streaming log tail

**Time:** ~30 min · **Skill:** `PROG-C-FILES` · **Platform:** C11

**Task:** Read n (1..5) followed by n whitespace-free log words; using a 2-entry ring, print the final min(2,n) entries.

**Cases (stdin → stdout):** `"3 alpha beta gamma"` → `"beta\ngamma\n"` · `"1 only"` → `"only\n"`

**Rules:** Preserve order; use `char[2][21]` and bounded reads.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0069`.
