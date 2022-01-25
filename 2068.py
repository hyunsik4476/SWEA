'''
최대수 구하기
'''
T = int(input())

for idx in range(1, T + 1):
    ans = max(map(int, input().split()))
    print(f'#{idx} {ans}')