#!/bin/bash
# Usage: ./new.sh <year> <day> OR ./new.sh for interactive mode

YEAR=$1
CURRENT_YEAR=$(date +%Y)
DAY=$2

if [ -z "$YEAR" ]; then
    read -p "Enter year (default: $CURRENT_YEAR): " YEAR
    YEAR=${YEAR:-$CURRENT_YEAR}
fi

if [ -z "$DAY" ]; then
    read -p "Enter day: " DAY
fi

DIR="src/${YEAR}/d${DAY}"

mkdir -p "$DIR"
cp src/template.py "$DIR/solution.py"
touch "$DIR/input.txt"
touch "$DIR/test-input.txt"
echo "Created directory and files for Year $YEAR, Day $DAY"
