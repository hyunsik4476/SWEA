"""
스도쿠
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    yx_lst = []
    for n in range(9):
        yx_lst.append(list(map(int, input().split())))
    
    ans = 1
    for y in range(9):
        if len(set(yx_lst[y])) != 9:
            ans = 0
            break
    
    for x in range(9):
        tmp_set = set()
        for y in range(9):
            tmp_set.add(yx_lst[y][x])

        if len(tmp_set) != 9:
            ans = 0
            break

    break_case = 0
    for x in [0, 3, 6]:
        for y in [0, 3, 6]:
            tmp_lst = []

            for cnt in range(3):
                tmp_lst += yx_lst[y+cnt][x: x+3]
            
            if len(set(tmp_lst)) != 9:
                ans = 0
                break_case = 1
                break

        if break_case:
            break

    print(f'#{idx} {ans}')
