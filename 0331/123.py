def nq(stx, sty):
    global cnt
    if dia_r[stx - sty + (N - 1)] == 1:
        return
    if dia_l[stx + sty] == 1:
        return
    if sty >= N-1:
        cnt += 1
        return

    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            dia_l[stx + sty] = 1
            dia_r[stx - sty + (N - 1)] = 1
            nq(i, sty + 1)
            visited[i] = 0
            dia_l[stx + sty] = 0
            dia_r[stx - sty + (N - 1)] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    visited = [0]*N
    dia_r = [0]*(2*(N - 1) + 1)
    dia_l = [0]*(2*(N - 1) + 1)
    cnt = 0
    for x in range(N):
        visited[x] = 1
        nq(x, 0)
        visited[x] = 0
    print(f'#{tc} {cnt}')