import sys

from common import OPERATORS, NumberGroup, OperatorFunction, grand_total

number_groups: list[NumberGroup] = []
operators: list[OperatorFunction] = []
for line in sys.stdin:
    elements = line.split()
    try:
        for i in range(len(elements)):
            try:
                numbers = number_groups[i]
            except IndexError:
                numbers = []
                number_groups.append(numbers)
            numbers.append(int(elements[i]))
    except ValueError:
        operators.extend(OPERATORS[x] for x in elements)
        break

total = grand_total(operators, number_groups)

assert total == 6725216329103
