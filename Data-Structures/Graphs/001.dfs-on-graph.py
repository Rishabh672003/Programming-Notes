class Solution:
    def dfs(self, adj: list[list[int]]) -> list[int]:
        n = len(adj)

        ans: list[int] = []
        visited = [False for _ in range(n)]

        def solve(u: int):
            visited[u] = True
            ans.append(u)

            for i in adj[u]:
                if not visited[i]:
                    solve(i)

        for i in range(n):
            if not visited[i]:
                solve(i)
        return ans

