"""
1289: 
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    ans = 0
    bin_num = input()
    if int(bin_num[0]) == 1:
        ans += 1
    
    for i in range(1, len(bin_num)):
        if bin_num[i] != bin_num[i-1]:
            ans += 1
    print(f'#{idx} {ans}')