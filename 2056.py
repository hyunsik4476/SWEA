"""
2056: 달력
날짜의 유효성 판단 후 'YYYY/MM/DD' 로 출력
유효하지 않을 경우 -1 출력
"""
'''
조건 더 간단하게 못바꾸나?
'''

import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    YMD = input()
    year = YMD[:4]
    month = YMD[4:6]
    day = YMD[6:]

    print(f'#{i} ', end = '')
    if int(month) > 0:
        if int(month) == 2:
            if 28 >= int(day) >= 1:
                print(f'{year}/{month}/{day}')
            else:
                print(-1)
        elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
            if 30 >= int(day) >= 1:
                print(f'{year}/{month}/{day}')
            else:
                print(-1)
        else:
            if 31 >= int(day) >= 1:
                print(f'{year}/{month}/{day}')
            else:
                print(-1)
    else:
        print(-1)