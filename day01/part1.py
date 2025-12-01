from common import VALUE_INIT, VALUE_SPAN, deltas

value = VALUE_INIT

total = sum(1 for delta in deltas() if (value := (value + delta) % VALUE_SPAN) == 0)

assert total == 980
