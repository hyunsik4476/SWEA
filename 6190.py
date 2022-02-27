T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = -1
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = lst[i]*lst[j]
            tmp_lst = list(str(tmp))
            K = len(tmp_lst)
            if K >= 2:
                for p in range(1,K):
                    if tmp_lst[p-1]>tmp_lst[p]:
                        break
                else:
                    if tmp> ans:
                        ans = tmp
    print(f'#{tc} {ans}')
