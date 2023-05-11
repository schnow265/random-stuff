import hashlib
import argparse

# Create argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-hash", help="Hash algorithm to use", choices=["md5", "sha1", "sha256"])
parser.add_argument("-file", help="File to hash")
args = parser.parse_args()

# Read file content
with open(args.file, "rb") as f:
    data = f.read()

# Compute hash
if args.hash == "md5":
    hash_value = hashlib.md5(data).hexdigest()
elif args.hash == "sha1":
    hash_value = hashlib.sha1(data).hexdigest()
elif args.hash == "sha256":
    hash_value = hashlib.sha256(data).hexdigest()
else:
    print("Unsupported hash algorithm")
    exit()

# Print hash value
print(hash_value)
