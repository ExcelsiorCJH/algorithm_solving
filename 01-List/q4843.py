'''
Q4843 - 특별한 정렬
'''

T = int(input())

for t_idx in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    sort_list = []
    while numbers:
        max_num = max(numbers)
        min_num = min(numbers)
        
        sort_list.extend([str(max_num), str(min_num)])
        numbers.remove(max_num)
        numbers.remove(min_num)

    print(f"#{t_idx} {' '.join(sort_list[:10])}")