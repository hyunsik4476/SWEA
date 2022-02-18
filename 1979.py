T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(N)]
    lst_x = []
    lst_y = []

    for y in range(N):
        cnt = 0
        x = idx = 0
        while x + idx != N:
            if lst[y][x+idx] == 1:
                cnt += 1
                idx += 1
            elif lst[y][x+idx] == 0:
                if cnt:
                    lst_x.append(cnt)
                cnt = 0
                x = x + idx + 1
                idx = 0
        if cnt:
            lst_x.append(cnt)

    for x in range(N):
        cnt = 0
        y = idx = 0
        while y + idx != N:
            if lst[y+idx][x] == 1:
                cnt += 1
                idx += 1
            elif lst[y+idx][x] == 0:
                if cnt:
                    lst_y.append(cnt)
                cnt = 0
                y = y + idx + 1
                idx = 0
        if cnt:
            lst_y.append(cnt)

    ans = 0
    for num in lst_x:
        if num == K:
            ans += 1
    for num2 in lst_y:
        if num2 == K:
            ans += 1

    print(f'#{tc} {ans}')


