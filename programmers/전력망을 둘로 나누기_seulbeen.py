# 1시간...
from collections import deque
def solution(n, wires):
    
    def bfs(graph, start):
        visit = [start]
        print(f"visit? {visit}")
        num = 1
        q = deque()
        q.append(start)
        while q:
            nodes = q.popleft()
            for n in graph[nodes]:
                print(n)
                if n not in visit:
                    visit.append(n)
                    q.append(n)
                    num += 1
        return num

    arr = []

    for i in wires:
        graph = [[] for _ in range(n + 1)]
        # 전력망 끊기
        first, second = i
        for j in wires:
            if i == j:
                continue
            # 끊고 나서 두개의 그래프로 만듬(끊은 노드를 제외한 나머지를 연걸하는거)
            a, b = j
            graph[a].append(b)
            graph[b].append(a)
        print(graph)
        # 각 그래프의 bfs 실행
        n1 = bfs(graph, first)
        n2 = bfs(graph, second)
        print(f"{n1},{n2}")
        print("---")

        #차이 구함
        arr.append(abs(n1 - n2))

    #차이의 최소값
    answer = min(arr)

    return answer
