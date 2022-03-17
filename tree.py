def po(v, ans = 0):
    global N
    if 1<= v <= N:
        c1 = po(ch1[v], ans)
        c2 = po(ch2[v], ans)
        # print(v, c1, lst[v], c2)
        if lst[v] == '+':
            lst[v] = int(c1) + int(c2)
        elif lst[v] == '-':
            lst[v] = int(c1) - int(c2)
        elif lst[v] == '*':
            lst[v] = int(c1) * int(c2)
        elif lst[v] == '/':
            lst[v] = int(c1) / int(c2)
        else:
            lst[v] = int(lst[v])
    return lst[v]



T = 10

for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(input().split()))
    ch1 = [0]*(N+1)
    ch2 = [0]*(N+1)
    lst = [0]*(N+1)
    for i in range(N):
        n, op, *c = arr[i]
        p = int(n)
        lst[p] = op
        if len(c) == 1:
            ch1[p] = int(c[0])
        elif len(c) == 2:
            ch1[p] = int(c[0])
            ch2[p] = int(c[1])
    # print(ch1)
    # print(ch2)
    # print(lst)

    po(1)
    print(f'#{tc} {int(lst[1])}')