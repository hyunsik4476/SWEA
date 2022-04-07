# 3차원 visited 배열 써보기( = 벽2개 부수고 가기)
from collections import deque
from pprint import pprint


def bfs(stx, sty):
    q = deque()
    cnt = 2
    q.append((stx, sty, cnt))
    visited = [[[0]*M for _ in range(N)] for _ in range(3)]
    for i in range(cnt+1):
        visited[i][0][0] = 1
    while q:
        x, y, cnt = q.popleft()
        if arr[y][x] == 2:
            pprint(visited)
            return
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if M > nx >= 0 and N > ny >= 0 and visited[cnt][ny][nx] == 0:
                if cnt > 0:
                    if arr[ny][nx] == 1 and visited[cnt-1][ny][nx] == 0:
                        visited[cnt-1][ny][nx] = visited[cnt][y][x] + 1
                        q.append((nx, ny, cnt-1))
                    elif arr[ny][nx] != 1 and visited[cnt][ny][nx] == 0:
                        visited[cnt][ny][nx] = visited[cnt][y][x] + 1
                        q.append((nx, ny, cnt))

                elif arr[ny][nx] != 1:
                    visited[cnt][ny][nx] = visited[cnt][y][x] + 1
                    q.append((nx, ny, cnt))




N, M = map(int, input().split())    # M*N 맵
arr = [list(map(int, input())) for _ in range(N)]
arr[-1][-1] = 2
bfs(0, 0)