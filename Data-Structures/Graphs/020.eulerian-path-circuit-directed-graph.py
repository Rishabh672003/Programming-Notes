class Solution:
    def isEulerCircuitExist(self, V: int, adj: list[list[int]]):
        # Simplified Kosaraju, to check if the whole graph is a single SCC
        def isStronglyConnected() -> bool:
            """Check if all nodes with non-zero degree belong to one strongly connected component"""
            visited = [False] * V

            # find first vertex with non-zero degree
            start = -1
            for i in range(V):
                if len(adj[i]) > 0:
                    start = i
                    break

            if start == -1:
                return True  # No edges → trivially Eulerian

            def dfs(u: int, visited: list[bool]):
                visited[u] = True
                for v in adj[u]:
                    if not visited[v]:
                        dfs(v, visited)

            # DFS on original graph
            dfs(start, visited)
            for i in range(V):
                if not visited[i] and len(adj[i]) > 0:
                    return False

            # Build transpose graph
            transpose: list[list[int]] = [[] for _ in range(V)]
            for u in range(V):
                for v in adj[u]:
                    transpose[v].append(u)

            visited = [False] * V
            dfs(start, visited)  # DFS on transpose

            for i in range(V):
                if not visited[i] and len(adj[i]) > 0:
                    return False

            return True

        if not isStronglyConnected():
            return 0  # neither

        in_deg = [0] * V
        out_deg = [0] * V

        for u in range(V):
            for v in adj[u]:
                out_deg[u] += 1
                in_deg[v] += 1

        start_nodes, end_nodes = 0, 0

        for i in range(V):
            if out_deg[i] - in_deg[i] == 1:
                start_nodes += 1
            elif in_deg[i] - out_deg[i] == 1:
                end_nodes += 1
            elif in_deg[i] != out_deg[i]:
                return 0  # neither

        if start_nodes == 0 and end_nodes == 0:
            return 2  # Euler Circuit
        elif start_nodes == 1 and end_nodes == 1:
            return 1  # Euler Path
        else:
            return 0  # neither
