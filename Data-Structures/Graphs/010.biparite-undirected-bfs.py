from collections import defaultdict, deque


class Solution:
    def isBipartite(self, V: int, edges: list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        color = [-1 for _ in range(V)]

        def bfs(node: int, currColor: int):
            q: deque[int] = deque([node])
            color[node] = currColor

            while q:
                cur = q.popleft()

                for v in adj[cur]:
                    if color[v] == color[cur]:
                        return False
                    if color[v] == -1:
                        color[v] = 1 - color[cur]
                        q.append(v)

            return True

        for i in range(V):
            if color[i] == -1:
                if not bfs(i, 0):
                    return False

        return True
