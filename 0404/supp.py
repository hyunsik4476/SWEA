def bfs(si, sj, ei, ej):
    q = []  # [1] q, v 생성
    v = [[100000] * N for _ in range(N)]    # INF

    q.append((si, sj))
    v[si][sj] = arr[si][sj]

    while q:
        ci, cj = q.pop(0)

        # 네방향/8방향/숫자차이가 일정값이하
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] > v[ci][cj] + arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + arr[ni][nj]

    return v[ei][ej]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = bfs(0, 0, N - 1, N - 1)
    print(f'#{test_case} {ans}')