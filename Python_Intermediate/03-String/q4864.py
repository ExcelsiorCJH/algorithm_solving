'''
Q4864 - 문자열 비교
'''

T = int(input())

for t_idx in range(1, T+1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        print(f'#{t_idx} 1')
    else:
        print(f'#{t_idx} 0')