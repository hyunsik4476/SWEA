"""
1244: 자리바꾸기
"""

# import sys
# sys.stdin = open('input.txt')

# T = int(input())

# for idx in range(1, T+1):
pay, n = input().split()
pay_lst = list(pay)

for i in range(int(n)): # max 랑 리스트 자르기로 어떻게 안될까
    # print(pay_lst)
    
    

    if i <= (len(pay_lst) - 2) and pay_lst[i] < max(tmp_lst): # i번 원소가 i~끝에서 최대가 아닐 때 12345 345
        tmp_lst = pay_lst[i:]
        print(pay_lst[i], max(tmp_lst))
        
        j = len(tmp_lst)-1 - tmp_lst[::-1].index(max(tmp_lst)) # 2 00000/5, 3까지 ㄱㅊ
        tmp_num = pay_lst[i] # 378466 
        print(pay_lst)
        print(f'j, 최솟값 = {j}, {tmp_num}')

        pay_lst[i] = max(tmp_lst) # 12545
        tmp_lst[j] = tmp_num # 343
        print(pay_lst[:i+1], tmp_lst[i+1:])
        pay_lst = pay_lst[:i+1] + tmp_lst[1:]

    if i > (len(pay_lst) - 2):
        tmp_num = pay_lst[-1]
        pay_lst[-1] = pay_lst[-2]
        pay_lst[-2] = tmp_num


print(pay_lst)