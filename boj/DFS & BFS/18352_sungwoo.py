import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):  # 인접리스트 방식 표현
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

visited = [-1 for i in range(n+1)]  # -1: 미방문, 0~n: 거리
q = deque([x])  # 큐 생성
visited[x] = 0

while q:  # BFS 수행
    v = q.popleft()

    for i in graph[v]:
        if visited[i] == -1:  # 미방문한 노드라면
            q.append(i)
            visited[i] = visited[v] + 1

flag = True
for v in range(1, n+1):
    if visited[v] == k:  # 최단거리가 k인 노드 출력
        print(v)
        flag = False
if flag:
    print(-1)