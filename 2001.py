from pprint import pprint

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # N*N 판, M*M 파리채
    lst = [list(map(int, input().split())) for _ in range(N)]

    ans = 0 # 최댓값
    for y in range(N-M+1):
        for x in range(N-M+1):
            tot = 0  # 매 순간 총 합
            for i in range(M):
                tot += sum(lst[y+i][x: x+M]) # M개 만큼 x방향으로 잘라서 M번 더함
            if tot > ans:
                ans = tot
    print(f'# {tc} {ans}')
