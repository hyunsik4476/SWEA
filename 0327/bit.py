def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        if i & (1 << j):
            output += '1'
        else:
            output += '0'
    print(output)

a = 0x10
x = 0x01020304
print(a)
Bbit_print(a)
print('=======')
for i in range(4):
    y_1 = (x >> i*8)
    y_2 = (x >> i*8) & 0xff
    print(f'{y_1} -> {y_2} : ', end = '')
    Bbit_print(y_2)