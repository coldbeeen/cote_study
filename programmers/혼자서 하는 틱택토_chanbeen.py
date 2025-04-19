#90+@, 구글링

def solution(board):
    def gameover(char):
        for row in board: #가로 연속 3개, 게임오버
            if row == [char, char, char]:
                return True
        
        for col in range(3): #세로 연속 3개, 게임오버
            if [board[row][col] for row in range(3)] == [char, char, char]:
                return True
            
        if [board[0][0], board[1][1], board[2][2]] == [char, char, char]: #오른 대각선 연속 3개, 게임오버
            return True
        if [board[0][2], board[1][1], board[2][0]] == [char, char, char]: #왼쪽 대각선 연속 3개, 게임오버
            return True
        
        return False
    
    board = [list(row) for row in board]
    
    idx_O = []
    idx_X = []
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                idx_O.append([i, j])
            elif board[i][j] == 'X':
                idx_X.append([i, j])
                
    print(idx_O)
    print(idx_X)
    
    if not (len(idx_O) == len(idx_X) or len(idx_O) == len(idx_X) + 1): #O, X 차례대로 놓으므로 O가 1개 많거나 O와 X의 개수가 같거나임
        return 0
    
    if gameover('O') and gameover('X'): #게임 구조 상 둘 다 승리할 수는 없음
        return 0
    
    if gameover('O') and len(idx_O) != len(idx_X) + 1: #O가 이겼다면, O와 X의 개수가 1개만 차이나야 함
        return 0
    
    if gameover('X') and len(idx_O) != len(idx_X): #X가 이겼다면, O와 X의 개수가 같아야 함
        return 0
    
    return 1

#가로, 세로, 대각선으로 3개가 연속으로 이어지면 게임 종료
#9칸 모두 차서 표시 못 하면 무승부
#O, X를 번갈아 가면서 표시해야하는데, 실수를 했을 수도?
#O개수와 X개수가 2이상 차이나면 그건 실수한 게 맞다
#O 또는 X가 연속 3개 존재한다면 게임이 종료되었어야하므로 실수한 게 맞다
#O가 선공이어야 하는데 X가 먼저 표시되어 있다면 실수한 게 맞다

#승리 기준을 코드로 구현하는 게 헷갈렸는데, 배열 인덱스로 접근하면 되는데 너무 어렵게 생각한 듯