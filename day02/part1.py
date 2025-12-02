from common import values


def check(value: int) -> bool:
    s = str(value)
    if len(s) % 2 != 0:
        return False
    p = len(s) // 2
    a, b = s[:p], s[p:]
    return a == b


total = sum(i for i in values() if check(i))

assert total == 18893502033
