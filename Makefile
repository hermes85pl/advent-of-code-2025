PYTHON ?= $(or $(shell which pypy3), python3)
DAYS ?= $(wildcard day*)

.PHONY: all last $(DAYS) next clean help .run

all: $(DAYS)

last: $(lastword $(DAYS))

$(DAYS):
	@DAY="$@" $(MAKE) -O --no-print-directory .run

next:
	@last_day=$(or $(lastword $(DAYS)), day00); \
	last_num=$$(echo "$$last_day" | grep -o '[0-9]\+'); \
	next_num=$$(printf %02d $$(echo "$$last_num + 1" | bc)); \
	next_day="day$$next_num"; \
	echo -n "Creating $$next_day... " \
	&& mkdir "$$next_day" \
	&& touch "$$next_day/input.txt" \
	&& touch "$$next_day/part1.py" \
	&& touch "$$next_day/part2.py" \
	&& touch "$$next_day/common.py" \
	&& echo "done"

clean:
	@git clean -dfx

help:
	@echo "Usage: make [day01|day*|DAYS='day01 day02']"
	@echo "  make                    # Run all days (default: day*)"
	@echo "  make -j12               # Run many days at once (yolo)"
	@echo "  make last               # Run the most recent day"
	@echo "  make day01 day02        # Run specific days"
	@echo "  make DAYS='day01 day02' # Run specific days"
	@echo "  make next               # Create files for the next day"
	@echo "  make clean              # Remove untracked changes"

.run:
	@input_file="$$DAY/input.txt"; \
	[ ! -f "$$input_file" ] && echo "Missing $$DAY input" && exit; \
	for part in part1 part2; do \
		script_file="$$DAY/$$part.py"; \
		[ ! -f "$$script_file" ] && echo "Missing $$DAY $$part" && continue; \
		echo -n "Running $$DAY $$part... "; \
		t=$$(time -f %e $(PYTHON) -Bbb "$$script_file" <"$$input_file" 2>&1); \
		exit_code=$$?; \
		echo "$${t}s"; \
		[ $$exit_code -eq 0 ] || exit $$exit_code; \
	done
