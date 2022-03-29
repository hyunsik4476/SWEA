from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0]*N
    time = [[0]*25 for _ in range(N+1)]
    for l in range(N):
        st, et = map(int, input().split())
        arr[l] = [et, et-st]
    arr.sort()

    for j in range(1, N+1):
        t, dt = arr[j-1]
        for i in range(1, 25):
            if i >= t:
                time[j][i] = max(time[j-1][i], time[j-1][t-dt] + 1)
            else:
                time[j][i] = time[j-1][i]

    print(f'#{tc} {time[-1][-1]}')