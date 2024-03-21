# 바이러스 문제처럼 양방향으로 해야 하나? 아니면 부모자식관계니 단방향으로 해야하나?
# 연결이 서로 되어있어야 하니 양방향이 맞겠다
# 버릇처럼 무조건 global로 했는데... 이건 global을 안써야되네... 삽질 무지함
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
s,e=map(int,input().split())
m=int(input())
graph=[[]for _ in range(n+1)]
visit=[False for _ in range(n+1)]
visit[s]=True

#exit()쓰기 싫었는데 재귀함수 전체 탈출을 시키고 싶은데 방법을 모르겠음
def search(idx,cnt):
    if idx==e: #찾고자 하는 상대방 찾았으면 촌수 출력 후 종료
        print(cnt)
        exit()
    for node in graph[idx]: #해당 노드의 연결된 노드들 중에서
        if visit[node]==False:#방문 안했으면
            visit[idx]=True
            search(node,cnt+1)#그 노드로 재귀함수 호출


for _ in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
search(s,0)
print(-1)
