# EX-0095 — Memory mapping explorer

**Time:** ~35 min · **Skill:** `PROG-C-MEMORY-MODEL` · **Platform:** Linux/POSIX

**Task:** Open `/dev/zero`, map one writable private page with `mmap`, store `A`, print it, then `munmap`.

**Cases (stdin → stdout):** `""` → `"A\n"`

**Rules:** Linux/POSIX; map 4096 bytes and check MAP_FAILED; close fd.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0095`.
