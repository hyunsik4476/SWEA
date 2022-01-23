'''
입력만큼 2 곱해서 출력
'''
number = int(input())
ans = 1

for i in range(1, number + 2):
    print(ans, end = ' ')
    ans = ans * 2