#!/usr/bin/env python3
"""Run Advent of Code solutions."""

import argparse
import importlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("--year", type=int, default=2025)
    parser.add_argument("--day", type=int, default=1)
    parser.add_argument("--type", choices=["main", "test"], default="main")
    parser.add_argument("--part", type=int, choices=[1, 2], default=1)
    args = parser.parse_args()

    module_path = f"src.{args.year}.d{args.day}.solution"
    class_name = f"Solution{args.year}D{args.day}"

    try:
        module = importlib.import_module(module_path)
        solution_class = getattr(module, class_name)
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Running {args.year} Day {args.day} Part {args.part} with {args.type}...")
    solution = solution_class()
    file_type = args.type
    
    if args.part == 1:
        solution.run_part_1(file_type)
    else:
        solution.run_part_2(file_type)


if __name__ == "__main__":
    main()

