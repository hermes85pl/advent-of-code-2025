from itertools import combinations

from common import banks, joltage

total = sum(joltage(max(combinations(bank, 2))) for bank in banks())

assert total == 17087
