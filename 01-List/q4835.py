'''
Q4835 - 구간합
'''

T = int(input())
for t_idx in range(T):
    N, M = list(map(int, (input().split())))
    numbers = input()
    numbers = numbers.split()
    numbers = list(map(int, numbers))

    sum_list = []
    for idx in range(len(numbers)):
        tmp = numbers[idx:idx+M]
        if len(tmp) == M:
            sum_list.append(sum(tmp))
    
    diff = max(sum_list) - min(sum_list)
    print(f'#{t_idx+1} {diff}')