"""
77. Combinations
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results, prevs = [], []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results


if __name__ == "__main__":
    n, k = 5, 3

    solution = Solution()
    results = solution.combine(n, k)
    print(f"results of {n}C{k}\n{results}")
