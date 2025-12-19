from src.utils.ufds import UFDS
from typing import Tuple
from typing import List
from src.utils.coords import Coords3D
from src.solution import Solution


class Solution2025D8(Solution):
    def parse_data(self, contents: str) -> List[Coords3D]:
        """Parse the input data into a usable format."""
        lines = contents.splitlines()
        coords = [
            Coords3D(int(x), int(y), int(z))
            for x, y, z in [line.split(",") for line in lines]
        ]
        return coords

    def solve_part_1(self, data: List[Coords3D]) -> int:
        """Solve part 1 of the problem."""
        pick = 10 if self.is_test else len(data)
        ordered_pairs = self.get_ordered_pairs(data)

        ufds = UFDS(len(data))
        for pair in ordered_pairs[:pick]:
            ufds.union(pair[0], pair[1])

        res = 1
        for v in sorted(ufds.union_sizes.values(), reverse=True)[:3]:
            res *= v
        return res

    def solve_part_2(self, data: List[Coords3D]) -> int:
        """Solve part 2 of the problem."""
        ordered_pairs = self.get_ordered_pairs(data)

        ufds = UFDS(len(data))
        for pair in ordered_pairs:
            ufds.union(pair[0], pair[1])
            if ufds.unions == 1:
                return data[pair[0]].x * data[pair[1]].x

        return -1

    def get_ordered_pairs(self, data: List[Coords3D]) -> List[Tuple[int, int, float]]:
        """Get all ordered pairs of points, ordered by distance (smallest first)."""
        pairs = []
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                pairs.append((i, j, data[i].distance_to(data[j])))
        pairs.sort(key=lambda x: x[2])
        return pairs
