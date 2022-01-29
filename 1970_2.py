import sys
sys.stdin = open('input.txt')

T = int(input())
money_lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
 
for idx in range(1, T+1):
    fee = int(input())
    fee = fee//10 * 10
    ans_lst = []

    for money in money_lst:
        n = fee // money

        if n > 0:
            ans_lst.append(n)
            fee -= n*money
        else:
            ans_lst.append(n)
            
    print(f'#{idx}')
    print(*ans_lst)