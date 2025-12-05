from common import input_ranges

ranges = sorted(input_ranges())

total = 0
limit = 0

for start, end in ranges:
    if (start := max(limit, start)) <= end:
        total += end - start + 1
        limit = max(limit, end) + 1

assert total == 369761800782619
