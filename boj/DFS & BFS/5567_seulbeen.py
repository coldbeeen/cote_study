# DFS인줄 알았는데 딱 '친구의 친구'(2hop)까지만 구하는 거였음 => BFS
import sys
from collections import deque

def BFS(idx):
    global cnt
    q=deque()
    q.append(idx)

    while q:
        i=q.popleft()

        for node in graph[i]:
            if not visit[node] and node not in q: # 방문한 적이 없고 이미 대기열에 들어가있는 노드가 아닌 경우
                visit[node]=True #방문처리
                distance[node]+= 1+ distance[i] # 부모노드의 거리 +1
                if distance[node]<=2: # 2hop 이내인 경우에만 카운트 증가 및 큐에 append(2 hop을 넘으면 그 다음부터는 탐색할 필요가 없음)
                    q.append(node)
                    cnt+=1

   

input=sys.stdin.readline
n=int(input())
m=int(input())

graph=[[]for _ in range(n+1)]
visit=[False for _ in range(n+1)]
visit[1]=True
distance=[0 for _ in range(n+1)]
cnt=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

BFS(1)
print(cnt)

