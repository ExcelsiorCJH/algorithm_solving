"""
5 - Longest Palindrome Substring
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1 : right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ""
        for i in range(len(s) - 1):
            result = max(result, expand(i, i + 1), expand(i, i + 2), key=len)

        return result


class Solution2:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s

        start, r = 0, 1
        for i in range(1, len(s)):
            sub1 = s[i - r - 1 : i + 1]
            sub2 = s[i - r : i + 1]

            if i - r - 1 >= 0 and sub1 == sub1[::-1]:
                start = i - r - 1
                r += 2
            elif i - r >= 0 and sub2 == sub2[::-1]:
                start = i - r
                r += 1

        return s[start : start + r]


if __name__ == "__main__":
    s = "babad"

    sol1 = Solution()
    print(sol1.longestPalindrome(s))

    sol2 = Solution2()
    print(sol2.longestPalindrome(s))
