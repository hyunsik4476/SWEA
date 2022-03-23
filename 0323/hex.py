T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(lambda x: bin(int(x, 16))[2:], input()))

    for i in range(len(lst)):
        while len(lst[i]) < 4:
            lst[i] = '0' + lst[i]

    str = ''.join(lst)

    i = 0
    dec = 0
    ans = []
    print(f'#{tc} ', end = '')
    for i in range(len(str)):
        n = 6 - i % 7
        dec += int(str[i]) * 2 ** n
        if n == 0:
            print(dec, end=' ')
            dec = 0
    print()
