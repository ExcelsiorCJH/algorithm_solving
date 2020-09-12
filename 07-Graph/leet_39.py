"""
39. Combination sum
"""
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                results.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        results = []
        dfs(target, 0, [])

        return results


if __name__ == "__main__":

    solution = Solution()

    candidates = [2, 3, 5]
    target = 8

    results = solution.combinationSum(candidates, target)
    print(f"results of combination sum\n{results}")
