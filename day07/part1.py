from common import SPLITTER, START, input_rows

rows = input_rows()

total = 0

x_set = {next(rows).index(START)}
for row in rows:
    new_x_set = set()
    for x in x_set:
        if row[x] != SPLITTER:
            new_x_set.add(x)
        else:
            new_x_set.update((x - 1, x + 1))
            total += 1
    x_set = new_x_set

assert total == 1613
