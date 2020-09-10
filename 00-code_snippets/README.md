# Code Snippets



## 01. Graph

### 1) DFS (Depth-First Search)

```python
graph = {
    1: [2, 3, 4],
    2: [5], 
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}
```



#### 재귀 구조

```python
def recursive_dfs(graph, v, discovered=[]):
    discovered.append(v)
    for w in graph[v]: # graph is dict{int: List}
        if not w in discovered:
            discovered = recursive_dfs(graph, w, discovered)
    return discovered
```



#### 스택을 이용한 반복 구조

```python
def iterative_dfs(graph, start_v):
    discovered = []
    stack = [start_v]
    
    # graph is dict{int: List}
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```



### 2) BFS(Breadth-First Search)

#### Deque를 이용한 반복 구조

```python
from collections import deque

def iterative_bfs(graph, start_v):
    discovered = [start_v]
    queue = deque([start_v])
    # graph is dict{int: List}
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in discovered:
                discovered.append(w)
                queue.append(w)
    return discovered
```



### 3) DFS 동서남북 탐색

```python
# up, down, left, right
directions = [
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
]

def dfs(graph, x, y, directions):
    visited = []
    stack = [(x, y)]

    while stack:
        sx, sy = stack.pop()
        # ch = graph[sx][sy]
        if (sx, sy) not in visited:
            visited.append((sx, sy))
            for nx, ny in directions:
                nx += sx
                ny += sy
                if (
                    (0 <= nx < N and 0 <= ny < N)
                    # and graph[nx][ny] == ch
                    and (nx, ny) not in visited
                ):
                    stack.append((nx, ny))
    return visited
```

