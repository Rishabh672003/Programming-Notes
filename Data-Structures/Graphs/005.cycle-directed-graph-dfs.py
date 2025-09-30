from collections import defaultdict


class Solution:
    def isCycle(self, V: int, edges: list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)

        visited = [False for _ in range(V)]
        inRecursion = [False for _ in range(V)]

        def dfs(u: int):
            visited[u] = True
            inRecursion[u] = True

            for i in adj[u]:
                if visited[i]:
                    if inRecursion[i]:
                        return True
                    return False
                if dfs(i):
                    return True

            inRecursion[u] = False
            return False

        for i in range(V):
            if not visited[i] and dfs(i):
                return True

        return False
