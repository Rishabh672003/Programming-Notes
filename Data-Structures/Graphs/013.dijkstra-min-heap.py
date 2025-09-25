from collections import defaultdict
import heapq
from math import inf


class Solution:
    def dijkstra(self, V: int, edges: list[list[int]], src: int):
        adj: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)

        for u, v, d in edges:
            adj[u].append((v, d))
            adj[v].append((u, d))

        min_heap: list[tuple[int, int]] = []
        res = [inf for _ in range(V)]
        res[src] = 0
        heapq.heappush(min_heap, (0, src))

        while min_heap:
            cur_dis, node = heapq.heappop(min_heap)
            if cur_dis > res[node]:
                continue

            for neigh, cost in adj[node]:
                if cur_dis + cost < res[neigh]:
                    res[neigh] = cur_dis + cost
                    heapq.heappush(min_heap, (cur_dis + cost, neigh))

        return res

