def find_set(i):
    while rep[i] != i:
        i = rep[i]
    return i


def union(n1, n2):
    rep[find_set(n2)] = find_set(n1)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edge.append((w, n1, n2))
    # Kruskal
    edge.sort()
    rep = [i for i in range(V+1)]

    cnt = 0 # 선택 간선 수
    s = 0   # 가중치 합
    for w, n1, n2 in edge:
        if find_set(n1) != find_set(n2):
            s += w
            union(n1, n2)
            cnt += 1
            if cnt == V:
                break

    print(f'#{tc} {s}')
