from collections import deque

def solution(n, edge):
    answer = 0
    
    def bfs(v):
        queue = deque([v])
        
        visited[v] = 1
        
        while queue:
            node = queue.popleft()
            
            for n in graph[node]:
                if visited[n] == 0:
                    visited[n] = visited[node] + 1
                    queue.append(n)
    
    graph = [[] for _ in range(n + 1)]
    
    for e in edge:
        start, end = e[0], e[1]
        
        graph[start].append(end)
        graph[end].append(start) #양방향 연결
    
    visited = [0] * (n + 1)
    
    bfs(1)
    
    answer = visited.count(max(visited))
    
    return answer

#간단한 bfs 구현 문제