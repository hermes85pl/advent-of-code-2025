import sys
from math import prod

*presents, regions = sys.stdin.read().split("\n\n")
tile_count_by_present_idx = [p.count("#", 3) for p in presents]


def check_region(region_str: str) -> bool:
    label, *requirements = region_str.split()
    region_area = prod(int(x) for x in label[:-1].split("x"))
    present_count_by_present_idx = (int(x) for x in requirements)
    return region_area >= sum(
        tile_count * present_count
        for tile_count, present_count in zip(
            tile_count_by_present_idx, present_count_by_present_idx
        )
    )


total = sum(check_region(region) for region in regions.splitlines())

assert total == 595
