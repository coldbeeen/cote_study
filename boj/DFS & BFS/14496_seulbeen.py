# a==b인 경우까지 고려해줬어야 함ㅋㅋ
# (애초에 이 경우가 테스트케이스에 왜 있는지 모르겠음;;)
from collections import deque
import sys

def BFS(idx):
    global flag
    q=deque()
    q.append(idx)
    if idx == b: # a==b인 경우 치환을 안해도 되므로 치환횟수 0
        flag=0
        return
    
    while q:
        i=q.popleft()
        if i==b: #목표에 도달하면 치환 횟수(거리)
            flag=distance[i]
            return

        for node in graph[i]:
            if not visit[node] and node not in q:
                visit[node]=True
                distance[node]+=distance[i]+1 #이전 노드(즉, 부모노드까지의 거리 +1)
                q.append(node)


input=sys.stdin.readline

a,b=map(int,input().split())
n,m=map(int,input().split())

graph=[[]for _ in range(n+1)]
visit=[False for _ in range(n+1)]
distance=[0 for _ in range(n+1)]
flag=-1

for _ in range(m): #단방향 그래프인줄 알았는데 양방향 그래프로 했어야됨(a->b가 된다는건 b->a도 되는거니까 )
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

BFS(a)
print(flag)