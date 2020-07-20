'''
Q4874 - Forth
'''

def calculator(num1, num2, op):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '/':
        result = num1 // num2
    elif op == '*':
        result = num1 * num2
    return result


T = int(input())

for t_idx in range(1, T+1):
    eq_list = input().split()[::-1]

    stack = []
    answer = 0

    while eq_list:
        x = eq_list.pop()
        if x.isdigit():
            stack.append(int(x))
        else:
            try:
                if x == '.' and len(stack) == 1:
                    answer = stack.pop()
                else:
                    num2 = stack.pop()
                    num1 = stack.pop()
                    stack.append(calculator(num1, num2, x))
            except:
                answer = 'error'

    print(f'#{t_idx} {answer}')