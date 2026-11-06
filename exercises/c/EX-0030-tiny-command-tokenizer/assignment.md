# EX-0030 — Tiny command tokenizer

**Time:** ~30 min · **Skill:** `PROG-C-STRINGS`

**Task:** Read one ASCII line with words separated by spaces/tabs; print one token per line.

**Cases (stdin → stdout):** `"a  b\tc\n"` → `"a\nb\nc\n"` · `"  hello  \n"` → `"hello\n"`

**Rules:** Max 10 tokens, each ≤20 chars; no quotes or escapes.

**Submit:** `src/main.c`. Check: `python3 tools/check_c.py EX-0030`.
