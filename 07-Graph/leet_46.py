"""
46. Permutations
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        if nums:
            dfs(nums)
        return results


if __name__ == "__main__":

    nums = [1, 2, 3]

    solution = Solution()
    results = solution.permute(nums)

    print(f"results of {nums}\n{results}")

