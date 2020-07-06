'''
Q4871 -  그래프 경로
'''
def DFS_with_stack(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    
    return visited


T = int(input())

for t_idx in range(1, T+1):
    V, E = list(map(int, input().split()))

    graph = []
    for _ in range(E):
        start, end = list(map(int, input().split()))
        graph.append((start, end))

    S, G = list(map(int, input().split()))

    N = {idx: set() for idx in range(1, V+1)}
    for edge in graph:
        start, end = edge
        N[start].add(end)

    if G in DFS_with_stack(N, S):
        print(f'#{t_idx} 1')
    else:
        print(f'#{t_idx} 0')