"""
1209: 
"""

import sys
sys.stdin = open('input.txt')

T = 10

for idx in range(1, T+1):
    tc_num = int(input())
    lst = []
    ans = 0

    for _ in range(100):
        tmp = list(map(int, input().split()))
        lst.append(tmp)
        if sum(tmp) >= ans:
            ans = sum(tmp)
    
    for x in range(100):
        tot = 0
        for y in range(100):
            tot += lst[y][x]
        if tot >= ans:
            ans = tot
    
    tot, x = 0, 0
    for y in range(100):
        tot += lst[y][x]
        x += 1
    if tot >= ans:
        ans = tot
        
    tot, y = 0, 0
    for x in range(-1, -101, -1):
        tot += lst[y][x]
        y += 1
    if tot >= ans:
        ans = tot

    print(f'#{idx} {ans}')