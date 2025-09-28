from math import inf


class Solution:
    def bellmanFord(
        self, V: int, edges: list[list[int]], src: int
    ) -> list[int | float]:
        res = [inf for _ in range(V)]
        res[src] = 0

        for _ in range(1, V):
            for u, v, cost in edges:
                if res[u] != inf and res[u] + cost < res[v]:
                    res[v] = res[u] + cost

        # For detecting **negative cycles**
        # if after 1 more relaxation cycle the res is different from before
        # than there is a -ve cycle
        for u, v, cost in edges:
            if res[u] != inf and res[u] + cost < res[v]:
                return [-1]

        return res
