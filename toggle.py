from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for k in range(1, M+1):
        if M % k == 0:
            for y in range(N):
                for x in range(N):
                    arr[y][x] = int(not arr[y][x])
        else:
            # print(k, end = ' ')
            for y in range(N):
                for x in range(N):
                    if (y+x+2) % k == 0:
                        arr[y][x] = int(not arr[y][x])

    ans = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x]:
                ans += 1

    # pprint(arr)
    print(f'#{tc} {ans}')