import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def DFS(y,x):
    visit[y][x]=True

    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=ny<h and 0<=nx<w:
            if graph[ny][nx]==1 and not visit[ny][nx]:
                DFS(ny,nx)

# 아 대각선도 하나의 섬이구나
dx=[1,-1,0,0,1,1,-1,-1]
dy=[0,0,1,-1,-1,1,-1,1]

while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break

    graph=[]
    visit=[[False for _ in range(w)] for _ in range(h)]
    cnt=0

    for _ in range(h):
        row=list(map(int,input().split()))
        graph.append(row)
    
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and not visit[i][j]:
                DFS(i,j)
                cnt+=1
    del visit
    del graph
    print(cnt)

    

    