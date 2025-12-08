from common import input_values


def check(value: int) -> bool:
    s = str(value)
    s_len = len(s)
    if s_len % 2 != 0:
        return False
    p = s_len // 2
    return s[:p] == s[p:]


total = sum(i for i in input_values() if check(i))

assert total == 18893502033
