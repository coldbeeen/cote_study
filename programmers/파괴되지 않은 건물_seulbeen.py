"""
오잉? 풀려있는데 커밋이 안되어있네...?
그래서 그냥 지우고 다시 풀었어용
"""
# 40분
# 누적합 구현에서 인덱스 디버깅을 못해서 시간을 조금 잡아먹었음
def solution(board, skill):
    answer = 0
    """
    누적합 계산용 (크기가 1 큰 이유는, 누적합을 구현할때 out of range를 관리하기 위함)
    cum_sum 배열에 모든 공격과 회복을 계산해서 건물 배열에 일괄적용해버리면 된다.
    """
    cum_sum = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
    # print(cumul_sum)

    for i in range(len(skill)):
        """ t=공격/수비, (r1,c1) ,(r2,c2), degree=공격/회복의 강도"""
        t = skill[i][0]
        r1 = skill[i][1]
        c1 = skill[i][2]
        r2 = skill[i][3]
        c2 = skill[i][4]
        degree = skill[i][5]
        
        """
        누적합 계산을 위한 바운더리(?) 밑작업, 예를 들어 4x4배열에 (1,1)부터 (2,2)까지 2만큼 힐한다고 하면
        0000           0 0 0 0
        0000           0 2 0 -2
        0000   -->     0 0 0 0
        0000           0 -2 0 2  요런식으로
        """
        # 공격
        if t == 1:
            cum_sum[r1][c1] += -degree
            cum_sum[r2 + 1][c1] += degree
            cum_sum[r1][c2 + 1] += degree
            cum_sum[r2 + 1][c2 + 1] += -degree

        # 힐
        elif t == 2:
            cum_sum[r1][c1] += degree
            cum_sum[r2 + 1][c1] += -degree
            cum_sum[r1][c2 + 1] += -degree
            cum_sum[r2 + 1][c2 + 1] += degree

    # for c in cum_sum:
    #     print(c)
    """행방향 (왼->오)으로 누적합 계산후 열방향(위->아래)로 계산(순서는 상관없음)"""
    for i in range(len(cum_sum)):
        for j in range(1, len(cum_sum[0])):
            cum_sum[i][j] += cum_sum[i][j - 1]
    for i in range(len(cum_sum[0])):
        for j in range(1, len(cum_sum)):
            cum_sum[j][i] += cum_sum[j - 1][i]
    # for i in range(len(cum_sum)):
    #     print(cum_sum[i])


    """누적합된 공격/힐을 원래 건물 판에 일괄적으로 적용"""
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += cum_sum[i][j]
    # for b in board:
    #     print(b)
    answer = sum(1 for row in board for col in row if col > 0)

    return answer
