"""
Leet 704. Binary Search

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2
            # mid = (low + high) // 2

            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return -1


class Solution2:
    def search(nums: List[int], target: int) -> int:
        def binary_search(low, high):
            if low <= high:
                mid = (low + high) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, high)
                elif nums[mid] > target:
                    return binary_search(low, mid - 1)
                else:
                    return mid
            else:
                return -1

        return binary_search(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9

    sol = Solution()
    result = sol.search(nums, target)
    print(result)