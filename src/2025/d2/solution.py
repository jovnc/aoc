from typing import List
from src.solution import Solution


class Solution2025D2(Solution):
    def parse_data(self, contents: str) -> List[List[str]]:
        """Parse the input data into a usable format."""
        return [
            [start, end]
            for start, end in [numRange.split("-") for numRange in contents.split(",")]
        ]

    def solve_part_1(self, data: List[List[str]]) -> int:
        """Solve part 1 of the problem."""
        sum = 0
        for start, end in data:
            for number in range(int(start), int(end) + 1):
                if not self.is_valid_number(number):
                    print(f"Invalid number found: {number}")
                    sum += number
        return sum

    def solve_part_2(self, data: List[List[str]]) -> int:
        """Solve part 2 of the problem."""
        sum = 0
        for start, end in data:
            for number in range(int(start), int(end) + 1):
                for chunk_size in range(1, len(str(number)) // 2 + 1):
                    if not self.is_valid_chunk(number, chunk_size):
                        sum += number
                        break
        return sum

    def is_valid_number(self, number: int) -> bool:
        """Check if a number is valid based on given criteria."""
        num_str = str(number)
        if len(num_str) % 2 != 0:
            return True
        mid = len(num_str) // 2
        if num_str[:mid] == num_str[mid:]:
            return False
        return True

    def is_valid_chunk(self, number: int, chunk_size: int) -> bool:
        """Check if a chunk of the number is valid."""
        num_str = str(number)
        if len(num_str) % chunk_size != 0:
            return True
        chunks = [
            num_str[i : i + chunk_size] for i in range(0, len(num_str), chunk_size)
        ]
        return not all(chunk == chunks[0] for chunk in chunks)
