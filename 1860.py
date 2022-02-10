"""
1860: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 사람 수/ 붕어빵 시간/ 붕어빵 갯수
    lst = sorted(list(map(int, input().split())))
    bbang_lst = [0]*(1 + lst[-1]//M)

    last = 0
    last_idx = 0
    for sec in lst:
        idx = sec//M
        if idx == 0:
            print(f'#{tc} Impossible')
            break
        bbang_lst[idx] = last + (idx-last_idx)*K
        bbang_lst[idx] -= 1
        last = bbang_lst[idx]
        last_idx = idx

        if bbang_lst[idx] < 0:
            print(f'#{tc} Impossible')
            break            

    else:
        print(f'#{tc} Possible')