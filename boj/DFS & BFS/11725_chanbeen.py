def DFS(v):
    visited[v] = 1
    
    for n in graph[v]:
        if visited[n] == 0:
            result[n] = v #자식 값을 key로, 부모 값을 value로 저장
            DFS(n)

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range (N + 1)]

for _ in range(N - 1):
    s, e = map(int, input().split())
    
    graph[s].append(e)
    graph[e].append(s)

visited = [0] * (N + 1)

result = {} #결과값 저장을 위해 딕셔너리 활용

DFS(1)

result = sorted(result.items(), key = lambda x : x[0]) #출력을 위해 key값 기준 정렬

for i in range(len(result)):
    print(result[i][1])