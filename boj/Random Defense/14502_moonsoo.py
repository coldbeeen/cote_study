from collections import deque
import copy

def BFS(copy, queue):

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx < 0) or (nx >= N) or (ny < 0) or (ny >= M):
                # 종료 조건
                continue

            if copy[nx][ny] == 0:
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