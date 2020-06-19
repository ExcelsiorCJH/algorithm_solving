'''
Q4839 - 이진탐색
'''

def bin_search(l, r, tg):
    cnt = 0
    while l < r:
        c = int((l+r)/2)
        if tg == c:
            return cnt+1
        elif c > tg:
            r = c
        else:
            l = c
        cnt += 1
    return cnt


# 재귀함수
# def bin_search(l, r, tg, cnt=0):
#     c = int((l+r)/2)
#     if c < tg:
#         l = c
#     elif c > tg:
#         r = c
#     if tg == c:
#         return cnt+1
#     return bin_search(l, r, tg, cnt+1)


T = int(input())

for t_idx in range(T):
    p, pa, pb = list(map(int, input().split()))
    cnt_a = bin_search(1, p, pa)
    cnt_b = bin_search(1, p ,pb)

    winner = 'A' if cnt_a < cnt_b else 'B'
    if cnt_a == cnt_b:
        winner = 0

    print(f'#{t_idx+1} {winner}')