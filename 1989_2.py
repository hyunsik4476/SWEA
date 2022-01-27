"""
1989_2: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+ 1):
    str_test = input()
    ans = 1
    for i in range(len(str_test)//2):
        if str_test[i] != str_test[-i-1]:
            ans = 0
            break
    print(f'#{idx} {ans}')