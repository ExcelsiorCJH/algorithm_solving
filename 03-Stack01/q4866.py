'''
Q4866 - 괄호검사
'''

T = int(input())

for t_idx in range(1, T+1):
    chars = input()
    
    stack = []
    flag = True
    for ch in chars:
        if ch in ['{', '(']:
            stack.append(ch)
        elif ch in [')', '}']:
            if stack:
                br = stack.pop()
                if (ch == '}' and br == '(') or \
                    (ch == ')' and br == '{'):
                    flag = False
                    break
            else:
                flag = False
                break

    if stack:
        flag = False

    print(f'#{t_idx} {1 if flag else 0}')