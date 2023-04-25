import sys
from utils.direct_construction import direct_construction

TEST_FILE = sys.argv[1] if (len(sys.argv) > 1) else "./tests/slr-1-test.txt"
FILE_STRING = ""

with open(TEST_FILE, "r", newline="") as file:
    for line in file:
        for char in line:
            FILE_STRING += char

print(FILE_STRING)
