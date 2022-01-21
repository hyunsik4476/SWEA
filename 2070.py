'''
대, 소 구별
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    input_map = list(map(int,input().split()))
    if input_map[0] > input_map[1]:
        print(f'#{i} >')
    elif input_map[0] < input_map[1]:
        print(f'#{i} <')
    else:
        print(f'#{i} =')