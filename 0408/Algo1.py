T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) # 세로, 가로, 그물 크기
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0 # 최댓값 구하기
    for y in range(N-K+1):
        for x in range(M-K+1):
            tmp_sum = 0
            # K K 합 구하기
            for j in range(K):
                for i in range(K):
                    tmp_sum += arr[y+j][x+i]
            # K-2 K-2 합 빼기
            for p in range(K-2):
                for k in range(K-2):
                    tmp_sum -= arr[y+p+1][x+k+1]
            if tmp_sum > ans:
                ans = tmp_sum
    print(f'#{tc} {ans}')
