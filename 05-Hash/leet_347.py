"""
347. Top K Frequent Elements
"""
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums).most_common(k)
        res = [val for val, _ in res]

        return res


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2

    sol = Solution()
    print(sol.topKFrequent(nums, k))
