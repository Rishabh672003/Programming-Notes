from collections import defaultdict
from heapq import heappop, heappush


# Assumes the Graph is connected
# if disconnected the mst value will be the component of the node `0`
class Solution:
    def spanningTree(self, V: int, edges: list[list[int]]) -> int:
        adj: defaultdict[int, list[tuple[int, int]]] = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
            adj[v].append((u, wt))

        inMst = [False for _ in range(V)]

        #                 weight, node, parent
        min_heap: list[tuple[int, int, int]] = []
        heappush(min_heap, (0, 0, -1))
        mst_edges: list[tuple[int, int, int]] = [] # gives the path of mst
        parents = [-1 for _ in range(V)]
        mst = 0

        while min_heap:
            weight, node, parent = heappop(min_heap)

            if inMst[node]:
                continue

            inMst[node] = True
            mst += weight
            if parent != -1:
                mst_edges.append((parent, node, weight))
                parents[node] = parent

            for nei, nei_wt in adj[node]:
                if not inMst[nei]:
                    heappush(min_heap, (nei_wt, nei, node))

        return mst
