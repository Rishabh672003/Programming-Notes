class Solution:
    def kosaraju(self, adj: list[list[int]]) -> int:
        V = len(adj)
        visited_top_sort = [False for _ in range(V)]
        top_sorted: list[int] = []

        def topological_sort(u: int):
            visited_top_sort[u] = True

            for v in adj[u]:
                if not visited_top_sort[v]:
                    topological_sort(v)

            top_sorted.append(u)

        for i in range(V):
            if not visited_top_sort[i]:
                topological_sort(i)

        new_adj: list[list[int]] = [[] for _ in range(V)]

        for index, elem in enumerate(adj):
            for j in elem:
                new_adj[j].append(index)

        visited = [False for _ in range(V)]

        def dfs(u: int):
            visited[u] = True

            for v in new_adj[u]:
                if not visited[v]:
                    dfs(v)

        count = 0

        while top_sorted:
            cur = top_sorted.pop()
            if not visited[cur]:
                dfs(cur)
                count += 1

        return count


sol = Solution()
print(sol.kosaraju([[2, 3], [0], [1], [4], []]))
