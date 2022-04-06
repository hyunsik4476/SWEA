from pprint import pprint
a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
pprint(a)
b = list(map(list, zip(*a)))
pprint(b)
# c = []
# for i in range(len(b)):
#     c.append(b[i][::-1])
# pprint(c)
d = a[::-1]
pprint(d)

a = [1,2,3,4,5]
b = [6,7,8,9,10]
print(list(zip(a, b)))