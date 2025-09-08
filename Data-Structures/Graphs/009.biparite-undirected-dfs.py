from collections import defaultdict


class Solution:
    def isBipartite(self, V: int, edges:list[list[int]]):
        adj: defaultdict[int, list[int]] = defaultdict(list)
        
        for i in range(V):
            adj[i] = []
            
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        
        color = [-1 for _ in range(V)]

        def dfs(u: int, currColor: int):
            color[u] = currColor

            for v in adj[u]:
                if color[v] == currColor:
                    return False

                elif color[v] == -1:
                    if not dfs(v, 1 - currColor):
                        return False
            return True

        for i in range(V):
            if color[i] == -1:
                if not dfs(i, 0):
                    return False

        return True
        
