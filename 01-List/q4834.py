from collections import Counter


T = int(input())
for t_idx in range(T):
    N = int(input())
    numbers = list(input())
    numbers = list(map(int, numbers))
    numbers = sorted(numbers, reverse=True)

    cnt_dict = Counter(numbers)
    num, cnt = cnt_dict.most_common(n=1)[0]

    print(f'#{t_idx+1} {num}, {cnt}')