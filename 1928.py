"""
1928: Base64 Decoder
주어진 조건을 거꾸로 올라가서 풀긴 풀었는데 이해가 안됨
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    input_strs = input()
    input_lst = []
    bit_24_lst = []
    ans = ''

    for input_alp in input_strs:
        try:
            input_lst.append(int(input_alp) + 52)
        except:
            if ord(input_alp) >= 97:
                input_lst.append(ord(input_alp) - 71)
            elif ord(input_alp) >= 65:
                input_lst.append(ord(input_alp) - 65)
            elif input_alp == '+':
                input_lst.append(62)
            else:
                input_lst.append(63)

    for i in range(len(input_lst)):
        input_lst[i] = int(format(input_lst[i], 'b'))    

    for i in range(len(input_lst)//4):
        bit_24 = str(input_lst[i*4]*10**18 + input_lst[i*4 + 1]*10**12 + input_lst[i*4 + 2]*10**6 + input_lst[i*4 + 3])
        ans += chr(int(bit_24[:-16], 2)) + chr(int(bit_24[-16:-8], 2)) + chr(int(bit_24[-8:], 2))

    print(f'#{idx} {ans}')
        
    # for i in range(len(input_lst)//4):
    #     bit_24 = str(input_lst[i*4]*10**18 + input_lst[i*4 + 1]*10**12 + input_lst[i*4 + 2]*10**6 + input_lst[i*4 + 3])
    #     bit_24_lst.append(chr(int(bit_24[:-16], 2)))
    #     bit_24_lst.append(chr(int(bit_24[-16:-8], 2)))
    #     bit_24_lst.append(chr(int(bit_24[-8:], 2)))
    # print(bit_24_lst)