from collections import defaultdict, deque

def solution(edges):

    def graph_search(start):
        nonlocal visited

        shape_of_8 = False  # 8자 그래프 여부 (BFS 진행 중 외부로 향하는 간선이 2개 이상인 정점이 나오면 8자임)
        q = deque([start])

        # start를 visited 처리하지 않는 이유는 BFS 수행 이후 시작점으로 돌아왔는지 확인하기 위함임

        while q:  # BFS 시작
            v = q.popleft()

            if len(graph[v]) > 1:  # 8자 그래프임 (8자 그래프의 방문 처리가 필요하므로 BFS는 계속 진행)
                shape_of_8 = True

            for i in graph[v]:  # 연결된 정점 순회
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                else:  # 해당 정점을 이미 방문했다면, 이는 8자/도넛 그래프 또는 '이미 탐색이 진행되던 막대그래프'일 수 있음
                    if not shape_of_8 and not visited[start]:  # 8자 그래프가 아니면서 start로 다시 돌아오지 않았다면 '진행되던 막대그래프'로, 방문처리 후 함수를 종료
                        visited[start] = True
                        return


        if visited[start]:  # 8자 그래프이거나 도넛 그래프임 (시작점으로 돌아왔기 때문)
            if shape_of_8:  # 8자
                answer[3] += 1
            else:  # 도넛
                answer[1] += 1
        else:  # 막대 (시작점으로 돌아오지 않았기 때문)
            answer[2] += 1

        visited[start] = True  # 시작 정점 방문처리 후 종료


    graph = defaultdict(list)  # 인접리스트 방식으로 딕셔너리 기반의 그래프 관리
    v_set = set()  # 정점 종류를 저장하기 위한 집합(set)

    for v1, v2 in edges:  # 방향그래프 표현 및 정점 종류를 저장
        graph[v1].append(v2)
        v_set.add(v1)
        v_set.add(v2)

    visited = {key: False for key in v_set}  # 딕셔너리 기반으로 방문 여부 관리를 위해
    answer = [-1, 0, 0, 0]

    for v in v_set:  # 모든 정점 순회
        if not visited[v] and len(graph[v]) <= 1:  # 방문하지 않았고, 외부로 향하는 간선이 1개 이하인 경우만 탐색 진행 (생성된 정점만 남겨놓기 위함)
            graph_search(v)

    for v in visited:  # 방문하지 않은 정점이 생성된 정점(answer[0])가 됨
        if not visited[v]:
            answer[0] = v

    return answer