"""
1984: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):
    lst = list(map(int, input().strip().split()))
    remove_set = {max(lst), min(lst)}
    
    new_lst = [num for num in lst if num not in remove_set]

    ans = round(sum(new_lst) / len(new_lst))

    print(f'#{idx} {ans}')