# 쇠막대기자르기
T = int(input())

for tc in range(1, T+1):
    input_str = input()
    new_str_lst = list(input_str)
    N = len(new_str_lst)

    for l in range(N-1):
        if new_str_lst[l] == '(' and new_str_lst[l+1] == ')':
            new_str_lst[l] = 0

    laser_lst = []
    stick_lst = []

    for p in range(N):
        if new_str_lst[p] == '0':
            laser_lst.append(p)
    M = len(laser_lst)

    idx = 0
    while idx < N-M:
        for i in range(N-1):
            if new_str_lst[i] == '(' and new_str_lst[i+1] == '0':
                j = i
            if new_str_lst[i] == '(' and new_str_lst[i+1] == '1':
                j = i

        for i2 in range(j, N):
            if new_str_lst[i2] == ')':
                k = i2
                break
        stick_lst.append([j, k])
        new_str_lst[j], new_str_lst[k] = '1', '1'
        idx += 2

    ans = 0
    for stick in stick_lst:
        tot = 1
        for laser in laser_lst:
            if stick[0] < laser < stick[1]:
                tot += 1
        ans += tot
    print(f'#{tc} {ans}')
