# 녹색 옷 입은 애가 젤다지?
# 50분
"""
BFS로 풀면될듯 하다
근데 ... 기존 BFS는 노드 한칸당 거리가 1이라는게 보장되어서 최단 경로가 최단 거리였는데
이 문제는 각 칸마다 가지고 있는 가중치가 달라서 풀고나니까 굳이 BFS로 풀 필요는 없었다고 생각
"""
import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    q = deque()
    q.append([0, 0])
    # visited 배열을 최댓값으로 초기화
    visited = [[float("inf")] * n for _ in range(n)]
    
    # 시작점의 값 초기화
    visited[0][0] = graph[0][0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            cx = x + dx[i]
            cy = y + dy[i]

            # 그래프의 범위 내에서, 현재 visited 값에 다음 그래프의 값을 더한 값이 최소일 때, 갱신 후 큐에 저장
            if (
                0 <= cx < n
                and 0 <= cy < n
                and visited[cx][cy] > visited[x][y] + graph[cx][cy]
            ):
                visited[cx][cy] = visited[x][y] + graph[cx][cy]
                q.append([cx, cy])
    return visited[-1][-1]


cnt = 1
while True:
    n = int(input())

    # q=deque()
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    # print(graph)
    print(f"Problem {cnt}: {bfs()}")
    cnt += 1
