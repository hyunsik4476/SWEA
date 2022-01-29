"""
1948: 날짜 계산
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
cal_dict = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, 
'7': 31, '8': 31, '9': 30, '10': 31, '11': 30, '12': 31}

for idx in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    
    ans = 0
    if m1 < m2:
        for month in range(m1+1, m2): # m1 다음달부터 m2 전달까지
            ans += cal_dict[str(month)]
        ans += (cal_dict[str(m1)] - d1 + 1)
        ans += d2
    else:
        ans = d2 - d1 + 1
    print(f'#{idx} {ans}')