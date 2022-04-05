from collections import deque


def bfs(stx, sty, edx, edy):
    q = deque()
    q.append((stx, sty))
    arr[sty][stx] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0:
                if input_map[ny][nx] >= input_map[y][x] and arr[ny][nx] > (arr[y][x] + (input_map[ny][nx] - input_map[y][x]) + 1):
                    arr[ny][nx] = (arr[y][x] + (input_map[ny][nx] - input_map[y][x]) + 1)
                    q.append((nx, ny))
                elif input_map[ny][nx] < input_map[y][x] and arr[ny][nx] > arr[y][x] + 1:
                    arr[ny][nx] = arr[y][x] + 1
                    q.append((nx, ny))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    input_map = [list(map(int, input().split())) for _ in range(N)]
    arr = [[100000]*N for _ in range(N)]
    bfs(0, 0, N-1, N-1)
    print(f'#{tc} {arr[-1][-1]}')