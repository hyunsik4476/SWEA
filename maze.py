def f(x, y):        # 이어진 길 모두 검사하기
    global ans      # 답 저장용
    # print(arr[y][x])
    if arr[y][x] == 3:  # 도착하면 답에 1 저장하고 리턴
        ans = 1
        return 1
    else:               # 그 외 경우에
        if arr[y][x] == 0 or arr[y][x] == 2:    # 현재 칸이 통로/ 시작점이면
            for dy, dx in [[-1, 0], [0, 1], [1, 0], [0, -1]]:   # 주변 4방향에 대해 검사
                check[y][x] = 1         # 이미 갔던 길 표시용
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and check[ny][nx] == 0:  # 범위가 정상적이고, 가지 않은 길이면
                    if f(nx, ny):          # 해당 범위에 대해 검사
                        return 'success'
                check[y][x] = 0         # 검사가 끝나고 돌아오면 check 클리어
        else:
            return

T = int(input())

for tc in range(1, T+1):
    ans = 0
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]   # 미로
    check = [[0]*N for _ in range(N)]                   # 갔던 길 체크용

    for s_y in range(N):                                # 시작점 찾기
        for s_x in range(N):
            if arr[s_y][s_x] == 2:
                start_y = s_y
                start_x = s_x
    a = f(start_x, start_y)
    print(f'#{tc} {ans}')
    print(a)