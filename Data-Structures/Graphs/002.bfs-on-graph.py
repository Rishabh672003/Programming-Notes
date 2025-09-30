from collections import deque


class Solution:
    def bfs(self, adj: list[list[int]]):
        n = len(adj)
        res: list[int] = []

        visited = [False for _ in range(n)]

        def bfs(u: int):
            d: deque[int] = deque([u])
            visited[u] = True
            res.append(u)

            while d:
                cur = d.popleft()
                for i in adj[cur]:
                    if not visited[i]:
                        d.append(i)
                        visited[i] = True
                        res.append(i)

        for i in range(n):
            if not visited[i]:
                bfs(i)

        return res
