import sys
input = sys.stdin.readline

def dfs(v, cnt):
    global b, result  # b는 타겟, result는 최종 결과
    if v == b:  # 종료 조건
        result = cnt
        return

    visited[v] = True  # 방문 처리 후
    for i in graph[v]:  # 인접 정점 순회
        if not visited[i]:  # 방문하지 않았다면
            dfs(i, cnt+1)  # 인접 정점으로 dfs 함수 재귀

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for i in range(n+1)]  # 인접리스트 구현
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for i in range(n+1)]
result = -1  # 기본값 -1로 설정
dfs(a, 0)  # a부터 시작해 dfs 함수 실행
print(result)