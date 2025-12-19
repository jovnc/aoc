from typing import Dict
from typing import List


class UFDS:
    def __init__(self, n: int):
        self.n = n
        self.parent = [i for i in range(n)]
        self.ranks = [1] * n
        self.unions = n

    def find(self, u: int) -> int:
        """Find with path compression."""
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        """Weighted union by rank."""
        root_u, root_v = self.find(u), self.find(v)
        if root_u == root_v:
            return False
        if self.ranks[root_u] < self.ranks[root_v]:
            self.parent[root_u] = root_v
            self.ranks[root_v] += self.ranks[root_u]
        else:
            self.parent[root_v] = root_u
            self.ranks[root_u] += self.ranks[root_v]
        self.unions -= 1
        return True

    @property
    def union_sizes(self) -> Dict[int, int]:
        """Get sizes of all unions."""
        sizes: Dict[int, int] = {}
        for p in range(self.n):
            root = self.find(p)
            sizes[root] = sizes.get(root, 0) + 1
        return sizes
