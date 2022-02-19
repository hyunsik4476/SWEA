from pprint import pprint

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(M-1)+list(map(int, input().split()))+[0]*(M-1) for _ in range(N)]
    arr = [[0]*(N+2*M-2) for _ in range(M-1)]+arr+[[0]*(N+2*M-2) for _ in range(M-1)]

    max_tot = 0
    for y in range(N+M-1):
        for x in range(N+M-1):
            tot = 0
            for i in range(M):
                tot += arr[y+i][x+i]
                tot += arr[y+i][x+M-1-i]
            if M%2 == 1:
                tot -= arr[y+M//2][x+M//2]
            if tot > max_tot:
                max_tot = tot

    print(f'#{tc} {max_tot}')

