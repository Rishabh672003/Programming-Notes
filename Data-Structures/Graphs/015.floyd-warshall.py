# Assumes the distance between two unconnected graph is `math.inf`
class Solution:
    def floydWarshall(self, dist: list[list[int | float]]):
        n = len(dist)
        minimum_dist = dist.copy() # can be done in_place

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    minimum_dist[i][j] = min(
                        minimum_dist[i][j], minimum_dist[i][via] + minimum_dist[via][j]
                    )

        return minimum_dist
