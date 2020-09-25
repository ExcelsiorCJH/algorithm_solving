"""
1504. 특정한 최단경로

https://www.acmicpc.net/problem/1504

힌트 : Dijkstra + 응용

input
------
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

result
------
7
"""

import heapq
from collections import defaultdict


def dijkstra(start_v):
    dist = defaultdict(int)
    Q = [(0, start_v)]
    while Q:
        length, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = length
            for v, w in graph[node]:
                alt = length + w
                heapq.heappush(Q, (alt, v))
    return dist


if __name__ == "__main__":
    N, E = list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(E):
        u, v, w = list(map(int, input().split()))
        graph[u].append((v, w))
        graph[v].append((u, w))

    v1, v2 = list(map(int, input().split()))
    dist1 = dijkstra(1)
    dist2 = dijkstra(v1)
    dist3 = dijkstra(v2)

    flag1, flag2 = 0, 0
    if (
        dist1.get(v1, "INF") != "INF"
        and dist2.get(v2, "INF") != "INF"
        and dist3.get(N, "INF") != "INF"
    ):
        result1 = dist1[v1] + dist2[v2] + dist3[N]
    else:
        flag1 = 1

    if (
        dist1.get(v2, "INF") != "INF"
        and dist3.get(v1, "INF") != "INF"
        and dist2.get(N, "INF") != "INF"
    ):
        result2 = dist1.get(v2, "INF") + dist3.get(v1, "INF") + dist2.get(N, "INF")
    else:
        flag2 = 1

    if flag1 and flag2:
        print(-1)
    else:
        print(min(result1, result2))