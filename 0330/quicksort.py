import sys
sys.stdin = open('input.txt')

def qsort(A, l, r):
    global depth
    depth += 1
    if l < r:
        print(f'depth: {depth}, l: {l}, r: {r}, list: {A} ', end = '')
        s = partition(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)


def partition(A, l, r):
    pivot = A[l]
    i, j = l, r
    while i <= j:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    print(f'pivot: {pivot}, s: {j}')
    return j


depth = 0
lst = [6,4,5,3,2,1]
qsort(lst, 0, 5)
print(lst)

# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#     qsort(lst, 0, N-1)
#     print(f'#{tc} ', end = '')
#     print(*lst)