from collections import deque
import copy

def BFS(copy, queue):
    # 바이러스(2) 기준 상하좌우로 증식하고 0이었던 것은 데크에 넣어주어 새로 증식 가능하게 함
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= M):
                # 종료 조건
                continue

            if copy[nx][ny] == 0:
                # 빈 칸인 경우, 바이러스가 증식하고 데크에 append
                copy[nx][ny] = 2
                queue.append((nx, ny))
    
    return copy

def count_zero(copy):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy[i][j] == 0:
                cnt += 1
    return cnt

def calcualte_area(i, j, k):
    """
    1. 2를 벽에 닿을 때까지 증식
    2. 0의 개수 구하기
    """
    queue = deque()

    # 원본을 침해하지 않는 행렬 복사본
    copy_lab = copy.deepcopy(lab)

    # 세 개의 기둥을 세워줌
    copy_lab[i//M][i%M] = 1
    copy_lab[j//M][j%M] = 1
    copy_lab[k//M][k%M] = 1

    for r in range(N):
        for c in range(M):
            if copy_lab[r][c] == 2:
                # 초기 바이러스 위치 데크에 넣어줌
                queue.append((r, c))


    # 바이러스 증식
    copy_lab = BFS(copy_lab, queue)

    # 안전지대 카운팅
    cnt = count_zero(copy_lab)

    # 최댓값 갱신
    return max(result, cnt)


""" main """
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

nm = N * M

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
for i in range(nm):
    for j in range(i + 1, nm):
        for k in range(j + 1, nm):
            if (lab[i//M][i%M] == 0) and (lab[j//M][j%M] == 0) and (lab[k//M][k%M] == 0):
                # print("Calculate:", i, j, k)
                result = calcualte_area(i, j, k)

            
print(result)

"""
문제:

NxM의 행렬에서 0:빈 칸, 1:벽, 2:바이러스.
바이러스는 상하좌우로 퍼져나가며 벽을 세 개 세울 수 있다.
벽을 세우고 바이러스가 퍼졌을 때 안전지대(0)의 최댓값 구하기.
-----------------------------------------------------------------
풀이:

N, M <= 8 이므로 완전탐색을 해도 시간 초과가 나지 않을 것 같다고 생각했다.
따라서 매 번 세 개의 0, 0, 0인 조합을 찾고 각각 벽을 세웠을 때, 안전지대의 값을 카운팅해주었다.

1. 완전탐색하며 0, 0, 0인 인덱스 찾기
2. BFS를 통해 바이러스 증식
3. 안전지대(바이러스 증식 이후에는 0만 카운팅하면 됨) 카운팅
4. 최댓값 갱신
"""