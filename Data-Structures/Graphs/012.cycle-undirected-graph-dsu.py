class Solution:
    class DSU:
        def __init__(self, n: int):
            self.pts = [i for i in range(n)]
            self.ranks = [0] * n
            self.components = n

        def find(self, u: int) -> int:
            if u == self.pts[u]:
                return u
            self.pts[u] = self.find(self.pts[u])
            return self.pts[u]

        def union(self, u: int, v: int) -> bool:
            """
            finds Rank based union of two sets
            returns True if the union was done
            else if the parent was the same it will return False
            """
            pU = self.find(u)
            pV = self.find(v)

            if pU == pV:
                return False

            if self.ranks[pU] < self.ranks[pV]:
                self.pts[pU] = pV
            elif self.ranks[pV] < self.ranks[pU]:
                self.pts[pV] = pU
            else:
                self.pts[pU] = pV
                self.ranks[pV] += 1

            self.components -= 1
            return True

    def detectCycle(self, V: int, adj: list[list[int]]):
        dsu = self.DSU(V)

        for u in range(V):
            for v in adj[u]:
                if u < v:
                    pU, pV = dsu.find(u), dsu.find(v)
                    if pU == pV:
                        return True
                    dsu.union(pU, pV)
        return False
