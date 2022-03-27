def change_endian(n):
    p = []
    for i in range(4):
        p.append((n >> (24 - i*8)) & 0xff)
    return p


x = 0x01020304
p = []
for i in range(4):
    p.append((x >> i*8) & 0xff)
print('x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))
p = change_endian(x)
print('change_endian x = %d%d%d%d' % (p[0], p[1], p[2], p[3]))