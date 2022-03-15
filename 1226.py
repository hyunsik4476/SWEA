from collections import deque


def BFS(node):
    global tc_num
    visited = []
    queue.append(node)

    while queue:
        x, y = queue.popleft()
        visited.append([x, y])
        if arr[y][x] == '3':
            print(f'#{tc_num} 1')
            return
        else:
            for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                nx, ny = x+dx, y+dy
                if arr[ny][nx] != '1' and [nx, ny] not in visited:
                    queue.append([nx, ny])
    print(f'#{tc_num} 0')


T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(input()) for _ in range(16)]
    queue = deque()

    for y in range(16):
        for x in range(16):
            if arr[y][x] == '2':
                sty, stx = y, x

    start = [stx, sty]

    BFS(start)