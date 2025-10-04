from collections import defaultdict, deque


class Solution:
    def find_diameter(
        self, adj: defaultdict[int, list[int]], src: int
    ) -> tuple[int, tuple[int, int]]:
        def bfs(start: int):
            farthest_node = 0
            dist = 0
            qu = deque([(start, -1)])

            while qu:
                n = len(qu)
                for _ in range(n):
                    u, parent = qu.popleft()
                    for v in adj[u]:
                        if v == parent:
                            continue
                        farthest_node = v
                        qu.append((v, u))

                dist += 1 if qu else 0

            return (farthest_node, dist)

        one_end, _ = bfs(src)
        second_end, diameter = bfs(one_end)

        return diameter, (one_end, second_end)
