# import sys
# from pprint import pprint
# sys.stdin = open('sample_input (9).txt', 'r')


def check(input_lst_1):
    cnt = [0]*4
    i = -1
    while i < (len(input_lst_1)):
        while input_lst_1[i] == 1:
            cnt[0] += 1
            i -= 1
        while input_lst_1[i] == 0:
            cnt[1] += 1
            i -= 1
        while input_lst_1[i] == 1:
            cnt[2] += 1
            i -= 1
        while input_lst_1[i] == 0:
            cnt[3] += 1
            i -= 1
        break
    return min(cnt)


def check2(input_lst_2):
    cnt = [0]*32
    i = 0
    j = 0
    while i < (len(input_lst_2)):
        while input_lst_2[i] == 0:
            cnt[j] += 1
            i += 1
        j += 1
        while input_lst_2[i] == 1:
            cnt[j] += 1
            i += 1
        j += 1
        while input_lst_2[i] == 0:
            cnt[j] += 1
            i += 1
        j += 1
        while i < len(input_lst_2) and input_lst_2[i] == 1:
            cnt[j] += 1
            i += 1
        j += 1
    return cnt


pwd = {3211: 0,
       2221: 1,
       2122: 2,
       1411: 3,
       1132: 4,
       1231: 5,
       1114: 6,
       1312: 7,
       1213: 8,
       3112: 9}


T = int(input())

for tc in range(1, T+1):
    M, N = map(int, input().split())    # 세로길이, 가로길이
    arr = [list(map(int, ''.join(list(map(lambda x: format(int(x, 16), '04b'),input()))))) for _ in range(M)]
    ans_lst = []

    for y1 in range(M):
        for x1 in range(N*4 - 1, -1, -1):
            if arr[y1][x1] == 1:
                tmp = arr[y1][x1-55:x1+1]
                k = check(tmp)

                lst = arr[y1][x1-(56*k-1):x1+1]
                if lst and [lst, k] not in ans_lst:
                    ans_lst.append([lst, k])

                arr[y1][x1-(56*k-1):x1+1] = [0]*(56*k)

    p_lst = []
    for lst in ans_lst:
        tmp = check2(lst[0])
        k = lst[1]
        tmp = list(map(lambda x: x//k, tmp))
        p = ''
        for l in range(8):
            tmp_4 = tmp[l*4:l*4 + 4]
            tmp_sum = tmp_4[0]*1000 + tmp_4[1]*100 + tmp_4[2]*10 + tmp_4[3]
            p += str(pwd[tmp_sum])
        p_lst.append(p)

    ans = 0
    for tmp_p in p_lst:
        tmp_lst = list(map(int, tmp_p))
        my_sum = 0

        for o in range(8):
            if o % 2:
                my_sum += tmp_lst[o]
            else:
                my_sum += tmp_lst[o] * 3
        if my_sum % 10 == 0:
            ans += sum(tmp_lst)

    print(f'#{tc} {ans}')
