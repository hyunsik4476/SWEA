def comb(idx, r, tmp = []):
    if len(tmp) == r:
        print(tmp)
        return
    else:
        for i in range(idx, len(lst)):
            comb(i+1, r, tmp + [lst[i]])


lst = [1,2,3,4]
comb(0, 2, [])