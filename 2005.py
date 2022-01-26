"""
2005: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    num = int(input())
    lst = [1]
    print(f'# {i}')
    
    for idx in range(1, num + 1):
        print(*lst)
        tmp_lst = [1]

        if idx == 1:
            lst = [1, 1]

        else:
            for num in range(1, idx):
                tmp_lst.append(lst[num] + lst[num - 1])
            tmp_lst.append(1)
            lst = tmp_lst