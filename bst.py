def inorder(i):
    global cnt
    if N >= i:
        inorder(2*i)
        lst[i] = cnt
        cnt += 1
        inorder(2*i+1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]*(N+1)
    cnt = 1
    inorder(1)
    print(f'#{tc} {lst[1]} {lst[N//2]}')
