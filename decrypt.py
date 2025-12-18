import sys
import pyAesCrypt
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--input", required=True, help="Input file path")
parser.add_argument("--output", required=True, help="Output file path")
parser.add_argument("--password", required=True, help="Decryption password")

args = parser.parse_args()

input_path = args.input
output_path = args.output
password = args.password


if len(password) < 10:
    parser.error("The password must contain at least 10 characters")

try:
    pyAesCrypt.decryptFile(input_path, output_path, password)
    print("File decrypted succesfully")
except FileNotFoundError as e:
    print(f"File not found: {e}")
    sys.exit(1)
except PermissionError as e:
    print(f"Permission error : {e}")
    sys.exit(1)
except Exception as e:
    print(f"Decryption failed {type(e).__name__}: {e}")

    # NOTE: Uncomment while debugging
    # traceback.print_exc()
    sys.exit(1)
