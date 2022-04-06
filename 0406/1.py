def bfs(stx, sty):
    q = []
    q.append((stx, sty))
    visited = [[0]*N for _ in range(N)]
    visited[sty][stx] = 1
    while q:
        x, y = q.pop(0)
        if arr[y][x] == 2:
            return visited[y][x]
        for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and visited[ny][nx] ==0 and arr[ny][nx] != 1:
                q.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

    return 0

