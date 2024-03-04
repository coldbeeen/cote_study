import sys
input=sys.stdin.readline
n=int(input())
graph=[[0]for _ in range(n+1)]
visit=[[False] for _ in range(n+1)]
result=0
for i in range(0,n):
    
    graph[i].extend(list(map(int,input().split())))
print(graph)
def back_tracking(idx):
    global result
    for nodes in graph[idx]:
        for cost in nodes:
            if visit[i]==False and nodes[i]!=0:
                visit[i]=True
                result+=nodes[i]
                back_tracking(i)
                visit[i]=False
                result-=nodes[i]