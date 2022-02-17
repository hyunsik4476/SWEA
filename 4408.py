# 너무 어렵게 접근하지 말자
# 결국 경로가 겹치는 인원이 n 명 있다면 최소 이동횟수는 n회 여야함
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    room_lst = [list(map(int, input().split())) for _ in range(N)]
    lst = [0]*201 # 복도의 상황

    for room in room_lst: # 학생마다 체크
        a, b = room
        start = a // 2 + 1 if a % 2 else a // 2
        end = b // 2 + 1 if b % 2 else b // 2
        if start < end:
            #갈 수 있는지 체크
            for j in range(start, end+1):
                lst[j] += 1

        elif end < start:
            #갈 수 있는지 체크
            for j in range(end, start+1):
                lst[j] += 1

        else:
            lst[start] += 1

    print(f'#{tc} {max(lst)}')
