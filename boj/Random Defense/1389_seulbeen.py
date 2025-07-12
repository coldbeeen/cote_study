# 케빈 베이컨의 6단계 볍칙
# 1444
"""
기본적인 플로이드 워셜 알고리즘으로 풀자.
노드와 노드 사이의 거리가 1로 통일된 양방향 그래프라고 생각하면 된다.
"""
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

# 그래프 선언 및 초기화
INF = float("inf")
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 거리는 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

# 간선끼리 양방향 연결, 거리는 무조건 1
for _ in range(m):
    s, e = map(int, input().split())
    graph[s][e] = 1
    graph[e][s] = 1

# for i in range(1,n+1):
# print(graph[i])

# 플로이드 워셜 알고리즘 수행. a->b로 가는 기존 거리와, x노드를 거쳐서 가는 a->x->b의 거리를 비교
# 아무생각 없이 구현했는데 26%에서 틀렸다고 한 부분
# 반복문의 x,a,b 순서를 준수할 것 (틀린 코드에서는 a,b,x 순으로 하였음)
for x in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][x] + graph[x][b])

# for i in range(1,n+1):
#     print(graph[i])

# 인원당 케빈 베이컨 값을 구하고, 가장 값이 작은 사람을 출력
result = [sum(g[1:]) for g in graph[1:]]
print(result.index(min(result)) + 1)
