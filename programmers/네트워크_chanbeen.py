def dfs(v, computers): #dfs로 해결
    visited[v] = 1

    for n in range(len(computers[v])):
        if computers[v][n] == 1 and visited[n] == 0:
            dfs(n, computers)

def solution(n, computers):
    global visited
    
    answer = 0
    
    visited = [0] * n
    
    for i in range(n):
        if visited[i] == 0:
            dfs(i, computers)
            answer += 1
            
    return answer