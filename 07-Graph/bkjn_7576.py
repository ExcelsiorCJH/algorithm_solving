"""
7576. 토마토

https://www.acmicpc.net/problem/7576

힌트: BFS + 응용
"""
from collections import deque


def bfs():
    queue = deque()
    cnt = -1

    for x in range(N):
        for y in range(M):
            if grid[x][y] == 1:
                queue.append((x, y))

    while queue:
        cnt += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for h, w in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                h, w = h + i, w + j
                if 0 <= h < N and 0 <= w < M and grid[h][w] == 0:
                    grid[h][w] = 1
                    queue.append((h, w))

    for x in range(N):
        for y in range(M):
            if grid[x][y] == 0:
                return -1

    return cnt


if __name__ == "__main__":
    M, N = list(map(int, input().split()))
    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    print(bfs())