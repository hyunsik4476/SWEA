"""
1244_1: 카드교환
"""

import sys
sys.stdin = open('input.txt')

def fn(pay_set, n):
    for K in range(int(n)):
        tmp_set = set()
        while pay_set:
            lst = list(pay_set.pop())

            for i in range(len(pay)):
                for j in range(i+1, len(pay)):
                    lst[i], lst[j] = lst[j], lst[i]
                    tmp_set.add(''.join(lst))
                    lst[i], lst[j] = lst[j], lst[i]

        pay_set = tmp_set
    return pay_set

T = int(input())

for idx in range(1, T+1):
    pay, n = input().split()
    pay_set = set([pay])

    if int(n) <= len(pay):

        pay_set = fn(pay_set, n)

        print(f'#{idx} {max(map(int, pay_set))}')

    elif int(n) >= len(pay) and (int(n)-len(pay)) % 2 == 0:
        n = len(pay)

        pay_set = fn(pay_set, n)
        
        print(f'#{idx} {max(map(int, pay_set))}')

    else:
        n = len(pay)

        pay_set = fn(pay_set, n)
        
        max_lst = list(str(max(map(int, pay_set))))
        max_lst[-1], max_lst[-2] = max_lst[-2], max_lst[-1]
        a = ''.join(max_lst)
        print(f'#{idx} {a}')