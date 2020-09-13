"""
78. Subsets
"""
from typing import List


class MySolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return

            for i in range(start, len(nums)):
                elements.append(nums[i])
                dfs(elements, i + 1, k - 1)
                elements.pop()

        results = []
        if nums:
            for k in range(len(nums) + 1):
                dfs([], 0, k)

        return results


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, path):
            # 매번 결과 추가
            results.append(path)
            # 경로를 만들면서 DFS
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])

        results = []
        if nums:
            dfs(0, [])

        return results


if __name__ == "__main__":
    nums = [1, 2, 3]

    solution = Solution()
    results = solution.subsets(nums)

    print(f"results of {nums}:\n{results}")

