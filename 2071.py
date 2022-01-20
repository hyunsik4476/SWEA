'''
평균값 구하기
'''
'''
요구사항에 답안을 반올림하라는게 있음
int() 대신 round()사용함
'''
import sys

sys.stdin = open('input.txt')

T = int(input())
lists = []

for idx in range(T):
    lists.append(list(map(int, input().split())))

for idx in range(T):
    total = 0
    for num in lists[idx]:
        total += num
    ans = total / len(lists[idx])
    print(f'#{idx +1} {round(ans)}')

