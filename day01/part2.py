from common import VALUE_INIT, VALUE_SPAN, deltas

value = VALUE_INIT

total = 0

for delta in deltas():
    total += (
        abs(delta) + ((VALUE_SPAN - value) % VALUE_SPAN if delta < 0 else value)
    ) // VALUE_SPAN
    value = (value + delta) % VALUE_SPAN

assert total == 5961
