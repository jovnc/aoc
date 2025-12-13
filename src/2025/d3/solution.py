from typing import Any, List
from src.solution import Solution


class Solution2025D3(Solution):
    def parse_data(self, contents: str) -> List[List[int]]:
        """Parse the input data into a usable format."""
        return [[int(n) for n in num] for num in contents.splitlines()]

    def solve_part_1(self, data: List[List[int]]) -> int:
        """Solve part 1 of the problem."""
        res = 0
        for row in data:
            res += self._find_pair(row)
        return res

    def solve_part_2(self, data: List[List[int]]) -> Any:
        """Solve part 2 of the problem."""
        res = 0
        for row in data:
            res += self._find_twelves(row)
        return res

    def _find_pair(self, row: List[int]) -> int:
        """
        Use stack of max size 2 to find largest pair in row.
        """
        stack = []
        currMax = 0
        for n in row:
            while len(stack) > 1 and n > stack[-1]:
                stack.pop()

            if len(stack) == 1:
                stack.append(n)
                currMax = max(currMax, stack[0] * 10 + stack[1])

                # If the new number is larger than the first in the stack,
                # we can replace the first with the new number to maximize future pairs.
                if n > stack[0]:
                    stack.pop()
                    stack.pop()
                    stack.append(n)
            else:
                stack.append(n)
        return currMax

    def _find_twelves(self, row: List[int]) -> int:
        """
        Uses a greedy approach: for each position, pick the largest available digit
        that still leaves enough digits to complete the number.
        """
        result = []
        start = 0  # keep track of where we are in the row

        for i in range(12):
            remaining = 12 - i
            end = len(row) - remaining + 1

            max_digit = 0
            max_index = start
            for j in range(start, end):
                if row[j] > max_digit:
                    max_digit = row[j]
                    max_index = j

            result.append(max_digit)
            start = max_index + 1

        num = 0
        for digit in result:
            num = num * 10 + digit

        return num
