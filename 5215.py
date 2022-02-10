"""
5215: 
"""

import sys
sys.stdin = open('input.txt')

def hamb(idx, cal, lst, check, tot_p, tot_c):
    global result
    
    if tot_c > cal:
        return
    if tot_p > result:
        result = tot_p      
    if idx == N:
        return

    check[idx] = 1  

    point, c = lst[idx][0], lst[idx][1]
    if tot_c <= cal:
        hamb(idx+1, cal, lst, check, tot_p+point, tot_c+c)
        check[idx] = 0
        hamb(idx+1, cal, lst, check, tot_p, tot_c)

T = int(input())

for tc in range(1, T+1):
    result = 0
    N, cal = map(int, input().split())
    lst = [0]*N
    for i in range(N):
        lst[i] = list(map(int, input().split()))
    
    check = [0]*N
    answer = hamb(0, cal, lst, check, 0, 0)
    print(f'#{tc} {result}')