'''
Q4873 - 반복문자 지우기
'''

T = int(input())

for t_idx in range(1, T+1):
    chars = list(input())[::-1]

    stack = [chars.pop()]
    while chars:
        ch = chars.pop()
        if stack:
            if stack[-1] == ch:
                stack.pop()
            else:
                stack.append(ch)
        else:
            stack.append(ch)
    
    print(f'#{t_idx} {len(stack)}')