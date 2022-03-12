"""
1213: 패턴 검색
"""

import sys
sys.stdin = open('input.txt', encoding='utf-8')

T = 10

for tc in range(1, T+1):
    tc_num =int(input())
    p = input()
    s = input()
    i, j = 0, 0
    cnt = 0
    while i < len(s):
        if s[i] == p[j]:
            if j == len(p)-1:
                cnt += 1
                j = -1
            i += 1
            j += 1
        else:
            if j > 0:
                j = 0
            else:
                i += 1
                j = 0
    print(f'#{tc} {cnt}')
