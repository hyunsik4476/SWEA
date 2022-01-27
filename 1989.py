"""
1989: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+ 1):
    str_test = input()
    if str_test == str_test[::-1]:
        print(f'#{idx} 1')
    else:
        print(f'#{idx} 0')