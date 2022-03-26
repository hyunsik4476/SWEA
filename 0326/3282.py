def dfs(idx, vol, tot):
    global ans
    global K
    if vol > K:
        return
    if idx >= len(lst):
        if tot > ans:
            ans = tot
        return
    for i in range(idx, len(lst)):
        dfs(i+1, vol+lst[i][0], tot+lst[i][1])
        dfs(i+1, vol, tot)


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = []
    ans = 0
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    dfs(0, 0, 0)
    print(f'#{tc} {ans}')

