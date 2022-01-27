"""
1986: 문제명을 입력해주세요 :)
"""

# import sys
# sys.stdin = open('1986_input.txt')

T = int(input())

for i in range(1, T + 1):
    ans = 0
    number = int(input())

    for num in range(1, number + 1):
        if num % 2:
            ans += num
        else:
            ans -= num
            
    print(f'#{i} {ans}')