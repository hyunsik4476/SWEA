def po(idx):
    if N >= idx >= 1:
        idxl = 2*idx
        idxr = 2*idx + 1
        l = po(idxl)
        r = po(idxr)
        if not l:
            return lst[idx]
        else:
            if not r:
                lst[idx] = lst[idxl]
                return lst[idx]
            else:
                lst[idx] = lst[idxl] + lst[idxr]
                return lst[idx]

    return False


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    lst = [0]*(N+1)
    for _ in range(M):
        i, n = map(int, input().split())
        lst[i] = n
    po(1)
    print(f'#{tc} {lst[L]}')
