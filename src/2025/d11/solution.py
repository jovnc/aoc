from functools import cache
from src.solution import Solution


class Solution2025D11(Solution):
    def parse_data(self, contents: str) -> dict[str, list[str]]:
        """Parse the input data into a usable format."""
        parts = [ln.split(":") for ln in contents.splitlines()]
        adj = {}
        for part in parts:
            start = part[0]
            nei = part[1].strip().split(" ")
            if start not in adj:
                adj[start] = []
            adj[start].extend(nei)

        return adj

    def solve_part_1(self, data: dict[str, list[str]]) -> int:
        """Find number of distinct paths from you to out"""
        src, dst = "you", "out"

        @cache
        def dfs(u):
            if u == dst:
                return 1
            if u not in data:
                return 0
            return sum(dfs(v) for v in data[u])

        return dfs(src)

    def solve_part_2(self, data: dict[str, list[str]]) -> int:
        """Solve part 2 of the problem."""
        return 0
