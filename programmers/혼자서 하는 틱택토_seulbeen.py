"""
c(O)>=c(X)
O와 X가 둘다 빙고가 뜰 수 없음
O가 빙고인데, X가 더 놓으면 안됨
X가 빙고인데, O가 더 놓으면 안됨
"""
#1시간 20분 후 구글링 참고


def solution(board):
    """ i,j에 해당하는 좌표를 
        012
        345
        678 
        형식으로 매핑
    """
    def is_Bingo():
        keypad = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        # 빙고가 되는 경우의 수
        bingo = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        o = []
        x = []
        
        # O와 X인 칸번호를 저장
        for r, row in enumerate(board):
            for c, value in enumerate(row):
                if value == "O":
                    o.append(keypad[r][c])
                elif value == "X":
                    x.append(keypad[r][c])
        # 2,5,
        bingo_o = [cases for cases in bingo if all(c in o for c in cases)]
        bingo_x = [cases for cases in bingo if all(c in x for c in cases)]

        #빈 리스트면 False, 값이 있으면 True
        return [bool(bingo_o), bool(bingo_x)]

    # O와 X의 개수
    def count_ox():
        cnt_o, cnt_x = 0, 0
        for b in board:
            for ox in b:
                if ox == "O":
                    cnt_o += 1
                elif ox == "X":
                    cnt_x += 1
        return (cnt_o, cnt_x)

    cnt = count_ox()
    Bingo = is_Bingo()

    # O와 X가 둘다 빙고인 경우는 불가능
    if Bingo[0] and Bingo[1]:
        return 0
    # O로 빙고를 만들었는데 개수가 짝수 -> X가 하나 더 잘못 놓은거
    elif Bingo[0] and sum(cnt) % 2 == 0:
        return 0
    # X로 빙고를 만들었는데 개수가 홀수 -> O가 하나 더 잘못 놓은거
    elif Bingo[1] and sum(cnt) % 2 == 1:
        return 0
    
    # O의 개수가 X의 개수보다 적을 수 없음
    if cnt[0] < cnt[1]:
        return 0
    # O와 X의 개수차가 1보다 크다면 -> X차례때 O를 한번 더 놓은거임 
    elif cnt[0] - cnt[1] > 1:
        return 0
    return 1
