import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n=int(input())
dol=[0]+list(map(int, input().split())) 
s=int(input()) 
cnt=1 
visited=[False for _ in range(n+1)] 
def dfs(x):
    global cnt
    nx=[x+dol[x],x-dol[x]]
    for i in nx:
        if 0<i<=n and visited[i]==False:
            cnt+=1
            visited[i]=True
            dfs(i)
dfs(s)
print(cnt)