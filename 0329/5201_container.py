T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # 화물 수, 트럭 수
    cont_lst = list(map(int, input().split()))
    truck_lst = list(map(int, input().split()))
    cont_lst.sort(reverse=True)
    truck_lst.sort(reverse=True)
    ans = 0
    i, j = 0, 0
    while cont_lst and truck_lst:
        truck = truck_lst.pop(0)
        for i in range(len(cont_lst)):
            if cont_lst[i] <= truck:
                ans += cont_lst.pop(i)
                break
    print(f'#{tc} {ans}')
