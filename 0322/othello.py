from pprint import pprint

def check(stx, sty, dx, dy, bw):
    x, y = stx, sty
    nx, ny = x+dx, y+dy
    if N>nx>=0 and N>ny>=0 and arr[ny][nx] == bw:
        return 1
    if N>nx>=0 and N>ny>=0 and arr[ny][nx] != bw and arr[ny][nx] != 0:
        r = check(nx, ny, dx, dy, bw)
        if r:
            arr[ny][nx] = bw
            return 1
    return 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # 판의 크기, 점 수
    arr = [[0]*(N) for _ in range(N)]
    # 4: 1~2 6: 2~3 8: 3~4
    for j in range(N//2 - 1, N//2 + 1):
        for i in range(N // 2 - 1, N // 2 + 1):
            if (j+i)%2:
                arr[j][i] = 1
            else:
                arr[j][i] = 2

    for _ in range(M):
        tmpx, tmpy, bw = map(int, input().split())    # 1: 흑 2: 백
        x, y = tmpx-1, tmpy-1
        arr[y][x] = bw
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            check(x, y, dx, dy, bw)

    ans1, ans2 = 0, 0
    for j in range(N):
        ans1 += arr[j].count(1)
        ans2 += arr[j].count(2)

    pprint(arr)
    print(f'#{tc} {ans1} {ans2}')

