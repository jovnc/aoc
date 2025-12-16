from typing import List, Tuple
from src.solution import Solution


class Solution2025D5(Solution):
    def parse_data(self, contents: str) -> Tuple[List[Tuple[int, int]], List[int]]:
        """Parse the input data into a usable format."""
        fresh_range = []
        ingredients = []
        for line in contents.splitlines():
            if "-" in line:
                start, end = map(int, line.split("-"))
                fresh_range.append((start, end))
            elif line:
                ingredients.append(int(line))

        return fresh_range, ingredients

    def solve_part_1(self, data: Tuple[List[Tuple[int, int]], List[int]]) -> int:
        """Solve part 1 of the problem."""
        fresh_range, ingredients = data
        res = 0

        for ingredient in ingredients:
            for start, end in fresh_range:
                if start <= ingredient <= end:
                    res += 1
                    break

        return res

    def solve_part_2(self, data: Tuple[List[Tuple[int, int]], List[int]]) -> int:
        """Solve part 2 of the problem."""
        fresh_range, _ = data
        sorted_ranges = sorted(fresh_range, key=lambda x: x[0])
        merged_ranges = []
        res = 0

        for start, end in sorted_ranges:
            if not merged_ranges or merged_ranges[-1][1] < start:
                merged_ranges.append([start, end])
            else:
                merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

        for start, end in merged_ranges:
            res += end - start + 1

        return res
