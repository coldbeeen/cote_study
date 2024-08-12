#구글링

def solution(board, skill):
    answer = 0
    
    damage = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        damage[r1][c1] += degree if type == 2 else -degree
        damage[r1][c2+ 1] += -degree if type == 2 else degree
        damage[r2 + 1][c1] += -degree if type == 2 else degree
        damage[r2 + 1][c2 + 1] += degree if type == 2 else -degree
        
    # 행 기준 누적합
    for i in range(len(damage) - 1):
        for j in range(len(damage[0]) - 1):
            damage[i][j + 1] += damage[i][j]
    
    # 열 기준 누적합
    for j in range(len(damage[0]) - 1):
        for i in range(len(damage) - 1):
            damage[i + 1][j] += damage[i][j]
            
    # 기존 배열과 연산
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += damage[i][j]
            
            if board[i][j] > 0:
                answer += 1
    
    return answer

# 누적합 활용 문제
# 행 또는 열의 연산 범위에서 다음 인덱스에는 무조건 degree의 역수를 저장해놓는 것이 중요
# 원하는 범위까지 연산을 했다면 다음 범위에서부터는 연산이 되면 안되기 때문
# 새로운 2차원 배열에 공격 및 치유 크기를 다 저장해놓고, board 배열에 한번에 연산해주는 방식
# 반복문을 남발하면 효율성 부분에서 시간 초과 발생