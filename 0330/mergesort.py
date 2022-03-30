def merge_sort(A):
    if len(A) <= 1:
        return A
    print(f'list : ', A)
    left_lst = []
    right_lst = []
    mid = len(A)//2
    for i in range(mid):
        left_lst.append(A[i])
    for j in range(mid, len(A)):
        right_lst.append(A[j])
    print(left_lst, right_lst)
    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)

    return merge(left_lst, right_lst)


def merge(left_lst, right_lst):
    result = []
    print(f'merge', left_lst, right_lst)
    while len(left_lst) > 0 or len(right_lst) > 0:
        if len(left_lst) > 0 and len(right_lst) > 0:
            if left_lst[0] <= right_lst[0]:
                result.append(left_lst.pop(0))
            else:
                result.append(right_lst.pop(0))
        elif len(left_lst) > 0:
            result.append(left_lst.pop(0))
        elif len(right_lst) > 0:
            result.append(right_lst.pop(0))
    print(result)

    return result


print('Merge Sort')
cnt = 0
lst = [2, 2, 1, 1, 3]
a = merge_sort(lst)
print(a)
