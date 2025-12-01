#!/usr/bin/env bash

set -eu -o pipefail

TIMEFORMAT='%R'
DAYS=${1:-day*}
FAILURERET=${2:-}

rundaypart() {
    local dir=$1
    local part=$2
    local input_file=$3
    local script_file=$dir/$part.py

    if [ -f "$script_file" ]; then
        echo -n "Running $dir $part... "
        local t
        t=$({
            time python -Bbb "$script_file" <"$input_file" || return "${FAILURERET:-$?}"
        } 2>&1)
        echo "${t}s"
    else
        echo "Missing $dir $part"
    fi
}

runday() {
    local dir=$1
    local input_file=$dir/input.txt

    if [ ! -f "$input_file" ]; then
        echo "Missing $dir input"
        return
    fi

    rundaypart "$dir" part1 "$input_file"
    rundaypart "$dir" part2 "$input_file"
}

for day in $DAYS; do
    runday "$day"
done
