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
        def dfs(u: str) -> int:
            if u == dst:
                return 1
            if u not in data:
                return 0
            return sum(dfs(v) for v in data[u])

        return dfs(src)

    def solve_part_2(self, data: dict[str, list[str]]) -> int:
        """Find every distinct path from svr to out, must visit fft and dac exactly once"""
        src, dst = "svr", "out"

        @cache
        def dfs(u: str, fft: bool, dac: bool) -> int:
            if u == dst:
                return int(fft and dac)
            if u not in data:
                return 0
            return sum(dfs(v, fft or v == "fft", dac or v == "dac") for v in data[u])

        return dfs(src, False, False)
