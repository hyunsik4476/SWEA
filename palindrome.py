from pprint import pprint
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 문자열 가로-세로, M: 찾아야하는 회문 길이
    str_lst = [input() for _ in range(N)]
    ans = ''    # 출력용 답
    done = 0    # 찾으면 1로 바꿀예정
    # 가로방향 검사
    for y in range(N):
        for x in range(N-M+1):  # 만약, N = M 이면 i = 0 한 번만 검사
            for i in range(M):  # 목표 회문 길이만큼 검사
                # print(y, x, str_lst[y][x+i], str_lst[y][-1-(N-M-x+i)], ans)
                if str_lst[y][x+i] != str_lst[y][x+M-1-i]: # 검사 인덱스를 어떻게 해야할지 잘..
                    ans = ''
                    break
                else:
                    ans += str_lst[y][x+i]
            else:
                done = 1
                break
        if done == 1:
            break

    if done == 0: # 위에서 못 찾았으면
        for x in range(N):
            for y in range(N-M+1):
                for j in range(M):
                    # print(x, y, str_lst[y+j][x], str_lst[-y-j-1][x], ans)
                    if str_lst[y+j][x] != str_lst[-1-(N-M-y+j)][x]:
                        ans = ''
                        break
                    else:
                        ans += str_lst[y+j][x]
                else:
                    done = 1
                    break
            if done == 1:
                break

    print(f'#{tc} {ans}')