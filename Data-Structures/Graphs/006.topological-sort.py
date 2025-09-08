from collections import defaultdict


class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        adj: defaultdict[int, list[int]] = defaultdict(list)

        for i in range(V):
            adj[i] = []

        for u, v in edges:
            adj[u].append(v)

        st: list[int] = []
        visited = [False for _ in range(V)]

        def solve(u: int):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    solve(v)

            st.append(u)
            return

        for i in range(V):
            if not visited[i]:
                solve(i)
        return st[::-1]
