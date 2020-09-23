"""
2178. 미로탐색

https://www.acmicpc.net/problem/2178

힌트: BFS 탐색 + 응용
"""
from collections import deque


def bfs(x, y):
    queue = deque([(x, y)])

    while queue:
        i, j = queue.popleft()
        for h, w in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            h, w = h + i, w + j
            if 0 <= h < N and 0 <= w < M and maze[h][w] == 1:
                queue.append((h, w))
                maze[h][w] = maze[i][j] + 1


if __name__ == "__main__":
    N, M = list(map(int, input().split()))

    maze = []
    for _ in range(N):
        row = list(map(int, list(input())))
        maze.append(row)

    for x in range(N):
        for y in range(M):
            if maze[x][y] == 1:
                bfs(x, y)

    print(maze[N - 1][M - 1])