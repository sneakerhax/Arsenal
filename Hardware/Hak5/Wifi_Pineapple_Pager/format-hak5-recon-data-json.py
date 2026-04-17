import json
import sys

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    data = json.load(f)

with open(filename, 'w') as f:
    json.dump(data, f, indent=2)

print(f"Formatted: {filename}")
