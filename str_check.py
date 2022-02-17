T = int(input())

for tc in range(1, T+1):
    str_1 = input()
    str_2 = input() # str_2 안에서 str_1찾는것
    ans = 0
    for i in range(len(str_2)-len(str_1)+1):
        for j in range(len(str_1)):
            if str_2[i+j] != str_1[j]: # 인덱스 헷갈리지 말자
                break
        else:
            ans = 1
    print(f'#{tc} {ans}')
