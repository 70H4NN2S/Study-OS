# EX-0057 — Undoable text editor

**Time:** ~30 min · **Skill:** `PROG-C-HEAP`

**Task:** Read two words (≤20 chars), treat first as old and second as new. Store heap-owned old copy, print new then restored old.

**Cases (stdin → stdout):** `"hello world\n"` → `"world\nhello\n"` · `"a b\n"` → `"b\na\n"`

**Rules:** Demonstrate one-level undo with no leak.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0057`.
