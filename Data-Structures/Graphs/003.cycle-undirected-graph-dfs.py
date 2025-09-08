from collections import defaultdict


class Solution:
    def isCycle(self, V: int, edges: list[list[int]]):
        adj:defaultdict[int, list[int]] = defaultdict(list)

        for v in range(V):
            adj[v] = []

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(V)]
        def dfs(u: int, parent: int) -> bool:
            visited[u] = True
            for v in adj[u]:
                if v == parent: continue

                if visited[v]: return True
                
                if dfs(v, u):
                    return True

            return False

        for i in range(V):
            if not visited[i] and dfs(i, -1):
                return True
        return False

