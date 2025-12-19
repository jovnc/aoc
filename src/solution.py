import abc
import inspect
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

FileType = Literal["test", "main"]


@dataclass
class Solution(abc.ABC):
    is_test: bool = False

    def load_data(self, type: FileType):
        filename = "input.txt" if type == "main" else "test-input.txt"
        if type == "test":
            self.is_test = True
        subclass_file = inspect.getfile(self.__class__)
        filepath = Path(subclass_file).parent / filename
        with open(filepath, "r") as f:
            contents = f.read().strip()
        return contents

    @abc.abstractmethod
    def parse_data(self, contents: str) -> Any:
        pass

    @abc.abstractmethod
    def solve_part_1(self, data: Any) -> Any:
        pass

    @abc.abstractmethod
    def solve_part_2(self, data: Any) -> Any:
        pass

    def run_part_1(self, type: FileType) -> Any:
        data = self.parse_data(self.load_data(type))
        ans = self.solve_part_1(data)
        print(f"Part 1: {ans}")
        return ans

    def run_part_2(self, type: FileType) -> Any:
        data = self.parse_data(self.load_data(type))
        ans = self.solve_part_2(data)
        print(f"Part 2: {ans}")
        return ans
