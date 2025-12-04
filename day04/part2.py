from common import LIMIT, PAPER, WHERE_PAPER_USED_TO_BE, Grid, input_raw_grid

grid = Grid(input_raw_grid())


def process() -> int:
    count = 0
    for pos in grid:
        if grid[pos] == PAPER and grid.neighbor_count(pos, PAPER) < LIMIT:
            grid[pos] = WHERE_PAPER_USED_TO_BE
            count += 1
    return count


total = sum(iter(process, 0))

assert total == 8354
