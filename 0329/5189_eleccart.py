def perm(idx, sum):
    global ans
    if sum > ans:
        return

    if idx == N:
        sum += arr[p[idx-1]-1][0]
        if ans > sum:
            ans = sum
        return

    else:
        for i in range(1, N):
            if not used[i]:
                used[i] = True
                p[idx] = route[i]
                perm(idx+1, sum + arr[p[idx-1]-1][p[idx]-1])
                used[i] = False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    route = [i for i in range(1, N+1)]
    ans = 1100
    p = [1]*(N+1)
    used = [0]*N
    perm(1, 0)
    print(f'#{tc} {ans}')
