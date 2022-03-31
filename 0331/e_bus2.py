T = int(input())

for tc in range(1, T+1):
    N, *lst = map(int, input().split())
    n_lst = [0]*len(lst)
    ans = N

    for i in range(len(lst)):
        n_lst[i] = [i, i + lst[i]]


    print(f'#{tc} {ans-1}')