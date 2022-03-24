def dfs(stx, sty, x, y, d, visited, eat, idx = 0): # stx, sty 는 고정값 d 는 먹은 디저트 수 visited 는 [x,y] 로 받음
    global ans
    if idx >= 4:
        return

    if d >= 4 and [x, y] == [stx-1, sty+1]:
        if d > ans:
            ans = d
        return 1
    else:
        for dx, dy in [[1, 1], [-1, 1], [-1, -1], [1, -1]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and [nx, ny] not in visited and arr[ny][nx] not in eat:
                dfs(stx, sty, nx, ny, d+1, visited+[nx, ny], eat+[arr[ny][nx]], idx)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for j in range(N):
        for i in range(N):
            dfs(i, j, i, j, 1, [i, j], [arr[j][i]])
    print(f'#{tc} {ans}')
