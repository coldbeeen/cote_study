# 친구
"""
2-친구의 정의가 조금 헷갈리네...
A가 B의 2친구가 되려면 :
1. A-B 직접 친구
2. A-C, C-B 인 친구 C가 있으면 된다

결국 그냥 내 친구의 친구까지 2친구라는 소리
즉 거리가 2이하인 노드끼리는 2친구임
각 사람 별로 각자의 최단거리들을 구하면 되므로 플로이드 워셜

"""


import sys

input = sys.stdin.readline

n = int(input())
# 그래프 인풋
graph = [list(input().rstrip()) for _ in range(n)]
# print(graph)

# 거리를 담을 배열
distance = [[0] * n for _ in range(n)]

# 플로이드 워셜 진행
for x in range(n):
    for a in range(n):
        for b in range(n):
            if a == b:
                continue
            if graph[a][b] == "Y" or (graph[a][x] == "Y" and graph[x][b] == "Y"):
                distance[a][b] = 1

# print(distance)
# 각 사람 별 2친구 수
result = [sum(d) for d in distance]

# print(result)

print(max(result))
