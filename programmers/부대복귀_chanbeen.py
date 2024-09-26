from collections import deque

def solution(n, roads, sources, destination):
    def bfs(v):
        queue = deque([v])
        
        visited[v] = 0
        
        while queue:
            popped = queue.popleft()
            
            for node in graph[popped]:
                if visited[node] == -1:
                    queue.append(node)
                    visited[node] = visited[popped] + 1
    
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    
    for road in roads:
        start, end = road
        
        graph[start].append(end)
        graph[end].append(start) #양방향
    
    visited = [-1] * (n + 1)
    
    bfs(destination)
    
    for s in sources:
        answer.append(visited[s])
    
    return answer

# 각 source마다 bfs 수행했더니, 시간 초과
# bfs를 source 개수만큼 도는 게 아니라 한번의 bfs로 각 source에서 destination까지의 비용을 모두 계산할 필요가 있어보임
# 그러기 위해서는 각 source에서 destination으로 가는 게 아닌, 하나의 destination에서 각 source로 가는 것이 어떨까?