"""
1012. 유기농 배추

https://www.acmicpc.net/problem/1012

주의: 재귀로 풀면 런타임에러남!
"""


def dfs(x, y):
    visited = []
    stack = [(x, y)]

    while stack:
        i, j = stack.pop()
        if (i, j) not in visited:
            visited.append((i, j))
            for nx, ny in directions:
                nx += i
                ny += j
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    stack.append((nx, ny))
    return visited


if __name__ == "__main__":
    # up, down, left, right
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for _ in range(int(input())):
        M, N, K = list(map(int, input().split()))

        grid = [[0 for _ in range(N)] for _ in range(M)]
        for _ in range(K):
            x, y = list(map(int, input().split()))
            grid[x][y] = 1

        cnt = 0
        for x in range(M):
            for y in range(N):
                if grid[x][y] == 1:
                    dfs(x, y)
                    cnt += 1

        print(cnt)