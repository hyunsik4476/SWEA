def search(left, right):
    global N
    mid = (left+right)//2
    print(left, mid, right)
    if right - left <= 0:
        if mid ** 3 == N:
            print(f'#{tc} {mid}')
            return
        else:
            print(f'#{tc} -1')
            return

    if mid ** 3 > N:
        search(left, mid-1)
    elif mid ** 3 < N:
        search(mid+1, right)
    elif mid ** 3 == N:
        print(f'#{tc} {mid}')
        return


T = int(input())


for tc in range(1, T+1):
    N = int(input())
    search(1, N)
