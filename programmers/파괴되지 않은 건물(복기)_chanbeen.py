#70분 +@, 구글링

def solution(board, skill):
    answer = 0
    
    N = len(board)
    M = len(board[0])
    
    damage = [[0] * (M + 1) for _ in range(N + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        value = -degree if type == 1 else degree
        
        damage[r1][c1] += value
        damage[r1][c2 + 1] -= value #12번 줄의 value 상쇄용
        damage[r2 + 1][c1] -= value
        damage[r2 + 1][c2 + 1] += value #14번 줄의 value 상쇄용
        
    for i in range(N): #열방향 데미지 누적
        for j in range(M):
            damage[i][j + 1] += damage[i][j]
            
    for j in range(M): #행방향 데미지 누적
        for i in range(N):
            damage[i + 1][j] += damage[i][j]
    
    for i in range(N):
        for j in range(M):
            board[i][j] += damage[i][j] #해당 건물에 누적된 데미지 한번에 계산 
            
            if board[i][j] > 0:
                answer += 1
    
    return answer

#skill 최대 길이는 25만, board의 최대 반복 수는 100만
#skill마다 board를 2중 반복문으로 순회할 경우 최악의 경우 시간 초과가 날 수 있음
#공격 스킬이든 아군 스킬이든 수치를 한 배열에 전부 저장해놨다가, board 배열과 연산
#이 과정에서도 2중 반복문은 사용하면 안 됨
#누적합 개념 적용
#회복 스킬의 경우 시작 지점에 +n, 끝 지점 한 칸 옆에 -n 처리 -> 공격 스킬은 반대
#끝 지점 한 칸 옆에 -n을 하는 이유는 지정 범위인 r1, c1, r2, c2에만 영향을 주기 위함
# +n -n = 0이 되어 범위 밖 건물에는 영향을 미치지 않음