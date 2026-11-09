# EX-0128 — Vigenère encrypt/decrypt

**Time:** ~25 min · **Skill:** `SEC-CRYPTO-CLASSICAL`

**Task:** Implement `encrypt(text: str, key: str) -> str` and `decrypt(text: str, key: str) -> str`. Repeat the alphabetic keyword over letters only; apply modular shifts.

**Cases:** `encrypt("ATTACKATDAWN", "LEMON")` → `"LXFOPVEFRNHR"`; `encrypt("HELLO WORLD", "KEY")` → `"RIJVS UYVJN"`.

**Rules:** ASCII letters only; preserve letter case and non-letters. Punctuation does not advance the key. Assume nonempty alphabetic key.

**Submit:** `exercises/security/EX-0128-vigenere-cipher/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0128`.
