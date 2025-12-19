from typing import Tuple, List
from src.solution import Solution


class Solution2025D9(Solution):
    def parse_data(self, contents: str) -> List[Tuple[int, int]]:
        """Parse the input data into a usable format."""
        lines = contents.splitlines()
        nums = [
            (int(start), int(end)) for start, end in [line.split(",") for line in lines]
        ]
        return nums

    def solve_part_1(self, data: List[Tuple[int, int]]) -> int:
        """Solve part 1 of the problem."""
        res = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                res = max(res, self.distance(data[i], data[j]))
        return res

    def solve_part_2(self, data: List[Tuple[int, int]]) -> int:
        """Solve part 2 of the problem."""
        print(data)
        return 0

    def distance(self, a: Tuple[int, int], b: Tuple[int, int]) -> int:
        """Calculate the special distance between two points."""
        diff_x = abs(a[0] - b[0] + 1)
        diff_y = abs(a[1] - b[1] + 1)
        return diff_x * diff_y
