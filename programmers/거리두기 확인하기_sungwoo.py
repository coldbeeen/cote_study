from collections import deque

def solution(places):

    def safe_check():  # 거리두기 준수 여부 체크 함수

        for i in range(len(place)):
            for j in range(len(place)):
                if place[i][j] == 'P':  # 응시자 위치에서 bfs 수행
                    if not bfs_for_safe_check(i, j):  # 거리두기가 지켜지지 않은 경우 False 리턴
                        return False

        return True  # 모든 응시자의 bfs_for_safe_check() 수행 결과가 True인 경우 최종적으로 True 리턴

    def bfs_for_safe_check(x, y):  # (x, y) 위치에서 맨해튼 거리 2 이하까지의 자리에 대해 BFS를 수행

        distance = [[-1 for _ in range(len(place))] for _ in range(len(place))]  # 거리 (-1은 미방문)
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]  # 좌표 변위

        # 큐 생성 및 초기 위치 거리 1로 초기화
        q = deque([(x, y)])
        distance[x][y] = 0

        # BFS 수행
        while q:
            x, y = q.popleft()
            if distance[x][y] >= 2:  # 맨해튼 거리 2부터는 더 이상 진행할 필요가 없으므로 반복문 종료
                break

            for i in range(4):  # 상하좌우 순회
                nx, ny = x + dx[i], y + dy[i]

                # 1. 유효한 인덱스이며, 2. 방문하지 않았고, 3. 파티션이 아닌 경우
                if 0 <= nx < len(place) and 0 <= ny < len(place) and distance[nx][ny] == -1 and place[nx][ny] != 'X':
                    if place[nx][ny] == 'P':  # 거리두기 실패 -> False 리턴
                        return False
                    elif place[nx][ny] == 'O':  # 빈 자리이므로 큐에 추가 및 거리 계산
                        q.append((nx, ny))
                        distance[nx][ny] = distance[x][y] + 1

        return True


    answer = []

    for place in places:
        for i in range(len(place)):  # place의 행 'str' -> 'list' 변환
            place[i] = list(place[i])

        safe = safe_check()  # 거리두기 준수 여부 체크
        answer.append(int(safe))  # 결과 저장

    return answer