import sys
sys.setrecursionlimit(10**6)

def dfs(graph, x, y):
    if (x < 0) or (x >= w) or (y < 0) or (y >= h):
        return 0
    
    if graph[y][x] == 1:
        # visit 처리
        graph[y][x] = 0

        dfs(graph, x-1, y-1)
        dfs(graph, x-1, y)
        dfs(graph, x-1, y+1)
        dfs(graph, x, y-1)
        dfs(graph, x, y+1)
        dfs(graph, x+1, y-1)
        dfs(graph, x+1, y)
        dfs(graph, x+1, y+1)

        return 1
    else:
        return 0
while True:
    w, h = map(int, input().split())
    result = 0

    if (w == 0) and (h == 0):
        # 종료조건
        break

    # 섬 0, 1 여부 받기
    graph = []
    for _ in range(h):
        islands = list(map(int, input().split()))
        graph.append(islands)

    # DFS하며 방문여부 확인
    for x in range(w):
        for y in range(h):
            if graph[y][x] == 1:
                result += dfs(graph, x, y)

    print(result)

"""
문제:

상하좌우 대각선으로 움직일 수 있음. 연속된 1을 하나의 섬으로 보고 총 섬의 개수 구하는 문제
____________________________________________________________________________________
풀이:

이코테의 DFS를 참고해서 풀었음.
근데 파이썬은 재귀 횟수가 정해져있어 RecursionError가 발생해 임의로 재귀 가능 횟수를 늘려주었음
이래도 되는건가?
"""