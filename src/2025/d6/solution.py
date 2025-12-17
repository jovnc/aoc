from typing import Any, List, Tuple
from src.solution import Solution


class Solution2025D6(Solution):
    def parse_data(self, contents: str) -> str:
        """Parse the input data into a usable format."""
        return contents

    def solve_part_1(self, data: str) -> int:
        """Solve part 1 of the problem."""
        numbers, operators = self._parse_helper_part_1(data)
        res = 0
        for col in range(len(operators)):
            op = operators[col]
            colRes = numbers[0][col]
            for row in range(1, len(numbers)):
                if op == "+":
                    colRes += numbers[row][col]
                elif op == "*":
                    colRes *= numbers[row][col]
            res += colRes

        return res

    def solve_part_2(self, data: Any) -> Any:
        """Solve part 2 of the problem."""
        numbers, operators = self._parse_helper_part_2(data)
        res = 0

        for col in range(len(operators)):
            op = operators[col]
            colRes = numbers[col][0]
            for row in range(1, len(numbers[col])):
                if op == "+":
                    colRes += numbers[col][row]
                elif op == "*":
                    colRes *= numbers[col][row]
            res += colRes

        return res

    def _parse_helper_part_1(self, contents: str) -> Tuple[List[List[int]], List[str]]:
        """Helper function to parse a line of integers."""
        lines = contents.splitlines()
        operators = [op for op in lines[-1].split(" ") if op]
        numbers = [[int(num) for num in line.split(" ") if num] for line in lines[:-1]]
        return numbers, operators

    def _parse_helper_part_2(self, contents: str) -> Tuple[List[List[int]], List[str]]:
        """Helper function to parse a line of integers."""
        lines = contents.splitlines()
        operator_line = lines[-1]
        number_lines = lines[:-1]

        numbers = []

        col_starts = [idx for idx, c in enumerate(operator_line) if c != " "]
        rows = len(number_lines)

        # Get numbers
        for start, end in zip(col_starts, col_starts[1:] + [len(number_lines[0]) + 1]):
            curr = [
                "".join(
                    [
                        number_lines[r][c]
                        for r in range(rows)
                        if number_lines[r][c] != " "
                    ]
                )
                for c in range(start, end - 1)
            ]
            numbers.append([int(num) for num in curr if num])

        # Get operators
        operators = [op for op in operator_line.split(" ") if op]

        return numbers, operators
