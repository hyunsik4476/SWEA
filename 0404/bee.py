def DFS(n, cnt, ssum, lst):
    global sol
    if cnt > C:
        return
    if n == M:
        if sol < ssum:
            sol = ssum
        return

    DFS(n + 1, cnt + lst[n], ssum + lst[n] ** 2, lst)  # 포함 시키는 경우
    DFS(n + 1, cnt, ssum, lst)  # 포함 시키지 않는 경우


T = int(input())
for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # [1] 메모이제이션
    mem = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            sol = 0
            DFS(0, 0, 0, arr[i][j:j + M])
            mem[i][j] = sol

    for i1 in range(N):
        for j1 in range(N - M + 1):
            for i2 in range(i1, N):
                sj = 0
                if i1 == i2:
                    sj = j1 + M
                for j2 in range(sj, N - M + 1):
                    ans = max(ans, mem[i1][j1] + mem[i2][j2])
    print(f'#{test_case} {ans}')