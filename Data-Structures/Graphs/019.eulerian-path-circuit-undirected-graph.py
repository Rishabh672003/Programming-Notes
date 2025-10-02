class Solution:
    def isEulerCircuitExist(self, V: int, adj: list[list[int]]):
        def isConnected() -> bool:
            """Check if all the non-zero degree nodes in the graph are connected or not"""
            non_zero_degree = -1
            for i in range(V):
                if len(adj[i]) > 0:
                    non_zero_degree = i
                    break

            if non_zero_degree == -1:
                return True

            visited = [False] * V

            def dfs(u: int):
                visited[u] = True

                for v in adj[u]:
                    if not visited[v]:
                        dfs(v)

            dfs(non_zero_degree)

            for i in range(V):
                if not visited[i] and len(adj[i]) > 0:
                    return False

            return True

        if not isConnected():
            return 0

        odd_degree = 0

        for i in range(V):
            if len(adj[i]) % 2 == 1:
                odd_degree += 1

        if odd_degree == 2:
            return 1  # Euler Path exists

        if odd_degree == 0:
            return 2  # Euler Circuit

        if odd_degree > 2:
            return 0  # neither
