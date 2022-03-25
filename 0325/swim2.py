T = int(input())

for tc in range(1, T+1):
    d1fee, m1fee, m3fee, y1fee = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    ans = 9999
    D = [0] * 13
    for i in range(1, 13):
        mmin = D[i-1] + plan[i]*d1fee
        mmin = min(mmin, D[i-1] + m1fee)
        if i >= 3:
            mmin = min(mmin, D[i - 3] + m3fee)
        if i >= 12:
            mmin = min(mmin, D[i - 12] + y1fee)
        D[i] = mmin
    print(f'#{tc} {D[12]}')