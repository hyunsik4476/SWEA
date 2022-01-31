"""
1288: 양세기
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
for idx in range(1, T+1):
    N = int(input())
    check_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    cnt = 0
    check_set = set()
    while check_lst:
        cnt += 1
        new_n = [num for num in str(N * cnt)]
        check_set.update(new_n)
        # print('check_set = ', check_set)

        for check_num in check_set:
            if check_num in check_lst:
                check_lst.remove(check_num)
        
    print(f'#{idx} {cnt*N}')

    #     for check_num in check_lst:
    #         print(cnt, check_num, check_set)
    #         if check_num in check_set:
    #             check_lst.remove(check_num)
    #         print('check_lst = ', check_lst)
        
    # print(f'#{idx} {cnt*N}')