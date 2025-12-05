from common import input_ranges, input_values


def fits(range: tuple[int, int], value: int) -> bool:
    start, end = range
    return start <= value <= end


ranges = list(input_ranges())

total = sum(any(fits(range, value) for range in ranges) for value in input_values())

assert total == 635
