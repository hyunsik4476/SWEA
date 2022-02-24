def f(i, N, S):     # 순열 만드는 함수
    global ans      # 답 저장용
    if S > ans:     # 합이 기존보다 커지면 돌아가기
        return
    elif i == N:      # 순열 완성되면
        if S < ans:                 # 합 S가 ans 보다 작으면 ans 에 대입
            ans = S
        return
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1, N, S + arr[i][lst[i]])   # 단계별로 i열의 lst[i] 번째 원소 더하기
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = [num for num in range(N)]     # 같은 세로줄을 피하기 위해 0~N 순열
    ans = 0
    for p in range(N):
        ans += arr[p][p]                # 일단 대각합으로 초기화
    f(0, N, 0)
    print(f'#{tc} {ans}')