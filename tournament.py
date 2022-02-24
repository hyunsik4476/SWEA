def f(i, j):
    # print("i, j = ", i, j)
    if i+1 == j:
        return win(i, j)
    elif i == j:
        return i
    else:
        mid = (i+j) // 2
        left = f(i, mid)
        right = f(mid+1, j)
        return win(left, right)


def win(a, b):  # 1 가위 2 바위 3 보
    if lst[a] == lst[b]:
        return a
    elif lst[a] == 1:
        if lst[b] == 2:
            return b
        elif lst[b] == 3:
            return a
    elif lst[a] == 2:
        if lst[b] == 3:
            return b
        elif lst[b] == 1:
            return a
    elif lst[a] == 3:
        if lst[b] == 1:
            return b
        elif lst[b] == 2:
            return a


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))
    idx = f(1, N)
    print(f'#{tc} {idx}')