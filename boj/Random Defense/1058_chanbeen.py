#60분 +@, bfs 내부 로직 구글링

from collections import deque

def bfs(v):
    visited = [False] * N
    visited[v] = True

    queue = deque([(v, 0)])

    cnt = 0

    while queue:
        node, cost = queue.popleft()

        if cost >= 2: #관계가 2단계 이상이면 친구로 고려 X
            continue
        
        #1번째 사람이 4, 6번째 사람과 친구 -> 4, 6번째 사람의 친구도 1번째 사람의 친구로 카운트
        for i in range(N): 
            if not visited[i]: #단 중복되는 친구는 중복 카운트 x
                if graph[node][i] == 'Y':
                    cnt += 1
                    visited[i] = True
                    queue.append((i, cost + 1))

    return cnt

N = int(input())

graph = [list(input().rstrip()) for _ in range(N)]

result = []

for i in range(N): #i번째 사람에 대한 인맥 체크
    result.append(bfs(i))

print(max(result))

#친구의 친구까지 자기 친구로 간주
#cost라는 변수를 두고, cost가 2가 넘으면 친구의 친구의 친구 ... 이므로 친구로 고려x
#bfs 알고리즘으로 시도
#친구가 가장 많은 사람 최종 출력