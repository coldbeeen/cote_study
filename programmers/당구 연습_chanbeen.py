#약 83분 소요

def solution(m, n, startX, startY, balls):
    answer = []
    
    for ball in balls:
        array = []
        flags = []
        x, y = ball
        
        if startX == x:
            if y > startY: #상 대칭 사용 불가
                flags.append(1)
            else: #하 대칭 사용 불가
                flags.append(2)
        
        if startY == y:
            if x > startX: #우 대칭 사용 불가 
                flags.append(3)
            else: #좌 대칭 사용 불가
                flags.append(4)

        if 1 not in flags:
            array.append((startX - x) ** 2 + (n + (n - y) - startY) ** 2) #상 방향으로 대칭
        if 2 not in flags:
            array.append((startX - x) ** 2 + (startY - (-y)) ** 2) #하 방향으로 대칭
        if 3 not in flags:
            array.append((m + (m - x) - startX) ** 2 + (startY - y) ** 2) #우 방향으로 대칭
        if 4 not in flags:
            array.append((startX - (-x)) ** 2 + (startY - y) ** 2) #좌 방향으로 대칭
        
        answer.append(min(array)) #최소 거리 answer에 저장
        
    return answer

# 입사각 반사각이 같으므로, 상하좌우로 목표점의 좌표를 적절하게 대칭시켜서 직선거리를 구하고, 최솟값을 answer 배열에 저장하자
# x 또는 y좌표가 같고 A와 벽 사이에 목표점이 존재하는 경우, 그 벽은 대칭으로 사용 못 함