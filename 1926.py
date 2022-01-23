'''
3 6 9 게임
타입 변환 말고 3 6 9 체크하는 방법이 뭘까
'''
input_num = int(input())

for num in range(1, input_num +1):
    cnt = 0

    for str_num in str(num):
        if '3' in str_num or '6' in str_num or '9' in str_num:
            cnt += 1
        result = '-' * cnt

    if '3' in str(num) or '6' in str(num) or '9' in str(num):
        print(result, end = ' ')
    else:
        print(num, end = ' ')