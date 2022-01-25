input_number = int(input())
    
for a in range(1, input_number + 1):
    lst = [num for num in str(a)]
    b = lst.count('3') + lst.count('6') + lst.count('9')
    
    if b >= 1:
        print('-' * b, end = ' ')
    else:
        print(a, end = ' ')