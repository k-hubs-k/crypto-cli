# CryptoCLI

A small Python CLI tool to encrypt and decrypt files using AES via [pyAESCrypt](https://pypi.org/project/pyAesCrypt/).
Designed as a proper Unix-style utility:

- Explicit exit codes
- Clear error messages
- Script / CI friendly
- Supports large files with a real progress bar

# Features

- AES file encryption
- AES file decryption
- Real progress bar (large files supported)
- Standardized exit codes
- Verbose mode with full stack trace
- Clean handling of Ctrl+C

# Requirements

- Python 3.9+ recommended
- Dependencies:

```bash
pip install pyAesCrypt tqdm
```

# Usage

## Encrypt a file

```bash
python crypto.py \
--encrypt \
--input file.txt \
--output file.txt.aes \
--password "very_secure_password"
```

## Decrypt a file

```bash
python crypto.py \
--decrypt \
--input file.txt.aes \
--output file.txt \
--password "very_secure_password"
```

## Verbose mode

```bash
python crypto.py --decrypt ... --verbose
```

# Password rules

- Minimum 10 characters
- The same password must be used for encryption and decryption

# Progress bar

- The progress bar is accurate and reliable, even for multi‑gigabyte files.
- Chunk-based streaming
- Low memory usage
- Shows size, speed, and ETA

# Exit codes

| Code | Meaning                           |
| ---- | --------------------------------- |
| 0    | Success                           |
| 1    | Unknown error                     |
| 2    | Invalid arguments                 |
| 10   | File not found                    |
| 11   | Permission denied                 |
| 12   | Invalid password / corrupted file |
| 130  | Cancelled by user (Ctrl+C)        |

> [!NOTE]
>
> - Avoid overwriting existing files without a backup
> - This project is intended for personal / educational use. Make sure you understand the security implications before using it for critical data.

# License

Free to use. Encrypt responsibly
