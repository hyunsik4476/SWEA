"""
2814: 문제명을 입력해주세요 :)
"""

import sys
sys.stdin = open('input.txt')

def DFS(graph, start, visited, ans):
    global answer
    visited.append(start)
    ans += 1
    if ans >= answer:
        answer = ans

    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited, ans)
    return visited

T = int(input())

for idx in range(1, T+1):
    answer = 0
    n, m = map(int, input().split()) # 노드 수, 길 수
    graph = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]
    print(graph)
    # if graph:
    for i in range(1, m+1):
        print(DFS(graph, i, [], 0))
    print(answer)