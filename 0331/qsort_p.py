def qsort(A, l, r):
    if l >= r:
        return
    else:
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s+1, r)


def partition(A, l, r):
    pivot = A[l]
    i, j = l, r
    # print(f'input : {i}, {j}')
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    # print(f'result : {i}, {j}')
    A[l], A[j] = A[j], A[l]
    return j



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    qsort(lst, 0, N-1)
    print(f'#{tc} {lst[N//2]}')