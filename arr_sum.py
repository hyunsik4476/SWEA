def f(i, N, S):     # 순열 만드는 함수
    global ans      # 답 저장용
    if i == N:      # 순열 완성되면
        for k in range(N):
            S += arr[k][lst[k]]     # 순열의 원소를 x좌표로 갖는 arr원소 합
        if S < ans:                 # 합 S가 ans 보다 작으면 ans 에 대입
            ans = S
        return
    else:
        for j in range(i, N):
            lst[i], lst[j] = lst[j], lst[i]
            f(i+1, N, S)
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