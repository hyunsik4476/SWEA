T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room_lst = [list(map(int, input().split())) for _ in range(N)]
    students = 0
    idx = 0

    while students < N:
        lst = [0]*401 # 복도의 상황

        idx += 1
        for i in range(len(room_lst)): # 학생마다 체크
            start, end = map(int, room_lst[i])
            if start < end:
                #갈 수 있는지 체크
                for j in range(start, end+1):
                    if lst[j] == 1:
                        break
                else: # 갈 수 있으면
                    lst[start: end+1] = [1]*(end-start+1)
                    students += 1

            elif end < start:
                #갈 수 있는지 체크
                for j in range(end, start+1):
                    if lst[j] == 1:
                        break
                else: # 갈 수 있으면
                    lst[end: start+1] = [1]*(start-end+1)
                    students += 1

    print(f'#{tc} {idx}')
