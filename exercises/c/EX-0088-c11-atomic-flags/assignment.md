# EX-0088 — C11 atomic flags

**Time:** ~30 min · **Skill:** `PROG-C-ATOMICS` · **Platform:** Linux/POSIX

**Task:** Create `atomic_int` counter initialized 0. Two pthreads each do 1000 `atomic_fetch_add`; print final count.

**Cases (stdin → stdout):** `""` → `"2000\n"`

**Rules:** Use `<stdatomic.h>`; no mutex for the counter.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0088`.
