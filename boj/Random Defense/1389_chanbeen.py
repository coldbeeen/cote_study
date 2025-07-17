#약 25분 소요

from collections import deque

def bfs(i):
    visited = [-1] * (N + 1)
    
    visited[i] = 0
    
    q = deque([i])
    
    while q:
        node = q.popleft()
        
        for k in graph[node]:
            if visited[k] == -1:
                visited[k] = visited[node] + 1 #거리 갱신
                q.append(k)
                
    return sum(visited[1:]) #노드는 1부터 존재

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    graph[b].append(a)

min_num = N * M # 임의이 최솟값 설정

result = 0

for i in range(1, N + 1):
	tmp = bfs(i)
 
	if min_num > tmp: # 최소 거리 갱신
		result = i #번호 저장
		min_num = tmp
  
print(result)