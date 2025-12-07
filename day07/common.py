import sys

START = "S"
SPLITTER = "^"


def input_rows():
    return (list(line.rstrip()) for line in sys.stdin)
