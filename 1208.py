"""
1208: 
"""

import sys
sys.stdin = open('input.txt')

T = 10

for idx in range(1, T+1):
    num = int(input())
    lst = list(map(int, input().split()))

    for _ in range(num):        
        if max(lst) - min(lst) <= 1:
            break

        i = lst.index(max(lst))
        j = lst.index(min(lst))
        lst[i] -= 1
        lst[j] += 1

    print(f'#{idx} {max(lst) - min(lst)}')