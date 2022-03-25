def dfs(month, tot):
    global ans
    if month > 12:
        if ans > tot:
            ans = tot
        return
    dfs(month+1, tot+ plan[month]*d1fee)
    dfs(month+1, tot + m1fee)
    dfs(month+3, tot + m3fee)
    dfs(month+12, tot + y1fee)


T = int(input())

for tc in range(1, T+1):
    d1fee, m1fee, m3fee, y1fee = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = 9999
    dfs(1, 0)
    print(f'#{tc} {ans}')