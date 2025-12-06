import sys

from common import OPERATORS, NumberGroup, grand_total

lines = [line.rstrip() for line in sys.stdin]

operators = [OPERATORS[x] for x in lines[-1].split()]
del lines[-1]

number_groups: list[NumberGroup] = []
numbers: NumberGroup = []
column_count = max(len(line) for line in lines)
for i in range(column_count):
    try:
        number = int("".join(line[i] for line in lines if i < len(line)))
    except ValueError:
        number_groups.append(numbers)
        numbers = []
    else:
        numbers.append(number)
number_groups.append(numbers)

total = grand_total(operators, number_groups)

assert total == 10600728112865
