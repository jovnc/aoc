from typing import Any
from src.solution import Solution


class Solution2025D1(Solution):
    def parse_data(self, contents: str) -> Any:
        """Parse the input data into a list of strings."""
        return contents.splitlines()

    def solve_part_1(self, data: Any) -> Any:
        """Count the number of times the lock returns to position 0."""
        curr_pos = 50
        res = 0

        for line in data:
            direction = line[0]
            distance = int(line[1:])

            curr_pos = self._move_lock_1(curr_pos, direction, distance)

            if curr_pos == 0:
                res += 1

        return res

    def solve_part_2(self, data: Any) -> Any:
        """Count the number of times the lock passes position 0."""
        curr_pos = 50
        res = 0

        for line in data:
            direction = line[0]
            distance = int(line[1:])

            curr_pos, passes = self._move_lock_2(curr_pos, direction, distance)
            res += passes

        return res

    def _move_lock_1(self, curr_pos: int, direction: str, distance: int) -> int:
        """Move the lock position based on direction and distance."""
        if direction == "R":
            curr_pos = (curr_pos + distance) % 100

        elif direction == "L":
            curr_pos = (curr_pos - distance) % 100

        return curr_pos

    def _move_lock_2(
        self, curr_pos: int, direction: str, distance: int
    ) -> tuple[int, int]:
        """Move the lock position based on direction and distance, returns the new position and number of times it passes 0."""
        if direction == "R":
            new_pos = curr_pos + distance
            passes = new_pos // 100
            return new_pos % 100, passes

        elif direction == "L":
            new_pos = curr_pos - distance
            passes = (curr_pos - 1) // 100 - (new_pos - 1) // 100
            return new_pos % 100, passes

        return curr_pos, 0
