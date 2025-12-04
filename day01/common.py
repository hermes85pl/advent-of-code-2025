import re
import sys

VALUE_INIT = 50
VALUE_SPAN = 100

PATTERN = re.compile(r"^([LR])(\d+)\n$")


def input_deltas():
    for line in sys.stdin:
        match = next(PATTERN.finditer(line))
        yield int(match[2]) if match[1] == "R" else -int(match[2])
