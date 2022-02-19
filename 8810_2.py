'''
고구마밭
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    check = 1
    max_check = 1
    cnt = 0

    for i in range(1, N):
        if lst[i] > lst[i-1]:
            check += 1
            if check > max_check:
                max_check = check
        else:
            if check >= 2:
                cnt += 1
            check = 1

    if check >= 2:
        cnt += 1

    tot = lst[0]
    max_tot = 0
    check = 1

    for j in range(1, N):
        if lst[j] > lst[j-1]:
            check += 1
            tot += lst[j]
            if check == max_check:
                if tot > max_tot:
                    max_tot = tot
        else:
            check = 1
            tot = lst[j]

    print(f'#{tc} {cnt} {max_tot}')