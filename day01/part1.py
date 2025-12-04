from common import VALUE_INIT, VALUE_SPAN, input_deltas

value = VALUE_INIT

total = sum((value := (value + delta) % VALUE_SPAN) == 0 for delta in input_deltas())

assert total == 980
