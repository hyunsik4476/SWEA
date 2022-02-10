T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    lst = list(map(int, input().split()))
    num_minus = 1
    check = 0

    while 1:
        for i in range(8):
            lst[i] = lst[i] - num_minus

            if lst[i] <= 0:
                lst[i] = 0
                check = 1
                break

            num_minus %= 5
            num_minus += 1

        if check == 1:
            break

    idx = lst.index(0)
    ans = lst[idx+1:] + lst[:idx+1]
    print(f'#{tc} ', end='')
    print(*ans)
