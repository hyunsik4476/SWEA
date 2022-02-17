def turn(NUM, input_lst):
    return_lst = [[0]*NUM for _ in range(NUM)]
    for y in range(N):
        for x in range(N):
            return_lst[y][x] = input_lst[-(x+1)][y]
    return return_lst

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst_1 = turn(N, lst)
    lst_2 = turn(N, lst_1)
    lst_3 = turn(N, lst_2)

    print(f"#{tc}")
    for j in range(len(lst_1)):
        print(''.join(map(str, lst_1[j])), end = ' ')
        print(''.join(map(str, lst_2[j])), end=' ')
        print(''.join(map(str, lst_3[j])))
