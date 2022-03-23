from collections import deque


def bfs(stx, sty):
    global N, M, ans
    visited = [[0] * N for _ in range(N)]
    visited[sty][stx] = 1
    q = deque()
    q.append([stx, sty])
    k = 1
    house = 0
    if arr[sty][stx] == 1:
        house += 1

    while q:
        x, y = q.popleft()

        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and visited[ny][nx] == 0:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1
                if visited[ny][nx] > k:
                    k = visited[ny][nx]
                if arr[ny][nx] == 1:
                    house += 1

        if (k*k +(k-1)*(k-1)) <= house * M:
            if house > ans:
                ans = house


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1

    for j in range(N):
        for i in range(N):
            bfs(i, j)
    print(f'#{tc} {ans}')