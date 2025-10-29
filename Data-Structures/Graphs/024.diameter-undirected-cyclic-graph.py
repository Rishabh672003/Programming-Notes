from collections import defaultdict


class Solution:
    def diameter(self, V: int, edges: list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def longest_distance(u: int) -> tuple[int, int]:
            node = -1
            dist = 0
            visited = [False] * V

            def dfs(u: int, d: int):
                nonlocal dist, node
                visited[u] = True
                if node == -1 or d > dist:
                    dist = d
                    node = u

                for v in adj[u]:
                    if not visited[v]:
                        dfs(v, d + 1)

            dfs(u, 0)
            return node, dist

        farthest, _ = longest_distance(0)
        _, longest = longest_distance(farthest)

        return longest
