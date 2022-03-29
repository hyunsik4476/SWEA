def dfs(idx, x, y, tmp_sum):
    global ans
    if tmp_sum > ans:
        return
    if idx == 2*N:
        if tmp_sum < ans:
            ans = tmp_sum
        return
    if N > x >= 0 and N > y >= 0:
        tmp_sum += arr[y][x]
        dfs(idx+1, x+1, y, tmp_sum)
        dfs(idx+1, x, y+1, tmp_sum)
    else:
        return


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 9 * 26
    dfs(1, 0, 0, 0)
    print(f'#{tc} {ans}')