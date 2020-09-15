"""
743. Network Delay Time
Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2

Key point: 가장 오래 걸리는 노드까지의 최단 거리를 구해서 리턴
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        # graph 생성
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Q = [(시간, 정점)] init
        Q = [(0, K)]
        dist = defaultdict(int)
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = w + time
                    heapq.heappush(Q, (alt, v))

        if len(dist) == N:
            return max(dist.values())

        return -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2

    solution = Solution()
    result = solution.networkDelayTime(times, N, K)

    print(f"result of {times}:\n{result}")
