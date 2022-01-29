"""
1961: 90도 돌리기
이상한 실수때문에 30분 넘게 고민했음
해결한 문제들은 단계마다 주석을 달던지 해서 헷갈리지말자
"""

import sys
sys.stdin = open('input.txt')

def d90(n,lst):        
    new_lst = []
    for i in range(n):
        new_lst.append([])

    for j in range(n):
        for i in range(n):
            new_lst[j].append(lst[n-i-1][j])
    return new_lst

T = int(input())



for idx in range(1, T+1):
    n = int(input())
    ans_lst = []
    lst = []
    for i in range(n):
        lst.append(list(map(int, input().split())))
    # [0][0] [0][1] [0][2]        [2][0] [1][0] [0][0]    
    # [1][0] [1][1] [1][2] - >    [2][1] [1][1] [0][1]
    # [2][0] [2][1] [2][2]        [2][2] [1][2] [0][2]
    
    print(f'#{idx}')
    for i in range(n):
        lst_1 = d90(n, lst)
        str_1 = ''.join(map(str,lst_1[i]))
        print(str_1, end = ' ')

        lst_2 = d90(n, lst_1)
        str_2 = ''.join(map(str,lst_2[i]))
        print(str_2, end = ' ')

        lst_3 = d90(n, lst_2)
        str_3 = ''.join(map(str,lst_3[i]))
        print(str_3)
    
        


