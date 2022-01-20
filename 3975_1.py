import sys
sys.stdin = open('input.txt')

T = int(input())


for idx in range(T):
    # lst = []
    # lst = [num for num in (map(int,input().split()))]
    # print(lst)

    A, B, C, D = map(int,input().split())

    print(f'#{idx} ', end ='')

    if A / B > C / D:
        print('ALICE')
    elif A / B < C / D:
        print('BOB')
    else:
        print('DRAW')