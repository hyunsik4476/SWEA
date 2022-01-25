'''
약수 구하기
'''
number = int(input())
lst = []
for num in range(1, number + 1):
    if number % num == 0:
        lst.append(num)
print(*lst)