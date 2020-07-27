"""
125 - Valid Palindrome
"""
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        s = [c.lower() for c in s if c.isalnum()]
        s = "".join(s)

        return s == s[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub("[^a-z0-9]", "", s)

        return s == s[::-1]
