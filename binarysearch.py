def bstsort(idx):
    if N >= idx >= 1:
        idxl = 2*idx
        idxr = 2*idx + 1
        l = bstsort(idxl)
        r = bstsort(idxr)
        if not l:
            return lst[idx]
        else:
            if not r:
                if lst[idx] < lst[idxl]:
                    lst[idx], lst[idxl] = lst[idxl], lst[idx]
                return lst[idx]
            else:
                tmp = sorted([l, lst[idx], r])
                lst[idxl] = tmp[0]
                lst[idx] = tmp[1]
                lst[idxr] = tmp[2]
                return lst[idx]

    return False


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0] * (N+1)
    for i in range(1, N+1):
        lst[i] = i
    bstsort(1)
    print(lst)