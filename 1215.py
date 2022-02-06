"""
1215: 
"""

import sys
sys.stdin = open('input.txt')

T = 10

for idx in range(1, T+1):
    ans = 0
    lst = []
    n = int(input())
    for _ in range(8):
        lst.append(list(input()))
    #가로검사
    for y in range(8):
        for x in range(9-n):
            str_x = ''.join(lst[y][x: x+n])
            if str_x == str_x[::-1]:                
                ans += 1
    #세로검사
    for x in range(8):
        str_y = ''
        for y in range(8):
            str_y += lst[y][x]
        for i in range(9-n): # 0 ~ 7, n = 3
            str_y2 = str_y[i:i+n] # 0 ~ 3, 5 ~ 8
            if str_y2 == str_y2[::-1]:
                ans += 1

    print(f'#{idx} {ans}')