T = int(input())

for tc in range(1, T+1):
    data = input()
    data = data.replace('()', '1')
    N = len(data)
    check = 0
    tot = 1
    ans = 0

    for i in range(N):
        if data[i] == '(':
            check += 1
        elif data[i] == '1':
            ans += check
        elif data[i] == ')':
            ans += 1
            check -= 1

    print(f'#{tc} {ans}')

