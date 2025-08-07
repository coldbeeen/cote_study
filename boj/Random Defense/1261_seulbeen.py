#알고스팟
#1시간 40분 후 구글링
"""
사실 문제 분류가 다익스트라라서 고른 문제
그런데 단순히 최단거리를 구하는게 아니라 '거리는 상관없으니 중간에 지나가면서 부숴야 하는 벽'의
개수가 가장 적은 경우를 구하는 것
다익스트라로 어떻게 풀지 감이 잘 안 잡힘

저번에 찬빈&성우가 다익스트라이고, 내가 BFS인줄 알았지만 다익스트라와 로직이 유사했던
그 느낌으로 풀어보자

distance를 inf로 선언해두고, 탐색을 진행하다가 벽을 만나면 부숴서 여태껏 부순 벽의 개수 +1 를 저장...

=>시간초과

=>구글링
벽이 아닌 경우에도 거리는 업데이트 안하지만 q에 추가하면 되긴함

근데 0-1BFS라고 새로운 알고리즘이 등장...

deque를 사용하는건 맞지만, 다음 노드를 q에 append할때의 경우가 다름
벽인경우: deque의 맨 뒤로
벽이아닌경우: deque의 맨 앞으로 append 하여 탐색의 우선순위 확보
"""

import sys
import heapq
from collections import deque
input=sys.stdin.readline

m,n=map(int,input().split())
graph=[list(int(c) for c in input().rstrip()) for _ in range(n)]

# print(graph)

dx=[1,-1,0,0]
dy=[0,0,1,-1]
distance=[[float("inf")]*m for _ in range(n)]

distance[0][0]=0

def bfs(height,width):
    q=deque()
    q.append((height,width))
    while q:
        x,y=q.popleft()
        cost=distance[x][y]
        for i in range(4):
            #다음 이동 좌표
            nx=x+dx[i]
            ny=y+dy[i]

            # 그래프의 범위 내에서
            if 0<=nx<n and 0<=ny<m:
                # 벽일경우
                if graph[nx][ny]==1:

                    # 거리 비교 후 deque의 "맨 뒤"에 추가
                    if distance[nx][ny]>cost+1:
                        distance[nx][ny]=cost+1
                        q.append((nx,ny))
                
                elif graph[nx][ny]==0:
                    # 거리 비교후 deque의 "맨 앞"에 추가!!!
                    if distance[nx][ny]>cost:
                        distance[nx][ny]=cost
                        q.appendleft((nx,ny))

    return distance[-1][-1]
    
result=bfs(0,0)
print(result)