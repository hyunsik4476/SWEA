from itertools import combinations


def permutation(inputlist, idx):
    if idx == len(inputlist):
        print(inputlist)
        return
    else:
        for j in range(idx, len(inputlist)):
            inputlist[idx], inputlist[j] = inputlist[j], inputlist[idx]
            permutation(inputlist, idx+1)
            inputlist[idx], inputlist[j] = inputlist[j], inputlist[idx]


def comb2(lst, picknum):
    def comb(lst, picknum, idx = 0, tmplst = []):
        if len(tmplst) == picknum:
            comblist.append(tmplst)
        else:
            for i in range(idx, len(lst)):
                comb(lst, picknum, i+1, tmplst+[lst[i]])

    comblist = []
    comb(lst, picknum)
    return comblist


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lsts = []
    ans = 9999

    for i in range(2**N):
        cnt = 0
        tmp = [0]*N
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                tmp[j] = 1
        if cnt == N//2:
            lsts.append(tmp)

    for lst in lsts:
        result1, result2 = 0, 0
        set1 = []
        set2 = []
        for i in range(N):
            if lst[i]:
                set1.append(i)
            else:
                set2.append(i)

        for i, j in comb2(set1, 2):
            result1 += arr[i][j]
        for j, i in comb2(set1, 2):
            result1 += arr[i][j]
        for i, j in comb2(set2, 2):
            result2 += arr[i][j]
        for j, i in comb2(set2, 2):
            result2 += arr[i][j]

        if abs(result2-result1) < ans:
            ans = abs(result2-result1)

    print(f'#{tc} {ans}')