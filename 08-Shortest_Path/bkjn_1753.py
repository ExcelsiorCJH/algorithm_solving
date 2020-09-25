"""
1753. 최단경로

https://www.acmicpc.net/problem/1753

힌트: Dijkstra
주의: 해당 풀이는 Pypy3로 제출해야지 통과함 (python3는 시간초과 뜸)
"""
import heapq
from collections import defaultdict


V, E = list(map(int, input().split()))
start = int(input())

graph = defaultdict(list)
for _ in range(E):
    u, v, w = list(map(int, input().split()))
    graph[u].append((v, w))

# Q = [(가중치, 정점)]
Q = [(0, start)]
dist = defaultdict(int)
while Q:
    weight, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = weight
        for v, w in graph[node]:
            alt = w + weight
            heapq.heappush(Q, (alt, v))

for idx in range(1, V + 1):
    print(dist.get(idx, "INF"))