"""
1240: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = []
    for _ in range(N):
        arr.append(list(input()))
    done = 0
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == '1':
                ans_str = arr[i][j-55:j+1]
                done = 1
                break
        if done:
            break
    # print(''.join(ans_str))
    ans = []
    while ans_str:
        result = ''
        for k in range(7):
            result += ans_str.pop(0)

            if result == '0001101':
                ans.append(0)
            elif result == '0011001':
                ans.append(1)
            elif result == '0010011':
                ans.append(2)
            elif result == '0111101':
                ans.append(3)
            elif result == '0100011':
                ans.append(4)
            elif result == '0110001':
                ans.append(5)
            elif result == '0101111':
                ans.append(6)
            elif result == '0111011':
                ans.append(7)
            elif result == '0110111':
                ans.append(8)
            elif result == '0001011':
                ans.append(9)
    # print(ans)
    mysum = 0
    if len(ans) == 8:
        for p in range(7):
            if p%2:
                mysum += ans[p]
            else:
                mysum += ans[p]*3
        if (mysum + ans[-1])%10 == 0:
            print(f'#{tc} {sum(ans)}')
        else:
            print(f'#{tc} 0')
    else:
        print(f'#{tc} 0')

