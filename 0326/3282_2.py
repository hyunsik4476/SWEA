from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(list(map(int, input().split())))
    # 고려해야 할 가치가 2개일 때,
    dp = [[0] * (K+1) for _ in range(N+1)]
    # i: 물건의 번호(행) j: 무게 (열)
    for i in range(1, len(dp)):
        vol, price = lst[i-1]
        for j in range(1, len(dp[i])):
            if j >= vol:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-vol] + price)
            else:
                dp[i][j] = dp[i-1][j]
    print(f'#{tc} {dp[-1][-1]}')
    # pprint(dp)
    for k in range(N+1):
        print(f'{k}번 물건까지 사용: {dp[k]}')



