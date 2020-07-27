"""
Q4865 - 글자수
"""
T = int(input())

for t_idx in range(1, T+1):
    dic = {key: 0 for key in str1}
    
    for key in str2:
        try:
            dic[key] += 1 
        except:
            continue
    
    print(f'#{t_idx} {max(dic.values())}')