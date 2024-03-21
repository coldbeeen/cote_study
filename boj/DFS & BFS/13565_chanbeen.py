import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(x, y):
    global flag
    
    graph[x][y] = 1 #방문처리
    
    if x == M - 1: #아래쪽에 도착, 전류가 침투함
        flag = 1 
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] == 0:
                DFS(nx, ny)

M, N = map(int, input().split())

fiber = [input().rstrip() for _ in range(M)]

graph = []

for i in range(M):
    tmp = []
    for j in range(N):
        tmp.append(int(fiber[i][j]))
    graph.append(tmp)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] #서, 동, 남, 북

flag = 0

for i in range(N):
    if graph[0][i] == 0: #격자 위쪽에서 출발점 설정
        DFS(0, i)

print("YES" if flag else "NO")

#1. 백트래킹처럼 DFS를 돌고 빠져나오면서 다시 0으로 초기화시키는건줄 알았음
#2-1. 그러나, 어느 출발점에서 지나간 포인트가 도착 루트로 사용되지 못 했다
#2-2. 이 뜻은 다른 출발점에서 그 포인트를 지나가도 어차피 도착지점에 못 가는 것
#2-3. 따라서 방문처리처럼 한번 방문한 지점은 그냥 막아버리면 된다
#3. 이번 문제와 같은 입력 예시에서 한번에 정수형 2차원 배열로 입력받을 수는 없을까?