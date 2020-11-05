"""
Leet 973. K Closest Points to Origin

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
"""
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dist = [(x * x + y * y) ** (1 / 2) for x, y in points]
        results = [point for _, point in sorted(zip(dist, points))]
        return results[:K]


class Solution2:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            dist = x ** 2 + y ** 2
            heapq.heappush(heap, (dist, x, y))

        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x, y))
        return result


if __name__ == "__main__":
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2

    solution = Solution2()
    results = solution.kClosest(points, K)
    print(results)
