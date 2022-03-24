T = int(input())

for tc in range(1, T+1):
    N, h = input().split()
    ans = ''
    for alp in h:
        ans += format(int(alp, 16), '04b')
    print(f'#{tc} {ans}')