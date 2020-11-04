"""
242. Valid Anagram

Input: s = "anagram", t = "nagaram"
Output: true
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


if __name__ == "__main__":
    s = "rat"
    t = "car"

    solution = Solution()
    result = solution.isAnagram(s, t)

    print(result)
