'''
Q4875 - 미로
'''

def dfs(maze, x, y, directions):
    
    if maze[x][y] == 3:
        return 1
    
    visited = []
    stack = [(x, y)]

    while stack:
        sx, sy = stack.pop()
        if (sx, sy) not in visited:
            visited.append((sx, sy))
            for nx, ny in directions:
                nx += sx
                ny += sy
                if (0 <= nx < N and 0 <= ny < N) and (nx, ny) not in visited:
                    if maze[nx][ny] == 0:
                        stack.append((nx, ny))
                    elif maze[nx][ny] == 3:
                        return 1
    
    tx, ty = visited[-1]
    if maze[tx][ty] == 3:
        result = 1
    else:
        result = 0
    
    return result


T = int(input())

# up, down, left, right
directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

for t_idx in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    for x in range(N):
        for y in range(N):
            if maze[x][y] == 2:
                sx, sy = x, y

    print(f'#{t_idx} {dfs(maze, sx, sy, directions)}')