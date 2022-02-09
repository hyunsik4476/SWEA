"""
2814_2:
"""

import sys
sys.stdin = open('input.txt')

def DFS(graph, start, visited, ans):
    global answer
    visited.append(start)

    if answer <= ans:
        answer = ans

    for node in graph[start]:
        if node not in visited:
            DFS(graph, node, visited, ans+1)
            visited.remove(node)
    print(visited)

T = int(input())

for tc in range(1, T+1):
    answer = 1
    N, M = map(int,input().split()) # 정점 수. 간선 수
    graph = dict()
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]

    
    for startnode in graph:
            DFS(graph, startnode, [], 1)

    print(f'#{tc} {answer}')