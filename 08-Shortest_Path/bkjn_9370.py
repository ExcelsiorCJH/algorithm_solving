"""
9370. 미확인 도착지

https://www.acmicpc.net/problem/9370

힌트: Dijkstra + 응용
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
                alt = w + length
                heapq.heappush(Q, (alt, v))
    return dist


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, t = list(map(int, input().split()))
        s, g, h = list(map(int, input().split()))

        graph = defaultdict(list)
        for _ in range(m):
            a, b, d = list(map(int, input().split()))
            graph[a].append((b, d))
            graph[b].append((a, d))
            if (a == g and b == h) or (a == h and b == g):
                dist_g_h = d

        dst_list = []
        for _ in range(t):
            dst_list.append(int(input()))

        s_dijk = dijkstra(s)
        g_dijk = dijkstra(g)
        h_dijk = dijkstra(h)

        dist_s_g = s_dijk[g]
        dist_s_h = s_dijk[h]

        result = []
        for dst in dst_list:
            dist_g_t = g_dijk.get(dst, "INF")
            dist_h_t = h_dijk.get(dst, "INF")
            dist_s_t = s_dijk.get(dst, "INF")

            if dist_g_t == "INF" or dist_h_t == "INF" or dist_s_t == "INF":
                continue

            dist_s_g_h_t = dist_s_g + dist_g_h + dist_h_t
            dist_s_h_g_t = dist_s_h + dist_g_h + dist_g_t

            if dist_s_g_h_t == dist_s_t or dist_s_h_g_t == dist_s_t:
                result.append(dst)

        result.sort()
        print(*result)
