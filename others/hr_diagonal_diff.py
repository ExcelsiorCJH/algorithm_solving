"""
HackerRank - Diagonal Difference

Input:
3
11 2 4
4 5 6
10 8 -12

Output:
15
"""
import math
import os
import random
import re
import sys


def diagonalDifference(arr):
    # Write your code here
    right = [arr[i][j] for i, j in zip(range(n), range(n))]
    left = [arr[i][j] for i, j in zip(range(n), range(n - 1, -1, -1))]

    return abs(sum(right) - sum(left))


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)