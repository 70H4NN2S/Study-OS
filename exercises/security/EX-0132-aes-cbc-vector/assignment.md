# EX-0132 — AES-CBC chaining and IV

**Time:** ~30 min · **Skill:** `SEC-CRYPTO-BLOCK`

**Task:** Using PyCryptodome, implement `encrypt_cbc_hex(key_hex: str, iv_hex: str, plaintext_hex: str) -> str`. Encrypt complete 16-byte blocks with AES-CBC.

**Cases:** Use the NIST AES-CBC vector provided in `tests/public_cases.json`; the output must match exactly.

**Rules:** Key and IV are 16 bytes; no padding needed for these vectors. Explain why CBC needs a fresh unpredictable IV for encryption; CBC alone does not authenticate data.

**Submit:** `exercises/security/EX-0132-aes-cbc-vector/src/main.py` (one file). Check: `python3 tools/check_crypto.py EX-0132`.
