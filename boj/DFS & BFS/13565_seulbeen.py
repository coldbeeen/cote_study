import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
m,n=map(int,input().split())
graph=[]
visited=[[False]*n for _ in range(m)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
percolate=False

for _ in range(m):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

def dfs(x, y):
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx, ny)

for y in range(n):
    if graph[0][y] == 0 and not visited[0][y]:
        dfs(0, y)

for item in visited[m-1]:
    if item:
        print('YES')
        exit()
print("NO")

