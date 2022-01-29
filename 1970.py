"""
1970: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    fee = int(input())
    fee = fee//10 * 10
    money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    ans_lst = []

    for money in money_lst:
        cnt = 0
        
        while 1:
            if fee - money*cnt < 0:
                cnt -= 1
                break
            cnt += 1
        
        fee = fee - money*cnt

        ans_lst.append(cnt)

    print(f'#{idx}')
    print(*ans_lst)