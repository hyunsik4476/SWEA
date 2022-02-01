"""
1206: 조망권
"""

import sys
sys.stdin = open('input.txt')

T = 50

for idx in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    tot = 0
    skip = 0

    for i in range(2, N-2):
        if skip == 1:
            skip = 2
            continue
        if skip == 2:
            skip = 0
            continue
        
        if lst[i] - lst[i-1] >= 1 and lst[i] - lst[i-2] >= 1:
            if lst[i] - lst[i+1] >= 1 and lst[i] - lst[i+2] >= 1:
                tot += min(lst[i] - lst[i-1], lst[i] - lst[i-2], lst[i] - lst[i+1], lst[i] - lst[i+2])

                skip = 1

    print(tot)