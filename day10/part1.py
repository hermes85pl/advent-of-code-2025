from collections import deque

from common import input_machines


def min_presses(indicator: int, buttons: list[int]) -> int | None:
    seen = set()
    queue = deque([(0, 0)])
    while queue:
        state, count = queue.popleft()
        if state not in seen:
            if state == indicator:
                return count
            seen.add(state)
            count += 1
            queue += [(state ^ b, count) for b in buttons]
    return None


total = sum(
    presses
    for indicator, buttons, _ in input_machines()
    if (presses := min_presses(indicator, buttons)) is not None
)

assert total == 425
