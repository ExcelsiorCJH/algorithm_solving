"""
전기 버스
"""

def solution(K, N, charges):
    K = int(K)
    N = int(N)

    stations = list(range(1, N+1))[::-1]
    l = len(stations)
    charges = list(map(int, charges.split()))

    c_idx = 1
    total_cnt = 0
    while stations and len(stations) > K:
        print(stations)
        cnt = 0
        curr_charges = [c for c in charges if c <= K*c_idx]
        print(curr_charges)
        for _ in range(K):
            curr = stations.pop()
            if curr in curr_charges:
                cnt += 1
                print(cnt)
        
        c_idx += 1
        if cnt >= 1:
            total_cnt += 1
        else:
            return 0

    return total_cnt


if __name__ == "__main__":
    T = int(input())

    for idx in range(T):
        K, N, _ = input().split()
        charges = input()

        answer = solution(K, N, charges)

        print(f'#{idx+1} {answer}')

