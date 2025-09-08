from collections import defaultdict, deque


class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        adj: defaultdict[int, list[int]] = defaultdict(list)

        indegree = [0 for _ in range(V)]
        for u, v in edges:
            indegree[v] += 1
            adj[u].append(v)

        q: deque[int] = deque()
        res: list[int] = []

        for index, elem in enumerate(indegree):
            if elem == 0:
                res.append(index)
                q.append(index)

        while q:
            cur = q.popleft()
            res.append(cur)
            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        return res


sol = Solution()
print(sol.topoSort(4, [[3, 0], [1, 0], [2, 0]]))
