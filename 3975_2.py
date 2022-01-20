'''
input 을 미리 다 받아서 2차원 배열을 만드는 방식으로 바꿈
->
두 번째 루프에서 리스트를 받아 각 요소에 할당
'''

import sys

sys.stdin = open('input.txt')

T = int(input())
lists = []

for idx in range(T):
    lists.append(map(int, input().split()))

for idx in range(T):
    A, B, C, D = lists[idx]

    print(f'#{idx + 1} ', end ='')
    if A / B > C / D:
        print('ALICE')
    elif A / B < C / D:
        print('BOB')
    else:
        print('DRAW')