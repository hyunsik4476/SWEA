def enque(v):
    global last
    last += 1
    heap[last] = v
    p = last//2
    c = last
    while p >= 1 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c//2


def mysum(heap):
    global last
    ans = 0
    c = last
    p = c//2
    while p >= 1:
        ans += heap[p]
        c = p
        p = c//2
    return ans


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    heap = [0]*(N+1)
    last = 0
    input_lst = list(map(int, input().split()))

    for num in input_lst:
        enque(num)
    ans = mysum(heap)

    print(f'#{tc} {ans}')
