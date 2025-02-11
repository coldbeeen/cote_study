#70 +@, 구글링

def solution(dirs):
    answer = 0
    
    direction = {'U' : (0, 1), 'D' : (0, -1), 'R' : (1, 0), 'L' : (-1, 0)}
    
    cases = set() #중복 경로 제거를 위한 set 자료형
    
    x, y = 0, 0
    
    for dir in dirs:
        dx, dy = direction[dir]
        
        nx = x + dx
        ny = y + dy
        
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            cases.add(((x, y), (nx, ny)))
            cases.add(((nx, ny), (x, y))) #왔던 길 복귀 가능, 따라서 경로 첫 방문 시 양방향으로 저장
            
            x = nx
            y = ny
    
    return len(cases) // 2 #양방향으로 add했으므로 길이는 절반

#1차 제출
#상하좌우 이동 문제
#visited 선언, 명령어대로 이동, 방문 안 했을 시 answer + 1, 방문 했을 시는 그대로 진행
#점에 대해 visited를 적용하면 경로는 처음 가지만 도착점이 방문했던 점인 경우 카운트가 안 됨
#점 대신 선분에 대해 visited 적용?

#구글링
#간선에 대해 visited를 관리할 방안이 정립이 안 되어 구글링
#처음 방문하는 경로의 길이를 측정하므로, set 자료형을 사용하여 값을 distinct하게 남겨줌
#왔던 길을 돌아갈 수도 있으므로, set에 add할 때 양방향으로 add해줌
#dictionary와 마찬가지로 set도 활용도가 높다는 것을 알게 되었음