from itertools import combinations

T = int(input())
A = list(range(1, 13))

for t_idx in range(T):
    N, K = list(map(int, input().split()))

    l = list(combinations(A, N))
    cnt = 0
    for el in l:
        if sum(el) == K:
            cnt += 1

    print(f'#{t_idx+1} {cnt}')