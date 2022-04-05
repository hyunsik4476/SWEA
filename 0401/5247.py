from collections import deque


def bfs(N, T):
    q = deque()
    q.append(N)
    visited[N] = 1

    while q:
        num = q.popleft()
        if num == T:
            return visited[num]

        for op in [num + 1, num -1, num * 2, num - 10]:
            if 1000000 >= op >= 1 and visited[op] == 0:
                q.append(op)
                visited[op] = visited[num] + 1


T = int(input())

for tc in range(1, T+1):
    N, T = map(int, input().split())
    visited = [0]*1000001
    ans = bfs(N, T)
    print(f'#{tc} {ans-1}')