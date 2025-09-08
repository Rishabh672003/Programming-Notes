from collections import deque


class Solution:
    def bfs(self, adj: list[list[int]]):
        visited = [False for _ in range(len(adj))]
        res: list[int] = []

        d: deque[int] = deque([0])
        visited[0] = True
        res.append(0)
        while d:
            cur = d.popleft()
            for i in adj[cur]:
                if not visited[i]:
                    d.append(i)
                    visited[i] = True
                    res.append(i)

        return res
