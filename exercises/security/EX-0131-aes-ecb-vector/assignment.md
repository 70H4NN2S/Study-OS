# EX-0131 — AES-ECB known-answer tests

**Time:** ~25 min · **Skill:** `SEC-CRYPTO-BLOCK`

**Task:** Using PyCryptodome, implement `encrypt_ecb_hex(key_hex: str, plaintext_hex: str) -> str`. Encrypt full 16-byte AES blocks without padding.

**Cases:** AES-128 key `000102030405060708090a0b0c0d0e0f` and block `00112233445566778899aabbccddeeff` → `69c4e0d86a7b0430d8cdb78070b4c55a`.

**Rules:** Use AES from a library, not homemade AES. 16-byte key and full blocks in all cases. Explain to the reviewer why identical plaintext blocks expose patterns.

**Submit:** `exercises/security/EX-0131-aes-ecb-vector/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0131`.
