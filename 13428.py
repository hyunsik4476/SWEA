"""
13428: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    data = input()
    data_set = {int(data)}
    lst = [num for num in data]

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            lst[i], lst[j] = lst[j], lst[i]
            result = int(''.join(lst))
            
            if result//(10**(len(data)-1)) >= 1:
                data_set.add(result)
            lst[i], lst[j] = lst[j], lst[i]
            
    print(f'#{idx} {min(data_set)} {max(data_set)}')