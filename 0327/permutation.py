def permutation(idx):
    if idx == len(lst):
        print(lst)
        return
    else:
        for i in range(idx, len(lst)):
            lst[i], lst[idx] = lst[idx], lst[i]
            permutation(idx+1)
            lst[i], lst[idx] = lst[idx], lst[i]


lst = [1, 2, 3, 4]
permutation(0)
