def find_set(n):
    while rep[n] != n:
        n = rep[n]
    return n


def union(a, b):
    rep[find_set(b)] = find_set(a)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    rep = [i for i in range(N+1)]
    for i in range(M):
        a, b = lst[2*i], lst[2*i + 1]
        union(a, b)
    # print(rep)
    res = set()
    for j in range(1, len(rep)):
        res.add(find_set(j))

    print(f'#{tc} {len(res)}')