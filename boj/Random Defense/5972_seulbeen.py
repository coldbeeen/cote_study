# 택배배송
# 20분
# 기본적인 다익스트라 같으나 다익스트라 다시 생각해내는데 조금 걸림
import sys
import heapq
input=sys.stdin.readline

def dijkstra(start):
    
    q=[]
    # 출발 지점의 거리와 노드
    heapq.heappush(q,(0,start))
    
    while q:
        cost,node=heapq.heappop(q)
        for cost,n_node in graph[node]:
            # 현재노드까지의 거리 + 다음 노드의 거리 vs 다음 노드까지의 최단거리 비교
            if distance[node]+cost<distance[n_node]:
                distance[n_node]=distance[node]+cost
                heapq.heappush(q,(distance[n_node],n_node))

    return

n,m=map(int,input().split())

# 그래프 선언
graph=[[]for _ in range(n+1)]

# 거리 배열 선언 및 초기화
distance=[float("inf") for _ in range(n+1)]
distance[1]=0

# 그래프 입력
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

# 다익스트라 알고리즘 실행 후 결과 출력
dijkstra(1)
print(distance[-1])