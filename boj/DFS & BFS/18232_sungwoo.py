import sys
from collections import deque
input = sys.stdin.readline

n, tp_num = map(int, input().split())
start, end = map(int, input().split())
tp_list = [[] for _ in range(n+1)]
for i in range(tp_num):  # 인접리스트 방식으로 텔레포트를 그래프로 표현
    v1, v2 = map(int, input().split())
    tp_list[v1].append(v2)
    tp_list[v2].append(v1)

visited = [False for _ in range(n+1)]  # 방문 여부 리스트
q = deque([start])  # 큐 생성
visited[start] = True  # 시작 지점 방문 처리
result = [0 for _ in range(n+1)]  # 각 정점에서의 시간 계산을 위한 리스트

# BFS 수행 - 최단시간(거리) 계산을 위함
while q:
    v = q.popleft()
    if v == end:
        break

    next_v_list = [v-1, v+1] + tp_list[v]  # 다음 방문할 정점 후보 생성 (좌, 우, 텔레포트)

    for next_v in next_v_list:  # 다음 정점 후보 탐색
        if 0 < next_v <= n and not visited[next_v]:  # 유효한 위치이며 방문하지 않았는지 검사
            q.append(next_v)  # 큐에 추가
            visited[next_v] = True  # 방문 처리
            result[next_v] = result[v] + 1  # 시간 1 증가

print(result[end])