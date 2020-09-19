"""
1260. DFS와 BFS

link: https://www.acmicpc.net/problem/1260
"""
from collections import defaultdict, deque


def dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited


def bfs(start_v):
    visited = []
    queue = deque([start_v])

    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                queue.append(w)
    return visited


if __name__ == "__main__":
    N, M, V = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(M):
        v1, v2 = list(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)
        graph[v1].sort()
        graph[v2].sort()

    print(*dfs(V, []))
    print(*bfs(V))