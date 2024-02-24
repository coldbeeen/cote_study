#BFS인듯?
# visit 겸 거리 배열 선언했는데 그렇게 되면 다시 시작 노드로 돌아올때 거리가 0이 아니게 됨 (23번째 줄에 node!=x 조건 추가)
# 근데 이럴바에 그냥 visit배열이랑 거리배열 따로 선언 해 놓는게 나을거 같음 ㅠㅠ
# 해당 예시
"""
4 4 2 1
1 2
1 3
3 4
2 1

answer: 4
output: 1,4
""" 
import sys
from collections import deque
input=sys.stdin.readline
n,m,k,x=map(int,input().split())
graph=[[]for _ in range(n+1)]
visited=[0 for _ in range(n+1)]
result=[]

for i in range(m):
    a,b=map(int,input().split())
    #단방향 그래프니까 하나만 연결
    graph[a].append(b)

def BFS(idx):
    global exist
    q=deque()
    q.append(idx)# 탐색할 노드 append
    while q: #더 이상 탐색할 노드가 없을때 까지
        i=q.popleft()
        for node in graph[i]:
            if not visited[node] and node!=x: # 방문 안한 노드일때
                visited[node]=visited[i]+1 #이전 노드까지의 거리 + 1을 방문배열에 더해줌(거리)
                q.append(node)
                if visited[node]==k: #거리가 딱 맞으면 정답배열에 추가
                    result.append(node)
    if result:
        result.sort()
        for i in range(len(result)):
            print(result[i])
    else:
        print(-1)


BFS(x)