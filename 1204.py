"""
1204: 딕셔너리 써보기?
"""

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T+1):
    TC = int(input())
    scores_lst = map(int, input().split())
    scores_dict = dict()

    for score in scores_lst:
        scores_dict[score] = scores_dict.get(score, 0) + 1
    
    max_key_lst = [key for key, value in scores_dict.items() if value == max(scores_dict.values())]
    max_key_1 = max(scores_dict, key = scores_dict.get)
    max_key_2 = max(scores_dict.items(), key = lambda x : x[1])

    print(f'#{idx} {max_key_lst}, {max_key_1}, {max_key_2}')