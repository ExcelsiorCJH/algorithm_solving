'''
Q4861 - 회문
'''

T = int(input())

for t_idx in range(1, T+1):
    N, M = list(map(int, input().split()))

    row_list = []
    for _ in range(N):
        row_list.append(input())
    
    col_list = []
    for c_idx in range(N):
        tmp = ''
        for r_idx in range(N):
            tmp += row_list[r_idx][c_idx]
        col_list.append(tmp)

    total_list = row_list + col_list
    for row in total_list:
        for idx in range(N):
            if M+idx > N:
                break
            s = row[idx:M+idx]
            if s == s[::-1]:
                print(f'#{t_idx} {s}')
                break