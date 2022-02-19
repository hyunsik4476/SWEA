'''
우주선 착륙
'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[9]+list(map(int, input().split()))+[9] for _ in range(N)]
    arr = [[9]*(M+2)] + arr + [[9]*(M+2)]
    dxy = [[-1,-1], [0,-1], [1,-1], [-1,0], [1,0], [-1,1], [0,1], [1,1]]


    ans = 0 # 갯수
    for y in range(1, N+1):
        for x in range(1, M+1):
            cnt = 0  # 주변 체크
            for dx, dy in dxy:
                if arr[y][x] > arr[y+dy][x+dx]:
                    cnt += 1
            if cnt >= 4:
                ans += 1

    print(f'#{tc} {ans}')