"""
15. 3Sum
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        for i in range(len(nums) - 2):
            # 중복된 값 넘기기
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                res = nums[i] + nums[left] + nums[right]

                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    # 정답 및 스킵 처리
                    results.append((nums[i], nums[left], nums[right]))

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

        return results


if __name__ == "__main__":
    nums = [0]  # [-1, 0, 1, 2, -1, -4]

    sol = Solution()
    print(sol.threeSum(nums))
