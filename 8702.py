T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]+ list(map(int, input().split()))
    sub_lst = []

    for X in range(1, N):
        sum_1 = 0
        sum_2 = 0
        for i in range(1, X+1):
            sum_1 += lst[i]
        for j in range(X+1, N+1):
            sum_2 += lst[j]
        sub = abs(sum_2 - sum_1)
        sub_lst.append(sub) # X 는 리스트 인덱스 + 1

    min_idx = 0
    for k in range(N-2, -1, -1):
        if sub_lst[min_idx] > sub_lst[k]:
            min_idx = k

    print(f'#{tc} {min_idx+1} {sub_lst[min_idx]}')