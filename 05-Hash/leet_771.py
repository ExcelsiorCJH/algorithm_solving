"""
771. Jewels and Stones
"""
from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = Counter(jewels)
        stones = Counter(stones)

        cnt = 0
        for key in jewels:
            cnt += stones[key]

        return cnt


class Solution2:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"

    sol = Solution2()
    print(sol.numJewelsInStones(jewels, stones))
