T = int(input())

for tc in range(1, T+1):
    str_1 = set(input())
    str_2 = input()
    ans_dict = dict()

    for alp_check in str_1: # str_1 셋 안의 알파벳들
        for alp in str_2: # 긴 문자열 전체에 대해서
            if alp_check == alp:
                ans_dict[alp_check] = ans_dict.get(alp_check, 0) + 1

    max_num = list(ans_dict.values())[0] # 여기 초기값을 어떻게 해야 할지 잘 모르겠음

    for num in ans_dict.values():
        if num > max_num:
            max_num = num
    print(f'#{tc} {max_num}')