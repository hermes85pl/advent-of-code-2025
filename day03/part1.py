from itertools import combinations

from common import input_banks, joltage

total = sum(joltage(max(combinations(bank, 2))) for bank in input_banks())

assert total == 17087
