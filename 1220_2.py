"""
1220_2:
"""

import sys
sys.stdin = open('input.txt')



def check(lst, col_check, x): # 아래로 체크
    cnt = 0
    check_1 = False
    check_2 = False

    for _ in range(100): # y 0에서 99까지 1 밑에 2가 있는지 확인
        if lst[cnt][x] == 1:
            check_1 = True

        if check_1 and lst[cnt][x] == 2:
            col_check[x] += 1
            check_1 = False

        cnt += 1
    
    if x == 99:
        return col_check[x]

    return col_check[x] + check(lst, col_check, x+1)


T = 10

for idx in range(1, T+1):
    lst=[]
    num = int(input())

    for _ in range(100):
        lst.append(list(map(int, input().split())))

    ans = check(lst, [0]*100, 0)

    print(f'#{idx} {ans}')