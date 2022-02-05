"""
2805: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    N = int(input())
    lst = []
    sum = 0

    for _ in range(N):
        lst.append(list(map(int, list(input()))))

    for y in range(N):
        for x in range(N):
            if N-1 + N//2 >= x+y >= N//2 and N//2 >= x-y>= -(N//2):
                sum += lst[y][x]
    print(f'#{idx} {sum}')