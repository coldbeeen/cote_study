import sys
sys.setrecursionlimit(10**6)

def valid(ny,nx): #탐색 가능 좌표인지 검사하는 함수(유효한 범위인지 and 양인지)
    if 0<=nx<w and 0<=ny<h and not visit[ny][nx] and grid[ny][nx]=="#":
        return True
    return False

def DFS(y,x):
    visit[y][x]=True #방문 표시

    for i in range(4): # 현재 노드 기준 상하좌우 노드에 대해서
        nx=x+dx[i]
        ny=y+dy[i]
        if valid(ny,nx): # 탐색 가능한 경우에 한해 DFS재귀호출
            DFS(ny,nx)

input=sys.stdin.readline

t=int(input())
dx=[1,-1,0,0]
dy=[0,0,-1,1]

for _ in range(t):

    h,w=map(int,input().split())
    grid=[list(input().rstrip()) for _ in range(h)]
    visit=[[False for _ in range(w)] for _ in range(h)]
    cnt=0

    for i in range(h):
        for j in range(w):
            if valid(i,j):#유효한 좌표일때(풀숲이 아니고, 이미 방문한 양이 아닌 경우)
                DFS(i,j)
                cnt+=1

    print(cnt)
