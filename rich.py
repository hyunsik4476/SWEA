T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))

    max_num = lst[-1]
    tot = 0
    for i in range(N-1, -1, -1):
        if lst[i] < max_num:
            tot += max_num-lst[i]
        else:
            max_num = lst[i]

    print(f'#{tc} {tot}')
