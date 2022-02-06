"""
가장 긴 길이의 회문 찾기
"""

import sys
sys.stdin = open('input.txt')

T = 10

for idx in range(1, T+1):
    check = 0
    tc_num = int(input())
    lst = []
    for _ in range(100):
        lst.append(list(input())) # lst 0~99
    #가로 검사
    for y in range(100):
        for x in range(100): # 0/99
            for n in range(1, 101-x): # 1 ~ 99/
                if n <= check:
                    continue
                str_1 = ''.join(lst[y][x: x+n]) # x+n: x+1 ~ x+100/[99:100]
                if str_1 == str_1[::-1]:
                    check = n

    for x in range(100):
        str_2 = ''
        for y in range(100): #0            
            str_2 = str_2 + lst[y][x]
        for i in range(101-check):
            for n in range(check, 101-i):
                if n <= check:
                    continue
                str_new = str_2[i: i+n]
                if str_new == str_new[::-1]:
                    check = n
                    
    print(f'#{idx} {check}')