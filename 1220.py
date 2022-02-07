"""
1220: 
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
        
    return col_check


T = 10

for idx in range(1, T+1):
    lst=[]
    num = int(input())
    for _ in range(100):
        lst.append(list(map(int, input().split())))
    
    col_check = [0]*100

    for x in range(100):
        col_check = check(lst, col_check, x)

    print(f'#{idx} {sum(col_check)}')