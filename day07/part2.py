from common import SPLITTER, START, input_rows

rows = input_rows()

total = 0

x_to_t_map = {next(rows).index(START): 1}
for row in rows:
    new_x_to_t_map: dict[int, int] = {}
    for x, t in x_to_t_map.items():
        for x in (x,) if row[x] != SPLITTER else (x - 1, x + 1):
            new_x_to_t_map[x] = new_x_to_t_map.get(x, 0) + t
    x_to_t_map = new_x_to_t_map

total = sum(x_to_t_map.values())

assert total == 48021610271997
