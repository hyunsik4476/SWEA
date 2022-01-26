"""
2007: 문제명을 입력해주세요 :)
주어진 조건에서 반복되는 패턴을 전체에서 제거하면 반드시 패턴 길이보다 짧다
20글자였다면..?
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(T):
    str_1 = input()
    for i in range(1, 11):
        if str_1[: i] == str_1[i: 2*i]:
            ans = i
            str_test = str_1.replace(str_1[:i], '')
            if len(str_test) < i:
                break
    print(f'#{idx + 1} {ans}')