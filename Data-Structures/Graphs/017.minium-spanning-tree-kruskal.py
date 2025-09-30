class Solution:
    class DSU:
        def __init__(self, n: int):
            self.parents = list(range(n))
            self.ranks = [0] * n

        def find(self, u: int) -> int:
            if u == self.parents[u]:
                return u

            self.parents[u] = self.find(self.parents[u])
            return self.parents[u]

        def union(self, u: int, v: int):
            pU, pV = self.find(u), self.find(v)

            if pU == pV:
                return

            if self.ranks[pU] < self.ranks[pV]:
                self.parents[pU] = pV
            elif self.ranks[pV] < self.ranks[pU]:
                self.parents[pV] = pU
            else:
                self.parents[pU] = pV
                self.ranks[pV] += 1

    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        dsu = self.DSU(V)

        # sort by weights in ascending order
        edges.sort(key=lambda x: x[2])
        mst = 0

        for u, v, weight in edges:
            # if both are in different components union them
            if dsu.find(u) != dsu.find(v):
                dsu.union(u, v)
                mst += weight

        return mst
