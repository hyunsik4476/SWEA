"""
1940: RC카
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    total_sec = int(input())
    d = 0
    v = 0

    for sec in range(total_sec):
        mod_input = input()

        if len(mod_input) == 1:
            mod = 0
        else:        
            mod, a = map(int, mod_input.split())

        if mod == 1:
            v += a
        elif mod == 2:
            if v - a > 0:
                v -= a
            else:
                v = 0
        d += v
    print(f'#{idx} {d}')
        