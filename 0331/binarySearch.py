def bs(t, l, r, lrcheck = 2):
    global tmp, cnt
    if tmp == lrcheck:
        return
    tmp = lrcheck

    mid = (l+r)//2
    # print(f'target: {t}, mid idx: {mid} , mid num: {lst1[mid]}')
    if l > r:
        return
    elif lst1[mid] == t:
        cnt += 1
        return
    else:
        if lst1[mid] > t:
            bs(t, l, mid-1, 0)
        else:
            bs(t, mid+1, r, 1)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))
    lst1.sort()

    cnt = 0

    for num in lst2:
        tmp = -1
        # print(f'num: {num}')
        bs(num, 0, N-1)
    print(f'#{tc} {cnt}')