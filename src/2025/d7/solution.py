from functools import cache
from typing import List, Tuple
from src.solution import Solution

START_CHAR = "S"
SPLIT_CHAR = "^"
EMPTY_CHAR = "."


class Solution2025D7(Solution):
    def parse_data(self, contents: str) -> List[List[str]]:
        """Parse the input data into a usable format."""
        lines = contents.splitlines()
        grid = [list(line) for line in lines]
        return grid

    def solve_part_1(self, data: List[List[str]]) -> int:
        """Solve part 1 of the problem."""
        start_coordinates = self._find_start_position(data)

        curr_set: set[int] = set()
        curr_set.add(start_coordinates[1])
        res = 0

        for r in range(1, len(data)):
            next_set = set()
            for pos in curr_set:
                nr, nc = r, pos
                if self._is_valid_position(data, nr, nc) and data[nr][nc] == SPLIT_CHAR:
                    res += 1
                    if (
                        self._is_valid_position(data, nr, nc + 1)
                        and data[nr][nc + 1] == EMPTY_CHAR
                    ):
                        next_set.add(nc + 1)
                    if (
                        self._is_valid_position(data, nr, nc - 1)
                        and data[nr][nc - 1] == EMPTY_CHAR
                    ):
                        next_set.add(nc - 1)
                else:
                    next_set.add(nc)
            curr_set = next_set

        return res

    def solve_part_2(self, data: List[List[str]]) -> int:
        start_r, start_c = self._find_start_position(data)
        rows, cols = len(data), len(data[0])

        @cache
        def dfs(r: int, c: int) -> int:
            if r >= rows:
                return 1

            if not (0 <= r < rows and 0 <= c < cols):
                return 0

            if r + 1 < rows and data[r + 1][c] == SPLIT_CHAR:
                return dfs(r + 1, c - 1) + dfs(r + 1, c + 1)

            return dfs(r + 1, c)

        return dfs(start_r, start_c)

    def _find_start_position(self, grid: List[List[str]]) -> Tuple[int, int]:
        """Find the starting position in the grid."""
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == START_CHAR:
                    return r, c
        raise ValueError(f"Start position '{START_CHAR}' not found in the grid.")

    def _is_valid_position(self, grid: List[List[str]], r: int, c: int) -> bool:
        """Check if the given position is valid within the grid."""
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
