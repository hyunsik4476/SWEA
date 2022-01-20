'''
시간초과로 실패
'''
'''
불필요한 변환이 실패 요인인가 싶어 방법을 조금 바꿔봤지만 시간이 많이 부족함
'''
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