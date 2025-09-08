from collections import defaultdict, deque


class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj: list[list[int]]):
        adj_mat: defaultdict[int, list[int]] = defaultdict(list)

        for i in range(len(adj)):
            adj_mat[i].extend([x for x in adj[i]])

        visited = [False for _ in range(len(adj_mat))]
        res: list[int] = []

        d: deque[int] = deque([0])
        visited[0] = True
        res.append(0)
        while d:
            cur = d.popleft()
            for i in adj_mat[cur]:
                if not visited[i]:
                    d.append(i)
                    visited[i] = True
                    res.append(i)

        return res
