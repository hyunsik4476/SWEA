"""
1946: 알파벳쌍
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    n = int(input())
    alp_dict = dict()
    ans_lst = []
    ans_str = ''
    cnt = 0

    for i in range(n): # 딕셔너리 만들기
        a, num = input().split() # 문자열/ 갯수
        num = int(num)
        alp_dict[a] = num

    for alp in alp_dict:
        for alp_num in range(alp_dict[alp]):
            ans_str += alp
            cnt += 1

            if cnt == 10:
                ans_str += '\n'
                cnt = 0
    print(f'#{idx}')
    print(ans_str)