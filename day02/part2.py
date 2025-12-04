from common import input_values


def check(value: int) -> bool:
    r"""return bool(re.fullmatch(r"(.+)\1+", str(value)))"""
    s = str(value)
    for cut in range(1, len(s) // 2 + 1):
        if len(s) % cut == 0 and s == s[:cut] * (len(s) // cut):
            return True
    return False


total = sum(i for i in input_values() if check(i))

assert total == 26202168557
