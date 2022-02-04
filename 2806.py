import sys
sys.stdin = open('input.txt')

'''
행을 하나씩 늘려가면서
[(세로, 좌대각, 우대각), (세로, 좌대각, 우대각)] 에 대한 정보를 모두 확인
'''
def check(y): # y좌표 받는 함수
    global n, cnt
    if y == n:
        cnt += 1
        return

    for x in range(n):
        if x in col or x+y in l_dia or x-y in r_dia:
            continue
        col.add(x)
        l_dia.add(x+y)
        r_dia.add(x-y)
        check(y+1)
        col.remove(x)
        l_dia.remove(x+y)
        r_dia.remove(x-y)


T = int(input())

for idx in range(1, T+1):
    n = int(input())
    cnt = 0
    col, l_dia, r_dia = set(), set(), set()
    check(0)
    print(cnt)