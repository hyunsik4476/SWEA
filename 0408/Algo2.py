def find_start():
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:
                return [x, y]


def dfs(x, y, dist):
    global ans
    visited[y][x] = 1
    if dist >= ans:
        return

    if arr[y][x] == 3:
        if ans > dist:
            ans = dist
        return
    else:
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and arr[ny][nx] != 1 and visited[ny][nx] == 0:
                dfs(nx, ny, dist+1)


def comb(idx, r, tmp):
    if len(tmp) == r:
        p.append(tmp)
        return

    for i in range(idx, len(wall_lst)):
        comb(i+1, r, tmp + [wall_lst[i]])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 100   # 8x8 이 최대이므로 100보다 작음
    stx, sty = find_start()

    wall_lst = []   # 1인 좌표 모두 구하기
    for j in range(N):
        for i in range(N):
            if arr[j][i] == 1:
                wall_lst.append([i, j])
    p = []          # 벽을 지울 수 있는 경우의 수
    comb(0, 2, [])

    for wall1, wall2 in p:
        visited = [[0] * N for _ in range(N)]   # 방문배열 초기화
        x1, y1 = wall1
        x2, y2 = wall2
        arr[y1][x1] = 0
        arr[y2][x2] = 0
        dfs(stx, sty, 1)    # 모든 경우의 수 검사
        arr[y1][x1] = 1
        arr[y2][x2] = 1

    if ans == 100: # 못찾으면
        ans = -1

    print(f'#{tc} {ans}')