import sys
from collections import deque
input = sys.stdin.readline

num_of_computer = int(input())
num_of_pair = int(input())

graph = [[] for i in range(num_of_computer+1)]  # 인접리스트 구현
for i in range(num_of_pair):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])  # 큐 생성 (1번 컴퓨터 추가)
visited = [0 for i in range(num_of_computer+1)]  # 바이러스 감염 여부
visited[1] = 1  # 1번 컴퓨터 감염 처리

while q:  # 큐각 빌 때까지 반복 (더 이상 감염되는 컴퓨터가 없을 때 까지)
    c1 = q.popleft()

    for c2 in graph[c1]:  # 연결된 컴퓨터 순회
        if visited[c2] == 0:  # 감염 여부 확인 - 이미 감염되었다면(1이라면) 큐에 추가하지 않음
            q.append(c2)  # 큐에 추가
            visited[c2] = 1  # 감염 처리


print(sum(visited) - 1)  # 1번 컴퓨터 제외하고 출력
