import sys
import time

start = time.time()
sys.stdin = open('input.txt')

T = int(input())

for i in range(1, T + 1):
    list_length = int(input())
    tot = 0
    input_list = list(map(int, input().split()))

    while len(input_list):
        max_num_idx = input_list.index(max(input_list))
        tot += ((max(input_list) * max_num_idx) - sum(input_list[:max_num_idx]))
        input_list = input_list[max_num_idx + 1:]

    print(f'#{i} {tot}')

print(time.time() - start)