# 교수님 코드

def f(A, N):
    d = [[1000000]*N for _ in range(N)] # visited
    q = [(0, 0)]
    d[0][0] = 0
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1],[1, 0], [0, -1], [-1, 0]]:
            ni, nj = i+di, j+dj
            if N > ni >= 0 and N > nj >= 0:
                # 이 부분 코드가 훨씬 깔끔해짐
                diff = arr[ni][nj] - arr[i][j] if arr[ni][nj] > arr[i][j] else 0
                if d[ni][nj] > d[i][j] + diff + 1:
                    d[ni][nj] = d[i][j] + diff + 1
                    q.append((ni, nj))
    return d[N-1][N-1]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    print(f'#{tc} {f(arr, N)}')