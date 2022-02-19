T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    check = 1 # 연속된 줄기 길이
    max_check = 0
    cnt = 0

    for i in range(1, N):
        if lst[i] > lst[i-1]:
            check += 1 # 줄기 길이 증가
        else:
            if check >= 2:
                cnt += 1

            if check > max_check:
                max_check = check

            check = 1

    if check >= 2:
        cnt += 1
    if check > max_check:
        max_check = check


    gogu_lst = []
    check = 1
    for i in range(1, N):
        if lst[i] > lst[i-1]:
            check += 1 # 줄기 길이 증가
        else:
            if check == max_check:
                gogu_lst.append(i-check)
            check = 1
    if check == max_check:
        gogu_lst.append(N - check)

    max_tot = 0
    max_idx = 0
    for idx in gogu_lst:
        tot = 0
        for k in range(max_check):
            tot += lst[idx+k]
        if tot > max_tot:
            max_tot = tot
            max_idx = idx


    print(f'#{tc} {cnt} {max_tot}')