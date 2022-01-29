"""
1959: 곱하기
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    ans = 0
    n, m = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))

    if n > m:
        
        for i in range(n-m+1): # 3, 2 면 2번 체크해야함/ 체크 시작점 좌표
            result_1 = 0
            # result_2 = 0

            new_lst_1 = n_lst[i: i+m] # 0 ~ m - 1 까지 m 개
            # new_lst_2 = n_lst[i: i+m] # 1 ~ m 까지 m 개
            
            for j in range(m): # 세로곱
                result_1 += m_lst[j] * new_lst_1[j]
                # result_2 += m_lst[j] * new_lst_2[j]

            if result_1 >= ans:
                ans = result_1
            else:
                ans = ans
    
    elif n < m:
        
        for i in range(1, m-n+1): # 3, 2 면 2번 체크해야함/ 체크 시작점 좌표
            result_1 = 0
            # result_2 = 0

            new_lst_1 = m_lst[i: i+n] # 0 ~ m - 1 까지 m 개
            # new_lst_2 = m_lst[i: i+n] # 1 ~ m 까지 m 개
            # print(new_lst_2)
            
            for j in range(n): # 세로곱
                result_1 += n_lst[j] * new_lst_1[j]
                # result_2 += n_lst[j] * new_lst_2[j]

            if result_1 >= ans:
                ans = result_1
            else:
                ans = ans

    else:

        for i in range(n):
            ans += n_lst[i] * m_lst[i]
        
    print(f'#{idx} {ans}')