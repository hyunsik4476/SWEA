"""
1234: 대칭 숫자 검사
"""

import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, input_num = input().split()
    N = int(N)
    lst = list(input_num)


    # for i in range(1, N):
    #     check = 0
    #     for j in range(N//2):
    #         if i-1-j >= 0 and i+j < len(lst):
    #             if lst[i-1-j] != lst[i+j]:
    #                 break
    #             else:
    #                 print(lst)
    #                 lst.pop(i+j)
    #                 lst.pop(i-1-j)
    #                 print(lst)
    i = 0
    for _ in range(N):
        while 1:
            if i+1 < len(lst) and lst[i] == lst[i+1]:
                lst.pop(i+1)
                lst.pop(i)
                i -= 1
            else: break
            
        i += 1


    ans = ''.join(lst)
    print(f'#{tc} {ans}')