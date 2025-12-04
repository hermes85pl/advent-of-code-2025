from common import LIMIT, PAPER, Grid, input_raw_grid

grid = Grid(input_raw_grid())

total = sum(
    grid[pos] == PAPER and grid.neighbor_count(pos, PAPER) < LIMIT for pos in grid
)

assert total == 1320
