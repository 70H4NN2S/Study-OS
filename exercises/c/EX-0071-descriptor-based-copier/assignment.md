# EX-0071 — Descriptor-based copier

**Time:** ~25 min · **Skill:** `PROG-C-POSIX-FS` · **Platform:** POSIX/Linux

**Task:** Read stdin via POSIX `read` and copy every byte to stdout using `write`.

**Cases (stdin → stdout):** `"hello\n"` → `"hello\n"` · `"xy"` → `"xy"`

**Rules:** Handle short writes and EOF. Do not use `stdio` for data transfer.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0071`.
