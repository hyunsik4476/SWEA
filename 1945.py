"""
1945: 소인수분해
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    input_num = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while input_num > 1:
        if input_num % 2 == 0:
            input_num = input_num//2
            a += 1

        elif input_num % 3 == 0:
            input_num = input_num//3
            b += 1

        elif input_num % 5 == 0:
            input_num = input_num//5
            c += 1

        elif input_num % 7 == 0:
            input_num = input_num//7
            d += 1

        elif input_num % 11 == 0:
            input_num = input_num//11
            e += 1
    
    print(f'#{idx}', a, b, c, d, e)
