"""
2817: 
"""

import sys
sys.stdin = open('input.txt')

def powersum(i, lst, ischecked, checkingnum, tot):
    global ans
    if tot > checkingnum:
        return
    if i > N-1:
        # tot = 0
        # for j in range(N):
        #     if ischecked[j]:
        #         tot += lst[j]
        if tot == checkingnum:
            ans +=1
        return

    ischecked[i] = 1
    powersum(i+1, lst, ischecked, checkingnum, tot + lst[i])

    ischecked[i] = 0
    powersum(i+1, lst, ischecked, checkingnum, tot)

T = int(input())

for idx in range(1, T+1):
    ans = 0
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))
    powersum(0, lst, [0]*N, K, 0)
    print(f'#{idx} {ans}')