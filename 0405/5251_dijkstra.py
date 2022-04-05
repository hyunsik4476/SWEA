T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    INF = 1000000

    adjM = [[INF]*(N+1) for _ in range(N+1)]

    for i in range(N+1):
        adjM[i][i] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        adjM[s][e] = w  # 방향성이 있는 그래프

    # 다익스트라
    # d : 출발점(0) 에서의 거리 adjM[0] 을 복사
    # u : 비용이 결정된 정점을 체크하는 리스트
    # d = adjM[0][:]
    d = [adjM[0][i] for i in range(N+1)]
    u = [0]*(N+1)
    u[0] = 1

    for _ in range(N):  # 출발을 제외한 N개 정점의 비용결정
        minV = INF
        w = 0
        for i in range(N+1):    # 비용이 결정되지 않았고 최소인 정점 i
            if u[i] == 0 and minV > d[i]:
                minV = d[i]
                w = i
        u[w] = 1    # 남은 정점 중 비용이 가장 적은 w
        # w에 인접한 정점 v에 대해 출발지점에서의 도착비용 d[v] 갱신 시도
        for v in range(N+1):
            if INF > adjM[w][v] > 0:    # 인접 조건
                d[v] = min(d[v], d[w] + adjM[w][v]) # 지금까지 정해진 거리 vs w를 거쳐서 v로 가는 거리
    
    print(f'#{tc} {d[N]}')
