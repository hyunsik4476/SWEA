from collections import deque


def bfs(stx, sty):
    global result
    q = deque()
    q.append([stx, sty])
    while q:
        x, y = q.popleft()
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and arr[ny][nx] == arr[y][x]+1:
                visited.add(arr[ny][nx])
                q.append([nx, ny])
                result += 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    ans_i = N**2
    tmp_result = 0
    visited = set()

    for y in range(N):
        for x in range(N):
            if arr[y][x] not in visited:
                visited.add(arr[y][x])
                result = 1
                bfs(x, y)

                if result >= tmp_result:
                    if result == tmp_result and ans_i > arr[y][x]:
                        ans_i = arr[y][x]
                    elif result > tmp_result:
                        ans_i = arr[y][x]
                    ans_r = result
                    tmp_result = result


    print(f'#{tc} {ans_i} {ans_r}')