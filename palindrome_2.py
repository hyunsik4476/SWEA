# 최장 거리의 회문을 찾는 문제, 회문의 길이르 ㄹ포문으로 사용해서 큰 거부터 찾는다
T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    lst = [list(input()) for _ in range(100)]
    done = 0
    for pal_length in range(100, 0, -1):
        for y in range(100):
            for x in range(100-pal_length+1):
                for j in range(pal_length//2):
                    if lst[y][x+j] != lst[y][x+pal_length-1-j]:
                        break
                else:
                    ans = pal_length
                    done = 1
                    break
            if done == 1:
                break
        if done == 1:
            break

    done = 0
    for pal_length in range(100, 0, -1):
        for x in range(100):
            for y in range(100-pal_length+1):
                for j in range(pal_length//2):
                    if lst[y+j][x] != lst[y+pal_length-1-j][x]:
                        break
                else:
                    if pal_length > ans:
                        ans = pal_length
                    done = 1
                    break
            if done == 1:
                break
        if done == 1:
            break


    print(f'#{tc} {ans}')