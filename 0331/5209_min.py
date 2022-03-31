def perm(idx, tot):
    global ans
    if tot >= ans:
        return

    if idx == N:
        if tot < ans:
            ans = tot
        return
    else:
        for i in range(N):
            if not used[i]:
                used[i] = 1
                perm(idx + 1, tot + arr[idx][i])
                used[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0]*N
    ans = 99*15
    perm(0, 0)
    print(f'#{tc} {ans}')
