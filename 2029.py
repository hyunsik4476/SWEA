'''
몫과 나머지 출력하기, print(f_'') _ 부분 띄어쓰지 말 것
'''
T = int(input())
for idx in range(1, T + 1):
    x, y = map(int, input().split())
    x, y = divmod(x, y)
    print(f'#{idx} {x} {y}')