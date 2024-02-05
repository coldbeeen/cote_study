# 런타임에러(Recursion Error) 떠서 구글링 해본 결과
# 파이썬의 기본 재귀 한계는 1000쯤인데, 이 문제는 그걸 살짝 넘는다고 해서 sys.setrecursionlimit(2000) 을 추가했더니 맞았다고 뜸

import sys
input=sys.stdin.readline
sys.setrecursionlimit(2000)
nodes,vertices=map(int,input().split())
cnt=0
def search(idx):
    global cnt
     # 방문하지 않은 곳일 때
    for i in graph[idx]:
        if visit[i]==False:
            visit[i]=True
            search(i)    

graph=[[] for _ in range(nodes+1)]
visit=[False for _ in range(nodes+1)]
for _ in range(vertices):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(1,len(graph)):
    if visit[i]==False: #이미 싸이클의 일부분(이미 재귀함수에서 방문했던 곳)이면 검사할 필요가 없음
        search(i)
        cnt+=1
    
print(cnt)
