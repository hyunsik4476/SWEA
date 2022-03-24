T = int(input())

for tc in range(1, T+1):
    N = float(input())
    ans = ''
    for i in range(1, 13):
        if N:
            if N >= (1/2)**i:
                N = N - (1/2)**i
                ans += '1'
            else:
                ans += '0'
        else:
            break
    if N:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {ans}')
