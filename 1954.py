'''
어거지로 풀었음
어떻게 풀어야되지?
채워야 할 칸이 n*n, n-1*n-1,... 으로 점점 줄어듬
'''

T = int(input())

for idx in range(1, T+1):
    n = int(input())

    ans_lst = []
    for i in range(n):
        ans_lst.append([0 for j in range(n)]) # 2차원 배열 초기화

    num = 1 # 추가할거
    cnt = 0 # -1 에 제곱해서 방향바꿀거
    new_n = n # 2번 지나면 1씩 감소할거
    x = -1
    y = 0
    # 아마 여기 루프
    while 1:
        for i_1 in range(new_n):
            x += (1 * (-1)**cnt)
            ans_lst[y][x] = num
            num += 1

        new_n -= 1

        for i_2 in range(new_n):
            y += (1 * (-1)**cnt)
            ans_lst[y][x] = num
            num += 1

        if num > n**2:
            break

        cnt += 1

    print(f'#{idx}')
    for print_i in range(n):
        print(*ans_lst[print_i])