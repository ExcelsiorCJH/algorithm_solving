"""
17. Letter Combinations of a Phone Number
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs function
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return

            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)

        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []
        if digits:
            dfs(0, "")
        return result


if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)

    print(f"result of {digits}:\n {result}")
