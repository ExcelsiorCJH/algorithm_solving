"""
2667. 단지번호붙이기

https://www.acmicpc.net/problem/2667

힌트: 동서남북 탐색 + 응용
"""
from collections import Counter


def dfs(i, j, num):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid) or grid[i][j] != 1:
        return

    grid[i][j] = 0
    cnt.append(num)

    # 동서남북 탐색
    dfs(i + 1, j, num)
    dfs(i - 1, j, num)
    dfs(i, j + 1, num)
    dfs(i, j - 1, num)


if __name__ == "__main__":
    N = int(input())

    grid = []
    for _ in range(N):
        row = list(map(int, list(input())))
        grid.append(row)

    num = 1
    cnt = []
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 1:
                dfs(i, j, num)
                num += 1

    cnt = Counter(cnt)
    print(len(cnt))
    for num in sorted(cnt.values()):
        print(num)