from collections import deque
from typing import Tuple, List, Dict
from src.solution import Solution

Coord = Tuple[int, int]


class Solution2025D9(Solution):
    def parse_data(self, contents: str) -> List[Coord]:
        """Parse the input data into a usable format."""
        lines = contents.splitlines()
        nums = [
            (int(start), int(end)) for start, end in [line.split(",") for line in lines]
        ]
        return nums

    def solve_part_1(self, data: List[Coord]) -> int:
        """Solve part 1 of the problem."""
        res = 0
        for i in range(len(data)):
            for j in range(i + 1, len(data)):
                res = max(res, self.distance(data[i], data[j]))
        return res

    def solve_part_2(self, data: List[Coord]) -> int:
        """Solve part 2 of the problem."""
        comp_x, comp_y, rev_x, rev_y, comp_points = self.build_compression(data)
        border = self.build_borders(comp_points)
        shape = self.flood_fill(border)
        res = 0
        n = len(data)

        for i in range(n - 1):
            x1c, y1c = comp_points[i]
            for j in range(i + 1, n):
                x2c, y2c = comp_points[j]

                # map back to original coordinates for real area
                xa, ya = rev_x[x1c], rev_y[y1c]
                xb, yb = rev_x[x2c], rev_y[y2c]
                area = (abs(xa - xb) + 1) * (abs(ya - yb) + 1)

                if area <= res:
                    continue

                if self.rect_fully_inside(shape, x1c, y1c, x2c, y2c):
                    res = area

        return res

    def build_compression(
        self,
        data: List[Coord],
    ) -> Tuple[
        Dict[int, int], Dict[int, int], Dict[int, int], Dict[int, int], List[Coord]
    ]:
        """
        Build compression for the given data.
        """
        xs = {x for (x, y) in data}
        ys = {y for (x, y) in data}

        # sort them and give them compressed index, allow reverse lookup
        comp_x = {}
        comp_y = {}
        rev_x = {}
        rev_y = {}
        for i, x in enumerate(sorted(xs)):
            comp_x[x] = i * 2
            rev_x[i * 2] = x
        for i, y in enumerate(sorted(ys)):
            comp_y[y] = i * 2
            rev_y[i * 2] = y

        # convert all corners to compressed corners
        comp_points = [(comp_x[x], comp_y[y]) for x, y in data]

        return comp_x, comp_y, rev_x, rev_y, comp_points

    def build_borders(
        self,
        comp_points: List[Coord],
    ) -> Tuple[Coord, Coord, Coord, Coord]:
        """
        Build borders for the given compressed points.
        """
        corners = comp_points[:]
        corners.append(corners[0])
        border = set()
        for i in range(len(corners) - 1):
            x1, y1 = corners[i]
            x2, y2 = corners[i + 1]
            if x1 == x2:
                y_lo, y_hi = sorted((y1, y2))
                for y in range(y_lo, y_hi + 1):
                    border.add((x1, y))
            elif y1 == y2:
                x_lo, x_hi = sorted((x1, x2))
                for x in range(x_lo, x_hi + 1):
                    border.add((x, y1))
        return border

    def flood_fill(
        self,
        border: List[Coord],
    ) -> int:
        """
        Flood fill the given border.
        """
        min_x = min(x for x, _ in border)
        min_y = min(y for x, y in border if x == min_x)

        seed = (min_x + 1, min_y + 1)

        shape = set(border)
        q = deque([seed])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            x, y = q.popleft()
            if (x, y) in shape:
                continue
            shape.add((x, y))
            for dx, dy in dirs:
                q.append((x + dx, y + dy))

        return shape

    def rect_fully_inside(
        self,
        shape: List[Coord],
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        """
        Check if the given rectangle is fully inside the shape.
        """
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if (x, y) not in shape:
                    return False
        return True

    def distance(self, a: Coord, b: Coord) -> int:
        """Calculate the special distance between two points."""
        diff_x = abs(a[0] - b[0]) + 1
        diff_y = abs(a[1] - b[1]) + 1
        return diff_x * diff_y
