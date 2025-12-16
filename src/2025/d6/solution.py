from typing import Any, List, Tuple
from src.solution import Solution


class Solution2025D6(Solution):
    def parse_data(self, contents: str) -> Tuple[List[List[int]], List[str]]:
        """Parse the input data into a usable format."""
        lines = contents.splitlines()
        operators = [op for op in lines[-1].split(" ") if op]
        numbers = [[int(num) for num in line.split(" ") if num] for line in lines[:-1]]
        return numbers, operators

    def solve_part_1(self, data: Tuple[List[List[int]], List[str]]) -> int:
        """Solve part 1 of the problem."""
        numbers, operators = data
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
        pass
