def dfs_stack(i, j):    # dfs의 진행 경로를 찾아낼 수 있음
    stack = []
    visited = [[0]*16 for _ in range(16)]
    stack.append(i, j)  # 시작점 push
    visited[i][j] = 1   # 갈림길 목록에 포함된 칸임을 표시
    while stack:
        i, j = stack.pop()
        if maze[i][j]==3:
            return 1
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj]!=1 and visited[ni][nj]==0:
                stack.append((ni,nj))
                visited[ni][nj] = 1
    return 0
