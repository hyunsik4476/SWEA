tmp = {'0001101': 0
,'0011001': 1
,'0010011': 2
,'0111101': 3
,'0100011': 4
,'0110001': 5
,'0101111': 6
,'0111011': 7
,'0110111': 8
,'0001011': 9}

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    done = 0
    for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                ans_str = arr[i][j - 55:j + 1]
                done = 1
                break
        if done:
            break

    ans = [0]*8
    j = 0
    result = ''
    for i in range(56):
        result += ans_str[i]
        if len(result) == 7:
            ans[j] = tmp[result]
            j += 1
            result = ''

    mysum = 0

    for p in range(8):
        if p % 2:
            mysum += ans[p]
        else:
            mysum += ans[p] * 3
    if mysum % 10 == 0:
        print(f'#{tc} {sum(ans)}')
    else:
        print(f'#{tc} 0')
