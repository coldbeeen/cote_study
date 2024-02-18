import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v, fee):
    
    if visited.count(1) == N: #N개의 도시 다 방문했으면 순회 성공
        if cost[v][0]: #출발점인 0번째 도시로 돌아갈 길이 있다면 
            result.append(fee + cost[v][0])
    
    for n in graph[v]:
        if visited[n] == 0:
            visited[n] = 1 #이동할 다음 도시 방문 처리
            DFS(n, fee + cost[v][n])
            visited[n] = 0 #순회가 불가능하다고 판단된 루트는 DFS 빠져나오면서 다음 루트에서 사용하기 위해 방문 처리 해제
            #백트래킹처럼 모든 경우의 수를 돌기 위함

N = int(input())

cost = [list(map(int, input().split())) for _ in range(N)] #다른 도시로 이동하는 비용 저장

graph = [[] for _ in range(N)] #이동 루트가 존재하는 도시, 즉 인접한 도시 저장

for i in range(N):
    for j in range(N):
        if cost[i][j] != 0: #비용이 0이 아니면 가는 길이 있는 것
            graph[i].append(j)

visited = [0 for _ in range(N)]

result = []

visited[0] = 1 #0번째 도시부터 시작, 방문처리
#구글링
DFS(0, 0) #for문 돌면서 각 도시로 출발점을 새롭게 설정해줄 필요가 없음
#0번째 도시에서 순회가 된다면 2번째 도시에서 출발해도 같은 루트로 순회가 되기 때문

print(min(result))