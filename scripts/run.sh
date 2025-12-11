#!/bin/bash
# Usage: ./run.sh [year] [day] [type] [part]
# Defaults: year=2025, day=1, type=main, part=1

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
YEAR=${1:-2025}
DAY=${2:-1}
TYPE=${3:-main}
PART=${4:-1}

# Interactive mode
if [ $# -eq 0 ]; then
    read -p "Enter year (default: 2025): " input_year
    YEAR=${input_year:-2025}
    
    read -p "Enter day (default: 1): " input_day
    DAY=${input_day:-1}
    
    read -p "Enter input type - main/test (default: main): " input_type
    TYPE=${input_type:-main}

    read -p "Enter part - 1/2 (default: 1): " input_part
    PART=${input_part:-1}
fi

cd "$PROJECT_ROOT"
python scripts/run.py --year "$YEAR" --day "$DAY" --type "$TYPE" --part "$PART"
