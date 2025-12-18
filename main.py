import pyAesCrypt
import argparse
import sys

EXIT_OK = 0
EXIT_INVALID_ARGS = 2
EXIT_FILE_NOT_FOUND = 10
EXIT_PERMISSION = 11
EXIT_INVALID_PASSWORD = 12
EXIT_UNKNOWN = 1
EXIT_CANCELLED = 130

parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using AES")

parser.add_argument("--input", required=True, help="Input file path")
parser.add_argument("--output", required=True, help="Output file path")
parser.add_argument("--password", required=True, help="Encryption password")
parser.add_argument("--verbose", action="store_true", help="Show full traceback")

mode = parser.add_mutually_exclusive_group(required=True)
mode.add_argument("--encrypt", action="store_true", help="Encrypt the file")
mode.add_argument("--decrypt", action="store_true", help="Decrypt the file")

args = parser.parse_args()

if len(args.password) < 10:
    parser.error("The password must contain at least 10 characters")

try:
    if args.encrypt:
        print("Encrypting...")
        pyAesCrypt.encryptFile(args.input, args.output, args.password)
        print("File encrypted successfully.")
    else:
        print("Decrypting...")
        pyAesCrypt.decryptFile(args.input, args.output, args.password)
        print("File decrypted successfully")
    sys.exit(EXIT_OK)

except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(EXIT_FILE_NOT_FOUND)

except PermissionError as e:
    print(f"Permission error: {e}")
    sys.exit(EXIT_PERMISSION)

except ValueError as e:
    print(f"Invalid password or corrupted encrypted file: {e}")
    sys.exit(EXIT_INVALID_PASSWORD)

except KeyboardInterrupt:
    print("\nOperation cancelled by user.")
    sys.exit(EXIT_CANCELLED)

except Exception as e:
    print(f"Operation failed ({type(e).__name__}): {e}")

    if args.verbose:
        import traceback

        traceback.print_exc()

sys.exit(EXIT_UNKNOWN)
