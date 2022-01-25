'''
크기순 정렬 후 중간값 찾기
'''
T = int(input())
lst = sorted(list(map(int, input().split())))
print(lst[T//2])