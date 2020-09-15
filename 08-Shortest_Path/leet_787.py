"""
787. Cheapest Flights Within K Stops

Input: 
n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, K = 0
Output: 500

key point: Dijkstra 알고리즘 응용
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        Q = [(0, src, K)]
        while Q:
            cost, node, k = heapq.heappop(Q)
            if node == dst:
                return cost
            if k >= 0:
                for v, w in graph[node]:
                    alt = cost + w
                    heapq.heappush(Q, (alt, v, k - 1))

        return -1


if __name__ == "__main__":
    n = 3
    flights = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    src = 0
    dst = 2
    K = 0

    solution = Solution()
    result = solution.findCheapestPrice(n, flights, src, dst, K)

    print(f"result of {flights}:\n{result}")
