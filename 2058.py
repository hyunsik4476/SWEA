'''
자릿수의 합 구하기
10으로 나눈 몫, 나머지 활용하기
'''
number = input()
number_int = int(number)
ans = 0

a = number_int
for num in range(1, len(number) + 1):
    a, b = divmod(a, 10)
    ans += b
    
print(ans)