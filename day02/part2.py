from common import input_values


def check(value: int) -> bool:
    r"""return bool(re.fullmatch(r"(.+)\1+", str(value)))"""
    s = str(value)
    s_len = len(s)
    for cut in range(1, s_len // 2 + 1):
        if s_len % cut == 0 and s == s[:cut] * (s_len // cut):
            return True
    return False


total = sum(i for i in input_values() if check(i))

assert total == 26202168557
