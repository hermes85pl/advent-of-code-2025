from common import banks, joltage


def best_cells(bank: list[int], size: int) -> list[int]:
    cells = bank[-size:]
    for cell in reversed(bank[:-size]):
        if cell < cells[0]:
            continue
        cells.insert(0, cell)
        for i in range(1, len(cells) - 1):
            if cells[i] < cells[i + 1]:
                del cells[i]
                break
        else:
            del cells[-1]
    return cells


total = sum(joltage(best_cells(bank, 12)) for bank in banks())

assert total == 169019504359949
