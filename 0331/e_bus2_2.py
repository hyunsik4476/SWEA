def dfs(idx, cnt):
    global ans
    if idx > len(lst):
        return
    if cnt > ans:
        return

    dist = lst[idx]
    if idx + dist >= N-1:
        if ans > cnt:
            ans = cnt
        return

    for i in range(idx+1, idx+dist+1):
        dfs(i, cnt+1)



T = int(input())

for tc in range(1, T+1):
    N, *lst = map(int, input().split())
    station = [0]*(N-1)
    ans = N
    dfs(0, 0)
    print(f'#{tc} {ans}')