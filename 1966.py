"""
1966: 다른 정렬 방법?
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    x = int(input())
    input_lst = list(map(int, input().split()))

    for j in range(x):
        for i in range(1, x):
            if input_lst[i-1] >= input_lst[i]:
                        
                tmp_num = input_lst[i-1]
                input_lst[i-1] = input_lst[i]
                input_lst[i] = tmp_num
    print(f'#{idx} ', end = '')
    print(*input_lst)