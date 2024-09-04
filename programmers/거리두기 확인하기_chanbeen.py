from collections import deque

def solution(places):
    def bfs(p):
        points = []
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        for i in range(5):
            for j in range(5):
                if p[i][j] == 'P':
                    points.append([i, j])

        for point in points: 
            queue = deque([point])
            
            visited = [[0] * 5 for _ in range(5)] #visited로 distance를 관리해도 되지만, 
            distance = [[0] * 5 for _ in range(5)] #직관적이기 위해 따로 생성
            
            visited[point[0]][point[1]] = 1 #초기값 방문 처리
            
            while queue:
                x, y = queue.popleft()
            
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                
                    if 0 <= nx < 5 and 0 <= ny < 5:
                        if visited[nx][ny] == 0:
                            if p[nx][ny] == 'O':
                                visited[nx][ny] = 1
                                queue.append([nx, ny])
                                distance[nx][ny] = distance[x][y] + 1
                        
                            if p[nx][ny] == 'P' and distance[x][y] <= 1:
                                return 0
        
        return 1
        
    answer = []
    
    for p in places:
        answer.append(bfs(p))
    
    return answer

# P인 지점을 미리 담아놓고 bfs를 돌려서 맨해튼 거리 2 이내에 다른 P가 있으면(파티션 있을 경우는 제외) False 반환
# 모든 포인트들을 한번에 관리할 수 있게 visited를 함수 내에서 한번만 선언하려 했는데, 잘 안 풀림..
# 효율적인지 모르겠으나 각 포인트마다 visited와 distance를 선언해서 bfs 순회를 도는 것이 직관적이라고 판단