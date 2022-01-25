import sys
sys.stdin = open('input.txt')

def find_max_and_slice(input_list):
    tot = 0    

    while len(input_list):
        max_num_idx = input_list.index(max(input_list))

        for i in range(max_num_idx + 1): # 최댓값까지
            tot += (max(input_list) - input_list[i])

        input_list = input_list[max_num_idx + 1:] # 최댓값 다음 숫자부터 끝까지

    return tot


T = int(input())

for i in range(1, T + 1):
    list_length = int(input())
    ans = find_max_and_slice(list(map(int, input().split())))
    print(f'#{i} {ans}')