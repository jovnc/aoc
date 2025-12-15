from typing import List
from src.solution import Solution

PAPER_ROLL = "@"
FORK_LIFT = "."
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]


class Solution2025D4(Solution):
    data: List[List[str]] = []

    def parse_data(self, contents: str) -> List[List[str]]:
        """Parse the input data into a usable format."""
        return [[col for col in row] for row in contents.splitlines()]

    def solve_part_1(self, data: List[List[str]]) -> int:
        """Solve part 1 of the problem."""
        self.data = data
        ROWS = len(data)
        COLS = len(data[0])
        count = 0

        for row in range(ROWS):
            for col in range(COLS):
                if self.data[row][col] == PAPER_ROLL:
                    if self._can_access(row, col, data):
                        count += 1

        return count

    def solve_part_2(self, data: List[List[str]]) -> int:
        """
        Solve part 2 of the problem.
        Possible optimisation: only check additional removals for changed positions.
        """
        self.data = data
        ROWS = len(data)
        COLS = len(data[0])
        count = 0
        frontier = []
        removed = set()

        for row in range(ROWS):
            for col in range(COLS):
                if data[row][col] == PAPER_ROLL:
                    if self._can_access(row, col, data):
                        frontier.append((row, col))

        # use queue to simulate removals by level order traversal
        while frontier:
            next_frontier = []
            for r, c in frontier:
                count += 1
                removed.add((r, c))

            # After removing all accessible rolls, check neighbors
            for r, c in frontier:
                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if self._is_valid(nr, nc):
                        if (nr, nc) not in removed and self.data[nr][nc] == PAPER_ROLL:
                            if self._can_access_with_removed(nr, nc, removed):
                                if (nr, nc) not in [pos for pos in next_frontier]:
                                    next_frontier.append((nr, nc))

            frontier = next_frontier

        return count

    def _is_valid(self, row: int, col: int) -> bool:
        """
        Check if position is valid in grid.
        """
        return 0 <= row < len(self.data) and 0 <= col < len(self.data[0])

    def _can_access(self, row: int, col: int, data: List[List[str]]) -> bool:
        """
        Forklift can access paper roll if less than 4 paper rolls are adjacent.
        """
        num = 0
        for dr, dc in DIRS:
            r, c = row + dr, col + dc
            if self._is_valid(r, c):
                if data[r][c] == PAPER_ROLL:
                    num += 1

        return num < 4

    def _can_access_with_removed(self, row: int, col: int, removed: set) -> bool:
        """
        Check if paper roll can be accessed considering already removed rolls.
        """
        num = 0
        for dr, dc in DIRS:
            r, c = row + dr, col + dc
            if self._is_valid(r, c):
                if self.data[r][c] == PAPER_ROLL and (r, c) not in removed:
                    num += 1

        return num < 4
