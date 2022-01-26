"""
2001: 문제명을 입력해주세요 :)
n*n 판에서 m*m 크기 합 중 최댓값 구하기
간단한 방법 없나?
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    n, m = map(int, input().split())
    lst_2d = []
    max_num =0
    cnt = 0

    for idx in range(n):
        lst_2d.append(list(map(int, input().split())))

    # n-m+1 제곱만큼 체크
    # 00 01 02/ 10 11 12/ 20 21 22
    
    for i2 in range(n-m+1): #세로 체크
        for i1 in range(n-m+1): # 가로 체크
            tmp_num = 0
            
            for j1 in range(m): # 33합
                tmp_num += sum(lst_2d[cnt + j1][i1: i1 + m])
            if tmp_num >= max_num:
                max_num = tmp_num
        
        cnt += 1

    print(f'#{i} {max_num}')
