from pprint import pprint

def pick3(idx = 0, tmplst = [0]*7):
    if sum(tmplst) == 3:
        mem.append(tmplst[:])
        return

    for i in range(idx, 7):
        tmplst[i] = 1
        pick3(i+1, tmplst)
        tmplst[i] = 0
        # tmplst[i] = 0
        # pick3(i+1, tmplst)


mem = []
pick3()
T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    res_lst = []
    for comb in mem:
        res = 0
        for i in range(7):
            if comb[i]:
                res += lst[i]
        res_lst.append(res)
    res_lst.sort(reverse=True)
    print(f'#{tc} {list(set(res_lst))[4]}')

