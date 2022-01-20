'''
리스트에 있는 숫자들 중 홀수들의 합 구하기
'''
'''
맵에서 조건에 맞는 걸 리스트에 넣고(if number % 2)
그 리스트를 요소로 갖는 리스트(lists)를 만들어 총합을 구함
->
맵을 리스트(lists)의 요소로 하고
2번째 for 문에 if문 검사 후 합치는 걸로 변경
'''
import sys
sys.stdin = open('input.txt')

T = int(input())

lists = []
for idx in range(T):
    #lists.append([number for number in map(int, input().split()) if number % 2])
    lists.append(map(int, input().split()))
print(lists)

for idx in range(T):
    total = 0
    numbers = lists[idx]
    for number in numbers:
        if number % 2:
            total += number
    print(f'#{idx + 1} {total}')
