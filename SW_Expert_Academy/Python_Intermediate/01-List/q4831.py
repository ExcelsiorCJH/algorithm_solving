"""
전기 버스
"""

def solution(K, N, c_list):
    K = int(K)
    N = int(N)
    c_list = list(map(int, c_list.split()))
    stations = [0] * (N+1)
    
    for idx in range(1, N+1):
        if idx in c_list:
            stations[idx] = 1
            
    start = 0
    end = K
    cnt = 0
    
    while True:
        zero = 0
        for i in range(start+1, end+1):
            if stations[i] == 1:
                start = i
            else:
                zero += 1

        if zero == K:
            cnt = 0
            break

        cnt += 1
        end = start + K
    
        if end >= N:
            break
            
    return cnt


if __name__ == "__main__":
    T = int(input())

    for idx in range(T):
        K, N, _ = input().split()
        charges = input()

        answer = solution(K, N, charges)

        print(f'#{idx+1} {answer}')

