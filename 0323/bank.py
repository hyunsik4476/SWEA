T = int(input())

for tc in range(1, T+1):
    num_bin = list(map(int, input()))
    num_tri = list(map(int, input()))
    bin_dec_lst = [int(''.join(map(str, num_bin)), 2)]
    tri_dec_lst = [int(''.join(map(str, num_tri)), 3)]
    # 2 -> 2` -> 10
    for i in range(len(num_bin)):
        if num_bin[i]:
            num_bin[i] = 0
            bin_dec_lst.append(int(''.join(map(str, num_bin[:])), 2))
            num_bin[i] = 1
        else:
            num_bin[i] = 1
            bin_dec_lst.append(int(''.join(map(str, num_bin[:])), 2))
            num_bin[i] = 0

    for i in range(len(num_tri)):
        if num_tri[i] == 0:
            for j in [1,2]:
                num_tri[i] = j
                tri_dec_lst.append(int(''.join(map(str, num_tri[:])), 3))
            num_tri[i] = 0
        elif num_tri[i] == 1:
            for j in [0,2]:
                num_tri[i] = j
                tri_dec_lst.append(int(''.join(map(str, num_tri[:])), 3))
            num_tri[i] = 1
        else:
            for j in [0,1]:
                num_tri[i] = j
                tri_dec_lst.append(int(''.join(map(str, num_tri[:])), 3))
            num_tri[i] = 2

    for num in bin_dec_lst:
        if num in tri_dec_lst:
            print(f'#{tc} {num}')
            break