"""
1493: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # arr = [[0]*101 for _ in range(101)]
    p, q = map(int, input().split())
    px, py, qx, qy = -1, -1, -1, -1
    x, y = 1, 1
    max_y = 1
    i = 1
    ans = 0
    while 1:        
        # print(f'x, y, i = {x}, {y}, {i}')
        # arr[y][x] = i
        if i == p:
            px, py = x, y
        if i == q:
            qx, qy = x, y
        if x == (px+qx) and y == (py + qy):
            ans = i
            break
        i += 1
        x += 1
        y -= 1
        if y == 0:
            x = 1
            y = max_y+1
            max_y = y
    print(f'#{tc} {ans}')