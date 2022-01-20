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