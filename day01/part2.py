from common import VALUE_INIT, VALUE_SPAN, input_deltas

value = VALUE_INIT

total = 0

for delta in input_deltas():
    extra = value if delta >= 0 else ((VALUE_SPAN - value) % VALUE_SPAN)
    total += (abs(delta) + extra) // VALUE_SPAN
    value = (value + delta) % VALUE_SPAN

assert total == 5961
