'''
q4869 - 종이붙이기
'''

def calc(n):
    l = [0, 1]
    for idx in range(2, n+1):
        if idx % 2 == 0:
            l.append(l[idx-1]*2 + 1)
        else:
            l.append(l[idx-1]*2 - 1)
    
    return l[-1]

T = int(input())

for t_idx in range(1, T+1):
    N = int(input()) // 10

    print(f'#{t_idx} {calc(N)}')
