# 또 RecursionError 뜸
# 그냥 재귀 할때 recursionlimit 설정해놓고 하는게 맘 편할듯?
# 별거 아니긴 한데 일반적인 x,y좌표랑 배열에서의 좌표랑 다르니까 헷갈리긴 함 생각 잘 해야될듯
import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)
t=int(input())
def DFS(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    for i in range(4):
        check_x=x+dx[i]
        check_y=y+dy[i]
        if 0<=check_x<n and 0<=check_y<m:
            if graph[check_x][check_y]:
                graph[check_x][check_y]=False 
                DFS(check_x,check_y)   
                
for _ in range(t):
    m,n,k=map(int,input().split())
    graph=[[False for _ in range(m)]for _ in range(n)]
    cnt=0
    for _ in range(k):
        y,x=map(int,input().split())
        graph[x][y]=True
    
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                DFS(x,y)
                cnt+=1
    print(cnt)