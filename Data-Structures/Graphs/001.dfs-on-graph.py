from collections import defaultdict


class Solution:
    def _dfs(
        self,
        elem: int,
        adj_mat: defaultdict[int, list[int]],
        visited: list[bool],
        ans: list[int],
    ):
        if visited[elem]:
            return

        visited[elem] = True
        ans.append(elem)

        for i in adj_mat[elem]:
            if not visited[i]:
                self._dfs(i, adj_mat, visited, ans)

    def dfs(self, adj: list[list[int]]) -> list[int]:
        adj_mat: defaultdict[int, list[int]] = defaultdict(list)

        for i in range(len(adj)):
            adj_mat[i].extend([x for x in adj[i]])

        ans: list[int] = []
        ans.append(0)
        visited = [False for _ in range(len(adj_mat))]
        self._dfs(0, adj_mat, visited, ans)
        return ans
