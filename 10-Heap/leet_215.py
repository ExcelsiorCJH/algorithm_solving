"""
215. kth-largest-element-in-an-array
"""

import heapq
from typing import List


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k - 1]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2

    sol1 = Solution1()
    sol2 = Solution2()

    print(sol1.findKthLargest(nums, k))
    print(sol2.findKthLargest(nums, k))