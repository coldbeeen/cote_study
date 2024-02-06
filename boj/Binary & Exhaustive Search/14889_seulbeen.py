# 백트래킹 공부도 해야하고
# 구현하는걸 연습해야할듯...
#구글링했음
import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
INF = 2147000000
res = INF

def DFS(L,idx):
    global res
    if L == N//2:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    A += board[i][j]
                elif not visited[i] and not visited[j]:
                    B +=board[i][j]
        res = min(res, abs(A-B))
        return
    for i in range(idx,N):
        if not visited[i]:
            visited[i] = True
            DFS(L+1,i+1)
            visited[i] = False
            
DFS(0,0)
print(res)