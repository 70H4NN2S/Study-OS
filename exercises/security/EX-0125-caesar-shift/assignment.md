# EX-0125 — Caesar encrypt/decrypt

**Time:** ~15 min · **Skill:** `SEC-CRYPTO-CLASSICAL`

**Task:** Implement `encrypt(text: str, shift: int) -> str` and `decrypt(text: str, shift: int) -> str`. Rotate ASCII letters modulo 26; preserve case, spaces, digits and punctuation.

**Cases:** `encrypt("Hello, World!", 3)` → `"Khoor, Zruog!"`; `decrypt("Khoor, Zruog!", 3)` → `"Hello, World!"`; `encrypt("abc", -1)` → `"zab"`.

**Rules:** Pure Python; no external cipher libraries. Any integer shift is valid.

**Submit:** `exercises/security/EX-0125-caesar-shift/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0125`.
