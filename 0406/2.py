# 천지창조문제?
def bfs1(islx, isly):
    q = []
    q.append([islx, isly])
    visited = [[0]*N for _ in range(N)]
    visited[isly][islx] = 1
    while q:
        x, y = q.pop(0)
        u.append([x, y])
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and visited[ny][nx] == 0 and arr[ny][nx] == arr[y][x]:
                q.append([nx, ny])
                visited[ny][nx] = 1


def bfs2():
    q = u
    visited = [[0]*N for _ in range(N)]
    for i, j in u:
        visited[j][i] = 1

    while q:
        x, y = q.pop(0)
        if arr[y][x] == 3:
            return visited[y][x]
        for dx, dy in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            nx, ny = x+dx, y+dy
            if N > nx >= 0 and N > ny >= 0 and visited[ny][nx] == 0:
                q.append([nx, ny])
                visited[ny][nx] = visited[y][x] + 1


N = 5
u = []