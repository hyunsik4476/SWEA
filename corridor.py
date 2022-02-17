T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [0]*401   #복도의 상황 / 방번호가 1부터 시작하므로 401
    idx = 1
    for _ in range(N):
        start, end = map(int, input().split())
        if start < end: # 방 번호 대소에 따라
            for i in range(start, end+1): # 갈 수 있는지 검사부터
                if lst[i] == 1: # 못가면
                    idx += 1
                    break
            else: # 갈 수 있으면
                for i in range(start, end+1):
                    lst[i] = 1


        else:   # 방 번호 대소에 따라
            for i in range(end, start+1):
                if lst[i] == 1: # 못가면
                    idx += 1
                    break
            else:
                for i in range(end, start+1):
                    lst[i] = 1

    print(f'#{tc} {idx}')
