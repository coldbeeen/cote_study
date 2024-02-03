#번호 잘못입력해서 recommit
import sys
input=sys.stdin.readline
from collections import deque
nodes,vertices,s_node=map(int,input().split())
graph=[[]for _ in range(nodes+1)]
visit_for_DFS=[False for _ in range(nodes+1)]
visit_for_BFS=[False for _ in range(nodes+1)]

for _ in range(vertices):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# 문제 조건에 방문할 수 있는 정점이 여러개라면 숫자가 작은 정점부터 방문하라고 명시되어있기 때문에 정렬    
for nodes in graph:
    nodes.sort()

def DFS(idx):
    visit_for_DFS[idx]=True #방문을 True로
    print(idx,end=' ')
    for node in graph[idx]:
        if visit_for_DFS[node]==False:# 정점과 연결되어있는 이웃 정점을 방문하는데, 방문한 적 없는 정점에 한해 방문
            DFS(node)

def BFS(idx):
    q=deque()
    q.append(idx)
    #방문할 노드를 큐에 담음

    while q:#방문할 노드가 없을때 까지
        i=q.popleft() # 방문한 노드를 pop
        visit_for_BFS[i]=True
        print(i,end=' ')

        for node in graph[i]:#해당 노드의 이웃 노드를 검사하며 방문할 노드라면 q에 append
            if visit_for_BFS[node]==False and node not in q:
                q.append(node) 

DFS(s_node)
#visit=[False for _ in range(nodes+1)]
print()
BFS(s_node)
# 궁금한점 : visit 배열 두개 만들기 좀 그래서 visit로 통일하고, DFS끝나고 visit 다시 초기화 하는 방식으로 해봤는데 왜 오류가 뜨지???