def runcheck(input_lst):
    cnt = 1
    for i in range(1, len(input_lst)):
        if input_lst[i-1] and input_lst[i]:
            cnt += 1
            if cnt == 3:
                return 1
        else:
            cnt = 1


def tricheck(input_lst):
    for i in range(3, 7):
        if input_lst.count(i):
            return 1


T = int(input())

for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    p1 = [0]*10
    p2 = [0]*10
    ans = 0

    for i in range(12):
        if i%2:
            p2[lst[i]] += 1
            if runcheck(p2) or tricheck(p2):
                ans = 2
                break
        else:
            p1[lst[i]] += 1
            if runcheck(p1) or tricheck(p1):
                ans = 1
                break

    print(f'#{tc} {ans}')