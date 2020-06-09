"""
가장 큰 수와 가장 작은 수의 차이를 출력

#T = 3
#N = 5
# numbers = "477162 658880 751280 927930 297191"
"""

T = int(input('T'))

for idx in range(T):
    _ = int(input('N'))
    
    numbers = input('Numbers')
    numbers = list(map(int, numbers.split()))
    
    min_num = min(numbers)
    max_num = max(numbers)
    
    print(f'#{idx+1} {max_num - min_num}')