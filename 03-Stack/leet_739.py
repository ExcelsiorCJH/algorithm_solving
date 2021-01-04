"""
739. Daily Temperatures
"""
from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer = [0] * len(T)
        stack = []

        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                last = stack.pop()
                answer[last] = i - last

            stack.append(i)

        return answer


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]

    sol = Solution()
    print(sol.dailyTemperatures(T))
