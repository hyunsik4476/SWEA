"""
1284: 계산
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    P, Q, R, S, W = map(int, input().split()) # A사/ B사 기본료/ B사 초과기준/ B 사 초과금/ 사용량
    ans_1 = P * W

    if W <= R:
        ans_2 = Q 
    else:
        ans_2 = Q + S * (W - R)

    result = min(ans_1, ans_2)

    print(f'#{idx} {result}')