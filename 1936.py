'''
가위바위보, 1 2 3 을 각각 가위, 바위 보 로 친다
'''
a, b = map(int,input().split())
# A 승 2 1, 3 2, 1 3
if a == b % 3 + 1:
    print('A')
# B 승 1 2, 2 3, 3 1
if a % 3 + 1 == b:
    print('B')