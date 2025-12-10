import sys


def parse_indicator(s: str) -> int:
    return int(s[-2:0:-1].replace("#", "1").replace(".", "0"), 2)


def parse_button(s: str) -> int:
    mask = 0
    for idx in s[1:-1].split(","):
        mask |= 1 << int(idx)
    return mask


def parse_joltage(s: str) -> list[int]:
    return [int(x) for x in s[1:-1].split(",")]


def input_machines():
    for line in sys.stdin:
        parts = line.split()
        indicator = parse_indicator(parts[0])
        buttons = [parse_button(s) for s in parts[1:-1]]
        joltage = parse_joltage(parts[-1])
        yield indicator, buttons, joltage
