from collections import defaultdict, deque


class Solution:
    def isCycle(self, V: int, edges: list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False for _ in range(V)]

        def bfs(i: int):
            q: deque[tuple[int, int]] = deque([(i, -1)])
            visited[i] = True
            while q:
                cur, parent = q.popleft()
                for node in adj[cur]:
                    if node == parent:
                        continue
                    if visited[node]:
                        return True

                    visited[node] = True
                    q.append((node, cur))

            return False

        for i in range(V):
            if not visited[i] and bfs(i):
                return True

        return False
