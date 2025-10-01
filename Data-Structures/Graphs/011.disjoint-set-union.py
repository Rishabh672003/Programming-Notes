class DSU:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.size = [1] * n
        self.components = n

    def find(self, u: int) -> int:
        """Find with path compression"""
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int) -> bool:
        """Union by No heuristic"""
        pU = self.find(u)
        pV = self.find(v)

        if pU == pV:
            return False

        self.parent[pU] = pV
        return True

    def union_by_rank(self, u: int, v: int) -> bool:
        """Union by rank heuristic"""
        pU, pV = self.find(u), self.find(v)
        if pU == pV:
            return False

        if self.rank[pU] < self.rank[pV]:
            self.parent[pU] = pV
        elif self.rank[pV] < self.rank[pU]:
            self.parent[pV] = pU
        else:
            self.parent[pV] = pU
            self.rank[pU] += 1

        self.components -= 1
        return True

    def union_by_size(self, u: int, v: int) -> bool:
        """Union by size heuristic"""
        pU, pV = self.find(u), self.find(v)
        if pU == pV:
            return False

        if self.size[pU] < self.size[pV]:
            self.parent[pU] = pV
            self.size[pV] += self.size[pU]
        else:
            self.parent[pV] = pU
            self.size[pU] += self.size[pV]

        self.components -= 1
        return True
