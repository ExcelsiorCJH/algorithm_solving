"""
Hacker Rank - Forming a Magic Square

Input:
4 9 2
3 5 7
8 1 5

Output:
1
"""

magic_squares = [
    [2, 7, 6, 9, 5, 1, 4, 3, 8],
    [2, 9, 4, 7, 5, 3, 6, 1, 8],
    [4, 3, 8, 9, 5, 1, 2, 7, 6],
    [4, 9, 2, 3, 5, 7, 8, 1, 6],
    [6, 1, 8, 7, 5, 3, 2, 9, 4],
    [6, 7, 2, 1, 5, 9, 8, 3, 4],
    [8, 1, 6, 3, 5, 7, 4, 9, 2],
    [8, 3, 4, 1, 5, 9, 6, 7, 2],
]

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    costs = []
    for magic_square in magic_squares:
        cost = sum([abs(magic_square[i] - s[i]) for i in range(9)])
        costs.append(cost)

    return min(costs)


if __name__ == "__main__":
    s = []
    for _ in range(3):
        s.extend(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)