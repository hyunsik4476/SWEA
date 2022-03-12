T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    ans = 0
    pizzas = []
    for i in range(M):
        pizzas.append([i, tmp[i]])
    fire = [[0, 0]]*N

    i = 0
    while pizzas:
        if fire[i][1] == 0:
            fire[i] = pizzas.pop(0)
        else:
            fire[i][1] //= 2
            if fire[i][1] == 0:
                ans = fire[i][0]
                fire[i] = pizzas.pop(0)
        i = (i+1) % N
        # print(fire)
    cnt = 0
    while cnt < N:
        if fire[i][1] == 0:
            fire[i][1] = -1
            cnt += 1
            ans = fire[i][0]
        elif fire[i][1] > 0:
            fire[i][1] //= 2
            if fire[i][1] == 0:
                fire[i][1] = -1
                ans = fire[i][0]
                cnt += 1
        i = (i+1) % N
        # print(fire, cnt)

    print(f'#{tc} {ans+1}')
