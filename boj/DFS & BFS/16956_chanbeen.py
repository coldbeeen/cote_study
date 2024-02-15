import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

R, C = map(int, input().split())

SaW = [] #Sheep and Wolf

for _ in range(R):
    s = list(input().rstrip())
    SaW.append(s)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서 동 남 북

flag = 1 #처음에는 울타리로 막을 수 있다고 가정

def DFS(x, y):
    global flag
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < R and 0 <= ny < C:
            if SaW[nx][ny] == 'S':
                if SaW[x][y] == 'W': #양 바로 옆에 늑대가 있다 : 울타리를 쳐도 못 막는다
                    flag = 0
                SaW[x][y] = 'D'
            elif visited[nx][ny] == 0: #늑대가 갈 수 있는 루트 탐색
                DFS(nx, ny)

visited = [[0 for _ in range(C)] for _ in range(R)]

for i in range(R):
    for j in range(C):
        if SaW[i][j] == 'W': #늑대만 움직이니까 늑대 기준으로 탐색
            DFS(i, j)

print(flag)
if flag == 1:
    for i in range(R):
        for j in range(C):
            print(SaW[i][j], end='')
        print()