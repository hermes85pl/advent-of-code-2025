.PHONY: all latest clean help _run FORCE

DAYS ?= day*

all:
	@DAYS="day*" $(MAKE) --no-print-directory _run

day%: FORCE
	@DAYS="$@" $(MAKE) --no-print-directory _run

latest:
	@DAYS=$$(ls -d day* 2>/dev/null | tail -1) $(MAKE) --no-print-directory _run

clean:
	@git clean -dfx

help:
	@echo "Usage: make [day01|day*|DAYS='day01 day02']"
	@echo "  make                    # Run all days (default: day*)"
	@echo "  make day* -j12 -O       # Run many days at once (yolo)"
	@echo "  make day01 day02        # Run specific days"
	@echo "  make DAYS='day01 day02' # Run specific days"
	@echo "  make latest             # Run the most recent day"
	@echo "  make clean              # Remove untracked changes"

_run:
	@for day in $$DAYS; do \
		input_file="$$day/input.txt"; \
		[ ! -f "$$input_file" ] && echo "Missing $$day input" && continue; \
		for part in part1 part2; do \
			script_file="$$day/$$part.py"; \
			[ ! -f "$$script_file" ] && echo "Missing $$day $$part" && continue; \
			echo -n "Running $$day $$part... "; \
			t=$$(bash -c "TIMEFORMAT='%R'; { time python -Bbb '$$script_file' <'$$input_file'; } 2>&1"); \
			exit_code=$$?; \
			echo "$${t}s"; \
			[ $$exit_code -eq 0 ] || exit $$exit_code; \
		done; \
	done

FORCE:
