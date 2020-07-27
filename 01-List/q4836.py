'''
Q4836 - 색칠하기
'''

T = int(input())
for t_idx in range(T):
    N = int(input())

    colors = []
    for _ in range(N):
        color = list(map(int, input().split()))
        colors.append(color)

    # 2차원 행렬 생성
    arr = [0 for _ in range(10)]
    for i in range(10):
        arr[i] = [0] * 10

    cnt = 0
    for color in colors:
        x_axis = list(range(color[0], color[2]+1))
        y_axis = list(range(color[1], color[3]+1))
        cmap = color[4]
        
        for x in x_axis:
            for y in y_axis:
                arr[x][y] += cmap
                if arr[x][y] == 3:
                    cnt += 1

    print(f'#{t_idx+1} {cnt}')

