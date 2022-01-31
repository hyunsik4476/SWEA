'''
다른사람코드
'''
T = int(input())

for idx in range(1, T+1):
    N = str(input())
    num = set(N)
    cnt = 1

    while len(num) != 10:
        cnt += 1
        ans = int(N) * cnt
        num = num | set(str(ans))

    print(f'#{idx} {ans}')