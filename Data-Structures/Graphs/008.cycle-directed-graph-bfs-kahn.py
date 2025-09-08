from collections import defaultdict, deque


class Solution:
    def isCycle(self, V: int, edges: list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)

        indegree = [0 for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        q: deque[int] = deque()
        count = 0
        for index, elem in enumerate(indegree):
            if elem == 0:
                q.append(index)
                count += 1

        while q:
            cur = q.popleft()
            for i in adj[cur]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
                    count += 1

        return not count == V
