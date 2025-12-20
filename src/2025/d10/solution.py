from typing import List, Tuple
from src.solution import Solution
import ast
from collections import deque

ON = "#"
OFF = "."

Data = Tuple[Tuple[str], List[Tuple[int]], List[str]]


class Solution2025D10(Solution):
    def parse_data(self, contents: str) -> List[Data]:
        """Parse the input data into a usable format."""
        return [self.parse_line(line) for line in contents.splitlines()]

    def solve_part_1(self, data: List[Data]) -> int:
        """
        Given the empty start state, find the minimum number of buttons needed to press to reach the end state.
        """
        res = 0
        for end_state, button_wiring, _ in data:
            start_state = tuple([OFF] * len(end_state))
            queue = deque([(start_state, 0)])
            visited = set()
            visited.add(start_state)

            while queue:
                state, steps = queue.popleft()
                if state == end_state:
                    res += steps
                    break
                for buttons in button_wiring:
                    new_state = list(state)
                    for button_idx in buttons:
                        new_state[button_idx] = (
                            ON if new_state[button_idx] == OFF else OFF
                        )
                    new_state_tuple = tuple(new_state)
                    if new_state_tuple not in visited:
                        visited.add(new_state_tuple)
                        queue.append((new_state_tuple, steps + 1))

        return res

    def solve_part_2(self, data: List[Data]) -> int:
        """Solve part 2 of the problem."""
        return 0

    def parse_line(self, line: str) -> Data:
        """Parse a single line of the input data."""
        parts = line.split(" ")
        end_state = tuple([c for c in parts[0] if c not in ["[", "]"]])
        button_wiring = [
            ast.literal_eval(b) if "," in b else (ast.literal_eval(b),)
            for b in parts[1:-1]
        ]
        joltage = [c for c in parts[-1] if c not in ["{", "}", ","]]
        return end_state, button_wiring, joltage
