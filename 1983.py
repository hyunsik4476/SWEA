"""
1983: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

T = int(input())
score_alp = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

for idx in range(1, T + 1):
    stu_num, stu_info = map(int, input().split())
    lst = []
    for i in range(stu_num): # 학생 수 만큼
        stu_score = list(map(int, input().split())) # 학생 점수 리스트
        lst.append(stu_score[0]*0.35 + stu_score[1]*0.45 + stu_score[2]*0.2)
    lst_tmp = sorted(lst)
    ans = stu_num - lst_tmp.index(lst[stu_info - 1])

    cnt = 1
    for i2 in range(10): # if 문 다 쓰기 귀찮아서
        if (cnt * stu_num//10) >= ans:
            print(f'#{idx} {score_alp[i2]}')
            break
        cnt += 1
    