"""
2606. 바이러스

https://www.acmicpc.net/problem/2606

힌트: 양방향 그래프!
"""
from collections import defaultdict


def dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = dfs(w, visited)
    return visited


if __name__ == "__main__":
    N = int(input())

    graph = defaultdict(list)
    for _ in range(int(input())):
        v1, v2 = list(map(int, input().split()))
        graph[v1].append(v2)
        graph[v2].append(v1)

    print(len(dfs(1, [])) - 1)
