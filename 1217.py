def f(N, M):
    if M == 1:
        return N
    return N*f(N, M-1)

T = 10

for tc in range(1, T+1):
    num = int(input())
    N, M = map(int, input().split())
    ans = 0
    if M == 0:
        ans = 1
    else:
        ans = f(N, M)
    print(f'#{tc} {ans}')