def merge_sort(A):
    if len(A) <= 1:
        return A

    mid = len(A)//2
    left_lst = [0]* mid
    right_lst = [0] * (len(A) - mid)

    for i in range(mid):
        left_lst[i] = A[i]
    for j in range(mid, len(A)):
        right_lst[j - mid] = A[j]
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    global cnt
    result = [0] * (len(left_lst) + len(right_lst))
    if left_lst[-1] > right_lst[-1]:
        cnt += 1

    i, j, k = 0, 0, 0
    while i < len(left_lst) or j < len(right_lst):

        if i < len(left_lst) and j < len(right_lst):
            if left_lst[i] <= right_lst[j]:
                result[k] = left_lst[i]
                i += 1
                k += 1
            else:
                result[k] = right_lst[j]
                j += 1
                k += 1
        elif len(left_lst) > i:
            result[k] = left_lst[i]
            i += 1
            k += 1
        elif len(right_lst) > j:
            result[k] = right_lst[j]
            j += 1
            k += 1

    return result


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    sorted_lst = merge_sort(lst)
    print(f'#{tc} {sorted_lst[N//2]} {cnt}')