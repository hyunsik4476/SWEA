"""
시간 더하기
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    h_ans = h1 + h2
    m_ans = m1 + m2

    if m_ans >= 60:
        h_ans += 1
        m_ans -= 60
    if h_ans > 12:
        h_ans -= 12
    
    print(f'#{idx} {h_ans} {m_ans}')