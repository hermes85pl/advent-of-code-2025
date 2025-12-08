import sys

START = "S"
SPLITTER = "^"


def input_rows():
    for line in sys.stdin:
        yield line.rstrip()
