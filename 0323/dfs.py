def dfs(i, x, y, tmp):
    tmp += str(arr[y][x])
    if i == 7:
        if tmp not in ans:
            ans.append(tmp)
        return
    for dx, dy in [[0,1], [0,-1], [1,0], [-1,0]]:
        nx, ny = x+dx, y+dy
        if 4 > nx >= 0 and 4 > ny >= 0:
            dfs(i+1, nx, ny, tmp)


T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = []

    for sty in range(4):
        for stx in range(4):
            dfs(1, stx, sty, '')
    print(f'#{tc} {len(ans)}')
