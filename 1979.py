"""
처음에 lst 합으로 접근했다가 포기하고 연속된 1 갯수 세기로 변경
리스트의 마지막에서 답 +1 하는 조건 추가
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    n, m = map(int, input().split())
    yx_lst = []
    for y_idx in range(n):
        yx_lst.append(list(map(int, input().split())))

    ans = 0
    for y in range(n):
        cnt = 0
        for x in range(n): # 5, 3 일 때 range 3  -> 0 1 2
            if yx_lst[y][x] == 1:
                cnt += 1
            else:
                if cnt == m:
                    ans += 1
                cnt = 0
        if cnt == m:
            ans += 1

    for x in range(n):
        cnt = 0
        for y in range(n):
            if yx_lst[y][x] == 1:
                cnt += 1
            else:
                if cnt == m:
                    ans += 1
                cnt = 0
        if cnt == m:
            ans += 1
    print(f'#{idx} {ans}')          
