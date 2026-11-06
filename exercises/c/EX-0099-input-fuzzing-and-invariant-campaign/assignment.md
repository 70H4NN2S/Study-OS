# EX-0099 — Input fuzzing and invariant campaign

**Time:** ~25 min · **Skill:** `PROG-C-SECURITY` · **Platform:** Linux/POSIX

**Task:** Using a fixed seed, generate 1000 `uint32_t` values with a simple LCG; verify `((x ^ 0xA5A5A5A5u) ^ 0xA5A5A5A5u)==x`; print `1000 ok` if every check passes.

**Cases (stdin → stdout):** `""` → `"1000 ok\n"`

**Rules:** Use unsigned arithmetic; no external fuzzing framework.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0099`.
