from typing import Any, List
from src.solution import Solution

PAPER_ROLL = "@"
FORK_LIFT = "."


class Solution2025D4(Solution):
    def parse_data(self, contents: str) -> List[List[str]]:
        """Parse the input data into a usable format."""
        return [[col for col in row] for row in contents.splitlines()]

    def solve_part_1(self, data: Any) -> Any:
        """Solve part 1 of the problem."""
        ROWS = len(data)
        COLS = len(data[0])
        count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if data[row][col] == PAPER_ROLL:
                    if self._can_access(row, col, data):
                        count += 1

        return count

    def solve_part_2(self, data: Any) -> Any:
        """Solve part 2 of the problem."""
        pass

    def _is_valid(self, row: int, col: int, grid: list[list[str]]) -> bool:
        """
        Check if position is valid in grid.
        """
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    def _can_access(self, row: int, col: int, grid: list[list[str]]) -> bool:
        """
        Forklift can access paper roll if less than 4 paper rolls are adjacent.
        """
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        num = 0
        for dr, dc in DIRS:
            r, c = row + dr, col + dc
            if self._is_valid(r, c, grid):
                if grid[r][c] == PAPER_ROLL:
                    num += 1

        return num < 4
