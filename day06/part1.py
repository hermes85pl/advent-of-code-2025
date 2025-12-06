import sys

from common import OPERATORS, NumberGroup, OperatorFunction

number_groups: list[NumberGroup] = []
operators: list[OperatorFunction] = []
for line in sys.stdin:
    elements = line.split()
    try:
        number_groups.append(list(int(x) for x in elements))
    except ValueError:
        operators.extend(OPERATORS[x] for x in elements)
        break

numbers = number_groups[0]

for i in range(1, len(number_groups)):
    next_numbers = number_groups[i]
    for j in range(len(next_numbers)):
        numbers[j] = operators[j](numbers[j], next_numbers[j])

total = sum(numbers)

assert total == 6725216329103
