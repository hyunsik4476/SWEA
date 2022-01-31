"""
1285: 돌던지기
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    people_num = int(input())
    stone_pos = list(map(int, input().split()))
    distance = 100000
    cnt = 0

    for pos in stone_pos:
        if abs(pos) < distance:
            distance = abs(pos)

    for pos in stone_pos:
        if abs(pos) == distance:
            cnt += 1

    print(f'#{idx} {distance} {cnt}')
        