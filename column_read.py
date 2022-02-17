T = int(input())

for tc in range(1, T+1):
    lst = [list(input()) for _ in range(5)]
    ans = ''
    length_lst = [len(strs) for strs in lst] # 각 줄마다 길이
    tot = sum(length_lst) # 총 문자 수

    # for i in range(15):
    #     for j in range(5):
    #         try:
    #             ans += lst[j][i]
    #         except:
    #             pass
    k = -1
    idx = 0
    while 1:
        k = k+1
        # if k >= max(length_lst)-1: # 조건이 잘못됨
        if idx == tot:
            break

        for i in range(5): # 세로줄 수
            if k <= length_lst[i]-1:
                ans += lst[i][k] # i번째 줄의 길이는 length_lst[i]
                idx += 1


    print(f'#{tc} {ans}')