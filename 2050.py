'''
문자 -> 숫자 변환
'''
alps = input()
for alp in alps:
    if 90 >= ord(alp) >= 65:
        print(ord(alp) - 64, end = ' ')