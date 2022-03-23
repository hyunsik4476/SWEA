lst = list(map(int, input()))
i = 0
dec = 0
ans = []
for i in range(len(lst)):
    n = 6 - i%7
    dec += lst[i] * 2**n
    if n == 0:
        print(dec, end = ' ')
        dec = 0

